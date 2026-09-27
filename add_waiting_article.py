# One-shot: append the G2 article "pet insurance waiting periods" to data/articles.json.
# Every figure below was read from the brand's own pages / sample policies on 2026-09-28 (see conditions).
import json, pathlib

ROOT = pathlib.Path(__file__).parent
P = ROOT / "data" / "articles.json"
D = "2026-09-28"

LM_GUIDE = "https://www.lemonade.com/pet/insurance-guide/waiting-periods/"
LM_PET = "https://www.lemonade.com/pet-insurance"
SPOT_HOME = "https://spotpet.com/"
SPOT_POLICY = "https://spotpet.com/sample-policy"
SPOT_DOG = "https://spotpet.com/dog-insurance"
FETCH_WAIT = "https://www.fetchpet.com/faqs/waiting-period"
FETCH_WELL = "https://www.fetchpet.com/faqs/is-there-a-waiting-period-for-pet-wellness"
FETCH_HOME = "https://www.fetchpet.com/"

SVG = (
    '<figure style="margin:1.2em 0">'
    '<img src="/assets/waiting-periods.svg" alt="Bar chart of published pet insurance waiting '
    'periods: accident and illness waits of 0, 14 and 15 days and orthopedic waits of 30 days, '
    '14 days and 6 months for Lemonade, Spot and Fetch, read 2026-09-28" width="720" height="500" '
    'loading="lazy" style="max-width:100%;height:auto;border:1px solid #e4e9ee;border-radius:8px">'
    "<figcaption>Every bar is a number the brand itself publishes: Lemonade's waiting-period guide, "
    "Spot's state sample policies, Fetch's waiting-period FAQ. Read 2026-09-28; the table below "
    "links each figure to the page it came from.</figcaption></figure>"
)

