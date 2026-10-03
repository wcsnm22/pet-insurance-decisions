"""Strict identity / sourcing audit for the cases section on the built cat page."""
import re
from pathlib import Path

t = Path("site/lemonade-cat-insurance.html").read_text(encoding="utf-8")

terms = [
    "reddit", "subreddit", "r/pet", "u/", "thread", "forum", "poster", "comment",
    "community", "according to", "upvote", "karma", "flair", "reviewer",
    "trustpilot", "yelp", "/r/", "OP said", "one owner said in",
]
hits = {x: t.lower().count(x.lower()) for x in terms}
print("trace-term hits:", {k: v for k, v in hits.items() if v} or "NONE")

cjk = [c for c in t if "\u4e00" <= c <= "\u9fff"]
print("CJK chars:", len(cjk))
print("markdown '**' leaks:", t.count("**"))

# every href on the page that is not an internal route or an official lemonade host
hrefs = sorted(set(re.findall(r'href="([^"]+)"', t)))
external = [h for h in hrefs if h.startswith("http") and "lemonade.com" not in h]
print("non-lemonade external links:", external or "NONE")

# the cases section must carry no source link at all
sec = re.search(
    r"<h2>Real cat claim cases.*?(?=<h2>|$)", t, re.S
)
print("links inside the cases section:", re.findall(r'href="[^"]+"', sec.group(0)) or "NONE")
print("sections on page:", len(re.findall(r"<h2>", t)))
