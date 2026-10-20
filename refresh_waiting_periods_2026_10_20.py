"""Refresh the waiting-periods page against Lemonade's 13 October 2026 rewrite.

Why this file exists
--------------------
The site's waiting-periods page cites Lemonade's waiting-period guide and
records it as "Last Updated: Jun 3, 2026". On 2026-10-20 the same URL was read
again and now carries "Last Updated: Oct 13, 2026", with a large block of new
material: a per-question FAQ set, five worked scenarios, and an explicit
"Reddit asked, we answered" section. The page therefore had a stale check date
and was missing every one of those answers.

This script is idempotent: it removes any section whose h2 matches one it is
about to write, skips facts/FAQs whose text is already present, then inserts.
Running it twice leaves the data file byte-identical.

Every fact written here carries the official Lemonade URL and checked date
2026-10-20, which is what build.py validates against OFFICIAL_HOSTS.
"""

import json
from pathlib import Path

ROOT = Path(__file__).parent
DATA = ROOT / "data" / "articles.json"
SLUG = "pet-insurance-waiting-periods"
CHECKED = "2026-10-20"
GUIDE = "https://www.lemonade.com/pet/insurance-guide/waiting-periods/"
PRODUCT = "https://www.lemonade.com/pet-insurance"

# ---------------------------------------------------------------- new facts
NEW_FACTS = [
    {
        "fact": (
            "Lemonade's waiting-period guide is now marked Last Updated: "
            "Oct 13, 2026 - it was marked Jun 3, 2026 when this page first "
            "cited it, and the whole guide was rewritten around the same "
            "0 / 14 / 30 day table"
        ),
        "condition": (
            "The date line at the top of the guide. The table beneath it is "
            "unchanged: accidents 0 days, illnesses 14 days, orthopedic "
            "conditions 30 days, pre-existing conditions never covered"
        ),
        "source_url": GUIDE,
        "checked": CHECKED,
    },
    {
        "fact": (
            "Illness coverage starts at \"12:01 AM on day 15\" of a 14-day "
            "wait - and a pet that shows symptoms on day 10 is not covered for "
            "that condition, because the wait has to finish completely before "
            "coverage begins"
        ),
        "condition": (
            "FAQ \"Will my pet be covered if they get sick on day 10 of a "
            "14-day waiting period?\" - the clock is counted to the minute, "
            "not to the day"
        ),
        "source_url": GUIDE,
        "checked": CHECKED,
    },
    {
        "fact": (
            "Lemonade lists what counts as \"showing signs\" during the wait: "
            "limping, vomiting, changes in appetite, lethargy, unusual "
            "behaviour, or symptoms a vet observes during an exam"
        ),
        "condition": (
            "FAQ \"What counts as showing signs of an illness during the "
            "waiting period?\" - these are the observations that convert a "
            "later diagnosis into a pre-existing condition"
        ),
        "source_url": GUIDE,
        "checked": CHECKED,
    },
    {
        "fact": (
            "A surgery or treatment scheduled before the waiting period ends "
            "is not covered even when the procedure itself takes place after "
            "the wait, because the timing shows the condition was already "
            "present or suspected"
        ),
        "condition": (
            "FAQ \"Can I get reimbursement for a surgery that was scheduled "
            "before the waiting period ended?\" - the scheduling date matters, "
            "not the surgery date"
        ),
        "source_url": GUIDE,
        "checked": CHECKED,
    },
    {
        "fact": (
            "Lemonade says no vet exam is required before buying a policy, and "
            "that waiting periods apply to every pet regardless of age - "
            "including a two-month-old puppy"
        ),
        "condition": (
            "FAQs \"Do I need to take my pet for a vet exam before I can get "
            "insurance?\" and \"If my puppy is only 2 months old, does the "
            "waiting period still apply?\" - only the preventative add-on "
            "starts without a wait"
        ),
        "source_url": GUIDE,
        "checked": CHECKED,
    },
    {
        "fact": (
            "Lemonade defines orthopedic conditions as those affecting bones, "
            "joints, ligaments and tendons - naming cruciate ligament "
            "injuries, hip dysplasia and arthritis as examples - and says the "
            "30-day wait exists because these develop gradually or have "
            "genetic components"
        ),
        "condition": (
            "FAQ \"What are orthopedic conditions and why do they have a "
            "30-day waiting period?\" - arthritis is named inside the "
            "orthopedic bucket, not treated as an illness"
        ),
        "source_url": GUIDE,
        "checked": CHECKED,
    },
    {
        "fact": (
            "Lemonade states the policy itself goes into effect at \"12:01 AM "
            "the day after purchase\", and that there is \"no such thing as "
            "truly same-day coverage\""
        ),
        "condition": (
            "FAQs \"How long does pet insurance take to go into effect?\" and "
            "\"Can pet insurance be active the same day?\" - the answer sits "
            "next to the claim that accident cover \"kicks in immediately\""
        ),
        "source_url": GUIDE,
        "checked": CHECKED,
    },
    {
        "fact": (
            "Spot's own waiting-period blog prints the same industry spread "
            "Lemonade does: accidents \"usually range from 0-15 days\", "
            "orthopedic conditions \"often 6-12 months\", and a 14-day illness "
            "wait as the norm"
        ),
        "condition": (
            "Spot blog page dated 09/25/2026 - independent of the state sample "
            "policies already cited on this page, and consistent with them"
        ),
        "source_url": "https://spotpet.com/blog/why-pet-insurance/what-is-the-waiting-period-in-pet-insurance",
        "checked": CHECKED,
    },
]

