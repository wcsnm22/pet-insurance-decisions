# Four self-checks before delivery:
# (1) no Chinese in generated output (2) every fact has official source + check date
# (3) rendered pages show source links + dates (4) JSON-LD + canonical per page
import json, re, pathlib

site = pathlib.Path(__file__).parent / "site"
data = json.loads((pathlib.Path(__file__).parent / "data" / "brands.json").read_text(encoding="utf-8"))
articles_path = pathlib.Path(__file__).parent / "data" / "articles.json"
articles = json.loads(articles_path.read_text(encoding="utf-8"))["articles"] if articles_path.exists() else []
fails = []


def latest_checked(items):
    """Newest check date actually recorded on a page ("" when none is)."""
    dates = [i["checked"] for i in items if i.get("checked")]
    return max(dates) if dates else ""

# (1) Chinese anywhere in site output
cn = []
for p in site.rglob("*"):
    if p.is_file() and p.suffix in {".html", ".css", ".js", ".xml", ".txt", ".svg"}:
        if re.search(r"[\u4e00-\u9fff]", p.read_text(encoding="utf-8", errors="ignore")):
            cn.append(str(p))
print("[1] Chinese in output:", len(cn), cn[:5])
if cn:
    fails.append("chinese-in-output")

# (2) every fact + faq has official source + check date
official = {"lemonade.com", "www.lemonade.com", "spotpet.com", "www.spotpet.com",
            "spotpetins.com", "www.spotpetins.com", "fetchpet.com", "www.fetchpet.com",
            "petinsurance.com", "www.petinsurance.com", "assets.ctfassets.net",
            "geico.com", "www.geico.com", "allstate.com", "www.allstate.com",
            "aspcapetinsurance.com", "www.aspcapetinsurance.com",
            "embracepetinsurance.com", "www.embracepetinsurance.com"}
n = bad = offsite = 0
for b in data["brands"]:
    for f in b["facts"] + b["faqs"]:
        n += 1
        u = f.get("source_url", "")
        if not u.startswith("http") or not f.get("checked"):
            bad += 1
        if u.split("/")[2] not in official:
            offsite += 1
            print("   non-official source:", u)

# articles.json: facts + FAQs + per-cell compare sources must be official and complete
for a in articles:
    for f in a["facts"] + a["faqs"]:
        n += 1
        u = f.get("source_url", "")
        if not u.startswith("http") or not f.get("checked"):
            bad += 1
            print("   article fact missing source/date:", a["slug"], f.get("fact") or f.get("q"))
        if u.startswith("http") and u.split("/")[2] not in official:
            offsite += 1
            print("   non-official article source:", u)
    ncols = len(a["columns"])
    for r in a["rows"]:
        if len(r["cells"]) != ncols or len(r.get("sources", [])) != ncols:
            bad += 1
            print("   compare shape mismatch:", a["slug"], r["label"])
            continue
        for i, u in enumerate(r["sources"]):
            cell = r["cells"][i]
            if u and u.split("/")[2] not in official:
                offsite += 1
                print("   non-official compare source:", u)
            if not u and not cell.strip().lower().startswith("not published"):
                bad += 1
                print("   compare cell has no source and is not a 'not published' cell:", a["slug"], r["label"])
            if u and cell.strip().lower().startswith("not published"):
                bad += 1
                print("   compare cell claims 'not published' but links a source:", a["slug"], r["label"])
print(f"[2] facts+faqs={n} missing_source_or_date={bad} non_official_domain={offsite}")
if bad or offsite:
    fails.append("fact-provenance")

# (3) rendered pages show source link + date per fact row; check dates == today
for slug in ("lemonade", "spot", "fetch"):
    html = (site / f"{slug}-pet-insurance.html").read_text(encoding="utf-8")
    rows = html.count("<tr>") - (1 if "<th>" in html else 0)
    srcs = len(re.findall(r'href="https://(?:www\.)?(?:lemonade|spotpet|spotpetins|fetchpet|petinsurance|geico|allstate|aspcapetinsurance|embracepetinsurance)[^"]*"|href="https://assets\.ctfassets\.net[^"]*"', html))
    dates = html.count(data["site"]["checked"])
    print(f"[3] {slug}: rows={rows} official_source_links={srcs} check_dates={dates}")
    if srcs < rows or dates < rows:
        fails.append(f"render-provenance-{slug}")

