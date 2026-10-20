"""Propagate Lemonade's 13 October 2026 revision to every page that dates it.

Lemonade's cost guide and its waiting-period guide were both re-read on
2026-10-20 and both now carry "Last Updated: Oct 13, 2026" (they carried
Jun 3, 2026 when this site first cited them). The numbers on those pages did
not move:
  * cost guide  - "starts at $10/month" (11 occurrences), $48/month dogs,
                  $27/month cats, and the "as of October, 2024" analysis stamp
                  are all still printed verbatim;
  * waiting guide - 0 / 14 / 30 days, unchanged.
So only the date a page records needs to move, plus the check date. Where the
old date is quoted as history ("it was marked Jun 3, 2026 when this page first
cited it") it is left alone on purpose.

Idempotent: every replacement is guarded by the old string still being present.
"""

import json
from pathlib import Path

ROOT = Path(__file__).parent
DATA = ROOT / "data" / "articles.json"
CHECKED = "2026-10-20"
OLD = "Jun 3, 2026"
NEW = "Oct 13, 2026"

data = json.loads(DATA.read_text(encoding="utf-8"))
log: list[str] = []


def swap(text: str, old: str, new: str, where: str) -> str:
    if old in text:
        log.append(f"{where}: {old[:60]!r}")
        return text.replace(old, new)
    return text


for art in data["articles"]:
    slug = art["slug"]

    # ---- cost-by-brand: this page's whole thesis is the date stamp
    if slug == "pet-insurance-cost-by-brand":
        for fact in art["facts"]:
            if fact["source_url"].endswith("/pet-insurance-guide/pet-insurance-cost/"):
                fact["condition"] = swap(
                    fact["condition"],
                    f"the page is marked Last Updated: {OLD}",
                    f"the page was marked Last Updated: {NEW} when re-read on {CHECKED}",
                    f"{slug} fact condition",
                )

        for faq in art["faqs"]:
            faq["a"] = swap(
                faq["a"],
                f'Lemonade marks its guide "Last Updated: {OLD}"',
                f'Lemonade marks its guide "Last Updated: {NEW}" (it read '
                f'{OLD} when first cited, and the analysis behind the averages '
                f'still reads "as of October, 2024")',
                f"{slug} faq",
            )
            if OLD not in faq["a"] and faq["checked"] < CHECKED:
                faq["checked"] = CHECKED

        for blk in art["blocks"]:
            if blk.get("type") != "section":
                continue
            if blk["h2"] == "How this page was checked":
                blk["html"] = swap(
                    blk["html"],
                    f"its pet insurance cost guide (page marked Last Updated: {OLD})",
                    f"its pet insurance cost guide (page then marked Last Updated: {OLD}, "
                    f"and re-read on {CHECKED} showing Last Updated: {NEW})",
                    f"{slug} checked-section",
                )
            if blk["h2"].startswith("The date stamp"):
                blk["html"] = swap(
                    blk["html"],
                    f"Lemonade dates the <em>page</em> ({OLD})",
                    f"Lemonade dates the <em>page</em> ({NEW}, as re-read on "
                    f"{CHECKED}; it read {OLD} before the revision)",
                    f"{slug} datestamp-section",
                )

        for row in art["rows"]:
            for i, cell in enumerate(row["cells"]):
                row["cells"][i] = swap(
                    cell,
                    f"the guide page is marked Last Updated: {OLD} (read 2026-09-28)",
                    f"the guide page is marked Last Updated: {NEW} (read {CHECKED})",
                    f"{slug} row '{row['label']}'",
                )
                row["cells"][i] = swap(
                    row["cells"][i],
                    f'Guide page marked "Last Updated: {OLD}"',
                    f'Guide page marked "Last Updated: {NEW}"',
                    f"{slug} row '{row['label']}'",
                )

    # ---- best-pet-insurance: one average-price fact cites the same guide
    if slug == "best-pet-insurance":
        for fact in art["facts"]:
            if fact["source_url"].endswith("/pet-insurance-guide/pet-insurance-cost/"):
                fact["condition"] = swap(
                    fact["condition"],
                    f"(last updated {OLD})",
                    f"(last updated {NEW}; re-read {CHECKED}, the averages themselves unchanged)",
                    f"{slug} fact condition",
                )
                fact["checked"] = CHECKED

DATA.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

if log:
    print(f"{len(log)} replacement(s):")
    for line in log:
        print("  -", line)
else:
    print("nothing to change (already applied)")
