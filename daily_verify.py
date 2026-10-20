#!/usr/bin/env python3
"""每天核对：品牌自己的页面上，我们引用的内容有没有变。

设计原则（这条最重要）：
  「今天检查过」只有在**真的读过那一页、并且那页的内容和上次一模一样**时才成立。
  所以 checked 日期只会在「抓取成功 + 正文指纹未变」时前进到今天；
  内容一变就停下来等人看过，绝不自动把日期往前推。

为什么按指纹而不是按数字：
  试过按「这条事实里的数字能不能在源页找到」来判断，误报率太高 ——
  一条问答经常同时引用多个品牌的数字（$10/$15/$9/$35/$22、$2,500/$10,000/$300），
  它们本来就分散在不同品牌的页面上，单页必然找不到。那套判据已弃用，
  只保留为 advisory（仅供参考，不阻塞）。

用法：
  python daily_verify.py             # 只核对，写报告
  python daily_verify.py --apply     # 核对通过的才把 checked 改成今天
  python daily_verify.py --apply --force   # 即使有页面变了也继续（不推荐）
"""
import hashlib
import json
import re
import sys
import time
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
DOCS = ROOT / "docs"
BASE = ROOT / "data/source_baseline.json"

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36"
)
HEADERS = {
    "User-Agent": UA,
    "Accept": "text/html,application/xhtml+xml,application/pdf;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

REV_PATTERNS = [
    r"Last\s+[Uu]pdated\s*:?\s*([A-Z][a-z]+\.?\s+\d{1,2},\s+\d{4})",
    r"Updated\s+on\s*:?\s*([A-Z][a-z]+\.?\s+\d{1,2},\s+\d{4})",
    r'"dateModified"\s*:\s*"(\d{4}-\d{2}-\d{2})',
    r'"modified"\s*:\s*"(\d{4}-\d{2}-\d{2})',
]


def fetch(url):
    """返回 (status, text, rev_date)。status: ok / http_NNN / err_X

    PDF 也照常核对：按字节算指纹。之前把 PDF 当作「无法核对」跳过，
    结果是那几条的日期永远冻在原地 —— 而 PDF 恰恰是最容易整份换掉的东西。
    """
    try:
        r = requests.get(url, headers=HEADERS, timeout=60, allow_redirects=True)
    except Exception as e:  # noqa: BLE001
        return f"err_{type(e).__name__}", "", None
    if r.status_code != 200:
        return f"http_{r.status_code}", "", None
    ctype = r.headers.get("content-type", "")
    if "pdf" in ctype or url.lower().endswith(".pdf"):
        # 用字节的 sha256 当作「正文」，走同一套指纹逻辑
        return "ok", "pdf-bytes:" + hashlib.sha256(r.content).hexdigest(), None

    html = r.text
    rev = None
    for p in REV_PATTERNS:
        m = re.search(p, html)
        if m:
            rev = m.group(1)
            break

    body = re.sub(r"(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>", " ", html)
    body = re.sub(r"(?s)<[^>]+>", " ", body)
    body = (
        body.replace("&nbsp;", " ")
        .replace("&amp;", "&")
        .replace("&#x27;", "'")
        .replace("&#39;", "'")
        .replace("&quot;", '"')
    )
    return "ok", re.sub(r"\s+", " ", body).strip(), rev


def fingerprint(text):
    """去掉空白差异后的指纹；只要正文措辞变了，指纹就变。"""
    return hashlib.sha256(re.sub(r"\s+", " ", text).encode("utf-8")).hexdigest()[:16]


def iter_items(node, path=""):
    if isinstance(node, dict):
        if isinstance(node.get("source_url"), str) and ("fact" in node or "q" in node):
            yield path, node
        else:
            for k, v in node.items():
                yield from iter_items(v, f"{path}/{k}")
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from iter_items(v, f"{path}[{i}]")


def main():
    apply = "--apply" in sys.argv
    force = "--force" in sys.argv
    today = date.today().isoformat()
    DOCS.mkdir(exist_ok=True)

    articles = json.loads((DATA / "articles.json").read_text(encoding="utf-8"))
    brands = json.loads((DATA / "brands.json").read_text(encoding="utf-8"))
    baseline = json.loads(BASE.read_text(encoding="utf-8")) if BASE.exists() else {}

    urls = Counter()
    for blob in (articles, brands):
        for _, node in iter_items(blob):
            urls[node["source_url"]] += 1

    print(f"来源页 {len(urls)} 个，被引用 {sum(urls.values())} 次\n")

    now = {}
    for i, url in enumerate(sorted(urls), 1):
        status, text, rev = fetch(url)
        fp = fingerprint(text) if status == "ok" else None
        old = baseline.get(url, {})
        accepted = old.get("fingerprint")  # 上一次被认可的指纹
        if status != "ok":
            state = status.upper()
        elif not accepted:
            state = "BASELINE"  # 第一次记录，没有可比对象
        elif accepted != fp:
            state = "CHANGED"
        else:
            state = "UNCHANGED"
        if state in ("BASELINE", "UNCHANGED"):
            accepted = fp
        now[url] = {
            "status": status,
            # fingerprint 是「认可的基线」：CHANGED 时故意保持旧值，
            # 否则下一次运行会把新内容当基线，改动就自己消失了。
            "fingerprint": accepted,
            "seen_fingerprint": fp,  # 今天实际抓到的
            "chars": len(text),
            "rev_date": rev,
            "prev_rev_date": old.get("rev_date"),
            "prev_fingerprint": old.get("fingerprint"),
            "state": state,
            "changed_since": (old.get("changed_since") or today) if state == "CHANGED" else None,
            "first_seen": old.get("first_seen") or today,
            "last_ok": today if status == "ok" else old.get("last_ok"),
        }
        flag = {
            "CHANGED": "!!",
            "UNCHANGED": "ok",
            "BASELINE": "+ ",
        }.get(state, "x ")
        revnote = ""
        if rev and rev != now[url]["prev_rev_date"] and now[url]["prev_rev_date"]:
            revnote = f"  rev {now[url]['prev_rev_date']} -> {rev}"
        print(f"  [{i:>2}/{len(urls)}] {flag} {state:<11} {len(text):>8}B  {url}{revnote}")
        time.sleep(0.25)

    tally = Counter(v["state"] for v in now.values())
    print("\n状态汇总：")
    for k, v in tally.most_common():
        print(f"  {k:<12} {v}")

    changed = [u for u, v in now.items() if v["state"] == "CHANGED"]
    down = [u for u, v in now.items() if v["state"] not in ("CHANGED", "UNCHANGED", "BASELINE")]
    if changed:
        print(f"\n内容变了的页面：{len(changed)}")
        print("  基线会一直停在改动前的版本，直到你确认后跑 --apply --force。")
        for u in changed:
            aff = [f"articles{p}" for p, n in iter_items(articles) if n["source_url"] == u]
            aff += [f"brands{p}" for p, n in iter_items(brands) if n["source_url"] == u]
            since = now[u].get("changed_since") or today
            print(f"  {u}")
            print(f"      最早发现于 {since}    影响 {len(aff)} 条：{', '.join(aff[:6])}{' ...' if len(aff) > 6 else ''}")
            ov, nv = now[u].get("prev_fingerprint"), now[u].get("seen_fingerprint")
            if ov and nv:
                print(f"      指纹 {ov} -> {nv}（{now[u].get('chars', 0)}B）")
    if down:
        print(f"\n抓不到的页面：{len(down)}")
        for u in down:
            print(f"  {now[u]['state']:<14} {u}")

    # 只有「抓取成功且内容没变」的来源，才允许把 checked 推到今天
    ok_sources = {u for u, v in now.items() if v["state"] in ("UNCHANGED", "BASELINE")}
    blocked = apply and changed and not force

    if apply and not blocked:
        changed_n = 0
        for blob in (articles, brands):
            for _, node in iter_items(blob):
                if node["source_url"] in ok_sources and node.get("checked") != today:
                    node["checked"] = today
                    changed_n += 1
        if changed_n:
            (DATA / "articles.json").write_text(json.dumps(articles, ensure_ascii=False, indent=1), encoding="utf-8")
            (DATA / "brands.json").write_text(json.dumps(brands, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"\nchecked 推进到 {today}：{changed_n} 条")
    elif blocked:
        changed_n = 0
        print(f"\n有 {len(changed)} 个来源页内容变了，不推进任何日期。看过之后再跑 --apply --force。")
    else:
        changed_n = 0
        print("\n[dry] 未写 data/*.json")

    # --apply --force 表示人已经看过新内容并认可：把新指纹收为基线，解除告警
    if force and apply:
        for u in changed:
            now[u]["fingerprint"] = now[u]["seen_fingerprint"]
            now[u]["changed_since"] = None

    BASE.write_text(json.dumps(now, ensure_ascii=False, indent=1), encoding="utf-8")
    report = {
        "date": today,
        "sources": len(urls),
        "tally": dict(tally),
        "changed": changed,
        "unreachable": down,
        "detail": now,
    }
    (DOCS / f"daily-verify-{today}.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8"
    )

    # 机器可读的统计行：全 ASCII，避免 Windows 控制台 GBK 把中文吞掉后解析失败
    fetch_ok = sum(1 for v in now.values() if v["status"] == "ok")
    print(f"STAT sources={len(urls)} fetch_ok={fetch_ok} "
          f"unchanged={tally.get('UNCHANGED', 0)} baseline={tally.get('BASELINE', 0)} "
          f"changed={len(changed)} unreachable={len(down)} applied={changed_n}")

    print(f"报告：docs/daily-verify-{today}.json")
    print(f"基线：data/source_baseline.json")
    return 1 if (changed and not force) else 0


if __name__ == "__main__":
    raise SystemExit(main())
