"""Print the two provenance declarations exactly as they currently exist (local + live)."""
import re
import urllib.request

LOCAL = "site/lemonade-cat-insurance.html"
LIVE = "https://furadvisor.com/lemonade-cat-insurance"


def find(body):
    hero = re.search(r'<p class="lede">.*?</p>\s*<div class="stats">.*?</div>\s*<p class="muted">(.*?)</p>', body, re.S)
    tail = re.findall(r'<p class="muted">(.*?)</p>', body, re.S)
    return (hero.group(1).strip() if hero else "NOT FOUND"), (tail[-1].strip() if tail else "NOT FOUND")


with open(LOCAL, encoding="utf-8") as f:
    local = f.read()
req = urllib.request.Request(LIVE, headers={"User-Agent": "Mozilla/5.0 (verify)"})
with urllib.request.urlopen(req, timeout=30) as r:
    live = r.read().decode("utf-8", "replace")

for label, body in (("LOCAL", local), ("LIVE", live)):
    head, tail = find(body)
    print(f"===== {label} ({len(body)} chars) =====")
    print(f"HEAD: {head}")
    print(f"TAIL: {tail}")
    print(f"identical to local: {head == find(local)[0] and tail == find(local)[1]}")
