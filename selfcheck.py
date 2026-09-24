# Four self-checks before delivery:
# (1) no Chinese in generated output (2) every fact has official source + check date
# (3) rendered pages show source links + dates (4) JSON-LD + canonical per page
import json, re, pathlib

site = pathlib.Path(__file__).parent / "site"
data = json.loads((pathlib.Path(__file__).parent / "data" / "brands.json").read_text(encoding="utf-8"))
fails = []

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
            "spotpetins.com", "www.spotpetins.com", "fetchpet.com", "www.fetchpet.com"}
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
print(f"[2] facts+faqs={n} missing_source_or_date={bad} non_official_domain={offsite}")
if bad or offsite:
    fails.append("fact-provenance")

# (3) rendered brand pages show source link + date per fact row; check dates == today
for slug in ("lemonade", "spot", "fetch"):
    html = (site / f"{slug}-pet-insurance.html").read_text(encoding="utf-8")
    rows = html.count("<tr>") - (1 if "<th>" in html else 0)
    srcs = len(re.findall(r'href="https://(?:www\.)?(?:lemonade|spotpet|spotpetins|fetchpet)[^"]*"', html))
    dates = html.count(data["site"]["checked"])
    print(f"[3] {slug}: rows={rows} official_source_links={srcs} check_dates={dates}")
    if srcs < rows or dates < rows:
        fails.append(f"render-provenance-{slug}")

# (4) JSON-LD + canonical on every page; sitemap/robots present
for p in sorted(site.glob("*.html")):
    h = p.read_text(encoding="utf-8")
    ld = "application/ld+json" in h
    ca = 'rel="canonical"' in h
    print(f"[4] {p.name}: jsonld={ld} canonical={ca}")
    if not (ld and ca):
        fails.append(f"meta-{p.name}")
for f in ("sitemap.xml", "robots.txt", "_worker.js", "assets/style.css"):
    ok = (site / f).exists()
    print(f"[4] {f}: {'ok' if ok else 'MISSING'}")
    if not ok:
        fails.append(f"missing-{f}")

# nav reaches all three utility pages from every page
for p in sorted(site.glob("*.html")):
    h = p.read_text(encoding="utf-8")
    for link in ("/about", "/privacy", "/contact"):
        if link not in h:
            fails.append(f"nav-{p.name}-{link}")

print("RESULT:", "PASS" if not fails else "FAIL " + ",".join(sorted(set(fails))))
