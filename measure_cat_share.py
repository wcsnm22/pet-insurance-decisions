"""Measure the three m00006 judging criteria for the live lemonade-cat-insurance page.

Counting rule, fixed here so the number can be reproduced:
  body words = every word of the article's own prose: the lede, all `section` blocks, and every
               cell of the official fact table and the FAQ block. Headings, nav, footer and JSON-LD
               are excluded. This is the whole page a reader sees.
  exclusive  = the two blocks written from owner-reported claim material:
               "Real cat claim cases, as their owners reported them" and
               "What these cases do not establish". They are read straight out of the block source,
               so the count cannot drift into the neighbouring official sections.
  share      = exclusive words / body words.

Criteria: (1) share >= 30%, (2) first screen is a direct answer, (3) no source trace.
The cases material is deliberately absent from the official fact table, which is asserted below.
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAGE = ROOT / "site" / "lemonade-cat-insurance.html"
ARTICLES = ROOT / "data" / "articles.json"
SLUG = "lemonade-cat-insurance"

EXCLUSIVE_H2 = {
    "Real cat claim cases, as their owners reported them",
    "What these cases do not establish",
}

raw = PAGE.read_text(encoding="utf-8")
data = json.loads(ARTICLES.read_text(encoding="utf-8"))
art = next(a for a in data["articles"] if a["slug"] == SLUG)


def words(s: str) -> int:
    return len(re.findall(r"[A-Za-z0-9$%.,'-]+", s))


def text_of(fragment: str) -> str:
    s = re.sub(r"<script.*?</script>", " ", fragment, flags=re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


# ---------- body words ----------
body_parts = [art["lede"]]
exclusive_parts = []
for blk in art["blocks"]:
    if blk.get("type") == "section":
        t = text_of(blk["html"])
        body_parts.append(t)
        if blk.get("h2") in EXCLUSIVE_H2:
            exclusive_parts.append(t)
    elif blk.get("type") == "facts":
        body_parts += [f["fact"] + " " + f["condition"] for f in art["facts"]]
    elif blk.get("type") == "faqs":
        body_parts += [q["q"] + " " + q["a"] for q in art["faqs"]]
    elif blk.get("type") == "compare":
        body_parts += [r["label"] + " " + " ".join(r["cells"]) for r in art["rows"]]

total_words = words(" ".join(body_parts))
exclusive_words = words(" ".join(exclusive_parts))
share = exclusive_words / total_words * 100

print(f"body words          : {total_words}")
print(f"exclusive words     : {exclusive_words}")
print(f"exclusive share     : {share:.1f}%  (>= 30% -> {'PASS' if share >= 30 else 'FAIL'})")

# ---------- first screen ----------
lede = re.search(r'<p class="lede">(.*?)</p>', raw, re.S)
first_screen_ok = bool(lede) and re.search(r"\b(yes|starts at|about \$)", lede.group(1)) is not None
print(f"first screen is answer: {'PASS' if first_screen_ok else 'FAIL'}")

# ---------- no source trace anywhere in the page ----------
TRACE = (r"(?i)\b(reddit|subreddit|thread|forum|poster|commenter|according to|reviewer|"
         r"community|OP|per a post|one poster)\b|r/[a-z0-9_]{3,}|u/[A-Za-z0-9_-]{3,}|\*\*")
hits = re.findall(TRACE, raw)
print(f"source-trace hits   : {hits if hits else 'NONE -> PASS'}")

# ---------- the case material must stay out of the official fact table ----------
facts_tbody = re.search(r"<tbody>(.*?)</tbody>", raw, re.S).group(1)
case_figures = ["9,000", "9000", "493", "1,106", "1106", "305", "275", "25,000", "25000"]
leaked = [x for x in case_figures if x in facts_tbody]
print(f"case figures inside the official fact table: {leaked if leaked else 'NONE -> PASS'}")
print(f"official hosts in fact table: {sorted({re.sub(r'^https?://', '', u).split('/')[0] for u in re.findall(r'https?://[^\"<> ]+', facts_tbody)})}")

# ---------- structure ----------
print("block order         :", [b.get("type") for b in art["blocks"]])
sections = [b["h2"] for b in art["blocks"] if b.get("type") == "section"]
print("sections            :")
for i, s in enumerate(sections, 1):
    tag = "  <- exclusive" if s in EXCLUSIVE_H2 else ""
    print(f"   {i}. {s}{tag}")
