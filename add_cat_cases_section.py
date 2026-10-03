"""Rebuild the community-cases section on the live lemonade-cat-insurance article.

The section is kept as its own `section` block placed AFTER the official `facts` block, so the
official fact table stays official-only. It is written from owner-reported claim histories, in the
third person, with no source link, no community name, no section-of-a-forum name and no post title.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ARTICLES = ROOT / "data" / "articles.json"
SLUG = "lemonade-cat-insurance"

H2 = "Real cat claim cases, as their owners reported them"

H2_LIMITS = "What these cases do not establish"

LIMITS_HTML = """<p>Three things are worth separating from the cases above, because the temptation is
to read them as a verdict on one company. They are not a verdict on the process: an owner who asked what
happens when a cat falls through a window was told that a window is not a named exclusion, so it is judged
on whether the accident counts as one, which is a coverage question rather than a character question. And
the file rules in those cases are not one insurer's invention. Human health cover written under the
Affordable Care Act can point to a pre-existing-condition protection statute; no such protection extends to
a pet policy, which is written as property-and-casualty cover and is not obliged to ignore a recorded
symptom. Nothing in the cases above turns on anyone having broken a rule.</p>

<p>What they do establish is narrower and more useful. A chart is a liability from the day it is written,
and how diligent the vet is when writing it changes what the policy will later pay. The advice that falls
out of these files is the advice that sounds least like advice: put the policy in force while the cat's
record is empty, read the full record rather than the summary sheet, and if a one-off cough or a passing
limp is ever written down, have it examined and closed rather than left standing. An open question in a
file is exactly what pre-existing language is built to find. There is one due-diligence step that follows
from the arithmetic rather than from anyone's experience: entry pricing is banded by age on the way in, but
renewal pricing is not locked on the way through, so the cheapest day to compare insurers is the day you buy.
Requesting a quote for the cat as it will be at four, five and six years old, not as it is today, is the only
way to see the curve before a chart makes leaving expensive.</p>"""

HTML = """<p>None of the following is a company statement or an audited record. Each case is an account
one cat owner published of how their own claim was decided. They are here because they are the only
public place where the mechanic that appears above stops being a sentence in a contract and becomes a
bill somebody had to pay. Grouped by what they actually have in common, they collapse into four
patterns, and every one of them turns on a date rather than on a diagnosis.</p>

<p><strong>One cough, seven months early.</strong> A cat's policy took effect in mid-January. A late-December
visit had already been charted for vomiting and restlessness, and in that same record the owner had
mentioned one cough, once, which was judged to be stress from a move. The cat was clear from then on.
In June the cat was diagnosed with asthma after X-rays and bloodwork, and put on a daily inhaler with a
rescue inhaler alongside it. The denial arrived five weeks later and cited the December cough. The
first-level dispute failed. The part of this case worth copying into your own thinking is what the file
contained at the time: perfectly normal visits on either side of that one note, and a checkup ten days
before it with nothing abnormal recorded. None of it mattered, because the claimed condition was asthma
and the recorded symptom was consistent with asthma. That is the whole mechanism. Nobody had to
demonstrate that the cough caused the asthma.</p>

<p><strong>One theory a vet was thinking out loud.</strong> A cat came in with hip or lower back pain, and the
vet proposed a blood panel and a monthly injectable for osteoarthritis pain. The claim was denied over a
visit from before the policy: the cat had been seen for gastrointestinal pain, and in that record the
vet had described the discomfort making the cat walk in a way that looked like a German Shepherd, adding
that if the gait did not resolve they might consider the injectable for possible arthritis. The gait
resolved. The subject never came up again. A stated possibility, never diagnosed and never treated, was
enough to convert the later injection into a pre-existing condition. It is worth separating what is
alarming here from what is merely careless: this is not an error a receptionist could have prevented. It
is a clinical note, written correctly, doing the only thing a note can do.</p>

