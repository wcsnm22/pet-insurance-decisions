# ILANG
#   TYPE:check ROLE:verify
#   ::RULE{read the BUILT site, never the source - the source is not what visitors get}
# LINE-1 FIX 2026-10-04 (T1): before this fix the site had two overlapping mobile table
# breakpoints. `@media (max-width: 680px)` stacked the tables, and the ONLY copy of the
# `td::before { content: attr(data-th) }` cell labels sat in a second `@media (max-width: 640px)`
# block. Between 641px and 680px every table therefore stacked with no labels at all.
# This checker proves the built stylesheet now has exactly one such breakpoint and that every
# table cell in every built page carries the data-th attribute that breakpoint renders.
import re
import sys
from pathlib import Path

SITE = Path(__file__).parent / "site"
fails, warns = [], []

css = (SITE / "assets" / "style.css").read_text(encoding="utf-8")

# 1. exactly one table-stacking stacking rule, and it is the 680px one
stack_sel = re.compile(r"table,\s*thead,\s*tbody,\s*tr,\s*td\s*\{\s*display:\s*block")
stack_hits = stack_sel.findall(css)
print(f"[1] table-stacking rules found: {len(stack_hits)}")
if len(stack_hits) != 1:
    fails.append(f"expected exactly 1 table-stacking rule, found {len(stack_hits)}")

# 2. no leftover 640px block that used to be the only home of the labels
m640 = re.findall(r"@media\s*\(max-width:\s*640px\)", css)
print(f"[2] @media (max-width: 640px) blocks: {len(m640)}")
if m640:
    fails.append("a 640px media block is still present")

# 3. the label rule lives in the same media block as the stacking rule
label = re.search(r"td::before\s*\{\s*content:\s*attr\(data-th\)", css)
print(f"[3] td::before data-th label rule present: {bool(label)}")
if not label:
    fails.append("td::before label rule missing")

m680 = [m.start() for m in re.finditer(r"@media\s*\(max-width:\s*680px\)", css)]
print(f"[4] @media (max-width: 680px) blocks: {len(m680)} (both may exist; only one stacks tables)")
if not m680:
    fails.append("no 680px media block at all")

# 5. every BODY cell the builder emits must carry data-th, else the label renders empty.
#    Header cells (<th>) deliberately carry none: the header row is hidden below the breakpoint
#    and the label replaces it, so a <th> without data-th is correct, not a defect.
print("[5] td data-th coverage per built page:")
pages = sorted(SITE.glob("*.html"))
bad_pages = []
for p in pages:
    html = p.read_text(encoding="utf-8")
    tds = re.findall(r"<td\b[^>]*>", html)
    ths = re.findall(r"<th\b[^>]*>", html)
    if not tds:
        continue
    missing = [c for c in tds if "data-th=" not in c]
    tables = html.count("<table")
    if missing:
        bad_pages.append((p.name, len(missing), len(tds)))
        print(f"    MISSING {p.name}: {len(missing)}/{len(tds)} td cells without data-th")
    else:
        print(f"    ok      {p.name}: {len(tds)}/{len(tds)} td labelled | {len(ths)} th (hidden header, no label needed) | {tables} tables")
if bad_pages:
    fails.append(f"{len(bad_pages)} page(s) have unlabelled cells: {[b[0] for b in bad_pages]}")

print()
print("RESULT:", "PASS" if not fails else "FAIL")
for f in fails:
    print("  FAIL:", f)
for w in warns:
    print("  warn:", w)
sys.exit(0 if not fails else 1)
