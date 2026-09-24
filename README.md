# Pet Insurance Decisions

Static site answering pet insurance questions with facts read only from each brand's own official pages.

- Pages: home + one page per brand (Lemonade, Spot, Fetch) + About / Privacy / Contact
- Every fact carries its official source URL and check date
- Zero dependencies: `python build.py` renders `site/` (JSON-LD, canonical, sitemap.xml, robots.txt included)
- Deploy: Cloudflare Pages, project `pet-insurance-decisions`

## Rules

- No invented prices, terms, promo codes or expiry dates — if the brand's site does not publish it, the page says so.
- No Chinese in output pages.
- A fact without `source_url` or `checked` in `data/brands.json` fails the build.