<p>The drug at the center of that case has published numbers that are unusually clean, and they are worth
knowing because a cat owner facing an arthritis decision usually reads only the marketing. Frunevetmab is
approved for the control of pain associated with osteoarthritis in cats; it is given subcutaneously once a
month at the full contents of one or two vials depending on weight; it has not been evaluated in cats under
seven months of age or under 5.5 pounds. The 112-day field study behind the approval ran 182 treated cats
against 93 controls. Vomiting was reported in 13.2 percent of treated cats against 10.8 percent of controls,
dermatitis in 6.0 percent against 1.1 percent, and dehydration in 4.4 percent against none. Owner-judged
treatment success at day 84 was 64.6 percent on the drug against 57.8 percent on the control. Four of 259
cats dosed monthly developed anti-drug antibodies and one of those was a treatment failure. The same
regulatory review records that rapidly progressing osteoarthritis has been reported in a small number of
human patients treated with anti-NGF antibody therapy, and that it has not been characterized or reported in
cats. Those percentages are not an argument against the drug. They are an argument for reading them before
treating the medication as the uncomplicated part of the case.</p>

<p><strong>The category denial.</strong> A cat insured from kittenhood developed bladder trouble: straining,
then crystals, then a blockage, then prescription food for life. Nothing related to the bladder is covered.
The reason is that the owner had raised a concern about the cat's urinating habits before the policy began,
at a time when nothing turned out to be wrong. The same cat was later diagnosed with heart muscle disease,
and every echo, diagnostic and medication for that has been paid. One body system swallowed whole by a
raised hand; an unrelated system paid without argument. This is the case that confuses owners most, and it
is the reason to stop reading a policy as covering your cat and start reading it as covering the conditions
your cat's chart has not mentioned.</p>

<p><strong>The single word that becomes a diagnosis.</strong> A kitten tore into a balloon string overnight and
needed surgery that came to roughly nine thousand dollars. The claim was denied under pica, because the cat
had once chewed a cotton swab. No vet had diagnosed anything of the kind and no behavioral assessment had
been performed. The owner paid for an independent behavioral assessment, obtained a second letter from the
vet stating the cat showed no signs of the disorder, and filed a complaint with the state insurance
regulator. The claim was approved four months after submission. The lesson is not that appealing is
pointless. It is what an appeal costs in time, cash and paperwork when a behavioral diagnosis has been
inferred from a single noun.</p>

<p>One pattern sits underneath all four of those cases and changes how the rest of them read: these claims
are decided one body system at a time, and the systems that end up excluded are the systems the chart
mentioned. Bladder, hips, back, lungs, skin, teeth. Two cats of the same age with identical bills can finish
thousands of dollars apart for no reason other than that one owner raised a concern too early and the other
did not. That is not a defect in any single decision. It is the shape of the product, and it is why two
owners can describe the same insurer as generous and as fraudulent without either of them being dishonest.</p>

<p><strong>The antibiotic that came back.</strong> A cat with a documented urinary tract infection before the
policy began later developed a skin infection and was treated with the same family of antibiotic. The claim
for the skin infection was denied on the basis that the drug had already been used once. The cat's owner
moved to a different insurer and stayed. The skin had nothing to do with the urinary tract, and no claim
ever depended on that; the shared ingredient was enough. The pattern generalizes past drugs: what connects
the two claims in the file is whatever an adjuster can point to, and the cheapest thing to point to is a
name that appears in both records.</p>

<p><strong>The old lump in the wrong place.</strong> A small stomach lump mentioned at a rescue exam and
dismissed as scar tissue later cost that owner coverage for a lump on the hip, years afterward, on a
different part of the body. The reasoning given was that any lump counted as pre-existing from the moment
the first one was written down. The clinical relationship between the two sites never entered into it.</p>"""


def main() -> None:
    data = json.loads(ARTICLES.read_text(encoding="utf-8"))
    art = next(a for a in data["articles"] if a["slug"] == SLUG)

    cases = {"type": "section", "h2": H2, "html": HTML}
    limits = {"type": "section", "h2": H2_LIMITS, "html": LIMITS_HTML}
    # idempotent: drop any earlier copy of either block before re-inserting
    art["blocks"] = [b for b in art["blocks"] if b.get("h2") not in (H2, H2_LIMITS)]

    # cases section: straight after the official facts block, before the FAQ block
    idx = next(i for i, b in enumerate(art["blocks"]) if b.get("type") == "facts")
    art["blocks"].insert(idx + 1, cases)

    # limits section: after the last official section, before the official fact table
    idx = next(i for i, b in enumerate(art["blocks"]) if b.get("type") == "facts")
    art["blocks"].insert(idx, limits)

    ARTICLES.write_text(
        json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
    )
    print("block order:", [b.get("type") + ":" + (b.get("h2") or "")[:34] for b in art["blocks"]])


if __name__ == "__main__":
    main()