# ------------------------------------------------------------- new sections
SECTION_UPDATE = (
    "What Lemonade changed on 13 October 2026",
    "<p>Lemonade rewrote its waiting-period guide on 13 October 2026 and left "
    "the day counts alone. The table still reads accidents 0 days, illnesses "
    "14 days, orthopedic conditions 30 days, pre-existing conditions never "
    "covered. What changed is the depth of the answers around that table: a "
    "full question-and-answer set, five worked scenarios, and a section that "
    "answers questions the company says came from Reddit.</p>"
    "<p>Three of the new answers are operational rather than definitional, and "
    "they are the ones worth reading before you buy:</p>"
    "<ul>"
    "<li><strong>The wait is counted to the minute.</strong> Illness cover "
    "begins at 12:01 AM on day 15. A pet that vomits on day 10 is not covered "
    "for whatever that turns out to be, because the condition became "
    "pre-existing before cover started.</li>"
    "<li><strong>The scheduling date decides, not the surgery date.</strong> A "
    "procedure booked while the wait was still running is excluded even if the "
    "operation happens afterwards - Lemonade reads the booking as proof the "
    "problem was already known.</li>"
    "<li><strong>A clean exam before symptoms is the only baseline that "
    "helps.</strong> No vet exam is required to buy a policy, and the waiting "
    "periods apply at every age, including a two-month-old puppy. What an exam "
    "does is fix your pet's health on a date, which is what a claim three "
    "months later gets judged against.</li>"
    "</ul>"
    "<p>Lemonade also names what counts as \"showing signs\" during the wait - "
    "limping, vomiting, changes in appetite, lethargy, unusual behaviour, or "
    "anything a vet notes at an exam. That list is the practical definition of "
    "a pre-existing condition, and it is wider than most owners assume: none "
    "of those needs a diagnosis attached to count.</p>"
)

SECTION_DISAGREE = (
    "Where Lemonade's own answers disagree",
    "<p>Reading the rewritten guide end to end turns up three places where "
    "answers on the same page pull against each other. None of them is "
    "dishonest, but each one changes what you should expect to be paid.</p>"
    "<p><strong>1. Is there a policy with no waiting periods?</strong> The "
    "heading says \"Nope.\" Two answers further down say some coverage types "
    "do not have waiting periods - accidents and preventative care - and a "
    "third says no insurer offers zero waiting periods \"across the board\". "
    "The three are reconcilable only if \"no waiting periods\" means the whole "
    "policy. Read as a per-coverage question, two of the three coverages on "
    "the policy really do start on day one.</p>"
    "<p><strong>2. When does accident cover actually begin?</strong> The "
    "comparison section says accident coverage \"kicks in immediately, with no "
    "waiting period at all\". The FAQ says the same cover is usable \"at 12:01 "
    "AM the day after purchase\". Both can be true - there is no waiting "
    "period, and the policy still is not effective the instant you pay - but "
    "the two sentences only add up to an answer once you supply the second "
    "half. Buy at noon and your pet is hurt that afternoon, and this is the "
    "paragraph that decides it.</p>"
    "<p><strong>3. When does preventative care start?</strong> The guide says "
    "the preventative packages take effect \"the date your policy becomes "
    "effective\". The product page says you can use them \"the day after you "
    "purchased the policy\". That is a one-day gap in the same company's "
    "description of the same benefit, and it has been there since before the "
    "13 October rewrite.</p>"
    "<p>For a reader, the useful habit is to take the strictest version of "
    "each answer: no waiting period on accidents still means the next "
    "midnight, and preventative care still means the effective date printed on "
    "your policy rather than the day you paid.</p>"
)