# (3b) rendered article pages: every fact/FAQ carries an official source link + its OWN check date
# (articles are rechecked on different days, so each item's own checked date must appear on the page)
for a in articles:
    html = (site / f"{a['slug']}.html").read_text(encoding="utf-8")
    fact_rows = len(a["facts"])
    srcs = len(re.findall(r'href="https://(?:www\.)?(?:lemonade|spotpet|spotpetins|fetchpet|petinsurance|geico|allstate|aspcapetinsurance|embracepetinsurance)[^"]*"|href="https://assets\.ctfassets\.net[^"]*"', html))
    missing_dates = sorted({f.get("checked", "") for f in a["facts"] + a["faqs"] if f.get("checked", "") not in html})
    in_sitemap = f"/{a['slug']}" in (site / "sitemap.xml").read_text(encoding="utf-8")
    print(f"[3b] {a['slug']}: facts={fact_rows} official_source_links={srcs} missing_check_dates={missing_dates} in_sitemap={in_sitemap}")
    if srcs < fact_rows or missing_dates or not in_sitemap:
        fails.append(f"render-provenance-{a['slug']}")

# (4) JSON-LD + canonical on every page; sitemap/robots present
for p in sorted(site.glob("*.html")):
    h = p.read_text(encoding="utf-8")
    ld = "application/ld+json" in h
    ca = 'rel="canonical"' in h
    print(f"[4] {p.name}: jsonld={ld} canonical={ca}")
    if not (ld and ca):
        fails.append(f"meta-{p.name}")
for f in ("sitemap.xml", "robots.txt", "_worker.js", "assets/style.css",
          "llms.txt", "llms-full.txt"):
    ok = (site / f).exists()
    print(f"[4] {f}: {'ok' if ok else 'MISSING'}")
    if not ok:
        fails.append(f"missing-{f}")

# (6) social card + E-E-A-T on every content page:
# absolute og:image that exists on disk, large-image preview allowed, and a VISIBLE
# byline + check date (not JSON-LD only), with Article author/publisher/dateModified.
CONTENT = [b["slug"] for b in data["brands"]] + [a["slug"] for a in articles]
for slug in CONTENT:
    h = (site / f"{slug}.html").read_text(encoding="utf-8")
    og = re.search(r'<meta property="og:image" content="([^"]+)"', h)
    tw = re.search(r'<meta name="twitter:card" content="([^"]+)"', h)
    rb = re.search(r'<meta name="robots" content="([^"]+)"', h)
    og_name = og.group(1).rsplit("/", 1)[-1] if og else ""
    problems = []
    if not og or not og.group(1).startswith("https://furadvisor.com/assets/og-"):
        problems.append("og:image-not-absolute-or-wrong-host")
    elif not (site / "assets" / og_name).exists():
        problems.append(f"og:image-missing-file:{og_name}")
    if not tw or tw.group(1) != "summary_large_image":
        problems.append("twitter-card-not-large-image")
    if not rb or "max-image-preview:large" not in rb.group(1):
        problems.append("robots-no-large-image-preview")
    if 'class="byline"' not in h:
        problems.append("no-visible-byline")
    # the byline must name the maintainer and print a check date that appears in the data
    by = re.search(r'<p class="byline">(.*?)</p>', h, re.S)
    txt = re.sub(r"<[^>]+>", " ", by.group(1)) if by else ""
    if "tangshoufu" not in txt:
        problems.append("byline-no-maintainer")
    dates = {f.get("checked", "") for f in
             next((b for b in data["brands"] if b["slug"] == slug), {}).get("facts", [])
             + next((b for b in data["brands"] if b["slug"] == slug), {}).get("faqs", [])}
    art = next((a for a in articles if a["slug"] == slug), None)
    if art:
        dates = {f.get("checked", "") for f in art["facts"] + art["faqs"]}
    if not any(d and d in txt for d in dates):
        problems.append("byline-date-not-a-recorded-check-date")
    # Article JSON-LD must carry a Person author and an Organization publisher
    ld = [json.loads(m.group(1)) for m in
          re.finditer(r'<script type="application/ld\+json">(.*?)</script>', h, re.S)]
    page_ld = [b for b in ld if b.get("@type") == "Article"]
    for b in page_ld:
        if b.get("author", {}).get("@type") != "Person":
            problems.append("article-author-not-person")
        if b.get("publisher", {}).get("@type") != "Organization":
            problems.append("article-publisher-not-organization")
        if not b.get("dateModified"):
            problems.append("article-no-dateModified")
        if "datePublished" in b:
            problems.append("article-invented-datePublished")
    print(f"[6] {slug}: og_image={og_name} problems={problems}")
    if problems:
        fails.append(f"eeat-{slug}")

