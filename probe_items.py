import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
A = json.loads((ROOT / "data/articles.json").read_text(encoding="utf-8"))
B = json.loads((ROOT / "data/brands.json").read_text(encoding="utf-8"))


def iter_items(node, path=""):
    if isinstance(node, dict):
        if isinstance(node.get("source_url"), str) and ("fact" in node or "q" in node):
            yield path, node
        else:
            for k, v in node.items():
                yield from iter_items(v, f"{path}/{k}")
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from iter_items(v, f"{path}[{i}]")


want = ["Which pet insurance is cheapest", "8 weeks and older", "How much does pet insurance cost per month"]
for label, blob in (("articles", A), ("brands", B)):
    for path, node in iter_items(blob):
        txt = node.get("fact") or node.get("q") or ""
        if any(w.lower() in txt.lower() for w in want):
            print("=" * 70)
            print("WHERE  ", f"{label}{path}")
            print("SOURCE ", node.get("source_url"))
            print("FACT   ", txt[:300])
            print("COND   ", (node.get("condition") or "")[:400])
