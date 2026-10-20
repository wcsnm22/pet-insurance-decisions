import json
import re
import requests

H = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36"
}

URLS = [
    "https://spotpet.com/",
    "https://www.fetchpet.com/pet-insurance-cost",
    "https://www.lemonade.com/pet/insurance-guide/waiting-periods/",
    "https://www.fetchpet.com/claims",
]

for u in URLS:
    h = requests.get(u, headers=H, timeout=30).text
    print("=" * 70)
    print(u, "raw", len(h))
    m = re.search(r'<script[^>]*id="__NEXT_DATA__"[^>]*>(.*?)</script>', h, re.S)
    if not m:
        print("  no __NEXT_DATA__")
        continue
    blob = m.group(1)
    print("  __NEXT_DATA__ bytes:", len(blob))
    for kw in ["10,000", "180", "8 weeks", "cheapest", "$22", "$300", "14 day"]:
        print(f"    {kw!r:12} inNEXT={kw in blob!s:5}")
    # 看看内部有多少可见文本
    try:
        d = json.loads(blob)
        text = json.dumps(d, ensure_ascii=False)
        print("  serialized len:", len(text))
        print("  sample:", text[:300])
    except Exception as e:
        print("  parse err", e)
