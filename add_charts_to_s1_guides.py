# One-shot: insert a self-drawn SVG infographic into the two oldest S1 guides that
# still had no figure (line-5 debt listed in the progress file as "S1 5 篇尚无自绘 SVG").
# Every number in the two SVGs is already a fact of the same article, checked 2026-09-25.
import json
import pathlib

ROOT = pathlib.Path(__file__).parent
P = ROOT / "data" / "articles.json"

FIGS = {
    "best-pet-insurance": {
        "h2": "Published prices, charted",
        "svg": "published-prices.svg",
        "height": 560,
        "alt": (
            "Bar chart of published pet insurance prices: starting price of 10 dollars for "
            "Lemonade and 15 dollars dogs, 9 dollars cats for Spot with Fetch publishing none, "
            "and average price of 48 dollars dogs, 27 dollars cats for Lemonade and 35 dollars "
            "dogs, 22 dollars cats for Fetch with Spot publishing none, checked 2026-09-25"
        ),
        "caption": (
            "Starting price and average price, drawn only from numbers each brand publishes on "
            "its own pages (facts checked 2026-09-25). The three brands publish three different "
            "kinds of number, so the table below links every figure to the page it came from."
        ),
    },
    "pet-insurance-cost": {
        "h2": "Where the price changes, charted",
        "svg": "state-averages.svg",
        "height": 600,
        "alt": (
            "Chart of published pet insurance prices: Lemonade state average bands of 45 to 49 "
            "dollars in California and Connecticut, 40 to 44 in Illinois and New York, 35 to 39 "
            "in Florida and Arizona and 30 to 34 in Texas, Ohio, Pennsylvania, Georgia and "
            "Michigan, plus the example quote each brand prints - Lemonade 61 dollars, Spot from "
            "15 dollars dogs and from 9 dollars cats, Fetch not published, checked 2026-09-25"
        ),
        "caption": (
            "Lemonade's published state bands (internal data as of October 2024) and the example "
            "quote each brand prints, read 2026-09-25. Each example keeps its own deductible, "
            "limit and reimbursement, so the bars are not comparable across brands - the table "
            "below carries the assumptions and the source link for every figure."
        ),
    },
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

for slug, cfg in FIGS.items():
    art = next((a for a in data["articles"] if a["slug"] == slug), None)
    if art is None:
        raise SystemExit(f"missing article: {slug}")
    if any(cfg["svg"] in json.dumps(b, ensure_ascii=False) for b in art["blocks"]):
        print("already has figure:", slug)
        continue
    idx = next(i for i, b in enumerate(art["blocks"]) if b["type"] == "compare")
    art["blocks"].insert(
        idx + 1, {"type": "section", "h2": cfg["h2"], "html": figure_html(cfg)}
    )
    print("inserted figure after compare block:", slug)

P.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("written", P)
