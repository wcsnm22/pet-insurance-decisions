# One-shot: append the N1 article "pet insurance waiting periods by condition" to data/articles.json.
# Every figure below was read from the official pages / sample contract documents on 2026-09-29.
import json, pathlib

ROOT = pathlib.Path(__file__).parent
P = ROOT / "data" / "articles.json"
D = "2026-09-29"

G_ART = "https://www.geico.com/living/pet-insurance-what-is-it-how-does-it-work/"
G_LAND = "https://www.geico.com/pet-insurance/"
A_PET = "https://www.allstate.com/pet-insurance"
A_DOG = "https://www.allstate.com/resources/pet-insurance/dog-insurance"
E_TERMS = "https://www.embracepetinsurance.com/coverage/embrace-terms"
E_V5 = "https://www.embracepetinsurance.com/state-terms/v5"
E_V6 = "https://www.embracepetinsurance.com/state-terms/v6"
E_WAIT = "https://www.embracepetinsurance.com/coverage/waiting-period"
E_ORTHO = "https://www.embracepetinsurance.com/help/article/what-is-the-waiting-period-for-orthopedic-conditions"
AS_QUOTE = "https://www.aspcapetinsurance.com/quote/"
AS_COV = "https://www.aspcapetinsurance.com/research-and-compare/pet-insurance-basics/whats-covered/"
AS_CA = "https://aspcapetinsurance.com/more-info/notice-to-california-residents"
AS_STATE = "https://www.aspcapetinsurance.com/more-info/state-documents-and-sample-policies"

