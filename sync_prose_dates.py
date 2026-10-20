#!/usr/bin/env python3
"""把正文里写死的核查日期，同步成该条记录自己的 checked 日期。

为什么需要：
  这些事实/问答的正文里常写「(checked 2026-09-28)」「read 2026-09-28」，
  说的是「我们哪一天读过这一页」。核对器把 checked 推到 2026-10-20 之后，
  结构化字段写 2026-10-20、正文却还写 2026-09-28，同一页上两个日期，
  读者会以为其中一个是错的。既然核对器只在「整页指纹未变」时才推进日期，
  把正文日期一起推上去是准确的 —— 那页今天确实又读过一次，内容一字未改。

安全的边界（只动这两类，其余原样保留）：
  * 正文里形如 2026-09-28 的 ISO 日期；
  * 且它不等于该条的 checked。
  品牌页自己声明的修订日期在本站一律写成「Oct 13, 2026」这种人读格式，
  不是 ISO，因此不会被误改 —— 已用正则扫过全站确认这一点。

用法：
  python sync_prose_dates.py          # 只报告
  python sync_prose_dates.py --apply  # 真改
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
ISO = re.compile(r"20\d\d-\d\d-\d\d")


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


def main():
    apply = "--apply" in sys.argv
    total = 0
    changed_items = 0
    for name in ("articles.json", "brands.json"):
        p = DATA / name
        blob = json.loads(p.read_text(encoding="utf-8"))
        for path, node in walk(blob):
            want = node.get("checked")
            if not want:
                continue
            touched = False
            for k in ("fact", "a", "condition", "q"):
                t = node.get(k)
                if not isinstance(t, str):
                    continue
                hits = [d for d in ISO.findall(t) if d != want]
                if not hits:
                    continue
                for d in set(hits):
                    t = t.replace(d, want)
                node[k] = t
                total += len(hits)
                touched = True
                print(f"  {path}/{k}: {sorted(set(hits))} -> {want}")
            if touched:
                changed_items += 1
        if apply:
            p.write_text(json.dumps(blob, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\n替换 {total} 处日期，涉及 {changed_items} 条记录"
          + ("（已写入）" if apply else "（dry，未写入）"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
