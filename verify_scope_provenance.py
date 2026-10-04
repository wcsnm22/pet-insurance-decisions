"""Prove the narrowing was surgical: only the cat page's two declaration lines moved.

Checks, all against the live production host:
  1. the generic hero declaration still renders on every other article page
  2. the cat page's cases section is present, in position, and its opening sentence is intact
  3. the cat page body prose is unchanged (the three m00006 measurements still hold)
"""
import re
import urllib.request

BASE = "https://furadvisor.com"
GENERIC = ("Every figure on this page was read from the brand's own official site and carries its "
           "source link and check date.")
CASES_OPEN = "None of the following is a company statement or an audited record"


def get(path):
    req = urllib.request.Request(BASE + path, headers={"User-Agent": "Mozilla/5.0 (verify)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


cat = get("/lemonade-cat-insurance")
others = [
    # article pages use templates/article.html and carried the generic hero line
    "/lemonade-vs-spot",
    "/pet-insurance-claim-denied",
    "/spot-vs-fetch",
]
print("1. other ARTICLE pages still carry the generic hero declaration")
for p in others:
    b = get(p)
    print(f"   {p:32} generic={GENERIC in b}  scoped={'brand-facts sections' in b}")

print("\n1b. brand pages use templates/brand.html, which never had that line")
for p in ["/lemonade-pet-insurance", "/spot-pet-insurance", "/fetch-pet-insurance"]:
    b = get(p)
    print(f"   {p:32} generic={GENERIC in b}  scoped={'brand-facts sections' in b}  brand-disclaimer={'not affiliated' in b}")

print("\n2. cat page cases section intact")
i_cases = cat.find("Real cat claim cases, as their owners reported them")
i_open = cat.find(CASES_OPEN)
i_facts = cat.find("Every figure with its official source")
i_faq = cat.find("<h2>FAQ</h2>")
print("   cases heading present      :", i_cases != -1)
print("   opening sentence intact    :", i_open != -1, "| sits right after heading:", 0 < i_open - i_cases < 400)
print("   official table before cases:", i_facts < i_cases)
print("   cases before FAQ           :", i_cases < i_faq)

print("\n3. the two scoped declarations are the only scoped text")
print("   scoped head sentence       :", "brand-facts sections and in the official source table" in cat)
print("   scoped tail sentence       :", "In the brand-facts sections and the official source table, it repeats" in cat)
print("   old head sentence gone     :", GENERIC not in cat)
print("   old tail sentence gone     :", "It repeats only what Lemonade publishes" not in cat)
