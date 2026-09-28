# -*- coding: utf-8 -*-
"""Add the G3 gap article: pet-insurance-wellness-add-on (data/articles.json).

All figures were read on 2026-09-28 from the brands' own official pages and
Spot's own sample policy PDFs (linked from spotpet.com/sample-policy).
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).parent
PATH = ROOT / "data" / "articles.json"
TODAY = "2026-09-28"

L_LEMON = "https://www.lemonade.com/pet/insurance-guide/lemonades-preventative-care-options-explained/"
S_WELL = "https://spotpet.com/wellness"
S_SAMPLE = "https://spotpet.com/sample-policy"
S_GOLD = "https://assets.ctfassets.net/m5ehn3s5t7ec/rcRJqNeeTUUYxIm0WS6bU/10732c41bdf344599e656aecfbb93125/Preventive_IAIC_Gold_copy.pdf"
S_PLAT = "https://assets.ctfassets.net/m5ehn3s5t7ec/4v8nxVvZL52Gzot7vlIfZz/b4210a777421682f3e6f2c7e09b6e618/Preventive_IAIC_Platinum_copy.pdf"
F_WELL = "https://www.fetchpet.com/pet-insurance/wellness"
F_DED = "https://www.fetchpet.com/faqs/is-there-a-deductible-for-pet-wellness"
F_WAIT = "https://www.fetchpet.com/faqs/is-there-a-waiting-period-for-pet-wellness"
F_ALONE = "https://www.fetchpet.com/faqs/can-i-get-a-pet-wellness-plan-on-its-own"
N_WELL = "https://www.petinsurance.com/petwellness/"

ARTICLE = {
    "slug": "pet-insurance-wellness-add-on",
    "nav_label": "Wellness Add-Ons",
    "type": "vs",
    "keyword": "pet insurance wellness add-on",
    "title": "Pet Insurance Wellness Add-Ons Compared: What Each Official Benefit Schedule Actually Pays",
    "description": (
        "Pet insurance wellness add-ons compared line by line: the per-item annual maximums Lemonade, Spot, "
        "Fetch and Nationwide print in their own benefit schedules - exams, vaccines, parasite tests, dental "
        "cleaning, spay/neuter, microchip - with the source page and the day each figure was read. 2026-09-28."
    ),
    "h1": "Pet insurance wellness add-ons: what each official benefit schedule pays, per item",
    "lede": (
        "Quick answer, read from four official schedules on 2026-09-28: only two of them print a plan-level "
        "dollar ceiling - Fetch $390 / $700 / $1,200 a year (Essentials / Advantage / Prime) and Nationwide "
        "$450 / $800 - while Spot prints per-item maximums only (they sum to $250 Gold and $450 Platinum) and "
        "Lemonade describes benefits as counts (1 exam, 3 vaccines) with no dollar ceiling at all. For a "
        "routine dental cleaning the caps run $250 at Fetch Prime and Nationwide's top tier, $150 at Spot "
        "Platinum and $150 in Lemonade's Preventative+ package. One item, four different shapes."
    ),
    "stats": [
        {
            "value": "$1,200 / $800 / $450",
            "label": "top published annual ceiling: Fetch Prime, Nationwide's $800 plan, Spot Platinum (our sum of its printed caps)",
        },
        {
            "value": "$250 vs $150",
            "label": "routine dental cleaning: Fetch Prime and Nationwide's top plan vs Spot Platinum and Lemonade Preventative+",
        },
        {
            "value": "4 schedules, 15 item lines",
            "label": "every figure read from the brand's own page or sample policy PDF on 2026-09-28",
        },
    ],
    "columns": [
        {"name": "Lemonade", "url": "/lemonade-pet-insurance"},
        {"name": "Spot", "url": "/spot-pet-insurance"},
        {"name": "Fetch", "url": "/fetch-pet-insurance"},
        {"name": "Nationwide", "url": "https://www.petinsurance.com/petwellness/"},
    ],
    "rows": [
        {
            "label": "How the add-on is sold",
            "cells": [
                "Four preventative packages on one official guide: Routine Vet Care (available nationwide), Routine Vet Care Plus (select states), the Preventative+ Care package and a Puppy/Kitten package for pets under two years old; the same page also names newer Core and Enhanced Preventative Care plans in some states. Added to a Lemonade pet policy.",
                "Two optional add-ons named on Spot's sample-policy page: Gold Preventive Care and Platinum Preventive Care, issued as an amendatory endorsement to the base policy; the endorsement says the procedures paid are the ones listed for the option on your declarations page, and the option can be changed or cancelled at renewal.",
                "One Wellness add-on in three plans - Essentials, Advantage and Prime. Fetch's own FAQ states Fetch Wellness coverage is only available as an add-on to a Fetch policy, never on its own.",
                "Two wellness plans added to an accident and illness plan, printed as maximum annual benefits of $450 and $800; the page states wellness plans are not available in all states.",
            ],
            "sources": [L_LEMON, S_SAMPLE, F_ALONE, N_WELL],
        },
        {
            "label": "Published annual ceiling",
            "cells": [
                "No dollar ceiling is published - the guide states benefits in counts and says every covered item is subject to an annual limit that resets at renewal, but prints no total.",
                "No plan total is printed either - only per-item annual maximums inside the two sample endorsements, which sum to $250 (Gold) and $450 (Platinum); that sum is our addition of Spot's printed figures.",
                "$390 a year (Essentials), $700 (Advantage), $1,200 (Prime), printed as reimbursed up to; the same page prints plan costs of $212, $357 and $478 a year.",
                "$450 and $800 printed as maximum annual benefits; the per-item maximums in each column add up to exactly those two totals (our addition of the printed figures).",
            ],
            "sources": [L_LEMON, S_SAMPLE, F_WELL, N_WELL],
        },
        {
            "label": "Annual wellness exam",
            "cells": [
                "1 wellness exam per year in Routine Vet Care, Routine Vet Care Plus and Preventative+; 2 wellness exams in the Puppy/Kitten package. No dollar cap published.",
                "$50.00 a year in both the Gold and Platinum sample endorsements, paid up to the lesser of that maximum or the amount charged.",
                "$50 (Essentials), $75 (Advantage), $100 (Prime) a year; the coverage cards print up to $100/yr, which is the Prime figure.",
                "$80 per policy term covering two exams, $40 max per exam - the same line in both the $450 and the $800 plan.",
            ],
            "sources": [L_LEMON, S_GOLD, F_WELL, N_WELL],
        },
        {
            "label": "Vaccinations",
            "cells": [
                "3 vaccines per year (up to 6 in the Puppy/Kitten package); the FAQ says Lemonade publishes no list of eligible vaccines - they must be recommended by a vet licensed in the state.",
                "Per-vaccine caps, not a package total: Gold pays $20 each for DHLPP/FVRCP and for rabies/lyme/FIP while Bordetella/FELV is $0.00; Platinum pays $25 on each of the three vaccine lines.",
                "$50 (Essentials), $80 (Advantage), $125 (Prime) a year.",
                "$80 for a vaccination or titer, in both the $450 and the $800 plan.",
            ],
            "sources": [L_LEMON, S_PLAT, F_WELL, N_WELL],
        },
        {
            "label": "Heartworm, flea and tick prevention medication",
            "cells": [
                "Covered in Routine Vet Care Plus (Life Essentials) and in Preventative+ - heartworm or flea/tick medication; no dollar cap published.",
                "$0.00 a year in Gold, $25.00 a year in Platinum.",
                "$35 (Essentials), $75 (Advantage), $250 (Prime) a year.",
                "$100 a year for flea control or heartworm prevention, in both plans.",
            ],
            "sources": [L_LEMON, S_PLAT, F_WELL, N_WELL],
        },
        {
            "label": "Fecal test",
            "cells": [
                "Included in every package as annual wellness testing (fecal or internal parasite test); no dollar cap published.",
                "$20.00 (Gold), $25.00 (Platinum) a year.",
                "$20 (Essentials), $50 (Advantage), $65 (Prime) a year.",
                "$30 a year, both plans.",
            ],
            "sources": [L_LEMON, S_PLAT, F_WELL, N_WELL],
        },
        {
            "label": "Heartworm or FeLV/FIV test",
            "cells": [
                "Included in every package as annual wellness testing; no dollar cap published.",
                "$20.00 (Gold), $25.00 (Platinum) a year.",
                "$20 (Essentials), $50 (Advantage), $65 (Prime) a year, printed as Heartworm test.",
                "$35 a year, both plans.",
            ],
            "sources": [L_LEMON, S_PLAT, F_WELL, N_WELL],
        },
        {
            "label": "Blood test, urinalysis and imaging",
            "cells": [
                "Bloodwork sits in every package's annual wellness testing; Routine Vet Care Plus adds blood testing, blood pressure monitoring and preventative x-rays and ultrasounds under Life Essentials. No dollar caps published.",
                "Blood test $0.00 in Gold and $25.00 in Platinum; urinalysis $0.00 in Gold and $25.00 in Platinum.",
                "Blood test $20 / $65 / $100 and urinalysis $20 / $50 / $65 a year across the three plans.",
                "One additional test per policy term - a health screen blood test, a radiograph (X-ray) or an EKG - $100 in the $800 plan and Not covered in the $450 plan; urinalysis is not a line in the published schedule.",
            ],
            "sources": [L_LEMON, S_PLAT, F_WELL, N_WELL],
        },
        {
            "label": "Deworming and health certificate",
            "cells": [
                "Deworming appears under Routine Vet Care Plus and Puppy/Kitten (Life Essentials); a health certificate is not a line on the guide. No dollar caps published.",
                "Deworming $20.00 (Gold) / $25.00 (Platinum); health certificate $0.00 (Gold) / $25.00 (Platinum).",
                "No deworming line in any of the three Fetch wellness plans; health certificate $30 a year in all three.",
                "Deworming $25 and health certificate $50, in both plans.",
            ],
            "sources": [L_LEMON, S_PLAT, F_WELL, N_WELL],
        },
        {
            "label": "Routine dental cleaning and spay/neuter",
            "cells": [
                "Preventative+ covers routine dental prophylaxis up to $150 a year (not treatment for dental illness); Routine Vet Care Plus states it does not include routine dental cleanings - that is the separate Dental Care add-on - but covers spay/neuter under Life Essentials, and the Puppy/Kitten package covers the spay/neuter procedure.",
                "One combined line: Dental Cleaning $100.00 in Gold, Dental Cleaning or Spay/Neuter $150.00 in Platinum; Spot's wellness page adds that spaying or neutering is covered for an extra cost in the Platinum Preventative Add-on.",
                "One combined line: Dental cleaning / Spaying / Neutering at $175 (Essentials), $200 (Advantage), $250 (Prime) a year; the coverage cards separately print dental cleaning up to $250/yr and spaying or neutering up to $250/yr.",
                "One combined line: Spay/Neuter or Dental cleaning - Not covered in the $450 plan, $250 in the $800 plan, and coverage starts 90 days after the original policy term effective date.",
            ],
            "sources": [L_LEMON, S_PLAT, F_WELL, N_WELL],
        },
        {
            "label": "Microchip",
            "cells": [
                "Microchipping (implantation and registration) is covered in the Puppy/Kitten package and in Routine Vet Care Plus under Life Essentials; no dollar cap published.",
                "Spot's wellness page advertises Microchip implantation coverage included, but neither the Gold nor the Platinum sample endorsement we read on 2026-09-28 contains a microchip line.",
                "$25 (Essentials), $25 (Advantage), $35 (Prime) a year.",
                "$50 a year, in both plans.",
            ],
            "sources": [L_LEMON, S_WELL, F_WELL, N_WELL],
        },
        {
            "label": "Waiting period on the wellness add-on",
            "cells": [
                "None: once you purchase a policy, coverage becomes active at 12:01 AM the next day and preventative care can be used from then.",
                "Not stated in the sample Preventive Care endorsement we read; the endorsement only repeats that it follows the base policy's terms, conditions and exclusions.",
                "None: wellness claims can be submitted on or after the effective date given in the enrollment confirmation email - the day you enroll.",
                "The only wellness wait printed on the page is 90 days for spay/neuter or dental cleaning in the $800 plan, from the original policy term effective date.",
            ],
            "sources": [L_LEMON, S_GOLD, F_WAIT, N_WELL],
        },
        {
            "label": "Deductible on wellness claims",
            "cells": [
                "None on preventative claims: you will not be asked to meet your deductible for preventative care claims.",
                "not published on the official site - neither Spot's wellness page nor the sample Gold and Platinum endorsements state how a deductible applies to preventive care claims.",
                "None: there is no deductible for Fetch Wellness coverage.",
                "The wellness page's own reimbursement FAQ states all plans have an annual deductible, and that plans with pre-set benefit allowances reimburse only up to those amounts.",
            ],
            "sources": [L_LEMON, "", F_DED, N_WELL],
        },
        {
            "label": "Price of the add-on (published)",
            "cells": [
                "not published on the official site - the guide sends readers to a quote and prints no package price.",
                "not published on the official site - Spot's wellness page shows Click For Price buttons that go to a quote.",
                "As low as $18/month (Essentials), $30/month (Advantage), $40/month (Prime), with printed annual plan costs of $212, $357 and $478.",
                "not published on the official site - the page offers a personalized quote and prints no premium.",
            ],
            "sources": ["", "", F_WELL, ""],
        },
        {
            "label": "Items only this schedule lists",
            "cells": [
                "Life Essentials items with no counterpart in the other three schedules: gastropexy, joint and organ screening, blood pressure monitoring, genetic testing, preventative x-rays and ultrasounds, nail trimming.",
                "No extras: the two sample schedules stop at exams, vaccines, tests, deworming, health certificate and the combined dental/spay-neuter line.",
                "Anal gland expression $30, behavioral exam $25 and activity monitor $50 a year - none of these three appears in the Lemonade, Spot or Nationwide schedules.",
                "Health certificate $50 and the choice of a radiograph (X-ray) or EKG test at $100 - the X-ray/EKG line appears in no other schedule here.",
            ],
            "sources": [L_LEMON, S_PLAT, F_WELL, N_WELL],
        },
    ],
    "facts": [
        {
            "fact": "Fetch publishes three wellness plans with a plan-level annual ceiling: Essentials reimburses up to $390/yr, Advantage up to $700/yr, Prime up to $1,200/yr",
            "condition": "Wellness is an add-on to a Fetch accident and illness policy; prices printed as low as $18, $30 and $40 per month and $212, $357 and $478 per year; the page notes plans vary by state",
            "source_url": F_WELL,
            "checked": TODAY,
        },
        {
            "fact": "Fetch's per-item annual maximums, top plan (Prime): annual exam $100, vaccinations $125, heartworm/flea/tick prevention $250, dental cleaning or spay/neuter $250, blood test $100, heartworm test $65, urinalysis $65, fecal test $65, microchip $35, anal gland expression $40, behavioral exam $25, health certificate $30, activity monitor $50",
            "condition": "Prime plan; each line is a per-year maximum printed in the plan table, paid as a set dollar amount rather than a percentage",
            "source_url": F_WELL,
            "checked": TODAY,
        },
        {
            "fact": "Fetch's per-item annual maximums, Essentials / Advantage: annual exam $50 / $75, vaccinations $50 / $80, heartworm-flea-tick prevention $35 / $75, dental cleaning or spay/neuter $175 / $200, blood test $20 / $65, heartworm test $20 / $50, urinalysis $20 / $50, fecal test $20 / $50, microchip $25 / $25, health certificate $30 / $30, activity monitor $50 / $50, anal gland expression $30 / $30, behavioral exam $25 / $25",
            "condition": "Essentials and Advantage plans respectively, from the same two plan tables on the wellness page",
            "source_url": F_WELL,
            "checked": TODAY,
        },
        {
            "fact": "Adding Fetch's own printed per-item maximums gives $550 (Essentials), $805 (Advantage) and $1,200 (Prime), while the plan totals Fetch prints are $390, $700 and $1,200 - only the Prime column agrees",
            "condition": "Our addition of the figures printed in Fetch's three plan tables on 2026-09-28; Fetch's page does not explain the difference between the item sums and the plan totals",
            "source_url": F_WELL,
            "checked": TODAY,
        },
        {
            "fact": "Fetch Wellness pays a set dollar amount for each type of preventive care instead of 70%, 80% or 90% of an approved claim, with no copay, no deductible and no waiting period",
            "condition": "Stated on the wellness page under What does pet wellness cover",
            "source_url": F_WELL,
            "checked": TODAY,
        },
        {
            "fact": "There is no deductible for Fetch Wellness coverage",
            "condition": "Fetch FAQ answer: No, there is no deductible for Fetch Wellness coverage",
            "source_url": F_DED,
            "checked": TODAY,
        },
        {
            "fact": "There is no waiting period for Fetch Wellness - claims can be submitted on or after the effective date in the enrollment confirmation email",
            "condition": "Fetch FAQ answer; the same page says wellness coverage starts on or after the day you enroll",
            "source_url": F_WAIT,
            "checked": TODAY,
        },
        {
            "fact": "Fetch Wellness coverage is only available as an add-on to a Fetch pet insurance policy, never on its own",
            "condition": "Fetch FAQ answer to Can I get a pet wellness plan on its own?",
            "source_url": F_ALONE,
            "checked": TODAY,
        },
        {
            "fact": "Spot's sample Gold Preventive Care endorsement prints annual maximums of: dental cleaning $100.00, annual exam $50.00, heartworm/flea prevention $0.00, deworming $20.00, health certificate $0.00, heartworm or FeLV test $20.00, urinalysis $0.00, blood test $0.00, fecal test $20.00, Bordetella/FELV vaccine $0.00, DHLPP/FVRCP $20.00, rabies/lyme/FIP $20.00 - they sum to $250",
            "condition": "Sample endorsement (Independence American Insurance Company, sample effective 08/02/2024 to 08/02/2025) linked from spotpet.com/sample-policy; the $250 total is our addition of the printed lines",
            "source_url": S_GOLD,
            "checked": TODAY,
        },
        {
            "fact": "Spot's sample Platinum Preventive Care endorsement prints annual maximums of: dental cleaning or spay/neuter $150.00, annual exam $50.00, heartworm/flea prevention $25.00, deworming $25.00, health certificate $25.00, heartworm or FeLV test $25.00, urinalysis $25.00, blood test $25.00, fecal test $25.00, Bordetella/FELV vaccine $25.00, DHLPP/FVRCP $25.00, rabies/lyme/FIP $25.00 - they sum to $450",
            "condition": "Same sample endorsement series; reimbursement is up to the lesser of the allowable maximum or the amount charged, and only for procedures listed for the option on the declarations page",
            "source_url": S_PLAT,
            "checked": TODAY,
        },
        {
            "fact": "Spot's sample-policy page offers Gold Preventive Care and Platinum Preventive Care as optional add-ons, and every Gold/Platinum link we read on that page (2026-09-28) pointed to the same two endorsement PDFs",
            "condition": "spotpet.com/sample-policy, which publishes separate Accident Only and Accident & Illness PDFs per state but shared preventive-care PDFs",
            "source_url": S_SAMPLE,
            "checked": TODAY,
        },
        {
            "fact": "Spot's wellness page advertises exam fees covered, microchip implantation coverage included, $1,000 in discounts from Spot Perks and any licensed vet in the U.S. or Canada, and says spaying or neutering is covered for an extra cost in the Platinum Preventative Add-on",
            "condition": "The page's footnote states exam fees for wellness or annual exams are not covered unless the optional preventive care coverage is purchased; neither sample schedule contains a microchip line",
            "source_url": S_WELL,
            "checked": TODAY,
        },
        {
            "fact": "Lemonade's Routine Vet Care package covers 1 wellness exam per year, 3 vaccines per year and annual wellness testing (fecal or internal parasite test, bloodwork, heartworm or FeLV/FIV test)",
            "condition": "Routine Vet Care is the basic package, available nationwide; preventative care is not subject to the policy's annual deductible",
            "source_url": L_LEMON,
            "checked": TODAY,
        },
        {
            "fact": "Lemonade's Preventative+ package adds flea/tick or heartworm medication and routine dental cleaning, and pays routine dental prophylaxis up to $150 per year",
            "condition": "Routine dental prophylaxis only - not treatment for dental illness; Routine Vet Care Plus explicitly excludes routine dental cleanings, which live in the separate Dental Care add-on",
            "source_url": L_LEMON,
            "checked": TODAY,
        },
        {
            "fact": "Lemonade's Routine Vet Care Plus package lists Life Essentials: spay/neuter, microchip, gastropexy, heartworm/flea/tick prevention medication, deworming, nail trimming, urinalysis, joint screening, organ screening, blood testing, blood pressure monitoring, genetic testing, preventative x-rays and ultrasounds",
            "condition": "Available in select states; every covered item is subject to an annual limit, and no dollar caps are printed on the page",
            "source_url": L_LEMON,
            "checked": TODAY,
        },
        {
            "fact": "Lemonade's Puppy/Kitten package covers 2 wellness exams, up to 6 vaccines, wellness testing, flea/tick or heartworm medication, the spay/neuter procedure and microchipping, and can only be added while the pet is under two years old",
            "condition": "Puppy/Kitten Preventative Care package, from the same official preventative care guide",
            "source_url": L_LEMON,
            "checked": TODAY,
        },
        {
            "fact": "Lemonade has no waiting period for preventative care (coverage activates at 12:01 AM the next day) and does not apply the deductible to preventative care claims; benefits reset each policy year",
            "condition": "Lemonade FAQ block on the same page; coverage options and availability vary by state",
            "source_url": L_LEMON,
            "checked": TODAY,
        },
        {
            "fact": "Lemonade publishes no list of specific vaccines eligible for reimbursement - the vaccine only has to be recommended by a vet licensed in the state where they operate",
            "condition": "Lemonade FAQ answer on the preventative care guide page",
            "source_url": L_LEMON,
            "checked": TODAY,
        },
        {
            "fact": "Nationwide's wellness page prints two maximum annual benefits, $450 and $800, with per-item maximums of: two exams per policy term at $80 total ($40 max per exam), vaccination or titer $80, heartworm or FeLV/FIV test $35, fecal test $30, deworming $25, microchip $50, health certificate $50, flea control or heartworm prevention $100",
            "condition": "Both columns carry the same lines; the $450 column shows Not covered for the extra test and for spay/neuter or dental cleaning; the columns sum to exactly $450 and $800",
            "source_url": N_WELL,
            "checked": TODAY,
        },
        {
            "fact": "Nationwide's $800 plan adds one additional test per policy term - health screen blood test, radiograph (X-rays) or electrocardiogram (EKG) - at $100, and Spay/Neuter or Dental cleaning at $250 that starts 90 days after the original policy term effective date",
            "condition": "Top tier only; both lines are marked Not covered in the $450 column; the page also states wellness plans are not available in all states",
            "source_url": N_WELL,
            "checked": TODAY,
        },
        {
            "fact": "Nationwide reimburses some plans on pre-set benefit allowances rather than a percentage, and its own FAQ answer on that page states all plans have an annual deductible",
            "condition": "From the How does reimbursement work? answer on the wellness page; the page also says most plans start 1-14 days after approval",
            "source_url": N_WELL,
            "checked": TODAY,
        },
        {
            "fact": "Fetch's wellness page states that Pets Best, AKC and Nationwide only offer 2 wellness plans while Fetch offers 3, and compares its own coverage against Trupanion, Healthy Paws, Lemonade and MetLife",
            "condition": "Fetch's own competitor claim, printed in the Compare Fetch Pet Wellness Plans section - it is a claim by an interested party, not an independent count",
            "source_url": F_WELL,
            "checked": TODAY,
        },
    ],
    "faqs": [
        {
            "q": "Which pet insurance wellness add-on pays the most per item?",
            "a": "On the published schedules read 2026-09-28, Fetch's Prime plan carries the highest printed caps on most lines ($100 exam, $125 vaccines, $250 dental cleaning or spay/neuter, $250 heartworm-flea-tick prevention) and the highest plan ceiling at $1,200 a year, with Nationwide's $800 plan second. Spot's Platinum endorsement sums to $450 and Lemonade prints no dollar caps at all. Those are published ceilings, not quotes - what you pay depends on your state, your pet and your declarations page.",
            "source_url": F_WELL,
            "checked": TODAY,
        },
        {
            "q": "Do wellness add-ons have a waiting period?",
            "a": "Lemonade says no waiting period for preventative care - coverage activates at 12:01 AM the day after purchase. Fetch says no waiting period for wellness either, with claims accepted from the effective date in the enrollment confirmation email. Spot's sample preventive-care endorsement states no wellness waiting period of its own. Nationwide publishes one: spay/neuter or dental cleaning starts 90 days after the original policy term effective date on the $800 plan (read 2026-09-28).",
            "source_url": L_LEMON,
            "checked": TODAY,
        },
        {
            "q": "Do I have to meet my deductible for wellness claims?",
            "a": "Lemonade says you will not be asked to meet your deductible for preventative care claims, and Fetch says there is no deductible for Fetch Wellness coverage. Spot's wellness page and its sample Gold and Platinum endorsements do not publish an answer, and Nationwide's own reimbursement FAQ states all plans have an annual deductible (read 2026-09-28).",
            "source_url": F_DED,
            "checked": TODAY,
        },
        {
            "q": "Can I buy a wellness plan on its own, without pet insurance?",
            "a": "No, not from any of these four. Fetch's FAQ says Fetch Wellness coverage is only available as an add-on to a Fetch policy; Spot sells its Gold and Platinum preventive care as endorsements to a base plan; Lemonade's packages attach to a Lemonade pet policy; Nationwide's wellness plans are added to its accident and illness plans (read 2026-09-28).",
            "source_url": F_ALONE,
            "checked": TODAY,
        },
        {
            "q": "How much does a wellness add-on cost?",
            "a": "Only Fetch publishes a price on the page: as low as $18, $30 and $40 a month for Essentials, Advantage and Prime, with printed annual plan costs of $212, $357 and $478. Lemonade, Spot and Nationwide all send readers to a quote and print no premium (read 2026-09-28).",
            "source_url": F_WELL,
            "checked": TODAY,
        },
        {
            "q": "Does a wellness add-on cover dental cleaning and spay/neuter?",
            "a": "The four schedules draw the line differently. Spot and Nationwide combine both procedures in one line ($150 Spot Platinum, $250 Nationwide's $800 plan, not covered in its $450 plan). Fetch combines them too at $175 / $200 / $250 a year. Lemonade pays routine dental prophylaxis up to $150 a year only in Preventative+ - Routine Vet Care Plus explicitly excludes routine cleanings - while spay/neuter sits in Routine Vet Care Plus and the Puppy/Kitten package (read 2026-09-28).",
            "source_url": L_LEMON,
            "checked": TODAY,
        },
        {
            "q": "Is a microchip covered by a wellness add-on?",
            "a": "Nationwide prints $50 a year in both plans; Fetch prints $25 / $25 / $35 a year across its three plans; Lemonade covers microchip implantation and registration in the Puppy/Kitten package and in Routine Vet Care Plus. Spot's wellness page advertises microchip implantation coverage included, but neither of the two sample preventive-care endorsements we read on 2026-09-28 contains a microchip line.",
            "source_url": N_WELL,
            "checked": TODAY,
        },
        {
            "q": "Can I just add up the per-item caps to see what a plan pays?",
            "a": "Sometimes the sum matches the printed ceiling, sometimes it does not. Nationwide's item caps add up to exactly $450 and $800, and Fetch's Prime caps add up to exactly $1,200 - but Fetch's Essentials caps add up to $550 against a printed $390 ceiling, and Advantage adds up to $805 against a printed $700. Spot prints no ceiling at all, so its $250 and $450 are our sums, and Lemonade's benefits are counts, not dollars. Compare the printed ceiling, not the item list (read 2026-09-28).",
            "source_url": F_WELL,
            "checked": TODAY,
        },
        {
            "q": "How do I check the schedule that applies to my own policy?",
            "a": "Read your declarations page and the endorsement attached to it - Spot's sample endorsement says outright that it pays only for procedures listed for the Preventive Care option on your declarations page, and both Fetch and Nationwide say plans vary by state. Spot also publishes state sample policies at spotpet.com/sample-policy, which is where the Gold and Platinum schedules on this page come from (read 2026-09-28).",
            "source_url": S_SAMPLE,
            "checked": TODAY,
        },
    ],
    "blocks": [
        {
            "type": "section",
            "h2": "How this page was checked",
            "html": (
                "<p>On <strong>2026-09-28</strong> we opened four official sources - and nothing else - looking for "
                "published dollar figures attached to individual wellness items:</p>"
                "<ul>"
                "<li><strong>Lemonade</strong> - its preventative care options guide, which is marked Last Updated: Aug 19, 2026 and describes four packages plus two newer plans.</li>"
                "<li><strong>Spot</strong> - its wellness marketing page, its sample-policy page, and the two sample Preventive Care endorsements those pages link (Gold and Platinum, Independence American Insurance Company, sample policy period 08/02/2024-08/02/2025).</li>"
                "<li><strong>Fetch</strong> - its wellness page with three plan tables, plus the wellness FAQ pages on deductibles, waiting periods and standalone purchase.</li>"
                "<li><strong>Nationwide (petinsurance.com)</strong> - its wellness coverage page with the two-column benefit schedule. We include Nationwide here because that page is the one place a full published benefit schedule exists, and because Fetch names it as a two-plan competitor.</li>"
                "</ul>"
                "<p>Two disciplines run through the table below. First, units are never converted: Lemonade publishes counts, so its cells say counts; Spot publishes no plan total, so the $250 and $450 figures are labelled as our addition of its printed lines. Second, where a brand prints nothing, the cell says "
                "<em>not published on the official site</em> instead of being filled from a broker or a review site.</p>"
            ),
        },
        {
            "type": "section",
            "h2": "The two ceilings, and one dental cleaning",
            "html": (
                "<figure style=\"margin:1.2em 0\">"
                "<img src=\"/assets/wellness-schedules.svg\" alt=\"Bar charts of published pet insurance wellness add-on ceilings: Fetch Prime 1,200 dollars, Nationwide 800 dollars, Spot Platinum 450 dollars summed from printed caps, Lemonade no published dollar ceiling; and routine dental cleaning caps of 250, 250, 150 and 150 dollars, read 2026-09-28\" width=\"720\" height=\"560\" loading=\"lazy\" style=\"max-width:100%;height:auto;border:1px solid #e4e9ee;border-radius:8px\">"
                "<figcaption class=\"muted\">Annual ceilings as printed by each brand, and the routine dental cleaning cap - read from the official pages and sample endorsement PDFs on 2026-09-28.</figcaption>"
                "</figure>"
            ),
        },
        {"type": "compare", "h2": "Every published figure, item by item - four official schedules"},
        {
            "type": "section",
            "h2": "Where the four schedules disagree",
            "html": (
                "<ul>"
                "<li><strong>The line items themselves are not the same shape.</strong> Spot and Nationwide each pay dental cleaning and spay/neuter out of one combined line, so a pet that only needs a cleaning is drawing from the same pot as one that needs a surgery. Fetch also combines them. Lemonade is the opposite: dental lives in Preventative+ only, spay/neuter lives in two other packages, so no single Lemonade package covers both.</li>"
                "<li><strong>Only two brands print a ceiling you can plan around.</strong> Fetch and Nationwide publish plan-level totals; Spot publishes per-item maximums and no total; Lemonade publishes counts and an annual limit it does not quantify. Anything that ranks these four on price is comparing a ceiling with a list.</li>"
                "<li><strong>An item's published cap can be zero.</strong> Spot's Gold endorsement prints $0.00 for heartworm/flea prevention, health certificate, urinalysis, blood test and the Bordetella vaccine - the line exists, the maximum is zero. Nationwide's $450 plan prints Not covered for the extra test and for spay/neuter or dental cleaning. A checklist that only asks whether an item is listed would call both of those covered.</li>"
                "<li><strong>A marketing page and its own policy schedule can disagree.</strong> Spot's wellness page says microchip implantation coverage is included; neither sample preventive-care endorsement we read contains a microchip line. We show both, and we do not reconcile them for the brand.</li>"
                "<li><strong>Adding up Fetch's own items does not reproduce two of its three plan totals.</strong> The printed caps sum to $550, $805 and $1,200 against printed ceilings of $390, $700 and $1,200; Nationwide's columns do sum to $450 and $800. Fetch's page does not explain the gap, and neither do we - we just report both numbers.</li>"
                "</ul>"
            ),
        },
        {"type": "facts", "h2": "Every figure with its official source"},
        {"type": "faqs", "h2": "Pet insurance wellness add-ons - FAQ"},
        {"type": "cards", "h2": "Every brand on this site, page by page"},
    ],
    "disclaimer": (
        "This page is not affiliated with Lemonade, Spot, Fetch or Nationwide. It repeats only figures the brands "
        "publish on their own official pages, FAQ pages and sample policy documents, with the source and the day we "
        "read it attached to every figure; totals marked as our addition are arithmetic on the brands' printed lines, "
        "not figures the brands publish. Wellness schedules, prices and plan names vary by state and change over "
        "time - check the brand's own page before buying."
    ),
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
