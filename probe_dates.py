import json
import re
import requests
from datetime import date

H = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

URLS = [
    "https://www.lemonade.com/pet/insurance-guide/waiting-periods/",
    "https://www.lemonade.com/pet/insurance-guide/pet-insurance-cost/",
    "https://www.lemonade.com/pet/insurance-guide/pet-claim-denials/",
    "https://spotpet.com/",
    "https://spotpet.com/faqs",
    "https://www.fetchpet.com/pet-insurance-cost",
    "https://www.fetchpet.com/claims",
    "https://www.petinsurance.com/exotics/",
    "https://www.embracepetinsurance.com/coverage/waiting-period",
    "https://www.geico.com/pet-insurance/",
]

PATTERNS = [
    r"Last\s+Updated\s*:?\s*([A-Z][a-z]+\.?\s+\d{1,2},?\s+\d{4})",
    r"Updated\s+on\s*:?\s*([A-Z][a-z]+\.?\s+\d{1,2},?\s+\d{4})",
    r"Last\s+updated\s*:?\s*([A-Z][a-z]+\.?\s+\d{1,2},?\s+\d{4})",
    r'"dateModified"\s*:\s*"(\d{4}-\d{2}-\d{2})',
    r'"modified"\s*:\s*"(\d{4}-\d{2}-\d{2})',
]

for u in URLS:
    try:
        r = requests.get(u, headers=H, timeout=30)
        h = r.text
    except Exception as e:
        print("ERR", u, e)
        continue
    found = []
    for p in PATTERNS:
        for m in re.finditer(p, h):
            found.append(m.group(1))
    # 去重保序
    seen, uniq = set(), []
    for f in found:
        if f not in seen:
            seen.add(f)
            uniq.append(f)
    print("=" * 70)
    print(f"{r.status_code}  {u}")
    print("   dates:", uniq[:8])
