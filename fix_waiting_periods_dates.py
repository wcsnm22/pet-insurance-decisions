"""Second pass: make the two remaining Jun 3, 2026 references accurate.

1. The "How this page was checked" section describes what was read on
   2026-09-28. That reading really did see "Last Updated: Jun 3, 2026", so the
   sentence stays true - but it now needs the word "then" so a reader does not
   mistake it for the current date.
2. The cost fact quotes Lemonade's cost guide as "last updated Jun 3, 2026".
   That guide was re-read on 2026-10-20 and is now marked Oct 13, 2026. The
   figure it supports (base policies "start around $10 per month") did not
   change, so only the date moves, and checked moves with it.

Idempotent: both replacements are guarded by the presence of the old string.
"""

import json
from pathlib import Path

ROOT = Path(__file__).parent
DATA = ROOT / "data" / "articles.json"
SLUG = "pet-insurance-waiting-periods"
CHECKED = "2026-10-20"

data = json.loads(DATA.read_text(encoding="utf-8"))
art = next(a for a in data["articles"] if a["slug"] == SLUG)

changed = []

# 1. section wording: this is history, mark it as history
for blk in art["blocks"]:
    if blk.get("h2") == "How this page was checked":
        old = "its waiting-period guide (page marked Last Updated: Jun 3, 2026)"
        new = "its waiting-period guide (page then marked Last Updated: Jun 3, 2026)"
        if old in blk["html"]:
            blk["html"] = blk["html"].replace(old, new, 1)
            changed.append("section wording")

# 2. cost fact: the guide behind it was revised on 13 October 2026
for fact in art["facts"]:
    if "Lemonade cost guide, last updated Jun 3, 2026" in fact.get("condition", ""):
        fact["condition"] = fact["condition"].replace(
            "Lemonade cost guide, last updated Jun 3, 2026",
            "Lemonade cost guide, which carried Last Updated: Oct 13, 2026 when "
            "re-read on 2026-10-20; the $10 figure was unchanged",
        )
        fact["checked"] = CHECKED
        changed.append("cost fact date")

DATA.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("changed:", changed if changed else "nothing (already applied)")
