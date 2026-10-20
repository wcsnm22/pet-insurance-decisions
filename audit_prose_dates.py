#!/usr/bin/env python3
"""找出正文里「过时」的日期。

判据要说清楚，否则会误报：
  * 正文里的日期有很多种语义 —— 「我们哪一天读过这一页」是历史动作，
    一旦写下就一直成立；而「本页事实截至哪天」是当前状态，必须跟着走。
  * 所以这里不按「不等于最新日期就报」来判，而是：
      - 收集本页所有记录自己的 checked 日期集合 S；
      - 正文里出现的日期，只要它 ∈ S，就算仍然成立（那天确实读过）；
      - 不在 S 里的，才是真正对不上的残留，列出来人工看。
  * 另有一条硬规则：如果本页有来源今天没核对成功（比如一直 403），
    本页就不得对外声称「所有数字都在今天重新核对过」——这一条单独报出来。
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
ISO = re.compile(r"20\d\d-\d\d-\d\d")
CURRENT_CLAIM = re.compile(
    r"(?i)(facts?\s+(last\s+)?checked|every\s+figure[^.]{0,80}?checked|"
    r"re-?checked|all\s+figures?\s+(were\s+)?read)"
)


def walk(node, path=""):
    if isinstance(node, dict):
        if isinstance(node.get("source_url"), str) and ("fact" in node or "q" in node):
            yield path, node
        else:
            for k, v in node.items():
                yield from walk(v, f"{path}/{k}")
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from walk(v, f"{path}[{i}]")


def dates_in(obj):
    return set(ISO.findall(json.dumps(obj, ensure_ascii=False)))


def main():
    A = json.loads((DATA / "articles.json").read_text(encoding="utf-8"))
    B = json.loads((DATA / "brands.json").read_text(encoding="utf-8"))
    baseline = json.loads((DATA / "source_baseline.json").read_text(encoding="utf-8"))
    # 今天核对成功的来源
    verified = {u for u, v in baseline.items() if v["state"] in ("UNCHANGED", "BASELINE")}

    problems = []
    unverifiable = []

    pages = []
    for a in A["articles"]:
        pages.append((a["slug"], a["facts"] + a["faqs"],
                      {k: v for k, v in a.items() if k not in ("facts", "faqs")}))
    for b in B["brands"]:
        pages.append((b["slug"], b["facts"] + b["faqs"],
                      {k: v for k, v in b.items() if k not in ("facts", "faqs")}))
    pages.append(("<home>", B["home_facts"] + B["home_faqs"], {}))

    for slug, items, rest in pages:
        S = {i["checked"] for i in items if i.get("checked")}
        # 本页出现的所有日期（含正文、stats、表格、小节）
        seen = dates_in(rest) | dates_in(items)
        orphan = seen - S
        if orphan:
            problems.append((slug, sorted(orphan), "正文日期不在本页任何记录的核查日里"))

        # 本页有没有今天没核对成功的来源
        bad = {i["source_url"] for i in items if i["source_url"] not in verified}
        if bad:
            unverifiable.append((slug, len(bad), sorted(bad)))
            newest = max(S) if S else ""
            for where, text in [
                ("disclaimer", rest.get("disclaimer") or ""),
                ("lede", rest.get("lede") or ""),
            ]:
                if newest and re.search(re.escape(newest), text) and CURRENT_CLAIM.search(text):
                    problems.append(
                        (slug, [newest],
                         f"{where} 声称所有数字在 {newest} 核对过，但本页有 {len(bad)} 个来源没核对成功"))

    for slug, ds, why in problems:
        print(f"[STALE] {slug}: {ds} — {why}")
    if unverifiable:
        print("\n以下页面的部分来源今天没核对成功（403/超时），这些页不能声称整体已核对：")
        for slug, n, urls in unverifiable:
            print(f"  {slug}: {n} 个")
            for u in urls:
                print(f"      {u}")

    print(f"\n过时/越界声明 {len(problems)} 处；有不可核对来源的页面 {len(unverifiable)} 个")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