# (5) llms.txt / llms-full.txt: generated from the same data, so they must cover
# every page and carry every recorded source URL - no invented or dropped figures.
idx = (site / "llms.txt").read_text(encoding="utf-8") if (site / "llms.txt").exists() else ""
full = (site / "llms-full.txt").read_text(encoding="utf-8") if (site / "llms-full.txt").exists() else ""
want_urls = [f"/{b['slug']}" for b in data["brands"]] + [f"/{a['slug']}" for a in articles]
missing_pages = [u for u in want_urls if f"{data['site']['base_url'].rstrip('/')}{u}" not in idx]
print(f"[5] llms.txt pages={len(want_urls)} missing={missing_pages}")
if missing_pages:
    fails.append("llms-index-incomplete")

all_sources = set()
for b in data["brands"]:
    for f in b["facts"] + b["faqs"]:
        all_sources.add(f["source_url"])
for a in articles:
    for f in a["facts"] + a["faqs"]:
        all_sources.add(f["source_url"])
    for r in a["rows"]:
        all_sources.update(u for u in r.get("sources", []) if u)
dropped = sorted(u for u in all_sources if u not in full)
print(f"[5] llms-full.txt source_urls={len(all_sources)} dropped={len(dropped)} {dropped[:3]}")
if dropped:
    fails.append("llms-full-dropped-sources")

worker = (site / "_worker.js").read_text(encoding="utf-8") if (site / "_worker.js").exists() else ""
routes = [u for u in ("/llms.txt", "/llms-full.txt") if f'"{u}"' not in worker]
print(f"[5] worker allowlist llms routes missing={routes}")
if routes:
    fails.append("worker-missing-llms-route")

# nav reaches all three utility pages from every page
for p in sorted(site.glob("*.html")):
    h = p.read_text(encoding="utf-8")
    for link in ("/about", "/privacy", "/contact"):
        if link not in h:
            fails.append(f"nav-{p.name}-{link}")

# (7) sitemap.xml: every URL it lists must be a page that exists, must carry
# that page's own lastmod (not one recycled site-wide date), and must not use a
# date the page has no record of.
sm = (site / "sitemap.xml").read_text(encoding="utf-8") if (site / "sitemap.xml").exists() else ""
sm_pairs = re.findall(r"<loc>([^<]+)</loc><lastmod>([^<]*)</lastmod>", sm)
want_lastmod = {data["site"]["base_url"].rstrip("/"): latest_checked(data["home_facts"] + data["home_faqs"])}
for b in data["brands"]:
    want_lastmod[f"{data['site']['base_url'].rstrip('/')}/{b['slug']}"] = latest_checked(b["facts"] + b["faqs"])
for a in articles:
    want_lastmod[f"{data['site']['base_url'].rstrip('/')}/{a['slug']}"] = latest_checked(a["facts"] + a["faqs"])
# utility pages record no facts of their own, so their lastmod is the site-wide check date
for util in ("about", "privacy", "contact"):
    want_lastmod[f"{data['site']['base_url'].rstrip('/')}/{util}"] = data["site"]["checked"]
sm_issues = []
for url, lastmod in sm_pairs:
    if url not in want_lastmod:
        sm_issues.append(f"unknown-url:{url}")
    elif not lastmod:
        sm_issues.append(f"no-lastmod:{url}")
    elif lastmod != want_lastmod[url]:
        sm_issues.append(f"wrong-lastmod:{url}:{lastmod}!={want_lastmod[url]}")
missing_urls = [u for u in want_lastmod if f"<loc>{u}</loc>" not in sm]
if missing_urls:
    sm_issues.append(f"absent-from-sitemap:{missing_urls}")
print(f"[7] sitemap urls={len(sm_pairs)} issues={sm_issues}")
if sm_issues:
    fails.append("sitemap-lastmod")

print("RESULT:", "PASS" if not fails else "FAIL " + ",".join(sorted(set(fails))))
