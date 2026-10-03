"""End-to-end check of the four things the deploy was supposed to achieve."""
import re
import urllib.request

BASE = "https://furadvisor.com"


def get(path):
    req = urllib.request.Request(BASE + path, headers={"User-Agent": "Mozilla/5.0 (verify)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.status, r.read().decode("utf-8", "replace")


for path in ["/", "/lemonade-cat-insurance", "/lemonade-pet-insurance", "/sitemap.xml"]:
    status, body = get(path)
    print(f"{path:28} HTTP {status}  {len(body):>7} chars")

_, brand = get("/lemonade-pet-insurance")
print("\nbrand page internal link:")
print("  <h2>More on Lemonade</h2>:", "<h2>More on Lemonade</h2>" in brand)
print("  href to cat page         :", '<a href="/lemonade-cat-insurance">' in brand)
m = re.search(r'<h2>More on Lemonade</h2>\s*<p>(.*?)</p>', brand, re.S)
print("  rendered                 :", re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else "MISSING")

_, sm = get("/sitemap.xml")
locs = re.findall(r"<loc>(.*?)</loc>", sm)
print("\nsitemap entries:", len(locs))
print("  cat page listed:", any("lemonade-cat-insurance" in u for u in locs))
for u in locs:
    if "lemonade" in u:
        print("   ", u)

_, home = get("/")
print("\nindex nav link to cat page:", "/lemonade-cat-insurance" in home)
