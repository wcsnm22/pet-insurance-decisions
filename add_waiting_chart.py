# One-shot: insert the self-drawn SVG infographic into the N1 guide that DAILY
# published without one (line-5 debt: pet-insurance-waiting-periods-by-condition,
# "无 SVG，留待线五"). Every number in the SVG is already a fact of the same
# article, checked 2026-09-29.
import json
import pathlib

ROOT = pathlib.Path(__file__).parent
P = ROOT / "data" / "articles.json"

CFG = {
    "slug": "pet-insurance-waiting-periods-by-condition",
    "h2": "Every published day count, charted",
    "svg": "waiting-period-day-counts.svg",
    "height": 740,
    "alt": (
        "Horizontal bar chart of every waiting-period day count the three brands print: GEICO "
        "prints none and its guide says ask an agent; Allstate prints one number, a 14-day "
        "(2-week) illness wait; ASPCA's quote table prints 0 days for accidents and preventive "
        "care and 14 days for illness, hereditary and ligament and knee conditions, while the "
        "text on the same page says accidents start after 14 days; second panel charts the "
        "Embrace contract behind GEICO and Allstate - V5 states accident 2 days, illness 14 "
        "days, dogs orthopedic 6 months, V6 states accident no wait, illness 14 days, "
        "cruciate and knee 180-day exclusion, exam waiver as few as 14 days, cats orthopedic "
        "14 days; all read 2026-09-29"
    ),
    "caption": (
        "Every bar is a day count printed on the brand's own pages or in the Embrace sample "
        "contracts GEICO's and Allstate's footers link to, all read 2026-09-29. ASPCA's quote "
        "page carries two different accident answers - 0 days in the table, 14 days in the text "
        "- and the six-month figure stays in months because that is how the contract prints it."
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
