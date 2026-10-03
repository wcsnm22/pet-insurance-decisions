"""Append the lemonade-cat-insurance article object to data/articles.json.

Keeps the file's existing formatting: json.dump with indent=1 and ensure_ascii=False,
which is what the current file already uses. Usage: python inject_cat_article.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ARTICLES = ROOT / "data" / "articles.json"
NEW = ROOT / "data" / "_cat_article.json"

data = json.loads(ARTICLES.read_text(encoding="utf-8"))
new = json.loads(NEW.read_text(encoding="utf-8"))

slugs = [a["slug"] for a in data["articles"]]
if new["slug"] in slugs:
    data["articles"] = [a for a in data["articles"] if a["slug"] != new["slug"]]
    print("replaced existing entry")
data["articles"].append(new)

ARTICLES.write_text(
    json.dumps(data, ensure_ascii=False, indent=1) + "\n",
    encoding="utf-8",
)
print("articles now: %d" % len(data["articles"]))
print("last slug: %s" % data["articles"][-1]["slug"])
