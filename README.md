# Pet Insurance Decisions

The source repository behind **[furadvisor.com](https://furadvisor.com)** — a static site answering pet insurance questions with facts read only from each brand's own official pages.

**Read the site: <https://furadvisor.com>**

Every number on the site exists because someone opened the insurer's own page, read it, and wrote down where it came from and when. This repository is where that record lives, so the site can be checked instead of trusted.

- Pages: home + one page per brand (Lemonade, Spot, Fetch) + editorial guides (`data/articles.json`) + About / Privacy / Contact
- Every fact carries its official source URL and check date
- Machine-readable summaries for crawlers and assistants: <https://furadvisor.com/llms.txt> and <https://furadvisor.com/llms-full.txt>
- Zero dependencies: `python build.py` renders `site/` (JSON-LD, canonical, sitemap.xml, robots.txt included)
- Deploy: Cloudflare Pages. The `furwell` Pages project is the one that serves production `furadvisor.com`; `pet-insurance-decisions` is the same site under its own `*.pages.dev` host.
  - `wrangler pages deploy site --project-name=furwell --branch=main --commit-dirty=true`
  - A path can 404 for a short while right after a deploy; check `https://<deployment-id>.furwell.pages.dev/...` to tell a propagation lag from a real routing problem.

## Rules

- No invented prices, terms, promo codes or expiry dates — if the brand's site does not publish it, the page says so.
- No Chinese in output pages.
- A fact without `source_url` or `checked` in `data/brands.json` fails the build.
- Guides in `data/articles.json` obey the same rules: sources must be on the brand's official domains, every comparison cell carries its source (or says `not published on the official site`), unknown block types fail the build.

## How a fact gets on the site

1. Open the insurer's own page (rate page, sample policy, claims page, state notice) — never an aggregator, a review site or another blog.
2. Record the figure, the exact URL it came from, and the date it was read.
3. If the brand does not publish it, the page says `not published on the official site` rather than estimating.
4. Re-read the source before the figure is treated as current; the check date is rendered on the page.

Anything that cannot be traced back to an official page this way is not published. That rule is enforced by `python selfcheck.py`, which fails the build rather than let an unsourced number through.

## Who maintains it

Maintained by [tangshoufu](https://github.com/wcsnm22). Not affiliated with, endorsed by, or compensated by any insurer. The site does not currently serve ads or affiliate links; outbound insurer links are citations, not paid placements.