SECTION_SCENARIOS = (
    "The five scenarios Lemonade now spells out",
    "<p>The guide's new scenario section is the most useful addition, because "
    "each case isolates one mechanism that decides a claim. Summarised, with "
    "the mechanism named:</p>"
    "<ul>"
    "<li><strong>A new puppy.</strong> An eight-week-old puppy insured the day "
    "it comes home, vomiting three weeks later, is covered - the 14-day wait "
    "has passed. The mechanism: hip dysplasia at six months is still inside "
    "the 30-day orthopedic wait if the policy lapsed and restarted in between. "
    "Continuous cover is what protects the second half of a dog's first year, "
    "not the first policy.</li>"
    "<li><strong>Switching insurers.</strong> A three-year-old cat healthy for "
    "two years, switched to a new policy, starts showing urinary signs on day "
    "six. The previous insurer's history is irrelevant: the signs appeared "
    "during the new waiting period, so the condition is pre-existing under the "
    "new policy. The mechanism: a switch restarts the clock, and anything that "
    "surfaces mid-clock belongs to the new insurer as an exclusion.</li>"
    "<li><strong>A large breed.</strong> A one-year-old German Shepherd "
    "limping at month two, with the vet suspecting hip dysplasia. Inside the "
    "30-day orthopedic wait, so flagged pre-existing and not covered. The "
    "mechanism: for joints, the 30 days is the whole risk window, and large "
    "breeds are the ones that walk into it.</li>"
    "<li><strong>A rescue with no history.</strong> A four-year-old rescue "
    "insured immediately. The insurer reviews whatever records exist to work "
    "out what was already there. The mechanism: an unknown history is read as "
    "possibly-symptomatic, so a clean exam soon after adoption is the only "
    "thing that turns unknown into a documented baseline.</li>"
    "<li><strong>A senior adoption.</strong> A nine-year-old cat from a "
    "shelter. More exclusions and narrower cover are expected; new unrelated "
    "conditions after the waits are still eligible. The mechanism: on an older "
    "pet the policy buys coverage of what happens next, not of what is already "
    "happening.</li>"
    "</ul>"
    "<p>All five use named people, which are illustrative examples rather than "
    "claim records, so read them as the company explaining its own rules "
    "rather than as cases it adjudicated.</p>"
)

NEW_SECTIONS = [SECTION_UPDATE, SECTION_DISAGREE, SECTION_SCENARIOS]

