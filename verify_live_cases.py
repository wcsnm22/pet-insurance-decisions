"""Verify the deployed cases section on production, not just locally."""
import re
import time
import urllib.error
import urllib.request

U = "https://furadvisor.com/lemonade-cat-insurance"
H2_CASES = "Real cat claim cases, as their owners reported them"
H2_LIMITS = "What these cases do not establish"

body = ""
for attempt in range(5):
    req = urllib.request.Request(U, headers={"User-Agent": "Mozilla/5.0 (verify)", "Cache-Control": "no-cache"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            body = r.read().decode("utf-8", "replace")
            if H2_CASES in body:
                break
            print(f"attempt {attempt + 1}: 200 but old content ({len(body)} chars), retrying")
    except urllib.error.HTTPError as e:
        print(f"attempt {attempt + 1}: HTTP {e.code}")
    time.sleep(4)

print("live chars:", len(body))
print("has cases section      :", H2_CASES in body)
print("has limits section     :", H2_LIMITS in body)
print("facts table before cases:", body.find("Every figure with its official source") < body.find(H2_CASES))
print("cases before FAQ       :", body.find(H2_CASES) < body.find("<h2>FAQ</h2>"))
print("limits before facts    :", body.find(H2_LIMITS) < body.find("Every figure with its official source"))
print("sections on live page  :", len(re.findall(r"<h2>", body)))
print("trace terms on live    :", {
    x: body.lower().count(x.lower())
    for x in ["reddit", "thread", "forum", "poster", "community", "according to", "u/"]
    if body.lower().count(x.lower())
} or "NONE")
print("case figures in live fact table:",
      [x for x in ["9,000", "493", "1,106", "305"] if x in re.search(r"<tbody>.*?</tbody>", body, re.S).group(0)] or "NONE")
print("cases section has links:",
      re.findall(r'href="[^"]+"', re.search(r"<h2>Real cat claim cases.*?(?=<h2>|$)", body, re.S).group(0)) or "NONE")