article = {
    "slug": "pet-insurance-waiting-periods",
    "nav_label": "Waiting Periods",
    "type": "guide",
    "keyword": "pet insurance waiting periods",
    "title": "Pet Insurance Waiting Periods Compared: Accident, Illness, Orthopedic and Knee - Read From Lemonade, Spot and Fetch",
    "description": "How long you wait before pet insurance pays: Lemonade 0 days accident, 14 days illness, 30 days orthopedic; Spot 14 days in the state sample policies read; Fetch up to 15 days plus 6 months orthopedic. Every figure from the brand's own pages and sample policies, checked 2026-09-28.",
    "h1": "Pet insurance waiting periods, side by side",
    "lede": (
        "Quick answer: Lemonade publishes 0 days for accidents, 14 days for illnesses and 30 days for orthopedic "
        "conditions, all counted from the policy's start date. Spot's official sample policies say 14 days - and Spot's "
        "own FAQ tells you to check your state's sample policy, because the wording is not identical everywhere. Fetch "
        "publishes one combined accident-and-illness wait of up to 15 days that begins the day after you enroll, plus a "
        "separate 6-month wait before orthopedic conditions, including hip dysplasia and cruciate ligament injuries. "
        "All three treat anything that happens inside the wait as a pre-existing condition. Every number on this page "
        "was read from the brand's own pages and sample policies on 2026-09-28 and links back to where it was read."
    ),
    "stats": [
        {"value": "0 days", "label": "Lemonade's published accident waiting period"},
        {"value": "6 months", "label": "Fetch's published orthopedic waiting period"},
        {"value": "2026-09-28", "label": "every figure rechecked on the brands' own pages"},
    ],
    "columns": [
        {"name": "Lemonade", "url": "/lemonade-pet-insurance"},
        {"name": "Spot", "url": "/spot-pet-insurance"},
        {"name": "Fetch", "url": "/fetch-pet-insurance"},
    ],
    "rows": [
        {
            "label": "Accident waiting period",
            "cells": [
                "0 days - the guide's own table prints Accidents: 0 days, next to an industry range of 0 to 2 days, and says accident coverage \"kicks in immediately, with no waiting period at all\" (checked 2026-09-28)",
                "14 days: the AZ, CO, FL, GA and IL Accident & Illness sample policies say 14 days for \"accidents, illnesses and ligament and knee conditions\"; the California sample's waiting-period section states only the 14-day illness wait and no separate accident figure (checked 2026-09-28)",
                "Not published as its own figure - Fetch publishes one combined accident and illness wait of up to 15 days instead (checked 2026-09-28)",
            ],
            "sources": [LM_GUIDE, SPOT_POLICY, ""],
        },
        {
            "label": "Illness waiting period",
            "cells": [
                "14 days, counted from the policy's start date (checked 2026-09-28)",
                "14 days: \"Spot plans typically have a 14 day waiting period for coverage\" (FAQ) and every state sample policy read repeats the 14-day figure (checked 2026-09-28)",
                "Up to 15 days, beginning the day after you enroll; claims submitted during it are not paid (checked 2026-09-28)",
            ],
            "sources": [LM_GUIDE, SPOT_POLICY, FETCH_WAIT],
        },
        {
            "label": "Orthopedic, cruciate and hip dysplasia",
            "cells": [
                "30 days for orthopedic conditions - the same table prints an industry range of 6 to 12 months for that row, and the guide names hip dysplasia and a luxating patella as conditions that must not appear before the wait ends (checked 2026-09-28)",
                "Inside the same 14 days: the five state samples list \"ligament and knee conditions\" with accidents and illnesses, and the California sample lists orthopedic illness inside its 14-day illness wait (checked 2026-09-28)",
                "6 months before orthopedic conditions can be covered - Fetch names elbow dysplasia, hip dysplasia, intervertebral disc degeneration, patellar luxation and ruptured cranial cruciate ligaments (checked 2026-09-28)",
            ],
            "sources": [LM_GUIDE, SPOT_POLICY, FETCH_WAIT],
        },
        {
            "label": "When the clock starts",
            "cells": [
                "On your policy's start date; the guide's glossary defines the effective date as the day the policy becomes active and waiting periods begin (checked 2026-09-28)",
                "On \"the first effective date of the applicable coverage\" - the wording used in every state sample policy read (checked 2026-09-28)",
                "The day after you enroll (checked 2026-09-28)",
            ],
            "sources": [LM_GUIDE, SPOT_POLICY, FETCH_WAIT],
        },
        {
            "label": "Preventive / wellness care",
            "cells": [
                "No wait: the pet insurance page says the preventative package benefits \"can be used the day after the policy is purchased\" (checked 2026-09-28)",
                "No wait: \"Preventative care coverage has no deductible or waiting period, meaning you can start using these benefits the next day\" (checked 2026-09-28)",
                "No wait: \"there is no waiting period for Fetch Wellness\" - claims work on or after the effective date in the enrollment confirmation email (checked 2026-09-28)",
            ],
            "sources": [LM_PET, SPOT_DOG, FETCH_WELL],
        },
        {
            "label": "Anything that happens during the wait",
            "cells": [
                "\"Anything your pet has shown signs of before the waiting periods are up is considered a pre-existing condition\" - and pre-existing conditions are not covered (checked 2026-09-28)",
                "\"Any condition that occurs during an applicable waiting period is a pre-existing condition\" (state sample policy wording) (checked 2026-09-28)",
                "Any accident, injury or illness during the wait is considered pre-existing and is not eligible for coverage (checked 2026-09-28)",
            ],
            "sources": [LM_PET, SPOT_POLICY, FETCH_WAIT],
        },
        {
            "label": "State-by-state differences",
            "cells": [
                "Not published on the cited Lemonade pages - the guide prints one national table (0 / 14 / 30 days) and lists no state variations (checked 2026-09-28)",
                "Published state by state: the FAQ says \"see our sample policy for more information on your states specific waiting periods\", and spotpet.com/sample-policy hosts Accident Only, Accident & Illness, Gold and Platinum sample PDFs for each state (checked 2026-09-28)",
                "No state table: Fetch publishes one national figure and adds that waiting periods \"vary by state or province and are subject to change without notice. Please see your policy\" (checked 2026-09-28)",
            ],
            "sources": ["", SPOT_POLICY, FETCH_HOME],
        },
        {
            "label": "Ways to shorten or waive the wait",
            "cells": [
                "Not published on the cited Lemonade pages - the waiting-period guide offers no waiver or shortened wait (checked 2026-09-28)",
                "California only, at your cost: a Waiting Period Health Assessment - qualifying vet exam 3 days before or 7 days after the effective date, form returned within 30 days of the exam, and the wait is waived to the effective date or the day after the exam, whichever is later (checked 2026-09-28)",
                "Knee injuries: have a vet examine your pet within 180 days of enrollment to confirm no relevant pre-existing conditions, then send that visit's \"SOAP notes\" with your first claim (checked 2026-09-28)",
            ],
            "sources": ["", SPOT_POLICY, FETCH_WAIT],
        },
        {
            "label": "Does the wait reset?",
            "cells": [
                "Yes on cancellation: cancelling in the app resets waiting periods (refunds apply within the first 30 days) (checked 2026-09-28)",
                "\"A new enrollment will result in new waiting periods\", and anything before it is pre-existing (California sample policy, general conditions) (checked 2026-09-28)",
                "Not published on the cited Fetch pages - the waiting-period FAQ carries no reset-on-switch statement (checked 2026-09-28)",
            ],
            "sources": [LM_PET, SPOT_POLICY, ""],
        },
    ],
    "facts": [
        {
            "fact": "Lemonade's published waiting periods are 14 days for illnesses and 30 days for orthopedic conditions, and they begin on the policy's start date",
            "condition": "Waiting-period guide, section \"How do pet insurance waiting periods work?\"; the page is marked Last Updated: Jun 3, 2026",
            "source_url": LM_GUIDE,
            "checked": D,
        },
        {
            "fact": "Lemonade prints its own comparison table: accidents 0 days (industry range 0 to 2), illnesses 14 days (14 to 30), orthopedic conditions 30 days (industry range 6 to 12 months), pre-existing conditions never covered",
            "condition": "Table under \"How do Lemonade's waiting periods compare to other providers?\" - the industry range column is Lemonade's own framing, not a measured survey",
            "source_url": LM_GUIDE,
            "checked": D,
        },
        {
            "fact": "Accident coverage at Lemonade kicks in immediately, with no waiting period at all",
            "condition": "Same guide page; the FAQ on that page also answers \"Is there pet insurance with no waiting periods?\" with \"Nope\" - every policy on the site has waiting periods on some coverage",
            "source_url": LM_GUIDE,
            "checked": D,
        },
        {
            "fact": "Lemonade's preventative care coverage kicks in the date the policy becomes effective",
            "condition": "Guide, \"Are there any exclusions to pet insurance waiting periods\" - applies to the preventative care options added to the policy",
            "source_url": LM_GUIDE,
            "checked": D,
        },
        {
            "fact": "Lemonade's pet insurance page words the same benefit as usable \"the day after the policy is purchased\", and says cancelling in the app resets waiting periods",
            "condition": "FAQ answer on the product page; the 30-day refund window is the first 30 days of the policy - note the two Lemonade pages describe the preventive start one day apart (guide: effective date; product page: day after purchase)",
            "source_url": LM_PET,
            "checked": D,
        },
        {
            "fact": "\"Anything your pet has shown signs of before the waiting periods are up is considered a pre-existing condition\", and pre-existing conditions are not covered",
            "condition": "FAQ on Lemonade's pet insurance page",
            "source_url": LM_PET,
            "checked": D,
        },
        {
            "fact": "Spot: \"Spot plans typically have a 14 day waiting period for coverage\", followed by \"See our sample policy for more information on your states specific waiting periods\"",
            "condition": "Question \"What is a waiting period for pet insurance?\" in the FAQ block on Spot's home page; the sample policy link points to spotpet.com/sample-policy",
            "source_url": SPOT_HOME,
            "checked": D,
        },
        {
            "fact": "Spot's Arizona, Colorado, Florida, Georgia and Illinois Accident & Illness sample policies all say: \"There is a 14 day waiting period for: diagnosis, treatment or surgery related to accidents, illnesses and ligament and knee conditions. The waiting period begins on the first effective date of the applicable coverage.\"",
            "condition": "Five state sample PDFs linked from spotpet.com/sample-policy, read 2026-09-28: AZ and CO form PET-P-20000-1024, FL PET-P-20000-FL-1024, IL PET-P-20000-IL-1024, GA PET-P-20000-0723 (same waiting-period sentence in all five)",
            "source_url": SPOT_POLICY,
            "checked": D,
        },
        {
            "fact": "Spot's California Accident & Illness sample policy reads differently: \"There is a 14 day waiting period for diagnosis, treatment or surgery related to any illness, including... congenital anomaly or disorder, hereditary disorder and orthopedic illness\", with no separate accident sentence in that section",
            "condition": "California sample PDF PET-P-20000-CA-IAIC-1024 (Independence American Insurance Company) linked from spotpet.com/sample-policy, read 2026-09-28 - this is the state-level wording difference Spot's FAQ points to",
            "source_url": SPOT_POLICY,
            "checked": D,
        },
        {
            "fact": "Spot's California policy adds a paid way to change the wait: a Waiting Period Health Assessment - qualifying vet exam 3 days before or 7 days after the initial effective date, form returned within 30 calendar days of the exam, and \"the waiting period will be waived to either the policy period effective date or the day after the qualifying exam, whichever is later\"",
            "condition": "California sample PDF PET-P-20000-CA-IAIC-1024, WAITING PERIODS section; the policy says \"You may elect at your cost\", and the waiver does not alter the pre-existing conditions exclusion",
            "source_url": SPOT_POLICY,
            "checked": D,
        },
        {
            "fact": "Spot's Accident Only sample policy for Arizona also uses 14 days: \"There is a 14 day waiting period for: diagnosis, treatment or surgery related to accidents and ligament and knee conditions\"",
            "condition": "AZ Accident Only sample PDF linked from spotpet.com/sample-policy, read 2026-09-28",
            "source_url": SPOT_POLICY,
            "checked": D,
        },
        {
            "fact": "Spot: a curable pre-existing condition that has been cured and free from treatment and symptoms for 180 days counts as a new occurrence - but that carve-out \"does not apply to chronic conditions or ligament and knee conditions\" in the AZ, CO, FL and IL samples, while the GA sample's sentence omits chronic conditions",
            "condition": "CURED CONDITION ELIGIBILITY section of the state sample policies, read 2026-09-28; the exact exclusion list differs between form versions",
            "source_url": SPOT_POLICY,
            "checked": D,
        },
        {
            "fact": "Spot: \"Preventative care coverage has no deductible or waiting period, meaning you can start using these benefits the next day\"",
            "condition": "Preventative care description on Spot's dog insurance page",
            "source_url": SPOT_DOG,
            "checked": D,
        },
        {
            "fact": "Fetch: \"The waiting period, which begins the day after you enroll, is a set period of time, of up to 15 days, before your coverage kicks in\"; conditions during it are pre-existing and claims submitted during it are not covered",
            "condition": "Fetch FAQ page \"What is a waiting period for pet insurance?\", read 2026-09-28",
            "source_url": FETCH_WAIT,
            "checked": D,
        },
        {
            "fact": "Fetch also applies \"a 6-month waiting period before orthopedic conditions can be covered\", and lists elbow dysplasia, hip dysplasia, intervertebral disc degeneration, patellar luxation and ruptured cranial cruciate ligaments as orthopedic conditions",
            "condition": "Same Fetch FAQ; it then offers the knee waiver: a vet exam within 180 days of enrollment with \"SOAP notes\" submitted with the first claim",
            "source_url": FETCH_WAIT,
            "checked": D,
        },
        {
            "fact": "Fetch: \"No, there is no waiting period for Fetch Wellness\" - wellness claims work on or after the effective date given in the enrollment confirmation email",
            "condition": "Fetch FAQ \"Is there a waiting period for pet wellness?\", read 2026-09-28",
            "source_url": FETCH_WELL,
            "checked": D,
        },
        {
            "fact": "Fetch's home page disclaimer: \"Policy activation periods, risk free cancellation terms, waiting periods, limitations, exclusions to coverage and other terms and conditions vary by state or province and are subject to change without notice. Please see your policy for full terms\"",
            "condition": "Footer disclaimer on fetchpet.com; the site publishes a single national waiting-period figure in its FAQ and no state-by-state table (checked 2026-09-28)",
            "source_url": FETCH_HOME,
            "checked": D,
        },
    ],
    "faqs": [
        {
            "q": "What is a pet insurance waiting period?",
            "a": "Spot's own definition: \"A waiting period is a set period between the day you enroll and the day your coverage begins. Conditions that occur during the waiting period will be considered pre-existing and will not be eligible for coverage under your plan.\" Fetch words it as the gap between enrollment and when coverage kicks in, and Lemonade calls it the time the insurer requires you to wait until your pet is eligible for reimbursement on specific conditions (all checked 2026-09-28).",
            "source_url": SPOT_HOME,
            "checked": D,
        },
        {
            "q": "How long is the waiting period with Lemonade?",
            "a": "0 days for accidents, 14 days for illnesses and 30 days for orthopedic conditions, counted from the policy's start date. Preventive care from a preventative package can be used the day after purchase. That is the whole national table Lemonade publishes - no state-by-state version appears on the pages cited here (checked 2026-09-28).",
            "source_url": LM_GUIDE,
            "checked": D,
        },
        {
            "q": "How long is the waiting period with Spot?",
            "a": "Spot says its plans \"typically\" have a 14-day waiting period and then points you at the sample policy for your state's specific waiting periods. Of the six state Accident & Illness samples read on 2026-09-28 (AZ, CA, CO, FL, GA, IL), five state 14 days covering accidents, illnesses and ligament and knee conditions; the California sample states 14 days for illness only and adds a paid Waiting Period Health Assessment that can waive it. Preventive care add-ons start the next day.",
            "source_url": SPOT_POLICY,
            "checked": D,
        },
        {
            "q": "How long is the waiting period with Fetch?",
            "a": "Up to 15 days for accident and illness coverage combined, beginning the day after you enroll, plus a separate 6-month waiting period before orthopedic conditions - hip dysplasia, elbow dysplasia, luxating patella, IVDD and ruptured cruciate ligaments are named. Fetch Wellness has no waiting period. Fetch also publishes a knee waiver: a vet exam within 180 days of enrollment with SOAP notes sent in your first claim (checked 2026-09-28).",
            "source_url": FETCH_WAIT,
            "checked": D,
        },
        {
            "q": "Do waiting periods change from state to state?",
            "a": "For Spot, yes - that is what its FAQ means by \"see our sample policy for more information on your states specific waiting periods\": spotpet.com/sample-policy hosts separate Accident Only and Accident & Illness sample PDFs per state, and the sentences are not identical (the California sample has no separate accident sentence and offers a waiver the others do not). Fetch does not publish a state table but disclaims that waiting periods vary by state or province. The two Lemonade pages read print one national table only (checked 2026-09-28).",
            "source_url": SPOT_POLICY,
            "checked": D,
        },
        {
            "q": "Can you shorten or waive a pet insurance waiting period?",
            "a": "Fetch publishes a way for knees: have your pet examined by a vet within 180 days of enrollment to show no relevant pre-existing conditions, then submit that visit's SOAP notes with your first claim. Spot's California sample policy offers a paid Waiting Period Health Assessment (exam 3 days before or 7 days after the effective date, form returned within 30 days) that waives the wait to the effective date or the day after the exam, whichever is later. The Lemonade pages cited here publish no such option (checked 2026-09-28).",
            "source_url": FETCH_WAIT,
            "checked": D,
        },
        {
            "q": "What happens if my pet gets sick during the waiting period?",
            "a": "All three treat it as pre-existing: Fetch says any accident, injury or illness during the wait \"will be considered a pre-existing condition, which means it won't be eligible for coverage\"; Spot's sample policy says any condition occurring during a waiting period is a pre-existing condition; Lemonade says anything your pet showed signs of before the wait ended counts as pre-existing. Spot adds that a curable pre-existing condition can count as new after 180 days symptom- and treatment-free, except chronic and ligament/knee conditions in the samples read (checked 2026-09-28).",
            "source_url": FETCH_WAIT,
            "checked": D,
        },
        {
            "q": "Do wellness and preventive add-ons have a waiting period?",
            "a": "No, according to all three brands' own pages: Fetch Wellness claims work \"on or after the effective date\" in your enrollment email; Spot says preventive care has no deductible or waiting period and starts the next day; Lemonade says preventative care coverage kicks in on the effective date (its product page says the day after purchase). The base accident and illness waits above still apply (checked 2026-09-28).",
            "source_url": FETCH_WELL,
            "checked": D,
        },
        {
            "q": "Does switching insurers restart the waiting periods?",
            "a": "Yes - that is the coverage gap Lemonade defines in its own glossary: \"A period when switching providers where your pet may temporarily lack full coverage, since new waiting periods apply with each new policy.\" Spot's California sample policy says the same thing for a new enrollment: \"A new enrollment will result in new waiting periods\", and conditions before it are pre-existing. This is why switching mid-treatment can cost coverage (checked 2026-09-28).",
            "source_url": LM_GUIDE,
            "checked": D,
        },
    ],
    "blocks": [
        {"type": "section", "h2": "How this page was checked", "html": (
            "<p>On <strong>2026-09-28</strong> we read the pages each brand itself publishes on waiting periods, not "
            "review sites or comparison tables:</p>"
            "<ul><li><strong>Lemonade</strong> - its waiting-period guide (page marked Last Updated: Jun 3, 2026) and "
            "the FAQ on its pet insurance product page.</li>"
            "<li><strong>Spot</strong> - the FAQ block on its home page, its dog insurance page, and six Accident &amp; "
            "Illness sample policies linked from spotpet.com/sample-policy: Arizona, California, Colorado, Florida, "
            "Georgia and Illinois (plus Arizona's Accident Only sample). The five non-California forms repeat the same "
            "waiting-period sentence; California's does not.</li>"
            "<li><strong>Fetch</strong> - its \"What is a waiting period for pet insurance?\" FAQ, its \"Is there a "
            "waiting period for pet wellness?\" FAQ, and the disclaimer on its home page.</li></ul>"
            "<p>Where a brand does not publish a figure - or does not publish one state by state - this page says so "
            "instead of filling the gap with a third-party estimate.</p>"
        )},
        {"type": "section", "h2": "Waiting periods at a glance", "html": SVG},
        {"type": "compare", "h2": "Side by side: what each brand's own pages say"},
        {"type": "section", "h2": "The state-by-state part, in plain terms", "html": (
            "<p>Only Spot puts this in writing. Its FAQ ends with \"See our sample policy for more information on your "
            "state's specific waiting periods\", and Spot's sample-policy page publishes a separate Accident Only and "
            "Accident &amp; Illness PDF for each state. Reading six of them on 2026-09-28 shows what that means in "
            "practice: five states carry the identical sentence (14 days covering accidents, illnesses and ligament and "
            "knee conditions), while California's form covers 14 days of <em>illness</em> only - including congenital, "
            "hereditary and orthopedic illness - and offers a paid Waiting Period Health Assessment that the other forms "
            "do not mention.</p>"
            "<p>Fetch does not publish a state table; its home page simply warns that waiting periods \"vary by state or "
            "province\" and tells you to read your policy. Lemonade's guide prints one national table: 0 / 14 / 30. So if "
            "your state matters, Spot is the only one of the three that hands you the documents directly - everyone else "
            "asks you to read the policy you are given.</p>"
        )},
        {"type": "facts", "h2": "Every figure with its official source"},
        {"type": "faqs", "h2": "Pet insurance waiting periods - FAQ"},
        {"type": "cards", "h2": "Every brand on this site, page by page"},
    ],
    "disclaimer": (
        "This page is not affiliated with Lemonade, Spot or Fetch. It repeats only what each brand publishes on its own "
        "guide pages, FAQ pages, product pages and sample policies, with the source and check date attached to every "
        "figure; waiting periods depend on the policy you are actually sold, your state and your pet's history, and the "
        "policy wording always governs. Facts last checked 2026-09-28."
    ),
}

data = json.loads(P.read_text(encoding="utf-8"))
slugs = [a["slug"] for a in data["articles"]]
if article["slug"] in slugs:
    raise SystemExit(f"already present: {article['slug']}")
data["articles"].append(article)
P.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("appended", article["slug"], "facts", len(article["facts"]), "faqs", len(article["faqs"]),
      "rows", len(article["rows"]))