# ------------------------------------------------------------------ new FAQs
NEW_FAQS = [
    {
        "q": "If my pet shows symptoms on day 10 of a 14-day wait, is that condition covered?",
        "a": (
            "No. Lemonade's guide answers this one directly: the wait has to "
            "end completely, so illness coverage starts at 12:01 AM on day 15, "
            "and symptoms that appear before then make the condition "
            "pre-existing. The same logic applies to a surgery booked during "
            "the wait - it stays excluded even if it happens afterwards, "
            "because the booking shows the problem was already known "
            "(checked 2026-10-20)."
        ),
        "source_url": GUIDE,
        "checked": CHECKED,
    },
    {
        "q": "Do I need a vet exam before I can buy pet insurance?",
        "a": (
            "Not with Lemonade - it says plainly that no exam is required "
            "before buying. What an exam does is create a dated record of your "
            "pet's health, and that record is what a later claim is measured "
            "against. Lemonade's rescue-pet scenario makes the point: an "
            "unknown history gets read as possibly-symptomatic, so a clean "
            "exam soon after adoption is the only thing that turns it into a "
            "baseline (checked 2026-10-20)."
        ),
        "source_url": GUIDE,
        "checked": CHECKED,
    },
    {
        "q": "Does the waiting period still apply to a very young puppy?",
        "a": (
            "Yes. Lemonade states that waiting periods apply to all pets "
            "regardless of age, even a two-month-old puppy: 14 days for "
            "illnesses and 30 days for orthopedic conditions. The exception is "
            "the preventative care add-on, which starts as soon as the policy "
            "takes effect (checked 2026-10-20)."
        ),
        "source_url": GUIDE,
        "checked": CHECKED,
    },
    {
        "q": "Is arthritis treated as an illness or an orthopedic condition?",
        "a": (
            "Orthopedic. Lemonade's new FAQ defines orthopedic conditions as "
            "those affecting bones, joints, ligaments and tendons and names "
            "cruciate ligament injuries, hip dysplasia and arthritis among the "
            "examples - which puts arthritis behind the 30-day wait rather "
            "than the 14-day one (checked 2026-10-20)."
        ),
        "source_url": GUIDE,
        "checked": CHECKED,
    },
    {
        "q": "Is there really such a thing as a pet insurance policy with no waiting periods?",
        "a": (
            "Not as a whole policy. Lemonade's guide answers the whole-policy "
            "question with one word - \"Nope\" - while separately saying that "
            "accident cover and preventative care have no waiting period at "
            "all. Both statements are on the same page. The practical reading: "
            "no policy has zero waits, but two of its coverages can start on "
            "day one (checked 2026-10-20)."
        ),
        "source_url": GUIDE,
        "checked": CHECKED,
    },
]


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    articles = data["articles"]
    art = next(a for a in articles if a["slug"] == SLUG)

    # 1. The guide's own date line moved; correct the condition that records it.
    fixed_dates = 0
    for fact in art["facts"]:
        if "Jun 3, 2026" in fact.get("condition", ""):
            fact["condition"] = fact["condition"].replace(
                "the page is marked Last Updated: Jun 3, 2026",
                "the page is marked Last Updated: Oct 13, 2026",
            )
            fixed_dates += 1

    # 2. Append facts that are not already present.
    existing = {f["fact"] for f in art["facts"]}
    added_facts = 0
    for fact in NEW_FACTS:
        if fact["fact"] not in existing:
            art["facts"].append(fact)
            added_facts += 1

    # 3. Append FAQs that are not already present.
    seen_q = {f["q"] for f in art["faqs"]}
    added_faqs = 0
    for faq in NEW_FAQS:
        if faq["q"] not in seen_q:
            art["faqs"].append(faq)
            added_faqs += 1

    # 4. Drop any earlier copy of the sections this script writes, then insert
    #    them directly after the compare block so the new material sits above
    #    the source table rather than buried under it.
    mine = {h2 for h2, _ in NEW_SECTIONS}
    art["blocks"] = [b for b in art["blocks"] if not (b.get("type") == "section" and b.get("h2") in mine)]

    insert_at = 0
    for i, blk in enumerate(art["blocks"]):
        if blk.get("type") == "compare":
            insert_at = i + 1
            break
    new_block_objs = [{"type": "section", "h2": h2, "html": html} for h2, html in NEW_SECTIONS]
    art["blocks"][insert_at:insert_at] = new_block_objs

    # 5. Move the page's own freshness marker.
    for stat in art["stats"]:
        if stat["label"].startswith("every figure rechecked"):
            stat["value"] = CHECKED

    # 6. Say in the "how this page was checked" section that it was re-read.
    sec = next((b for b in art["blocks"] if b.get("h2") == "How this page was checked"), None)
    if sec and "2026-10-20" not in sec["html"]:
        sec["html"] = sec["html"].replace(
            "<p>Where a brand does not publish a figure",
            "<p>On <strong>2026-10-20</strong> the same Lemonade guide was read "
            "again and had been rewritten on 13 October 2026. The new answers, "
            "the three places where the page's own statements pull against each "
            "other, and the five worked scenarios are recorded below; the day "
            "counts themselves did not move.</p><p>Where a brand does not "
            "publish a figure",
            1,
        )

    DATA.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    print(f"date conditions corrected : {fixed_dates}")
    print(f"facts added               : {added_facts}")
    print(f"FAQs added                : {added_faqs}")
    print(f"sections inserted         : {len(new_block_objs)}")
    print(f"page total facts/faqs     : {len(art['facts'])}/{len(art['faqs'])}")
    print(f"blocks order              : {[b.get('type') for b in art['blocks']]}")


if __name__ == "__main__":
    main()
