import re
import json
import requests

H = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36"
}

URLS = [
    "https://spotpet.com/",
    "https://spotpet.com/sample-policy",
    "https://www.lemonade.com/pet/insurance-guide/pet-insurance-cost/",
]


def clean_text(html):
    html = re.sub(r"(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>", " ", html)
    text = re.sub(r"(?s)<[^>]+>", " ", html)
    text = (
        text.replace("&nbsp;", " ")
        .replace("&amp;", "&")
        .replace("&#x27;", "'")
        .replace("&#39;", "'")
        .replace("&quot;", '"')
    )
    return re.sub(r"\s+", " ", text)


for u in URLS:
    h = requests.get(u, headers=H, timeout=30).text
    print("=" * 70)
    print(u, "raw", len(h))
    print("  text:", len(clean_text(h)))
    print("  raw has 10,000:", "10,000" in h, "| html-escaped 10,000:", "10,000" in h)
    jsonld = re.findall(r'<script[^>]*application/(?:ld\+)?json[^>]*>(.*?)</script>', h, re.S)
    print("  json-ld blocks:", len(jsonld), "chars:", sum(len(x) for x in jsonld))
    blob = " ".join(jsonld)
    for kw in ["10,000", "180", "8 weeks", "cheapest", "$22"]:
        print(f"    {kw!r:12} jsonld={kw in blob!s:5} text={kw in clean_text(h)!s:5}")
    # 找 next 的 __NEXT_DATA__ 或 nuxt 数据
    for marker in ["__NEXT_DATA__", "__NUXT__", "window.__", "application/x-www-form"]:
        if marker in h:
            print("  marker:", marker, "count", h.count(marker))
