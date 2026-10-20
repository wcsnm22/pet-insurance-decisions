#!/usr/bin/env python3
"""把「页面级核查日期」同步成该页记录里最新的 checked。

区分两类日期，这是本次修复的核心：
  * 条目级历史日期（facts/faqs 正文里的「read 2026-09-28」）—— 由
    sync_prose_dates.py 按每条记录自己的 checked 处理。
  * 页面级当前状态（stats 卡片、disclaimer 的「Facts last checked X」、
    表格里的「sitemap checked on X」、小节的「On X we read three pages」）——
    它宣称的是「本页事实截至哪天」，必须跟着本页最新的 checked 走，
    否则同一页上会同时出现两个互相矛盾的日期。

安全边界：
  * 只改紧邻 read/check 类动词的日期。品牌页自己声明的修订日期在本站一律写成
    「Oct 13, 2026」这种人读格式（不是 ISO），因此不会被误改；
    日期区间也用人读格式（07.01.2024 through 06.30.2025），同样不受影响。
  * 只在该页**所有**来源今天都核对成功时才推进。有来源 403 的页面
    不能对外声称整体已核对。
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
ISO = re.compile(r"20\d\d-\d\d-\d\d")
CLAIM = re.compile(
    r"(?i)(facts?\s+(last\s+)?checked|every\s+figure|all\s+figures?"
    r"|re-?checked|read|checked|verified|opened)")
NEAR = 220  # 日期前后多少字符内出现 claim 动词才算「核查日期」
# 220 是实测需要的宽度：句子常写成「Every discount on this page was read from
# the brand's own site - its renewals page, FAQ, employers page, partner pages
# or terms - on <strong>2026-09-25</strong>」，动词离日期超过 100 个字符。


def newest(items):
    ds = [i.get("checked") for i in items if i.get("checked")]
    return max(ds) if ds else ""


def rewrite(text, want, where, stats):
    """把 text 里紧邻 claim 动词的 ISO 日期换成 want。返回新文本。"""
    out, pos = [], 0
    for m in ISO.finditer(text):
        ctx = text[max(0, m.start() - NEAR):m.end() + NEAR]
        if not CLAIM.search(ctx):
            stats["skipped"].append((where, m.group(0), ctx.strip()[:90]))
            continue
        if m.group(0) == want:
            continue
        out.append(text[pos:m.start()])
        out.append(want)
        pos = m.end()
        stats["replaced"].append((where, m.group(0), want))
    out.append(text[pos:])
    return "".join(out)


def walk_strings(node, path, fn):
    if isinstance(node, str):
        return fn(node, path)
    if isinstance(node, dict):
        return {k: walk_strings(v, f"{path}.{k}", fn) for k, v in node.items()}
    if isinstance(node, list):
        return [walk_strings(v, f"{path}[{i}]", fn) for i, v in enumerate(node)]
    return node


def main():
    apply = "--apply" in sys.argv
    A = json.loads((DATA / "articles.json").read_text(encoding="utf-8"))
    baseline = json.loads((DATA / "source_baseline.json").read_text(encoding="utf-8"))
    verified = {u for u, v in baseline.items() if v["state"] in ("UNCHANGED", "BASELINE")}

    stats = {"replaced": [], "skipped": []}
    skipped_pages = []

    for a in A["articles"]:
        items = a["facts"] + a["faqs"]
        bad = {i["source_url"] for i in items if i["source_url"] not in verified}
        if bad:
            skipped_pages.append((a["slug"], len(bad)))
            continue
        want = newest(items)
        if not want:
            continue

        # stats 是结构化的一对 value/label：日期常常单独占 value，
        # 「every figure rechecked」写在 label 里，两半必须拼起来判断，
        # 否则纯日期永远匹配不到任何声明词。
        for s in a.get("stats") or []:
            val, lab = s.get("value"), s.get("label")
            if isinstance(val, str) and isinstance(lab, str) \
                    and ISO.fullmatch(val.strip()) and CLAIM.search(val + " " + lab):
                if val.strip() != want:
                    print(f"  {val} -> {want}   {a['slug']}.stats.value")
                    stats["replaced"].append((f"{a['slug']}.stats.value", val, want))
                    s["value"] = want

        # 只处理条目之外的页面级内容；facts/faqs 交给 sync_prose_dates.py
        shell = {k: v for k, v in a.items() if k not in ("facts", "faqs")}
        a_shell = walk_strings(shell, a["slug"], lambda t, p: rewrite(t, want, p, stats))
        for k in a_shell:
            a[k] = a_shell[k]

    if apply and stats["replaced"]:
        (DATA / "articles.json").write_text(
            json.dumps(A, ensure_ascii=False, indent=1), encoding="utf-8")

    for where, old, new in stats["replaced"]:
        print(f"  {old} -> {new}   {where}")
    for where, old, ctx in stats["skipped"]:
        print(f"  [keep] {old}  {where}   ...{ctx}...")
    for slug, n in skipped_pages:
        print(f"SKIP {slug}: {n} 个来源今天没核对成功，不动它的页面级日期")

    print(f"\n页面级日期替换 {len(stats['replaced'])} 处，保留 {len(stats['skipped'])} 处"
          + ("（已写入）" if apply else "（dry）"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
