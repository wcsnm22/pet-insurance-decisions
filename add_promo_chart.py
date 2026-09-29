# One-shot: insert the self-drawn SVG infographic into the last S1 guide that still
# has no figure (line-5 debt: pet-insurance-promo-code). Every number in the SVG is
# already a fact of the same article, checked 2026-09-25.
import json
import pathlib

ROOT = pathlib.Path(__file__).parent
P = ROOT / "data" / "articles.json"

CFG = {
    "slug": "pet-insurance-promo-code",
    "h2": "Every published discount, charted",
    "svg": "promo-discounts.svg",
    "height": 570,
    "alt": (
        "Bar chart of every pet insurance discount the three brands publish on one 0 to 20 "
        "percent scale: Spot employer plans up to 20 percent, Lemonade multi-pet up to 10 "
        "percent, Lemonade bundle up to 10 percent, Spot 10 percent on the 2nd pet and every "
        "pet after, Fetch 10 percent every month for life for military and AARP members, Fetch "
        "10 percent for a whole year for Walmart shoppers, Lemonade up to 5 percent when you "
        "pay for a full year, with the fine print for each brand underneath and no promo-code "
        "page in any of the three official sitemaps, checked 2026-09-25"
    ),
    "caption": (
        "Every percentage is printed on the brand's own renewals, multi-pet, employer, FAQ or "
        "partner pages (all read 2026-09-25), and the bars share one 0-20% scale. What the "
        "discount does not cover differs per brand, so compare the fine print before counting "
        "on a number - the table below links every figure to the page it came from."
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
