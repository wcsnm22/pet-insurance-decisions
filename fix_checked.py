# Fill explicit "checked" date on any fact/FAQ missing it (site-level check date).
import json, pathlib
p = pathlib.Path(__file__).parent / "data" / "brands.json"
d = json.loads(p.read_text(encoding="utf-8"))
date = d["site"]["checked"]
fixed = 0
for b in d["brands"]:
    for key in ("facts", "faqs"):
        for item in b[key]:
            if not item.get("checked"):
                item["checked"] = date
                fixed += 1
for item in d.get("home_faqs", []):
    if not item.get("checked"):
        item["checked"] = date
        fixed += 1
p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("fixed:", fixed)
