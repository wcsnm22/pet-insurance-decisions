"""Post-build verification for the lemonade-cat-insurance page and the whole site."""
import re
from pathlib import Path

root = Path(__file__).resolve().parent
site = root / "site"
page = site / "lemonade-cat-insurance.html"
t = page.read_text(encoding="utf-8")

cjk = sorted({c for c in t if "\u4e00" <= c <= "\u9fff"})
print("new page:", len(t), "chars, CJK:", cjk if cjk else "none")
print("h1:", re.findall(r"<h1[^>]*>(.*?)</h1>", t, re.S)[:1])
print("h2 count:", len(re.findall(r"<h2>", t)))
print("facts table rows:", len(re.findall(r"<tr>", t)))
print("ld+json blocks:", len(re.findall(r"application/ld\+json", t)))
print("FAQ details:", len(re.findall(r"<details open>", t)))
print("canonical:", re.findall(r'rel="canonical" href="([^"]+)"', t))
print("sources:", sorted(set(re.findall(r"https://www\.lemonade\.com[^\"'<> ]*", t))))
print("checked dates:", sorted(set(re.findall(r"checked (\d{4}-\d{2}-\d{2})", t))))

bad = []
for f in sorted(site.rglob("*.html")):
    s = f.read_text(encoding="utf-8")
    c = [ch for ch in s if "\u4e00" <= ch <= "\u9fff"]
    if c:
        bad.append((str(f.relative_to(root)), len(c)))
print("pages containing CJK across site:", bad if bad else "none")

sm = (site / "sitemap.xml").read_text(encoding="utf-8")
print("sitemap entries:", sm.count("<loc>"), "| has cat page:", "lemonade-cat-insurance" in sm)
print("nav has cat page on index:", "lemonade-cat-insurance" in (site / "index.html").read_text(encoding="utf-8"))
