# One-shot: insert the self-drawn SVG infographic into the last P1 guide that
# has no <figure> data chart (line-5 debt: pet-insurance-claim-denied still has
# only the old direct <img src=/assets/appeal-flow.svg>). Every number in the
# SVG is already a fact of the same article, checked 2026-09-25: Fetch's
# 90-day appeal deadline, Spot's ~30-day review time, and the two "not
# published" absences that are stated in the article's compare rows.
import json
import pathlib

ROOT = pathlib.Path(__file__).parent
P = ROOT / "data" / "articles.json"

CFG = {
    "slug": "pet-insurance-claim-denied",
    "h2": "Appeal deadlines and review times, charted",
    "svg": "appeal-deadlines.svg",
    "height": 580,
    "alt": (
        "Bar chart and route cards for appealing a denied claim: top panel plots the "
        "appeal deadline after a denial on one 0-90 day scale - Fetch is the only brand "
        "with a printed deadline, 90 days from the denial in its policy's APPEALS section, "
        "while Spot and Lemonade are shown as not published on the pages cited; bottom "
        "cards give each brand's published route and review time - Lemonade in the app "
        "with extra vet documents and no time published, Spot by email in writing with a "
        "review of around 30 days, Fetch in writing within 90 days followed by an Internal "
        "Review with a written notice but no published duration; all read 2026-09-25"
    ),
    "caption": (
        "The top panel is one scale: only Fetch prints an appeal deadline - 90 days from "
        "the denial, in its policy's section 2 (APPEALS). Spot's and Lemonade's cited pages "
        "print no deadline at all, which is what the dashed rows mean; it is not our estimate. "
        "The cards below count a different thing - the review time each brand publishes - so "
        "the 90 days and the ~30 days are not the same measurement and cannot be subtracted "
        "from each other. Every figure read from the linked official pages on 2026-09-25."
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