article = {
    "slug": "pet-insurance-waiting-periods-by-condition",
    "nav_label": "Waiting by Condition",
    "type": "guide",
    "keyword": "pet insurance waiting periods by condition",
    "title": "Pet Insurance Waiting Periods by Condition: Accident, Illness, Cancer, Orthopedic and Cruciate - GEICO, ASPCA and Allstate Compared",
    "description": (
        "GEICO publishes no waiting-period day counts, Allstate publishes one (a 2-week illness wait), ASPCA "
        "publishes a five-row table. The day counts behind GEICO and Allstate sit in the Embrace sample policy "
        "both sites link to: 2 days accident / 14 days illness / 6 months orthopedic in KS, NM and SC, and "
        "no accident wait / 14 days illness / a 180-day orthopedic exclusion list in the other 48 states and DC. "
        "Every figure read 2026-09-29."
    ),
    "h1": "Pet insurance waiting periods, condition by condition",
    "lede": (
        "Quick answer: of these three sites, only ASPCA prints a day-by-day table. Its quote page says: accidents "
        "and injuries (excluding ligament and knee injuries) no waiting period, preventive care no waiting period, "
        "ligament and knee injuries 14 days, illnesses 14 days, hereditary and congenital conditions 14 days. "
        "Allstate publishes exactly one number - \"All policies have a 2-week illness waiting period. Other waiting "
        "periods and exclusions vary by state.\" GEICO publishes none at all: its guide says to \"ask an agent what "
        "waiting periods apply to your policy.\" The day counts behind GEICO and Allstate are written in a single "
        "document - the Embrace sample policy that both sites link to in their own footers - which prints two days "
        "for accidents, fourteen days for illnesses and six months for orthopedic conditions in dogs in the Kansas, "
        "New Mexico and South Carolina contract, and no accident wait, a fourteen-day illness wait and a 180-day "
        "orthopedic exclusion list covering cruciate ligament disease, IVDD, patellar luxation and hip dysplasia in "
        "the other 48 states and DC. Every number on this page was read from the brand's own pages and contract "
        "documents on 2026-09-29 and links back to where it was read."
    ),
    "stats": [
        {"value": "0 day counts", "label": "printed anywhere on GEICO's own pet insurance pages (read 2026-09-29)"},
        {"value": "1 number", "label": "published by Allstate: a 2-week illness waiting period"},
        {"value": "2 answers", "label": "for accidents on one ASPCA page: 0 days in the table, 14 days in the text"},
    ],
    "columns": [
        {"name": "GEICO", "url": "https://www.geico.com/pet-insurance/"},
        {"name": "Allstate", "url": "https://www.allstate.com/pet-insurance"},
        {"name": "ASPCA", "url": "https://www.aspcapetinsurance.com/quote/"},
    ],
    "rows": [
        {
            "label": "Accident (anything that is not a ligament or knee injury)",
            "cells": [
                "No day count on any GEICO page. The guide says: \"Waiting periods vary by condition (accident, illness, etc.) and insurer, so be sure to ask an agent what waiting periods apply to your policy.\" The landing page mentions the waiting period only inside its pre-existing-condition definition (read 2026-09-29)",
                "No accident figure published. The FAQ gives one number for everything else: \"All policies have a 2-week illness waiting period. Other waiting periods and exclusions vary by state\" (read 2026-09-29)",
                "The table row \"Accidents & Injuries (Excluding ligament and knee injuries)\" reads \"No waiting period\" - yet the effective-date section on the same page says \"Coverage for accidents and illnesses begins 14 days after your coverage effective date\" (read 2026-09-29)",
            ],
            "sources": [G_ART, A_PET, AS_QUOTE],
        },
        {
            "label": "Illness (general sickness)",
            "cells": [
                "Nothing on geico.com itself. The contract its footer points to prints fourteen (14) days in both published versions - the fourteenth-day Illness Waiting Period of the V6 form and the fourteen (14) days for Illnesses of the V5 form (read 2026-09-29)",
                "2 weeks, stated twice: \"All policies have a 2-week illness waiting period\", which matches the fourteen (14) day Illness Waiting Period in the Embrace terms its own footer links to (read 2026-09-29)",
                "14 days: the quote-page table row \"Illnesses\" reads \"14-day waiting period\", and the effective-date text repeats that coverage begins 14 days after the effective date (read 2026-09-29)",
            ],
            "sources": [E_V6, A_PET, AS_QUOTE],
        },
        {
            "label": "Cancer",
            "cells": [
                "No cancer line on GEICO's pages. In the linked contract cancer is an Illness - \"Illnesses, including but not limited to Genetic Conditions, cancer, and Chronic Conditions\" - so it follows the fourteen-day illness wait, with two written traps: a mass found before that wait ends is not covered \"including those caused by cancer\", and osteosarcoma showing signs inside the orthopedic period is excluded (read 2026-09-29)",
                "No cancer-specific wait published. Allstate's own coverage list files cancer under illness - \"Coverage for accidents and illnesses: This type of policy covers ... illnesses, including cancer\" - so the published figure that applies is the 2-week illness wait (read 2026-09-29)",
                "Cancer is filed under illness: its coverage page lists cancer under \"Illnesses\" and again under \"Chronic Conditions\", and its quote table puts a 14-day wait on Illnesses - no separate cancer row exists (read 2026-09-29)",
            ],
            "sources": [E_V5, A_DOG, AS_COV],
        },
        {
            "label": "Orthopedic conditions (dogs)",
            "cells": [
                "Not printed on geico.com. The linked contract splits by state form: the V5 form (Kansas, New Mexico, South Carolina) sets the orthopedic Waiting Period at six (6) months from the Pet Original Start Date, while the V6 form used in the other 48 states and DC uses a 180-day exclusion instead of a named orthopedic wait (read 2026-09-29)",
                "Allstate publishes no orthopedic figure of its own - the page only says other waiting periods vary by state. Its footer links the same Embrace terms, where dogs get six (6) months (V5) or the 180-day orthopedic exclusion list (V6), and cats get a 14-day orthopedic wait on Embrace's own help page (read 2026-09-29)",
                "The quote-page table has no orthopedic row at all; the closest rows are \"Illnesses\" and \"Hereditary and congenital conditions\", both 14 days, and \"Ligament and knee injuries\", 14 days (read 2026-09-29)",
            ],
            "sources": [E_V5, A_PET, AS_QUOTE],
        },
        {
            "label": "Cruciate ligament / knee (CCL, TPLO)",
            "cells": [
                "Not printed on GEICO's pages. The linked contract is explicit: in the V6 form \"Orthopedic conditions that occur or show Clinical Signs during the first 180 days after the Pet Original Start Date are excluded and are Pre-existing Conditions for the life of the policy: Cruciate Ligament Disease; Intervertebral Disk Disease (IVDD); Patellar Luxation; and Hip Dysplasia\"; the V5 form uses the six (6) month orthopedic wait instead (read 2026-09-29)",
                "No cruciate figure on allstate.com - its FAQ defers to state variation and its own text stops at \"read your specific policy\". The contract it links to carries the same cruciate wording as GEICO's (read 2026-09-29)",
                "14 days: the table row \"Ligament and knee injuries\" reads \"14-day waiting period\". Its California policy notice tells a longer story for one plan family - \"Diagnosis and treatment for ligament and knee conditions are subject to a 12 month waiting period on all policies\" on the Levels 2, 3 and 4 disclosure (read 2026-09-29)",
            ],
            "sources": [E_V6, A_PET, AS_QUOTE],
        },
        {
            "label": "Hereditary and congenital conditions",
            "cells": [
                "No line of its own on GEICO's pages. In the linked contract genetic conditions are Illnesses - \"Illnesses, including but not limited to Genetic Conditions, cancer, and Chronic Conditions\" - so the fourteen-day illness wait applies (read 2026-09-29)",
                "No day count published; the coverage list instead states the condition: \"Genetic and breed-specific conditions are covered if there are no related signs or symptoms prior to enrollment\" (read 2026-09-29)",
                "14 days: the table row \"Hereditary and congenital conditions\" reads \"14-day waiting period\". Note the California notice prints 180 days for the Hereditary, Genetic or Congenital List on Levels 3 and 4 of one plan family (read 2026-09-29)",
            ],
            "sources": [E_V5, A_PET, AS_QUOTE],
        },
        {
            "label": "Preventive and wellness care",
            "cells": [
                "Not published on the two GEICO pages read - neither the landing page nor the guide states when preventive benefits start (checked 2026-09-29)",
                "Not published on the Allstate pet insurance pages read - no preventive-care start date appears on allstate.com/pet-insurance (checked 2026-09-29)",
                "No waiting period: the table row \"Preventive Care\" reads \"No waiting period\", and the effective-date text says preventive care \"will begin on the same day as your base plan coverage effective date\" (read 2026-09-29)",
            ],
            "sources": ["", "", AS_QUOTE],
        },
        {
            "label": "When the clock starts, and does it restart",
            "cells": [
                "GEICO prints no start rule. The linked contract does: the wait \"starts from the Pet Original Start Date\", \"also applies again when there are Coverage increases but is waived for policy renewals and optional Coverage renewals\" (read 2026-09-29)",
                "Allstate publishes no clock rule - its FAQ only defines a pre-existing condition as anything noticed 'before the end of your waiting period' and never says when the clock starts or whether it restarts (read 2026-09-29)",
                "From the policy effective date: \"This is the date when your coverage begins\", with accident and illness coverage starting 14 days later and preventive care on day one (read 2026-09-29)",
            ],
            "sources": [E_V6, A_PET, AS_QUOTE],
        },
        {
            "label": "Ways to shorten or waive the wait",
            "cells": [
                "GEICO's own pages publish no waiver. The contract it links to allows an orthopedic exam: in some states the Orthopedic Exam and Waiver Process can cut the wait to as few as 14 days - an exam inside the first 14 days moves the end date to the end of the illness wait, a later exam moves it to the exam date (read 2026-09-29)",
                "Not published on allstate.com - no waiver or shortened wait appears on the Allstate pages read (checked 2026-09-29)",
                "A state-specific option exists: its state documents page says \"choose your state below to view sample plans and, where applicable, the Insurer Disclosure of Important Policy Provisions and Waiting Period Waiver Form specific to your state\", and the same site links a \"Waiting Period Health Assessment\" (read 2026-09-29)",
            ],
            "sources": [E_ORTHO, "", AS_STATE],
        },
    ],
    "facts": [
        {
            "fact": "GEICO publishes no waiting-period day counts: \"Waiting periods vary by condition (accident, illness, etc.) and insurer, so be sure to ask an agent what waiting periods apply to your policy\"",
            "condition": "Flagship guide \"Pet insurance: what is it, how does it work\", bylined August 31, 2026 by GEICO Team; the article mentions waiting periods four times and prints a day count zero times, and geico.com/pet-insurance mentions it once, inside the pre-existing definition",
            "source_url": G_ART,
            "checked": D,
        },
        {
            "fact": "GEICO's own footer: \"Pet Health Insurance is administered by Embrace Pet Insurance Agency, LLC (Lic. No 0G89328) and underwritten by one of the licensed insurers of American Modern Insurance Group, Inc., including American Modern Home Insurance Company ... and American Southern Home Insurance Company ... For full terms and conditions, visit www.embracepetinsurance.com/coverage/embrace-terms\"",
            "condition": "Legal disclaimer block in the footer of geico.com/pet-insurance - this is the only place GEICO hands over the contract wording, and it hands over Embrace's",
            "source_url": G_LAND,
            "checked": D,
        },
        {
            "fact": "Allstate's complete published answer on waiting periods: \"Pet insurance usually has waiting periods for accidents, illnesses, and specific conditions ... All policies have a 2-week illness waiting period. Other waiting periods and exclusions vary by state.\"",
            "condition": "FAQ block on allstate.com/pet-insurance, item \"When does coverage start?\"; no accident, orthopedic, cruciate or cancer figure appears anywhere else on that page",
            "source_url": A_PET,
            "checked": D,
        },
        {
            "fact": "Allstate's footer carries the same administrator and underwriters as GEICO's - Embrace Pet Insurance Agency, LLC and the American Modern Insurance Group insurers - and the same link: \"For full terms and conditions, visit www.embracepetinsurance.com/coverage/embrace-terms\"",
            "condition": "Footnote 1 on allstate.com/pet-insurance - the disclaimer block that names the administrator, the underwriters and the link to the full terms",
            "source_url": A_PET,
            "checked": D,
        },
        {
            "fact": "Allstate files cancer under illness coverage: \"Coverage for accidents and illnesses: This type of policy covers worst-case scenarios, such as poisoning, dental trauma and illnesses, including cancer\"",
            "condition": "Section \"What do the different pet insurance coverage types cover?\" on Allstate's dog insurance resource page (Last Updated: October 2025 banner on that page)",
            "source_url": A_DOG,
            "checked": D,
        },
        {
            "fact": "The Embrace sample policy that both GEICO and Allstate link to states: \"the time period is two (2) days for Accidents and fourteen (14) days for Illnesses, except for Orthopedic conditions for dogs where the Waiting Period is six (6) months. The Waiting Period starts from the Pet Original Start Date.\"",
            "condition": "Sample contract \"Embrace Pet Health Insurance V5\", definition of Waiting Period; the state selector on the terms page maps this version to Kansas, New Mexico and South Carolina only",
            "source_url": E_V5,
            "checked": D,
        },
        {
            "fact": "The V6 version of the same contract - the one used in the other 48 states and DC - defines only \"Illness Waiting Period is the fourteen (14) day period of time where the policy's Coverage is restricted\" and its coverage section says \"Accidents (no Waiting Periods apply)\", so accident coverage starts with no wait in those states",
            "condition": "Sample contract \"Embrace Pet Health Insurance V6\", definitions and \"which result from\" coverage list; state selector maps V6 to 48 states plus the District of Columbia",
            "source_url": E_V6,
            "checked": D,
        },
        {
            "fact": "V6 cruciate and orthopedic rule: \"Orthopedic conditions that occur or show Clinical Signs during the first 180 days after the Pet Original Start Date are excluded and are Pre-existing Conditions for the life of the policy: Cruciate Ligament Disease; Intervertebral Disk Disease (IVDD); Patellar Luxation; and Hip Dysplasia\"",
            "condition": "Pre-existing Conditions section of the V6 sample contract - note this is an exclusion period, not a named orthopedic waiting period, and it attaches for the life of the policy",
            "source_url": E_V6,
            "checked": D,
        },
        {
            "fact": "Embrace's terms page lets you read the contract for your own state, and the two live versions split three ways for orthopedics: V5 (KS, NM, SC) says six (6) months for dogs; V6 (48 states and DC) uses the 180-day exclusion list; and Embrace's help article adds that cats have a 14-day orthopedic waiting period",
            "condition": "State selector on embracepetinsurance.com/coverage/embrace-terms (options read 2026-09-29) plus the orthopedic help article's cats-only paragraph",
            "source_url": E_TERMS,
            "checked": D,
        },
        {
            "fact": "Cancer sits inside the illness wait in the contract wording: \"Illnesses, including but not limited to Genetic Conditions, cancer, and Chronic Conditions\"",
            "condition": "Coverage list of the V5 sample contract; V6 adds that \"If a Pet has had Undiagnosed masses prior to the end of the Illness Waiting Period, any mass, or condition where a mass is a Clinical Sign, is not covered, including those caused by cancer\", and V5 excludes \"Osteosarcoma diagnosed or showing Clinical Signs within the Orthopedic Waiting Period\"",
            "source_url": E_V5,
            "checked": D,
        },
        {
            "fact": "Embrace's own marketing page says \"All Embrace insurance policies have a 14-day waiting period for illnesses, while accident coverage starts on your policy's effective date\" and that orthopedic waiting periods vary by state",
            "condition": "Waiting-period guide page - read alongside the contracts: the \"accident coverage starts on your policy's effective date\" line matches the V6 form (48 states and DC) but not the V5 form's two-day accident wait in KS, NM and SC",
            "source_url": E_WAIT,
            "checked": D,
        },
        {
            "fact": "Embrace's orthopedic help article: for dogs, conditions that show symptoms before the end of the illness wait or during the first 180 days - IVDD, cruciate ligament injury, patellar luxation, canine hip dysplasia - \"are excluded from coverage and are pre-existing for the life of the policy\"; all other orthopedic conditions fall under the 14-day illness wait; for cats \"there is also a 14-day waiting period for orthopedic conditions\"",
            "condition": "Help-center article \"What Is the Waiting Period for Orthopedic Conditions?\", which also notes orthopedic waiting periods vary by state",
            "source_url": E_ORTHO,
            "checked": D,
        },
        {
            "fact": "The orthopedic wait can be cut: \"Some states allow you have the option to reduce the waiting period for certain orthopedic conditions to as few as 14 days by following the Orthopedic Exam and Waiver Process\" - an exam inside the first 14 days moves the end date to the end of the 14-day illness wait, an exam after that moves it to the exam date",
            "condition": "Same orthopedic help article; the V5 contract words the same option as reducing the wait to \"two (2) days for Accidents or fourteen (14) days for Illnesses, or from the Orthopedic examination date, whichever is later\"",
            "source_url": E_ORTHO,
            "checked": D,
        },
        {
            "fact": "ASPCA's published waiting-period table: \"Accidents & Injuries (Excluding ligament and knee injuries) - No waiting period\"; \"Preventive Care - No waiting period\"; \"Ligament and knee injuries - 14-day waiting period\"; \"Illnesses - 14-day waiting period\"; \"Hereditary and congenital conditions - 14-day waiting period\"",
            "condition": "Waiting-period table inside the quote flow on aspcapetinsurance.com/quote/ (the page returned 403 to direct requests, so it was read through a text-rendering fetch of the same URL on 2026-09-29)",
            "source_url": AS_QUOTE,
            "checked": D,
        },
        {
            "fact": "The same ASPCA quote page contradicts its own accident row: \"Coverage for accidents and illnesses begins 14 days after your coverage effective date. This means any accident or illness that occurs during the 14-day waiting period is ineligible.\"",
            "condition": "\"Accident & Illness Effective Date\" section of aspcapetinsurance.com/quote/, read 2026-09-29 - one page therefore publishes 0 days and 14 days for accidents, and the page never reconciles them",
            "source_url": AS_QUOTE,
            "checked": D,
        },
        {
            "fact": "ASPCA preventive care starts day one: \"There is no waiting period for preventive care coverage, so it will begin on the same day as your base plan coverage effective date\"",
            "condition": "\"Preventive Care Effective Date\" section of the quote page; its What's Covered page says those benefits have no waiting period and \"you can sign up today and have this coverage tomorrow\"",
            "source_url": AS_QUOTE,
            "checked": D,
        },
        {
            "fact": "ASPCA's California policy notice publishes three different waiting-period sets on one page: \"On Levels 2, 3, and 4, a 30-day illness waiting period applies to the first policy period. On Levels 3 and 4, conditions that appear on the Hereditary, Genetic, or Congenital List are subject to a 180 day waiting period. Diagnosis and treatment for ligament and knee conditions are subject to a 12 month waiting period on all policies.\"; \"On Complete CoverageSM, a 14 day illness waiting period applies ... ligament and knee conditions ... 14 day\"; and \"A 14 day accident and illness waiting period apply to the first policy period ... ligament and knee conditions ... 14 day\"",
            "condition": "\"Notice to California Residents\" page on aspcapetinsurance.com, three consecutive Waiting Periods disclosures for different plan forms - the day count depends on the form you are sold, and the notice does not say which one that is",
            "source_url": AS_CA,
            "checked": D,
        },
        {
            "fact": "ASPCA hands the per-state paperwork over: \"Please choose your state below to view sample plans and, where applicable, the Insurer Disclosure of Important Policy Provisions and Waiting Period Waiver Form specific to your state\"",
            "condition": "State Documents and Sample Policies page, which also links a \"Waiting Period Health Assessment\" and an Insurer Disclosure per state - the only one of the three sites that publishes state-level waiting-period documents",
            "source_url": AS_STATE,
            "checked": D,
        },
        {
            "fact": "ASPCA treats cancer as an illness: \"With illness coverage, you can get reimbursed for the eligible costs of major and minor illnesses, such as cancer, arthritis ... \" and its FAQ answers \"Does pet insurance cover cancer treatments?\" with \"Complete CoverageSM can help you manage those costs\"",
            "condition": "What's Covered page - cancer therefore sits inside the 14-day illness wait printed on the quote page; no cancer-specific day count is published",
            "source_url": AS_COV,
            "checked": D,
        },
        {
            "fact": "Allstate defines the pre-existing cut-off by the waiting period: \"A pre-existing condition is any injury, illness, or irregularity noticed by you or your veterinarian before the end of your waiting period\"",
            "condition": "FAQ on allstate.com/pet-insurance - the page never says when the waiting period starts or how long the non-illness waits are",
            "source_url": A_PET,
            "checked": D,
        },
    ],
    "faqs": [
        {
            "q": "How long is the waiting period with GEICO?",
            "a": "GEICO does not say. Its guide answers the question with \"ask an agent what waiting periods apply to your policy\", and its landing page only defines pre-existing conditions in terms of the waiting period. The day counts exist one step away: GEICO's footer links to Embrace's terms, where the sample contract for 48 states and DC has no accident wait, a 14-day illness wait and a 180-day orthopedic exclusion list, and the Kansas, New Mexico and South Carolina contract says two days accident, fourteen days illness and six months orthopedic for dogs (all read 2026-09-29).",
            "source_url": G_ART,
            "checked": D,
        },
        {
            "q": "How long is the waiting period with Allstate?",
            "a": "\"All policies have a 2-week illness waiting period. Other waiting periods and exclusions vary by state.\" That is the whole published answer: no accident figure, no orthopedic figure, no cruciate figure and no cancer figure appear on the Allstate pet insurance pages read 2026-09-29. Its footer links to the same Embrace terms GEICO links to.",
            "source_url": A_PET,
            "checked": D,
        },
        {
            "q": "How long is the waiting period with ASPCA?",
            "a": "Its quote page prints a five-row table: accidents and injuries excluding ligament and knee injuries - no waiting period; preventive care - no waiting period; ligament and knee injuries - 14 days; illnesses - 14 days; hereditary and congenital conditions - 14 days. The same page's effective-date text then says accident and illness coverage begins 14 days after the effective date, so accidents are published as both 0 and 14 days on one page (read 2026-09-29).",
            "source_url": AS_QUOTE,
            "checked": D,
        },
        {
            "q": "Where do GEICO's and Allstate's day counts actually live?",
            "a": "In one document neither of them hosts. Both footers say the product is administered by Embrace Pet Insurance Agency and underwritten by American Modern Insurance Group companies, then point to embracepetinsurance.com/coverage/embrace-terms for full terms and conditions. That terms page publishes two versions: V5 for Kansas, New Mexico and South Carolina (2 days accident, 14 days illness, 6 months orthopedic for dogs) and V6 for the other 48 states and DC (no accident wait, 14 days illness, 180-day orthopedic exclusion list) (read 2026-09-29).",
            "source_url": E_TERMS,
            "checked": D,
        },
        {
            "q": "How long before cancer is covered?",
            "a": "No brand publishes a cancer-specific wait, so the illness wait is what applies. In the Embrace contract behind GEICO and Allstate, cancer is named inside \"Illnesses\" - fourteen days - with two written traps: an undiagnosed mass before the end of that wait is not covered \"including those caused by cancer\", and osteosarcoma showing signs during the orthopedic period is excluded. Allstate files cancer under illnesses, so its 2-week figure applies. ASPCA lists cancer under illness coverage, so its 14-day row applies (all read 2026-09-29).",
            "source_url": E_V5,
            "checked": D,
        },
        {
            "q": "How long is the cruciate ligament (CCL or TPLO) waiting period?",
            "a": "In the Embrace contract GEICO and Allstate link to, a cruciate ligament injury showing signs in the first 180 days after the start date is excluded and pre-existing for the life of the policy (V6, 48 states and DC), while the V5 form for KS, NM and SC uses a six-month orthopedic waiting period instead - reducible by an orthopedic exam in states that allow it. ASPCA publishes 14 days for \"Ligament and knee injuries\" on its quote page, but its California notice prints 12 months for ligament and knee conditions on the Levels 2, 3 and 4 disclosure (all read 2026-09-29).",
            "source_url": E_V6,
            "checked": D,
        },
        {
            "q": "Do waiting periods change from state to state?",
            "a": "For all three, yes - in three different ways. Allstate just says they \"vary by state\". The Embrace contract GEICO and Allstate link to splits into two versions: V5 for KS, NM and SC and V6 for the other 48 states and DC, and the accident wait is 2 days in the first and none in the second. ASPCA publishes state-by-state documents - sample plans, an Insurer Disclosure of Important Policy Provisions and a Waiting Period Waiver Form per state - plus a California notice with three different waiting-period sets (read 2026-09-29).",
            "source_url": E_TERMS,
            "checked": D,
        },
        {
            "q": "Can you shorten or waive a pet insurance waiting period?",
            "a": "Two of the three publish a route. Embrace's orthopedic exam and waiver process can cut the orthopedic wait \"to as few as 14 days\" in states that allow it - an exam inside the first 14 days moves the end date to the end of the illness wait, a later exam moves it to the exam date. ASPCA links a state-specific Waiting Period Waiver Form and a Waiting Period Health Assessment from its state documents page. GEICO's own pages publish no waiver; Allstate's publish none either (all read 2026-09-29).",
            "source_url": E_ORTHO,
            "checked": D,
        },
        {
            "q": "Does the waiting period restart later on?",
            "a": "In the contract behind GEICO and Allstate, yes on a coverage increase: the waiting period \"also applies again when there are Coverage increases but is waived for policy renewals and optional Coverage renewals\". ASPCA's quote page does not publish a restart rule; it only says conditions during the wait are ineligible. Switching insurers still means a fresh wait with the new company (read 2026-09-29).",
            "source_url": E_V6,
            "checked": D,
        },
    ],
    "blocks": [
        {"type": "section", "h2": "How this page was checked", "html": (
            "<p>On <strong>2026-09-29</strong> we read the pages each brand itself publishes about waiting periods, "
            "plus the contract documents those pages point to:</p>"
            "<ul><li><strong>GEICO</strong> - its pet insurance landing page (footer disclaimer included) and its "
            "flagship guide, which was bylined August 31, 2026.</li>"
            "<li><strong>Allstate</strong> - the pet insurance landing page with its FAQ block and footnotes, and its "
            "dog insurance resource page for how it classifies cancer.</li>"
            "<li><strong>ASPCA</strong> - the quote page with its waiting-period table and effective-date sections, "
            "the What's Covered page, the California policy notice and the state documents page. Direct requests to "
            "that domain return 403, so those four pages were read through a text-rendering fetch of the same URLs on "
            "2026-09-29.</li>"
            "<li><strong>Embrace terms</strong> - the terms page with its state selector, and both live sample "
            "contracts (V5 and V6), because GEICO's and Allstate's own footers link there for \"full terms and "
            "conditions\".</li></ul>"
            "<p>Where a brand does not publish a figure, this page says so instead of filling the gap with a "
            "third-party estimate.</p>"
        )},
        {"type": "compare", "h2": "Side by side: what each brand's own pages say"},
        {"type": "section", "h2": "GEICO and Allstate both point at the same contract", "html": (
            "<p>Neither GEICO nor Allstate underwrites its own pet insurance, and neither prints a waiting-period day "
            "count of its own - GEICO's guide hands the question to an agent, Allstate's FAQ gives one number and "
            "defers the rest to the states. Both sites then say the same thing in their footer: administered by "
            "Embrace Pet Insurance Agency, underwritten by American Modern Insurance Group companies, and <em>\"For "
            "full terms and conditions, visit www.embracepetinsurance.com/coverage/embrace-terms\"</em>.</p>"
            "<p>That terms page publishes the contract in two live versions, chosen by a state dropdown: <strong>V5 "
            "for Kansas, New Mexico and South Carolina</strong> (two days accident, fourteen days illness, six months "
            "orthopedic for dogs) and <strong>V6 for the other 48 states and DC</strong> (no accident wait, fourteen "
            "days illness, and a 180-day exclusion that attaches cruciate ligament disease, IVDD, patellar luxation "
            "and hip dysplasia to the policy for life if they show up early). The accident answer therefore differs by "
            "state: 0 days in most of the country, 2 days in three states.</p>"
            "<p>Cancer gets no separate line in any of this: the contract names cancer inside \"Illnesses\", so the "
            "fourteen-day illness wait is the number, with two written traps - an undiagnosed mass before the end of "
            "that wait is not covered even when cancer caused it, and osteosarcoma that shows up inside the "
            "orthopedic period is excluded.</p>"
        )},
        {"type": "section", "h2": "ASPCA publishes a table - and two different accident answers", "html": (
            "<p>ASPCA is the only one of the three that prints day counts on its own site, and the table is genuinely "
            "useful: no waiting period for accidents (excluding ligament and knee injuries), no waiting period for "
            "preventive care, and 14 days each for ligament and knee injuries, illnesses, and hereditary and "
            "congenital conditions.</p>"
            "<p>Then the same page undercuts its own first row: the effective-date section states that \"Coverage for "
            "accidents and illnesses begins 14 days after your coverage effective date\" and that anything happening "
            "inside those 14 days is ineligible. Both statements were read on 2026-09-29 and neither references the "
            "other.</p>"
            "<p>The state paperwork goes further than the marketing pages: ASPCA's California notice prints three "
            "waiting-period sets on one page - 30-day illness plus a 180-day hereditary window plus a 12-month "
            "ligament-and-knee wait for Levels 2, 3 and 4; a 14-day illness and 14-day ligament wait for Complete "
            "Coverage; and a 14-day accident-and-illness and 14-day ligament set on a third form. The page does not "
            "say which form a given reader is sold.</p>"
        )},
        {"type": "section", "h2": "State by state, in plain terms", "html": (
            "<p>All three say waiting periods vary by state - and each one proves it differently. Allstate says it in "
            "one sentence and stops. The Embrace contract behind GEICO and Allstate publishes two versions and lets "
            "you pick your state from a dropdown to see which one you get. ASPCA publishes per-state sample plans, an "
            "Insurer Disclosure of Important Policy Provisions and, where it applies, a Waiting Period Waiver Form, "
            "and links a Waiting Period Health Assessment.</p>"
            "<p>Practical consequence: any single \"GEICO waiting period\" number you read on a comparison site is at "
            "best a summary of one of two contract versions, and comparison sites do not usually say which. The "
            "contract you are sold - and the state you live in - decides.</p>"
        )},
        {"type": "section", "h2": "The same table for Lemonade, Spot and Fetch", "html": (
            "<p>We already read this field for the three brands we track most closely: "
            "<a href=\"/pet-insurance-waiting-periods\">pet insurance waiting periods compared</a> covers "
            "Lemonade's 0 / 14 / 30 days, Spot's 14-day state sample policies and Fetch's up-to-15-day plus "
            "6-month orthopedic wait, with the same source-per-cell discipline used here. The two pages are meant to "
            "be read together: one answers \"what do the brands on this site publish\", the other answers \"what do "
            "GEICO, ASPCA and Allstate publish\".</p>"
        )},
        {"type": "facts", "h2": "Every figure with its official source"},
        {"type": "faqs", "h2": "Pet insurance waiting periods by condition - FAQ"},
        {"type": "cards", "h2": "Every brand on this site, page by page"},
    ],
    "disclaimer": (
        "This page is not affiliated with GEICO, Allstate, the ASPCA or Embrace. It repeats only what those brands "
        "publish on their own pages, footers, notices and sample contract documents, with the source and check date "
        "attached to every figure; waiting periods depend on your state, the plan form you are sold and your pet's "
        "history, and the policy wording always governs. Facts last checked 2026-09-29."
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
