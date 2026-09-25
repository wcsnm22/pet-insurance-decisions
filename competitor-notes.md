# Competitor structure notes — 线二 (frozen three)

Method: 2026-09-25. Ranking set from the pinned SERP (`serp-final.json`, same-load capture, `q=pet insurance&hl=en&num=10&pws=0`, google.com.hk, this machine). Landing URLs confirmed by exact title match against the SERP title. Page structure fetched same day: petinsurance.com + lemonade via curl (HTTP 200), pawlicy.com via real Chrome (Cloudflare challenge blocks curl). Facts below are measured; guesses are marked **[inference]** with the chain.

## 1. petinsurance.com — rank #1 (homepage)

**Measured:** title `Pet Insurance by Nationwide® | America's Best Pet & Vet Insurance` (exact SERP match). H1 `Best. Pet insurance. Ever.SM`. H2s: "Pet insurance trusted by 1 million Americans" → customize-to-budget → Dog insurance → Cat insurance → How pet insurance works → Frequently Asked Questions. 1,182 words of text, 0 tables, JSON-LD present but no usable `@type` parsed. Full-site silo visible in nav: coverage / what's covered / FAQ / compare providers / reviews / customer stories.

**Why it ranks:** **[inference]** authority, not depth — the page itself is thin (1,182 words, no comparison table, no parsed FAQ schema). Chain: Nationwide = licensed insurer (E-E-A-T entity) + brand queries + exact-match title + internal silo feeding the homepage. Not from on-page content richness.

**What we lack:** trust magnitude on the first screen ("1 million Americans" — we have no true equivalent number and will NOT invent one), dog/cat split pages, whole-site topical silo.

**Learn (structure/angle only):** ① one concrete trust statement in the hero built only from verifiable facts ("every row cites the brand's official policy page + check date"); ② dog/cat as dedicated pages — we have neither, and autocomplete confirms demand (`how much is pet insurance for a dog/cat`); ③ keep the silo nav we already have.

## 2. lemonade.com/pet — rank #6 visible (the /pet URL, not /pet-insurance)

**Measured:** title `Pet Insurance for Dogs & Cats by Lemonade` (exact SERP match → this is the ranking URL; lemonade also runs a separate /pet-insurance page that did NOT rank for the head term). H1 `Pet insurance with super fast everything`. JSON-LD: **Product + FAQPage + BreadcrumbList**. 2,133 words, 0 tables. First screen = brand claims + `Check our prices` CTA (quote funnel). H2 pattern: benefit → coverage → savings → "Got questions about pet insurance?" (FAQ) → price → mission.

**Why it ranks:** **[inference]** on-page completeness + brand + engagement funnel. Chain: FAQ/Product schema eligible for rich results, answer-shaped FAQ H2 matching PAA questions, quote-CTA drives interaction, plus `lemonade pet insurance` brand volume (135k/mo per step-7 data).

**What we lack:** BreadcrumbList schema (ours: WebSite/FAQPage/Article/ItemList/ClaimReview — rich already, breadcrumb is the one missing type), a price/quote CTA (we deliberately don't sell — that's our positioning, not a defect), word depth on the homepage.

**Learn (structure/angle only):** ① add BreadcrumbList to build.py (cheap, verifiable); ② title/H2 phrasing that answers the query instead of selling — keep our "answered on the first screen" direction; ③ FAQ block sits low on their page but exists as schema — ours already does this ✓.

## 3. pawlicy.com — rank #7 (homepage)

**Measured:** title `Pawlicy Advisor - Compare & Shop Best Pet Insurance | Top-Rated Marketplace, Recommended by Veterinarians` (exact SERP match). H1 `Compare top pet insurance quotes and coverage, instantly.` First screen: "#1 BEST PET INSURANCE FINDER" → answer H1 → "100% free service | Expert matches" → **Dog / Cat buttons** → `Compare Quotes →` → "4.9 stars across hundreds of reviews". H2s: market-compare promise → 1-2-3 steps → done-for-you → marketplace → FAQ. **590 words total** (thin), 0 tables, JSON-LD without a usable `@type`.

**Why it ranks:** **[inference]** intent-match + conversion structure + links. Chain: H1 literally restates the query's job ("compare … instantly"), interactive first screen satisfies intent on the spot, review scores + vet-recommendation in title supply trust, yet 590 words shows content depth is NOT what's carrying it — **[inference]** backlinks + marketplace brand + review aggregate.

**What we lack:** interactive first move (dog/cat choice), star-rating/social-proof display (no true rating exists for us yet — do not fabricate), super-direct H1 (ours is close: "Pet insurance, answered on the first screen").

**Learn (structure/angle only):** ① make the first screen not just an answer but a **choice** (dog/cat entry — pairs with the dog/cat pages from #1); ② keep H1 as the query's job stated plainly; ③ when we have real, verifiable proof numbers (e.g. from GSC), surface them — never invented ones.

## Side-by-side (all measured today)

| | furadvisor.com | petinsurance.com | lemonade.com/pet | pawlicy.com |
|---|---|---|---|---|
| Words (page text) | 1,472 | 1,182 | 2,133 | 590 |
| Comparison table | 1 | 0 | 0 | 0 |
| Per-fact source + check date | **yes, every row** | no | no | no |
| FAQ schema | yes (6 pages) | not parsed | yes | not parsed |
| Breadcrumb schema | no | – | yes | – |
| Trust number in hero | none (won't invent) | "1 million Americans" | rating claims | "4.9 stars / 1,000,000+" |
| Dog/cat split pages | **no** | yes | partial | first-screen buttons |
| Price CTA | no (not a seller) | quotes | "Check our prices" | "Compare Quotes →" |

## Bottom line for the main line
- Their #1 and #7 win on **authority + intent match**, not because their copy is deeper — ours already has more text, a table, and per-fact citations none of them show. Our exclusivity lever = receipts on every row + first-screen answer (≥30% exclusive ✓).
- Concrete follow-ups queued: ① BreadcrumbList in build.py; ② dog/cat pages (new URLs from ammo-list demand); ③ hero trust line built only from verifiable facts; ④ first-screen dog/cat choice.
- 死线 honored: nothing above was copied into the site — structure and angles only.
