# -*- coding: utf-8 -*-
"""Add the G4 gap article: pet-insurance-claim-filing-deadline (data/articles.json).

Every figure was read on 2026-09-28 from the brands' own official claim pages,
FAQ pages and Spot's own sample policy PDFs (linked from spotpet.com/sample-policy).
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).parent
PATH = ROOT / "data" / "articles.json"
TODAY = "2026-09-28"

L_FILE = "https://www.lemonade.com/pet/insurance-guide/how-to-file-a-pet-insurance-claim/"
S_FAQ = "https://spotpet.com/faqs"
S_HOME = "https://spotpet.com/"
S_CA = "https://assets.ctfassets.net/m5ehn3s5t7ec/1BnVbZD0bckBstD3zXO6wE/05ab8626875f3adbc9c06bf1134664b0/Sample_PolicyPages_CA_AccidentIllness_IAIC.pdf"
S_AZ = "https://assets.ctfassets.net/m5ehn3s5t7ec/1jSJ3wibAqaL8wdIY3yKhQ/5c6fe63f297179c6da4cef326dc5fc3e/Sample_PolicyPages_AZ_AccidentandIllness_47_copy.pdf"
F_CLAIMS = "https://www.fetchpet.com/claims"
F_WHEN = "https://www.fetchpet.com/faqs/when-to-claim-pet-insurance"
F_SUB = "https://www.fetchpet.com/faqs/claim-submission"
N_FAQ = "https://www.petinsurance.com/faq/"

ARTICLE = {
    "slug": "pet-insurance-claim-filing-deadline",
    "nav_label": "Claim Deadline",
    "type": "vs",
    "keyword": "how long do you have to file a pet insurance claim",
    "title": "How Long Do You Have to File a Pet Insurance Claim? Official Windows Side by Side",
    "description": (
        "How long do you have to file a pet insurance claim: Spot's 270 days, Lemonade's 180 days "
        "(90 days for Texas policies) and Fetch's 90 days, each quoted from the brand's own claim page, "
        "FAQ or sample policy, with the link and the day the figure was read. 2026-09-28."
    ),
    "h1": "How long do you have to file a pet insurance claim? The three official windows",
    "lede": (
        "Quick answer, read from the brands' own pages on 2026-09-28: Spot lets you file within 270 days "
        "from the date of treatment (its sample policy says 270 days from the date of service), Lemonade "
        "within 180 days of treatment - 90 days if your Lemonade Pet policy is in Texas - and Fetch within "
        "90 days of the vet visit, after which Fetch states in writing that the claim is not covered. All "
        "three clocks start at the treatment or the vet visit, not at the date you noticed something wrong. "
        "The paperwork has to be finished inside that same window: Lemonade wants an invoice or receipt plus "
        "records from that visit, Spot wants your vet bill and Fetch will only take an invoice showing a zero "
        "balance together with the records from your pet's most recent checkup."
    ),
    "stats": [
        {
            "value": "270 / 180 / 90",
            "label": "days to file: Spot / Lemonade / Fetch (Lemonade Texas policies: 90)",
        },
        {
            "value": "not covered",
            "label": "what Fetch's own claims page says happens to a claim filed after day 90",
        },
        {
            "value": TODAY,
            "label": "every figure on this page rechecked against the official source",
        },
    ],
    "columns": [
        {"name": "Lemonade", "url": "/lemonade-pet-insurance"},
        {"name": "Spot", "url": "/spot-pet-insurance"},
        {"name": "Fetch", "url": "/fetch-pet-insurance"},
    ],
    "rows": [
        {
            "label": "Official window to file after treatment",
            "cells": [
                "Within 180 days of treatment, filed through the Lemonade app; Lemonade ties filing on time to whether the claim is eligible for coverage",
                "Within 270 days from the date of treatment, per the FAQ on its own site",
                "Within 90 days of the vet visit - claims must be submitted within 90 days to be eligible for reimbursement",
            ],
            "sources": [L_FILE, S_FAQ, F_CLAIMS],
        },
        {
            "label": "What the clock is counted from",
            "cells": [
                "'Within 180 days of treatment' - the treatment date, with all requested information supplied during that process",
                "FAQ says 'from the date of treatment'; Spot's own Accident & Illness sample policy says 'from the date of service'",
                "Claims page says 'within 90 days of the vet visit'; the claim FAQ says 'within 90 days of your pet's treatment'",
            ],
            "sources": [L_FILE, S_CA, F_CLAIMS],
        },
        {
            "label": "Shorter window published for some states",
            "cells": [
                "Yes - Lemonade states that a Lemonade Pet policy in Texas has 90 days to file a claim",
                "not published on the pages we read on 2026-09-28",
                "not published on the pages we read on 2026-09-28",
            ],
            "sources": [L_FILE, "", ""],
        },
        {
            "label": "What the official pages say happens if you file late",
            "cells": [
                "Filing within the window is stated as a condition: 'in order to be eligible for coverage, you'll need to file a claim ... within 180 days of treatment'",
                "'You must submit your claim within 270 days from the date of service' - sentence printed in the sample policy itself",
                "'Claims submitted after 90 days won't be covered' - stated in plain words on its claims page",
            ],
            "sources": [L_FILE, S_CA, F_CLAIMS],
        },
        {
            "label": "Paperwork that must be complete inside the window",
            "cells": [
                "Vet invoice or paid receipt plus medical records from that visit, and a record from a visit within 12 months of the policy's start date",
                "Your vet bill; medical records only if Spot asks for them - Spot contacts your vet directly, though sending records may speed things up",
                "A finalized invoice showing a zero balance or paid in full, plus detailed records from your pet's most recent checkup",
            ],
            "sources": [L_FILE, S_FAQ, F_SUB],
        },
        {
            "label": "Published decision or payout speed",
            "cells": [
                "50% of eligible claims processed instantly by its AI; most others resolved within 5 business days, complex claims may take longer",
                "Claims reimbursed in 48 hrs or less (homepage), with claim status emailed at receipt, at request for more info and at completion",
                "Typically processed in less than 10 days; direct deposit pays 5 to 10 days faster than a paper check",
            ],
            "sources": [L_FILE, S_HOME, F_CLAIMS],
        },
        {
            "label": "Appeal route after a denial, and its deadline",
            "cells": [
                "Appeal through the app with additional documentation from your vet; no day count published on that page",
                "Written appeal by email; the number of days to appeal varies by the state the policy was issued in, review takes around 30 days",
                "not published on the pages we read on 2026-09-28",
            ],
            "sources": [L_FILE, S_FAQ, ""],
        },
    ],
    "facts": [
        {
            "fact": "Spot's FAQ answer to 'How Long Do I Have to File a Claim?' is: you can submit a claim within 270 days from the date of treatment",
            "condition": "Published in the FAQPage data on spotpet.com/faqs; no state exception is printed next to it",
            "source_url": S_FAQ,
            "checked": TODAY,
        },
        {
            "fact": "Spot's sample Accident & Illness policy (California) prints the contract sentence: You must submit your claim within 270 days from the date of service",
            "condition": "Sample policy form for California, Independence American Insurance Company, linked from spotpet.com/sample-policy",
            "source_url": S_CA,
            "checked": TODAY,
        },
        {
            "fact": "Spot's sample Accident & Illness policy (Arizona) prints the same 270-day sentence, so the two state forms we read agree",
            "condition": "Sample policy form for Arizona, linked from spotpet.com/sample-policy",
            "source_url": S_AZ,
            "checked": TODAY,
        },
        {
            "fact": "Lemonade requires the claim to be filed through its app within 180 days of treatment, with all requested information supplied in that process",
            "condition": "The page frames this as a coverage condition: in order to be eligible for coverage, you'll need to file within 180 days",
            "source_url": L_FILE,
            "checked": TODAY,
        },
        {
            "fact": "A Lemonade Pet policy in Texas has 90 days to file a claim - half the 180 days printed for the rest of the book",
            "condition": "Stated on the same claim guide page: if you have a Lemonade Pet policy in Texas, you have 90 days to file a claim",
            "source_url": L_FILE,
            "checked": TODAY,
        },
        {
            "fact": "Fetch states that claims must be submitted within 90 days of the vet visit to be eligible for reimbursement, and that claims submitted after 90 days won't be covered",
            "condition": "Printed in the Claims section of Fetch's own claims page",
            "source_url": F_CLAIMS,
            "checked": TODAY,
        },
        {
            "fact": "Fetch's claim FAQ wording is 90 days of your pet's treatment, with both the paid vet bill (invoice) and your pet's medical record attached",
            "condition": "FAQ page 'When can I submit a pet insurance claim?'; same 90-day number as the claims page, different starting phrase",
            "source_url": F_WHEN,
            "checked": TODAY,
        },
        {
            "fact": "Fetch requires the invoice to show a zero balance or that it was paid in full before it will accept the claim",
            "condition": "From Fetch's claim submission FAQ; a photo of the paid invoice plus records from the most recent checkup are the two required documents",
            "source_url": F_SUB,
            "checked": TODAY,
        },
        {
            "fact": "Fetch says claims are typically processed within 15 days from when we receive all your documents",
            "condition": "Claim submission FAQ; the clock it describes starts when every document is in hand, not when you file",
            "source_url": F_SUB,
            "checked": TODAY,
        },
        {
            "fact": "Fetch's claims page separately says claims are typically processed in less than 10 days - a second, different published figure from the same brand",
            "condition": "Both figures were read on 2026-09-28; we report them side by side and do not reconcile them",
            "source_url": F_CLAIMS,
            "checked": TODAY,
        },
        {
            "fact": "Fetch says direct deposit gets you paid back 5 to 10 days faster than paper checks",
            "condition": "Published on both its claims page and its claim submission FAQ; up to 90% reimbursement once the deductible is met",
            "source_url": F_CLAIMS,
            "checked": TODAY,
        },
        {
            "fact": "Lemonade says 50% of eligible claims are processed instantly by its AI and most others are resolved within 5 business days",
            "condition": "Complex claims may take longer depending on documentation requirements, per the same FAQ block",
            "source_url": L_FILE,
            "checked": TODAY,
        },
        {
            "fact": "Spot prints 'Claims reimbursed in 48 hrs or less' on its homepage next to its published sample reimbursement example",
            "condition": "The homepage text does not say what moment the 48 hours is measured from; we quote it as printed",
            "source_url": S_HOME,
            "checked": TODAY,
        },
        {
            "fact": "Spot emails you when it receives your claim, when it needs more information and when the claim is complete, and shows status under the claims icon",
            "condition": "FAQ answer on status of a claim, spotpet.com/faqs",
            "source_url": S_FAQ,
            "checked": TODAY,
        },
        {
            "fact": "Spot's appeal deadline is not a fixed number: the number of days to appeal a claim varies by the state in which your policy was issued",
            "condition": "Appeal must be in writing to service@customer.spotpetins.com with supporting documents; Spot says appeals may take around 30 days to be reviewed",
            "source_url": S_FAQ,
            "checked": TODAY,
        },
        {
            "fact": "Lemonade's claim guide tells readers to appeal through the app with additional documentation from their vet, but prints no day count for appeals",
            "condition": "Read on the same guide page on 2026-09-28; no appeal window appears anywhere in its text",
            "source_url": L_FILE,
            "checked": TODAY,
        },
        {
            "fact": "Lemonade requires a medical record from a visit that took place within 12 months of your policy's start date",
            "condition": "Stated as a prerequisite in the same guide, so a first claim often waits on that record even inside the 180-day window",
            "source_url": L_FILE,
            "checked": TODAY,
        },
        {
            "fact": "Fetch publishes no appeal route on the pages we read: its claims and FAQ pages describe filing, tracking and payment only",
            "condition": "Absence noted, not filled from a third party - nothing on this page comes from a broker or a review site",
            "source_url": F_CLAIMS,
            "checked": TODAY,
        },
        {
            "fact": "Nationwide (petinsurance.com) publishes how to file a claim in three steps and when coverage begins (most plans start 1-14 days after approval), but no filing deadline in days",
            "condition": "Its public FAQ page was read on 2026-09-28 looking specifically for a day count; none was found, so we do not quote one",
            "source_url": N_FAQ,
            "checked": TODAY,
        },
        {
            "fact": "Spot lets you cancel a claim request at any time by calling 1.800.905.1595",
            "condition": "FAQ answer under Administrative questions, spotpet.com/faqs",
            "source_url": S_FAQ,
            "checked": TODAY,
        },
    ],
    "faqs": [
        {
            "q": "How long do I have to file a claim with Spot?",
            "a": "Spot's own FAQ answer is 270 days: you can submit a claim within 270 days from the date of treatment. Spot's sample Accident & Illness policy prints the same 270 days and calls it the date of service. Both were read on 2026-09-28.",
            "source_url": S_FAQ,
            "checked": TODAY,
        },
        {
            "q": "Does Lemonade give me 180 days to file?",
            "a": "Yes - Lemonade's claim guide says you file through the app within 180 days of treatment, and it presents that as a condition of the claim being eligible for coverage. The same page says a Lemonade Pet policy in Texas has 90 days to file a claim.",
            "source_url": L_FILE,
            "checked": TODAY,
        },
        {
            "q": "How long after the vet visit can I file with Fetch?",
            "a": "90 days. Fetch's claims page says claims must be submitted within 90 days of the vet visit to be eligible for reimbursement, and that claims submitted after 90 days won't be covered. Its claim FAQ gives the same 90 days counted from your pet's treatment.",
            "source_url": F_CLAIMS,
            "checked": TODAY,
        },
        {
            "q": "Does the clock start on the day of the accident?",
            "a": "Not on any of the pages we read. Spot's sample policy counts its 270 days from the date of service, Lemonade counts from the date of treatment and Fetch counts from the vet visit - so the window starts when your pet is treated, and the paperwork (invoice, records) has to be finished inside that same window.",
            "source_url": S_CA,
            "checked": TODAY,
        },
        {
            "q": "What happens if I file after the deadline?",
            "a": "Fetch is the only one of the three that writes the consequence out: claims submitted after 90 days won't be covered. Spot's sample policy says you must submit within 270 days, and Lemonade frames the 180 days as a condition of eligibility for coverage.",
            "source_url": F_CLAIMS,
            "checked": TODAY,
        },
        {
            "q": "Do some states get a shorter window?",
            "a": "Yes for Lemonade: its claim guide states that a Lemonade Pet policy in Texas has 90 days to file a claim instead of 180. Spot and Fetch publish no state variation in the filing window on the pages we read - Spot does publish state variation for its appeal deadline, which is a different clock.",
            "source_url": L_FILE,
            "checked": TODAY,
        },
        {
            "q": "How fast does Spot pay a claim?",
            "a": "Spot's homepage prints claims reimbursed in 48 hrs or less, and it emails you when the claim is received, when it needs more information and when it is complete. The homepage text does not say what moment the 48 hours is measured from.",
            "source_url": S_HOME,
            "checked": TODAY,
        },
        {
            "q": "How long does Fetch take to process a claim?",
            "a": "Fetch's claim submission FAQ says claims are typically processed within 15 days from when we receive all your documents, and that direct deposit pays you back 5 to 10 days faster than a check. Its claims page separately prints under 10 days - two official figures from one brand, reported as published.",
            "source_url": F_SUB,
            "checked": TODAY,
        },
        {
            "q": "How do I appeal a denied claim?",
            "a": "Spot's route is a written appeal by email to service@customer.spotpetins.com with your reasons and supporting documents; it says the number of days to appeal varies by the state your policy was issued in and that reviews take around 30 days. Lemonade tells you to appeal in the app with extra documentation from your vet. Fetch publishes no appeal route on the pages we read.",
            "source_url": S_FAQ,
            "checked": TODAY,
        },
        {
            "q": "Does Nationwide publish a filing deadline?",
            "a": "No. Its public FAQ explains how to file a claim in three steps and says most plans start 1-14 days after your application is approved, but it prints no number of days for filing a claim. We read that page on 2026-09-28 specifically looking for one and found none.",
            "source_url": N_FAQ,
            "checked": TODAY,
        },
    ],
    "disclaimer": (
        "This page is not affiliated with Lemonade, Spot or Fetch. It quotes only what the brands publish on "
        "their own claim guides, FAQ pages, claims pages and sample policy documents, with the source and the "
        "day we read it attached to every figure; policy terms always govern, deadlines vary by state and by "
        "plan, and your own claim timeline will differ. Facts last checked 2026-09-28."
    ),
    "blocks": [
        {
            "type": "section",
            "h2": "How this page was checked",
            "html": (
                "<p>On <strong>2026-09-28</strong> we opened the official pages that publish a filing "
                "deadline - and nothing else - looking for a number of days and the sentence around it:</p>"
                "<ul>"
                "<li><strong>Lemonade</strong> - its claim guide (how to file a pet insurance claim), which carries the 180-day window, the Texas exception, the document list, the AI speed figures and the in-app appeal route.</li>"
                "<li><strong>Spot</strong> - its FAQ page (the 270-day answer, the appeal rules, the status emails), its homepage (48 hrs or less) and two of its own sample Accident & Illness policy forms - California and Arizona - which print the 270 days as a contract sentence.</li>"
                "<li><strong>Fetch</strong> - its claims page (90 days and the 'won't be covered' sentence, under 10 days, direct deposit), its 'when can I submit' FAQ and its claim submission document FAQ (zero-balance invoice, 15 days from all documents in hand).</li>"
                "<li><strong>Nationwide (petinsurance.com)</strong> - its public FAQ, checked specifically to see whether a fourth brand publishes a filing deadline. It does not, so no number appears for it here.</li>"
                "</ul>"
                "<p>No figure on this page comes from a broker, a review site or a comparison chart. Where a brand "
                "prints nothing - a state exception, an appeal window, an appeal route - the table says "
                "<em>not published on the official site</em> instead of filling the cell from somewhere else.</p>"
            ),
        },
        {
            "type": "section",
            "h2": "Three windows, and two clocks that run after them",
            "html": (
                "<figure style=\"margin:1.2em 0\">"
                "<img src=\"/assets/claim-windows.svg\" alt=\"Bar charts of official pet insurance claim filing windows: Spot 270 days, Lemonade 180 days, Lemonade Texas policies 90 days, Fetch 90 days; and of published decision or payout times: Spot 48 hours, Lemonade 5 business days, Fetch under 10 days and Fetch 15 days from all documents received; read from official pages on 2026-09-28\" width=\"720\" height=\"600\" loading=\"lazy\" style=\"max-width:100%;height:auto;border:1px solid #e4e9ee;border-radius:8px\">"
                "<figcaption class=\"muted\">The window you get, and the speed each brand publishes afterwards - read from the official pages on 2026-09-28. Units are kept exactly as each brand prints them.</figcaption>"
                "</figure>"
            ),
        },
        {"type": "compare", "h2": "The three filing windows, side by side - official published figures only"},
        {
            "type": "section",
            "h2": "Where the three windows disagree",
            "html": (
                "<ul>"
                "<li><strong>The spread is three to one.</strong> 270 days at Spot against 90 days at Fetch - the same product category, the same reimbursement model, and a 180-day difference in how long you can wait before the paperwork has to be in.</li>"
                "<li><strong>All three start the clock at the treatment, not at the incident.</strong> Spot's sample policy says date of service, Lemonade says date of treatment, Fetch says the vet visit. Nothing we read starts the count on the day the accident happened, so the window is about getting the invoice and the records filed, not about noticing a symptom late.</li>"
                "<li><strong>Only one brand spells out the penalty.</strong> Fetch prints that claims submitted after 90 days won't be covered. Spot's sample policy uses the word must. Lemonade phrases it as eligibility for coverage. Three different levels of bluntness for the same kind of rule.</li>"
                "<li><strong>One brand contains a second deadline inside it.</strong> Lemonade prints 180 days for the general case and 90 days for Texas policies on the same page - a reader who only skims the headline number will have the wrong deadline in one state.</li>"
                "<li><strong>A brand's FAQ and its own contract can use different words.</strong> Spot's FAQ says 270 days from the date of treatment; Spot's sample policy says 270 days from the date of service. We quote both, and we do not choose one for them.</li>"
                "<li><strong>The paperwork is on the same clock.</strong> Fetch's zero-balance invoice and the records from the most recent checkup both have to exist inside its 90 days, and Lemonade needs a record from within 12 months of the policy start - which is why a first claim often waits on the vet's office rather than on the insurer.</li>"
                "</ul>"
            ),
        },
        {
            "type": "section",
            "h2": "The second clock: what happens after you file",
            "html": (
                "<p>Filing deadlines are one number; the wait afterwards is another, and the three brands measure "
                "different things by different units. Spot prints a payout claim (48 hrs or less) without saying "
                "what moment its clock starts from. Lemonade publishes a processing mix (50% instant via its AI, "
                "most others within 5 business days) and warns that complex claims take longer. Fetch publishes "
                "<strong>two</strong> processing figures: under 10 days on its claims page, and within 15 days "
                "from when it receives all your documents in its claim submission FAQ. Both were read on the same "
                "day. We show both figures and both sources rather than picking the one that reads better.</p>"
                "<p>One more asymmetry: only Spot publishes an appeal deadline at all, and even then it is not a "
                "fixed number - the days to appeal vary by the state that issued the policy, the appeal goes in "
                "writing, and Spot says reviews take around 30 days. Lemonade routes appeals through the app "
                "without a day count, and Fetch's official pages describe no appeal route.</p>"
            ),
        },
        {"type": "facts", "h2": "Every deadline figure with its official source"},
        {"type": "faqs", "h2": "Filing deadlines - FAQ"},
        {"type": "cards", "h2": "The three brands compared, page by page"},
    ],
}


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    slugs = [a["slug"] for a in data["articles"]]
    if ARTICLE["slug"] in slugs:
        raise SystemExit(f"article already present: {ARTICLE['slug']}")
    data["articles"].append(ARTICLE)
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"added {ARTICLE['slug']}: rows={len(ARTICLE['rows'])} facts={len(ARTICLE['facts'])} faqs={len(ARTICLE['faqs'])}")


if __name__ == "__main__":
    main()
