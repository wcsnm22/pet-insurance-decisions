"""Narrow the two provenance declarations on the Lemonade cat page to the official-sourced parts only.

Targets exactly two strings on one article:
  facts_note  - the line under the hero
  disclaimer  - the line above the footer
Nothing else in data/articles.json is touched. The page's owner-reported cases section is out of
scope for both declarations and is left byte-for-byte alone.
"""
import json
from pathlib import Path

ARTICLES = Path(__file__).resolve().parent / "data" / "articles.json"
SLUG = "lemonade-cat-insurance"

FACTS_NOTE = (
    "Every figure in the brand-facts sections and in the official source table below was read from "
    "Lemonade's own official site and carries its source link and check date. The owner-reported "
    "section further down uses separate sourcing."
)

DISCLAIMER = (
    "This page is not affiliated with Lemonade. In the brand-facts sections and the official source "
    "table, it repeats only what Lemonade publishes on its own cat, cost, claim and "
    "pre-existing-condition pages, with the source and check date attached to every figure; the "
    "owner-reported section further down states its own sourcing. Policy terms always govern and your "
    "own quote and renewal will differ. Facts last checked 2026-09-28."
)

data = json.loads(ARTICLES.read_text(encoding="utf-8"))
art = next(a for a in data["articles"] if a["slug"] == SLUG)

before = {"facts_note": art.get("facts_note"), "disclaimer": art.get("disclaimer")}
# snapshot every other article's declarations so we can prove none of them moved
others_before = {a["slug"]: (a.get("facts_note"), a.get("disclaimer")) for a in data["articles"] if a["slug"] != SLUG}

art["facts_note"] = FACTS_NOTE
art["disclaimer"] = DISCLAIMER
after = {"facts_note": art["facts_note"], "disclaimer": art["disclaimer"]}

others_after = {a["slug"]: (a.get("facts_note"), a.get("disclaimer")) for a in data["articles"] if a["slug"] != SLUG}
moved = [s for s in others_before if others_before[s] != others_after[s]]
ARTICLES.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

print("BEFORE facts_note :", before["facts_note"] or "(unset -> template default)")
print("BEFORE disclaimer :", before["disclaimer"])
print()
print("AFTER  facts_note :", after["facts_note"])
print("AFTER  disclaimer :", after["disclaimer"])
print()
print("other articles whose declarations moved:", moved or "none")
print("total articles:", len(data["articles"]))
