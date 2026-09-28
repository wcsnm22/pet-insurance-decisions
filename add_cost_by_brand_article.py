# -*- coding: utf-8 -*-
"""Add the G1 gap article: pet-insurance-cost-by-brand (data/articles.json)."""
import json
import pathlib

ROOT = pathlib.Path(__file__).parent
PATH = ROOT / "data" / "articles.json"
TODAY = "2026-09-28"

GUIDE = "https://www.lemonade.com/pet/insurance-guide/pet-insurance-cost/"
HOME = "https://spotpet.com/"
COST = "https://www.fetchpet.com/pet-insurance-cost"

ARTICLE = {
    "slug": "pet-insurance-cost-by-brand",
    "nav_label": "Cost by Brand",
    "type": "pricing",
    "keyword": "pet insurance cost by brand",
    "title": "Pet Insurance Cost by Brand: Published Prices From Each Official Site, Date-Stamped",
    "description": (
        "Pet insurance cost by brand: every price Lemonade, Spot and Fetch print on their own sites - "
        "starting prices, species averages, breed and state figures, and each brand's own competitor table - "
        "with the quote assumptions and the date the brand itself stamped on the number. Read 2026-09-28."
    ),
    "h1": "Pet insurance cost by brand: every price each insurer publishes, with its assumptions and date",
    "lede": (
        "Quick answer, read from the three brands' own pages on 2026-09-28: Lemonade prints a starting price of "
        "$10/month, species averages of about $48/month for dogs and about $27/month for cats, a 47-state range "
        "table stamped \"as of October, 2024\", and a six-insurer competitor table for one Chicago Goldendoodle. "
        "Spot prints two starting prices - dogs from $15/month and cats from $9/month - each with a footnote that "
        "names the ZIP code, deductible and limit the advertised premium assumes, dated Dec. 11 2024. Fetch prints "
        "no starting price at all: it publishes species averages of $35/month and $22/month under a stated policy "
        "configuration and period, twelve breed averages, and its own four-insurer comparison table stamped "
        "\"as of March 2026\". The trap: Fetch's table prices Lemonade at $14.97/month against Fetch's own $27.51, "
        "while Lemonade's table prices Lemonade at $61/month against Fetch's $99 - the same two brands in opposite "
        "orders, because the two quotes assume different pets, different deductibles and different dates. Never "
        "subtract a number from one brand's table against a number from another's."
    ),
    "stats": [
        {"value": "$27.51 vs $14.97", "label": "Fetch's own table: Fetch vs Lemonade, one identical quote (as of March 2026)"},
        {"value": "$61 vs $99", "label": "Lemonade's own table: Lemonade vs Fetch, a different identical quote"},
        {"value": TODAY, "label": "every figure rechecked on the brands' own pages"},
    ],
    "columns": [
        {"name": "Lemonade", "url": "/lemonade-pet-insurance"},
        {"name": "Spot", "url": "/spot-pet-insurance"},
        {"name": "Fetch", "url": "/fetch-pet-insurance"},
    ],
    "rows": [
        {
            "label": "Lowest price published",
            "cells": [
                "$10/month: \"a policy for a dog or a cat starts at $10/month\", basic accident and illness, varying by breed and state; the guide page is marked Last Updated: Jun 3, 2026 (read " + TODAY + ")",
                "Dogs from $15/month. The footnote: \"Advertised premium is from Dec. 11 2024 based on an accident and illness plan with an 80% reimbursement rate, $500 annual deductible, and a $2,500 annual limit for a 2-year-old small mixed dog (11-25lbs) in 32009\" (read " + TODAY + ")",
                "not published on the official site - the cost page opens with averages, not a floor price, and says the price depends on age, breed and where you live (read " + TODAY + ")",
            ],
            "sources": [GUIDE, HOME, ""],
        },
        {
            "label": "Published species average",
            "cells": [
                "About $48/month for dogs and about $27/month for cats, \"across different ages, breeds, and locations\"; the state table behind those averages carries the footnote \"as of October, 2024\" (read " + TODAY + ")",
                "not published on the official site - the home page shows starting prices and quote buttons only, no average (read " + TODAY + ")",
                "$35/month for dogs and $22/month for cats, \"based on U.S. annual premiums ... using the most common coverage configuration of $10,000 annual limit, $300 deductible, and 80% reimbursement rate for the period of 07.01.2024 through 06.30.2025\" (read " + TODAY + ")",
            ],
            "sources": [GUIDE, "", COST],
        },
        {
            "label": "Price tied to a named pet and breed",
            "cells": [
                "One worked example: a 4-year-old Goldendoodle in Chicago at 80% co-insurance, the maximum annual limit and a $250 deductible averages $61/month; the cat example is a 1-year-old short-haired cat in Danbury (read " + TODAY + ")",
                "not published on the official site - Spot's advertised premiums are tied to species, age, weight band and ZIP code, not to a breed (read " + TODAY + ")",
                "Twelve breed averages on one page: French Bulldog $71, German Shepherd $53, Golden Doodle $50, Golden Retriever $50, Maltipoo $35, Shih-Tzu $30, Siamese $29, Mixed Breed $27, Maine Coon $35, Domestic Long Hair $27, Domestic Medium Hair $25, Domestic Shorthair $24 - \"calculated using all policy configurations for the total amount of active policies of that breed, for the period of 01.01.25 through 11.01.25\" (read " + TODAY + ")",
            ],
            "sources": [GUIDE, "", COST],
        },
        {
            "label": "Price tied to a state",
            "cells": [
                "A range for each of 47 states plus DC, e.g. California $45 to $49, New York $40 to $44, Florida $35 to $39, Oklahoma $20 to $24; footnote: \"Lemonade Insurance analyzed policy rates to calculate average pet premiums as of October, 2024\" (read " + TODAY + ")",
                "not published on the official site (read " + TODAY + ")",
                "not published on the official site - the cost page prints one national average and links out to \"pet insurance by state\" instead (read " + TODAY + ")",
            ],
            "sources": [GUIDE, "", ""],
        },
        {
            "label": "The brand's own competitor price table",
            "cells": [
                "Six insurers priced for one quote: Trupanion $336, Fetch $99, Healthy Paws $85, Pets Best $77, ManyPets $73, Lemonade $61 - \"Based on rates for a 4-year-old Goldendoodle in Chicago\", base policy standardized to a $250 deductible, 80% co-insurance and the maximum annual limit, no add-ons or discounts; the competitor rows carry no date of their own (read " + TODAY + ")",
                "not published on the official site - Spot compares coverage and shows a sample claim, but prints no competitor premiums (read " + TODAY + ")",
                "Four insurers priced for one quote: Fetch $27.51, Spot $19.79, Pets Best $21.91, Lemonade $14.97 - footnote: \"Provider comparisons ... prepared solely by Fetch ... as of March 2026. Monthly premium is for a 1 year old small mixed breed in Tampa Florida (zip 33602) with a $5,000 / $500 / 80% policy configuration, no wellness\" and \"Monthly premiums do not include any taxes or fees\" (read " + TODAY + ")",
            ],
            "sources": [GUIDE, "", COST],
        },
        {
            "label": "Price shown inside a claim example",
            "cells": [
                "not published on the official site - the guide walks through claim math (e.g. ($6,000 x 80%) - $250 = $4,550) without attaching a monthly premium to the example pet (read " + TODAY + ")",
                "$75.01/month: the footnote on its $12,345 vet-bill example reads \"an accident and illness policy at $75.01/month with a $500 deductible, 90% reimbursement, and unlimited annual benefit for a 1-year-old giant mix dog\", based on actual policyholder claims from 2023 (read " + TODAY + ")",
                "not published on the official site - its $889 anxiety-claim example lists the four comparison premiums instead of a premium for Fetch's own sample pet (read " + TODAY + ")",
            ],
            "sources": ["", HOME, ""],
        },
        {
            "label": "Date stamp the brand puts on the number",
            "cells": [
                "Guide page marked \"Last Updated: Jun 3, 2026\"; the state averages and the premium analysis behind them are stamped \"as of October, 2024\"; the competitor rows carry no date (read " + TODAY + ")",
                "\"Advertised premium is from Dec. 11 2024\" in the starting-price footnote; no other date on the price figures (read " + TODAY + ")",
                "Comparison \"as of March 2026\"; species averages cover 07.01.2024 through 06.30.2025; breed averages cover 01.01.25 through 11.01.25; page statistics \"as of 9.10.2026\" (read " + TODAY + ")",
            ],
            "sources": [GUIDE, HOME, COST],
        },
        {
            "label": "Page each figure was read from",
            "cells": [
                "lemonade.com/pet/insurance-guide/pet-insurance-cost/ - an editorial guide page (read " + TODAY + ")",
                "spotpet.com - the home page hero, plan cards and the footnotes under the FAQ block (read " + TODAY + ")",
                "fetchpet.com/pet-insurance-cost - a dedicated pricing page with its methodology footnotes (read " + TODAY + ")",
            ],
            "sources": [GUIDE, HOME, COST],
        },
    ],
    "facts": [
        {"fact": "Lemonade's published floor price: \"a policy for a dog or a cat starts at $10/month\"",
         "condition": "Cost guide, first figure on the page; the page is marked Last Updated: Jun 3, 2026; the same page states the base accident and illness policy \"starts around $10 per month, but this can vary by breed and state\"",
         "source_url": GUIDE, "checked": TODAY},
        {"fact": "Lemonade's published averages are about $48/month for dogs and about $27/month for cats",
         "condition": "\"On average, across different ages, breeds, and locations\" - Lemonade's own policyholder data, not a quote",
         "source_url": GUIDE, "checked": TODAY},
        {"fact": "Lemonade's worked dog example averages $61/month",
         "condition": "4-year-old Goldendoodle in Chicago, 80% co-insurance, maximum annual limit available, $250 annual deductible",
         "source_url": GUIDE, "checked": TODAY},
        {"fact": "Lemonade's own competitor table for dogs: Trupanion $336, Fetch $99, Healthy Paws $85, Pets Best $77, ManyPets $73, Lemonade $61 per month",
         "condition": "\"We picked the base policy offered by six different pet insurance companies ... $250 deductible, 80% co-insurance, and the maximum annual limit available, with no add-ons or discounts\"; caption: \"Based on rates for a 4-year-old Goldendoodle in Chicago\" - the competitor rows carry no date",
         "source_url": GUIDE, "checked": TODAY},
        {"fact": "Lemonade's own competitor table for cats: Trupanion $58, ManyPets $44, Fetch $36, Pets Best $35, Lemonade $29 per month",
         "condition": "Caption: \"Based on rates for a 1-year-old short-haired cat in Danbury\"; the page notes Trupanion only offered a 90% co-insurance option, so the offers were standardized as far as possible",
         "source_url": GUIDE, "checked": TODAY},
        {"fact": "Lemonade publishes a state-by-state average range, from $20 to $24 in Oklahoma to $45 to $49 in California, Connecticut and New Hampshire",
         "condition": "Table footnote: \"Lemonade Insurance analyzed policy rates to calculate average pet premiums as of October, 2024. This analysis is based on Lemonade's internal data and is meant for illustrative purposes only\"; for states with no Lemonade data the average was supplemented from another source",
         "source_url": GUIDE, "checked": TODAY},
        {"fact": "Lemonade's published premium levers: deductible options of $100, $250, $500 and $750 (and $1,000 in the same page's FAQ), annual limits from $5,000 to $100,000, and the co-insurance percentage",
         "condition": "Cost guide, \"how to lower your premium\" section; the deductible list in the FAQ adds a $1,000 option",
         "source_url": GUIDE, "checked": TODAY},
        {"fact": "Spot's published dog price: \"Dog insurance Starting from $15/mo\"",
         "condition": "Footnote ^: \"Advertised premium is from Dec. 11 2024 based on an accident and illness plan with an 80% reimbursement rate, $500 annual deductible, and a $2,500 annual limit for a 2-year-old small mixed dog (11-25lbs) in 32009\"",
         "source_url": HOME, "checked": TODAY},
        {"fact": "Spot's published cat price: \"Cat insurance Starting from $9/mo\"",
         "condition": "Footnote ^^: \"Advertised premium is based on an accident and illness plan with an 80% reimbursement rate, $750 annual deductible, and a $2,500 annual limit for a 2-year-old mixed cat in 33801\" - the cat footnote carries no date, the dog footnote is dated Dec. 11 2024",
         "source_url": HOME, "checked": TODAY},
        {"fact": "Spot prices a named example policy at $75.01/month",
         "condition": "Footnote on the $12,345 osteosarcoma claim example: \"an accident and illness policy at $75.01/month with a $500 deductible, 90% reimbursement, and unlimited annual benefit for a 1-year-old giant mix dog\"; the claim itself is \"based on actual policyholder claims from 2023\"",
         "source_url": HOME, "checked": TODAY},
        {"fact": "Spot publishes no average and no state table - its home page shows starting prices, a \"Click For Price\" quote button, a 10% multi-pet discount and a 20% employee discount",
         "condition": "Home page, header and FAQ block, read " + TODAY,
         "source_url": HOME, "checked": TODAY},
        {"fact": "Fetch's published averages: $35/month for dogs and $22/month for cats",
         "condition": "\"Average monthly premiums are based on U.S. annual premiums for dogs and cats, using the most common coverage configuration of $10,000 annual limit, $300 deductible, and 80% reimbursement rate for the period of 07.01.2024 through 06.30.2025\"",
         "source_url": COST, "checked": TODAY},
        {"fact": "Fetch publishes twelve breed averages: French Bulldog $71, German Shepherd $53, Golden Doodle $50, Golden Retriever $50, Maltipoo $35, Shih-Tzu $30, Siamese $29, Mixed Breed $27, Maine Coon $35, Domestic Long Hair $27, Domestic Medium Hair $25, Domestic Shorthair $24 per month",
         "condition": "\"Calculated using all policy configurations for the total amount of active policies of that breed, for the period of 01.01.25 through 11.01.25\" - so these are portfolio averages, not quotes",
         "source_url": COST, "checked": TODAY},
        {"fact": "Fetch's own four-insurer table: Fetch $27.51, Spot $19.79, Pets Best $21.91, Lemonade $14.97 per month",
         "condition": "Footnote: \"Provider comparisons contained herein was prepared solely by Fetch based upon a comparison of the company's policy form or core policy coverages available on Trupanion's Healthy Paws's Lemonade's and Spot's website as of March 2026. Monthly premium is for a 1 year old small mixed breed in Tampa Florida (zip 33602) with a $5,000 / $500 / 80% policy configuration, no wellness. Monthly premiums do not include any taxes or fees. Lemonade & Pets Best Pricing does not include optional add on for Exam Fee\"",
         "source_url": COST, "checked": TODAY},
        {"fact": "On the same table's $889 sample claim, Fetch reimburses $889.00, Spot $311.20, Pets Best $71.00 and Lemonade $71.00",
         "condition": "\"Sample claim to treat anxiety for a small, mixed-breed, 1-year-old dog in Tampa, FL\"; the $889.00 row is marked covered because Fetch includes 100% reimbursement on 7 coverage areas at no extra cost, the other three rows are marked \"Not covered\"",
         "source_url": COST, "checked": TODAY},
        {"fact": "Fetch publishes no starting price: \"The average monthly pet insurance price for Fetch is $35/mo. for dogs and $22/mo. for cats. Your price will vary depending on 3 key factors: your pet's age, their breed and where you live\"",
         "condition": "Pricing page opening answer, read " + TODAY,
         "source_url": COST, "checked": TODAY},
        {"fact": "Fetch's cost page is itself date-stamped three times: comparison \"as of March 2026\", averages for 07.01.2024-06.30.2025, breed figures for 01.01.25-11.01.25",
         "condition": "Footnotes on fetchpet.com/pet-insurance-cost; the page's own data line adds \"Policies in force and number of pets helped based on Fetch data as of 9.10.2026\"",
         "source_url": COST, "checked": TODAY},
        {"fact": "The two brand-printed competitor tables rank Lemonade and Fetch opposite ways: Fetch's table has Fetch at $27.51 against Lemonade at $14.97, Lemonade's table has Lemonade at $61 against Fetch at $99",
         "condition": "Both figures read " + TODAY + " from the brands' own pages; the quotes are not the same - Tampa 1-year-old small mixed breed at $5,000/$500/80% versus Chicago 4-year-old Goldendoodle at $250 deductible/80%/maximum limit, and the two sets of competitor numbers carry different date stamps",
         "source_url": COST, "checked": TODAY},
        {"fact": "Where each brand puts its price: Lemonade on an editorial guide page, Spot in the home-page hero with footnotes under the FAQ block, Fetch on a dedicated pricing page",
         "condition": "All three pages read " + TODAY + "; none of the three shows a price without an assumption footnote somewhere on the page",
         "source_url": HOME, "checked": TODAY},
    ],
    "faqs": [
        {"q": "What is the cheapest pet insurance, by brand, from published numbers?",
         "a": "Only within one table. The lowest figures each brand publishes for itself are Lemonade's $10/month starting price, Spot's $9/month cat and $15/month dog starting prices, and Fetch's $22/month cat and $35/month dog averages - but those three are three different assumption sets (read " + TODAY + "). The only same-assumption cross-brand numbers available are Fetch's table ($14.97 to $27.51/month for one Tampa quote) and Lemonade's table ($61 to $336/month for one Chicago Goldendoodle). Comparing across the two tables produces nonsense.",
         "source_url": COST, "checked": TODAY},
        {"q": "Why do Lemonade and Fetch publish competitor prices that disagree about who is cheaper?",
         "a": "Because each one prices a different pet under a different policy. Fetch prices a 1-year-old small mixed breed in Tampa, FL 33602 at a $5,000 limit, $500 deductible and 80% reimbursement, without wellness, \"as of March 2026\". Lemonade prices a 4-year-old Goldendoodle in Chicago at a $250 deductible, 80% co-insurance and the maximum annual limit, with no date on the competitor rows. Same two brands, opposite order - the assumption footnote is the difference.",
         "source_url": GUIDE, "checked": TODAY},
        {"q": "What does Spot's \"Starting from $15/mo\" actually assume?",
         "a": "Spot's footnote spells it out: an accident and illness plan with an 80% reimbursement rate, a $500 annual deductible and a $2,500 annual limit, for a 2-year-old small mixed dog of 11-25 lbs in ZIP 32009, advertised as of Dec. 11 2024. The cat version uses a $750 deductible and ZIP 33801. Your ZIP, your pet's age and a different deductible all move that number.",
         "source_url": HOME, "checked": TODAY},
        {"q": "Why doesn't Fetch publish a starting price?",
         "a": "It publishes averages instead: $35/month for dogs and $22/month for cats under a stated $10,000 limit / $300 deductible / 80% reimbursement configuration for 07.01.2024-06.30.2025, plus twelve breed averages from its own in-force policies. The page says your price depends on age, breed and location, so it gives portfolio figures rather than a floor.",
         "source_url": COST, "checked": TODAY},
        {"q": "How old are the prices on this page?",
         "a": "Each brand dates its own figures differently: Lemonade marks its guide \"Last Updated: Jun 3, 2026\" while the underlying premium analysis and state table are \"as of October, 2024\"; Spot dates its advertised premium \"Dec. 11 2024\"; Fetch dates its comparison \"as of March 2026\", its averages 07.01.2024-06.30.2025 and its breed figures 01.01.25-11.01.25. All three pages were read again on " + TODAY + ".",
         "source_url": GUIDE, "checked": TODAY},
        {"q": "Are the three brands' published prices comparable?",
         "a": "No. Lemonade's averages come from its own policyholders across ages, breeds and locations; Spot's starting prices are one fixed plan for one age, weight band and ZIP; Fetch's averages use the most common configuration of $10,000 limit, $300 deductible and 80% reimbursement. Subtracting one from another tells you about the assumptions, not about the brands.",
         "source_url": COST, "checked": TODAY},
        {"q": "Do these published prices include taxes, fees and add-ons?",
         "a": "Fetch states its comparison premiums \"do not include any taxes or fees\" and that Lemonade and Pets Best pricing excludes the optional Exam Fee add-on. Spot's advertised premium is a specific accident and illness configuration, and its other discounts (10% multi-pet, 20% employee) are listed separately. Lemonade's figures assume no add-ons or discounts.",
         "source_url": COST, "checked": TODAY},
        {"q": "What is the actual price I would pay?",
         "a": "The quote each brand gives you for your pet - Lemonade's quote flow, Spot's \"Click For Price\" button and Fetch's \"Get your price\" button. The published numbers on this page are averages, floors and worked examples stamped with someone else's pet, ZIP and deductible (read " + TODAY + ").",
         "source_url": HOME, "checked": TODAY},
        {"q": "Do the brands update these published prices?",
         "a": "Only by rewriting the page. Each price carries whatever stamp the brand gave it (Jun 3 2026 / October 2024, Dec. 11 2024, March 2026), so a figure can sit on an official page for months after the analysis behind it. Re-reading the page - as this page does, most recently on " + TODAY + " - is the only way to know what is printed today.",
         "source_url": COST, "checked": TODAY},
    ],
    "blocks": [
        {"type": "section", "h2": "How this page was checked", "html":
            "<p>On <strong>" + TODAY + "</strong> we read three pages - and only official pages - looking for every monthly price each brand publishes, together with the assumption footnote the brand prints underneath it:</p>"
            "<ul>"
            "<li><strong>Lemonade</strong> - its pet insurance cost guide (page marked Last Updated: Jun 3, 2026): starting price, species averages, the Goldendoodle and Danbury worked examples, the two six-insurer tables and the 47-state range table.</li>"
            "<li><strong>Spot</strong> - the home page: the two \"Starting from\" prices in the hero and plan cards, their ^ and ^^ footnotes, the $12,345 claim example and its $75.01/month policy footnote.</li>"
            "<li><strong>Fetch</strong> - fetchpet.com/pet-insurance-cost: the species averages, the twelve breed averages, the four-insurer comparison table and the three methodology footnotes at the bottom of the page.</li>"
            "</ul>"
            "<p>No third-party comparison site, review site or broker table was used. Where a brand does not publish a figure, this page says \"not published on the official site\" instead of borrowing an estimate from somewhere else, and every cell in the table below links the page it came from.</p>"},
        {"type": "section", "h2": "Two brands print each other's prices", "html":
            "<figure style=\"margin:1.2em 0\"><img src=\"/assets/cost-by-brand.svg\" alt=\"Two bar charts of published pet insurance prices: Fetch's own table prices Fetch at 27.51 dollars against Spot 19.79, Pets Best 21.91 and Lemonade 14.97 for one Tampa quote as of March 2026, while Lemonade's own table prices Trupanion 336, Fetch 99, Healthy Paws 85, Pets Best 77, ManyPets 73 and Lemonade 61 for one Chicago Goldendoodle, read 2026-09-28\" width=\"720\" height=\"560\" loading=\"lazy\" style=\"max-width:100%;height:auto;border:1px solid #e4e9ee;border-radius:8px\">"
            "<figcaption>Left: the four premiums Fetch publishes for one identical quote (footnote: 1-year-old small mixed breed, Tampa FL 33602, $5,000 limit / $500 deductible / 80% reimbursement, no wellness, comparison as of March 2026). Right: the six premiums Lemonade publishes for a different identical quote (4-year-old Goldendoodle, Chicago, $250 deductible, 80% co-insurance, maximum annual limit, competitor rows undated). Both read " + TODAY + "; note the two panels use different scales.</figcaption></figure>"},
        {"type": "compare", "h2": "Side by side: every price each brand publishes"},
        {"type": "section", "h2": "The two competitor tables disagree - on purpose", "html":
            "<p>This is the part of \"pet insurance cost by brand\" that comparison sites skip. Two of the three brands price their rivals themselves, and the two tables put the same companies in opposite order:</p>"
            "<ul>"
            "<li><strong>Fetch's table</strong> (as of March 2026): Fetch <strong>$27.51</strong>, Spot $19.79, Pets Best $21.91, Lemonade <strong>$14.97</strong> - so on this quote Lemonade is the cheapest of the four and Fetch the most expensive.</li>"
            "<li><strong>Lemonade's table</strong> (competitor rows undated): Trupanion $336, Fetch <strong>$99</strong>, Healthy Paws $85, Pets Best $77, ManyPets $73, Lemonade <strong>$61</strong> - so on this quote Fetch is more than 50% dearer than Lemonade.</li>"
            "</ul>"
            "<p>Both are published by the brand itself, on its own domain, and neither is wrong: they are answers to different questions. Fetch prices a 1-year-old small mixed breed in Tampa at a $5,000 limit, $500 deductible and 80% reimbursement with no wellness; Lemonade prices a 4-year-old Goldendoodle in Chicago at a $250 deductible, 80% co-insurance and the maximum annual limit. Change the pet, the deductible and the limit, and the ranking flips. That is exactly why this page stamps every figure with the page it came from, the assumption it carries and the date we read it - and why any sentence that starts \"Brand A is cheaper than Brand B\" needs the assumption attached to be worth anything.</p>"},
        {"type": "section", "h2": "The date stamp is the whole point", "html":
            "<p>Every brand dates its prices, but they date different things. Lemonade dates the <em>page</em> (Jun 3, 2026) and the <em>analysis behind its averages</em> (October, 2024) - the competitor rows in between carry no date at all. Spot dates only the advertised starting premium (Dec. 11 2024), and only on the dog footnote. Fetch dates everything: the comparison (March 2026), the species averages (07.01.2024-06.30.2025), the breed averages (01.01.25-11.01.25) and its own site statistics (9.10.2026).</p>"
            "<p>So a price printed today can rest on an analysis that is 11, 17 or 20 months old. That is not a scandal - insurers cannot publish live rates - but it means the honest way to state a figure is <em>number + assumption + brand's own date + the day you read it</em>, which is the format every row and fact above uses.</p>"},
        {"type": "facts", "h2": "Every published price with its official source"},
        {"type": "faqs", "h2": "Pet insurance cost by brand - FAQ"},
        {"type": "cards", "h2": "Every brand on this site, page by page"},
    ],
    "disclaimer": (
        "This page is not affiliated with Lemonade, Spot or Fetch. It repeats only prices the brands publish on "
        "their own guide pages, home pages and pricing pages, with the source, the brand's own date stamp and the "
        "day we read it attached to every figure; published prices are averages, floors or worked examples for the "
        "pet, ZIP code, deductible and limit each brand states, your quote will differ, and the policy you are sold "
        "governs. Facts last checked " + TODAY + "."
    ),
}

data = json.loads(PATH.read_text(encoding="utf-8"))
if any(a["slug"] == ARTICLE["slug"] for a in data["articles"]):
    raise SystemExit("article already exists")
data["articles"].append(ARTICLE)
PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("added", ARTICLE["slug"], "| facts", len(ARTICLE["facts"]), "| faqs", len(ARTICLE["faqs"]), "| rows", len(ARTICLE["rows"]))
