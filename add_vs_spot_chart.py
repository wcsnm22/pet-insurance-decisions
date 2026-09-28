# One-shot: insert a self-drawn SVG infographic into the lemonade-vs-spot guide
# (line-5 debt: S1 oldest guides still without a figure). Every number in the SVG
# is already a fact/row of this same article, checked 2026-09-25.
import json
import pathlib

ROOT = pathlib.Path(__file__).parent
P = ROOT / "data" / "articles.json"

CFG = {
    "slug": "lemonade-vs-spot",
    "h2": "Prices and windows, charted",
    "svg": "lemonade-vs-spot-windows.svg",
    "height": 700,
    "alt": (
        "Bar charts of what Lemonade and Spot each publish: starting prices of 10 dollars "
        "for Lemonade and 15 dollars dogs, 9 dollars cats for Spot, Lemonade averages of 48 "
        "dollars dogs and 27 dollars cats, Lemonade's 61 dollar example quote, and Spot "
        "publishing no average; and windows in days - 14-day illness waits for both brands, "
        "30-day orthopedic wait and 30-day cancellation refund at Lemonade, 30-day money-back "
        "window at Spot and 180 symptom-free days for a curable pre-existing condition, "
        "checked 2026-09-25"
    ),
    "caption": (
        "Every bar is a figure the brand prints on its own pages (facts checked 2026-09-25). "
        "The two panels use different units - dollars per month on the left, days on the right - "
        "so nothing can be subtracted across panels; the table below keeps each figure's "
        "conditions and links it to the page it came from."
    ),
}


def figure_html(cfg):
    return (
        '<figure style="margin:1.2em 0">'
        f'<img src="/assets/{cfg["svg"]}" alt="{cfg["alt"]}" width="720" '
        f'height="{cfg["height"]}" loading="lazy" '
        'style="max-width:100%;height:auto;border:1px solid #e4e9ee;border-radius:8px">'
        f"<figcaption>{cfg['caption']}</figcaption></figure>"
    )


data = json.loads(P.read_text(encoding="utf-8"))
art = next((a for a in data["articles"] if a["slug"] == CFG["slug"]), None)
if art is None:
    raise SystemExit(f"missing article: {CFG['slug']}")
if any(CFG["svg"] in json.dumps(b, ensure_ascii=False) for b in art["blocks"]):
    print("already has figure:", CFG["slug"])
else:
    idx = next(i for i, b in enumerate(art["blocks"]) if b["type"] == "compare")
    art["blocks"].insert(
        idx + 1, {"type": "section", "h2": CFG["h2"], "html": figure_html(CFG)}
    )
    print("inserted figure after compare block:", CFG["slug"])
    P.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("written", P)
