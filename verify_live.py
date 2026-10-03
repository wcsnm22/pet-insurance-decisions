import urllib.request
import urllib.error

urls = [
    "https://furadvisor.com/lemonade-cat-insurance",
    "https://furadvisor.com/lemonade-pet-insurance",
    "https://furadvisor.com/sitemap.xml",
    "https://furadvisor.com/",
]

for u in urls:
    req = urllib.request.Request(u, method="GET", headers={"User-Agent": "Mozilla/5.0 (verify)"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            body = r.read().decode("utf-8", "replace")
            print(f"{r.status} {u} len={len(body)}")
            if u.endswith("lemonade-cat-insurance"):
                print("   h1:", 'Lemonade cat insurance' in body)
                print("   source lemonade.com:", "lemonade.com/pet/cats" in body)
            if u.endswith("lemonade-pet-insurance"):
                print("   internal link to cat page:", 'href="/lemonade-cat-insurance"' in body)
            if u.endswith("sitemap.xml"):
                print("   has cat loc:", "lemonade-cat-insurance" in body, "| loc count:", body.count("<loc>"))
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code} {u}")
    except Exception as e:
        print(f"ERR {u}: {e}")
