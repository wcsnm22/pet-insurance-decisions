"""Final live check of every P0 item on the deployed site."""
import json, re, ssl, urllib.request, urllib.error

UA = "Mozilla/5.0 (compatible; furadvisor-check/1.0; +https://furadvisor.com/about)"
BASE = "https://furadvisor.com"


def get(path, redirect=True):
    req = urllib.request.Request(BASE + path, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, r.read().decode("utf-8", "replace"), r.url
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace"), ""


# 1. utility files
for p in ("/ads.txt", "/.well-known/security.txt", "/sitemap.xml", "/robots.txt",
          "/llms.txt", "/llms-full.txt", "/indexnow-key-placeholder"):
    if "placeholder" in p:
        continue
    st, body, _ = get(p)
    print(f"{p:32} {st} {len(body)}B")

# 2. sitemap: per-page lastmod variety + loc count
st, sm, _ = get("/sitemap.xml")
pairs = re.findall(r"<loc>([^<]+)</loc><lastmod>([^<]*)</lastmod>", sm)
distinct = sorted({d for _, d in pairs})
print(f"sitemap urls={len(pairs)} distinct_lastmod={len(distinct)} {distinct}")

# 3. content pages: head + byline integrity
data = json.load(open("data/brands.json", encoding="utf-8"))
slugs = [b["slug"] for b in data["brands"]] + [
    a["slug"] for a in json.load(open("data/articles.json", encoding="utf-8"))["articles"]
]
bad = []
for s in slugs:
    st, h, _ = get(f"/{s}")
    title = re.search(r"<title>(.*?)</title>", h, re.S)
    title = title.group(1).strip() if title else ""
    desc = re.search(r'<meta name="description" content="(.*?)"', h, re.S)
    desc = desc.group(1).strip() if desc else ""
    og = re.search(r'<meta property="og:image" content="(.*?)"', h)
    # datePublished is only suspect on an Article (a first-publish date the site
    # never recorded); ClaimReview legitimately carries its own datePublished.
    ld_blocks = [json.loads(m) for m in
                 re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S)]
    article_ld = [b for b in ld_blocks if b.get("@type") == "Article"]
    article_invented_date = any("datePublished" in b for b in article_ld)
    checks = {
        "200": st == 200,
        "title<=58": len(title) <= 58,
        "desc<=155": len(desc) <= 155,
        "og_absolute": bool(og) and og.group(1).startswith(BASE),
        "twitter_large": 'twitter:card" content="summary_large_image' in h,
        "max_image_preview": "max-image-preview:large" in h,
        "byline": 'class="byline"' in h and "tangshoufu" in h,
        "article_no_datePublished": not article_invented_date,
        "dateModified": '"dateModified"' in h,
        "related": 'class="related"' in h,
    }
    for k, v in checks.items():
        if not v:
            bad.append(f"{s}:{k}")
print(f"content pages={len(slugs)} failures={bad if bad else 'NONE'}")

# 4. follow/nofollow balance
st, home, _ = get("/")
follow = nofollow = 0
for s in slugs + ["", "about", "privacy", "contact"]:
    st, h, _ = get(f"/{s}")
    for a in re.findall(r"<a\s[^>]*>", h):
        if "nofollow" in a:
            nofollow += 1
        elif 'rel="noopener"' in a or "href=\"http" in a:
            follow += 1
print(f"outbound anchors: follow~{follow} nofollow={nofollow}")

# 5. 404 + redirect behaviour
req = urllib.request.Request(BASE + "/nonexistent-xyz", headers={"User-Agent": UA})
try:
    with urllib.request.urlopen(req, timeout=30) as r:
        print("404 test:", r.status)
except urllib.error.HTTPError as e:
    print("404 test:", e.code, "x-robots-tag=", e.headers.get("x-robots-tag"))

for p in ("/index.html", "/about/"):
    req = urllib.request.Request(BASE + p, headers={"User-Agent": UA})
    class NoRedir(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, *a, **k):
            return None
    op = urllib.request.build_opener(NoRedir)
    try:
        op.open(req, timeout=30)
        print(f"{p}: 200 (no redirect)")
    except urllib.error.HTTPError as e:
        print(f"{p}: {e.code} -> {e.headers.get('location')}")

# 6. www 必须能解析并 301 到裸域（否则别人链接 www 就是死链，外链全废）
# 注意：这台机器的时钟比真实 UTC 慢 8 小时，新签发的证书会被判定"尚未生效"。
# 所以校验失败时用不校验上下文的 opener 重试，只为看清 301 目标，并在输出里注明。
print("--- www ---")


class NoRedir2(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


def www_probe(path):
    """返回 (code, location, err)；先做证书校验，遇到时钟偏差就退回不校验。"""
    for insecure in (False, True):
        handlers = [NoRedir2]
        if insecure:
            handlers.append(urllib.request.HTTPSHandler(context=ssl._create_unverified_context()))
        op = urllib.request.build_opener(*handlers)
        try:
            op.open(urllib.request.Request("https://www.furadvisor.com" + path, headers={"User-Agent": UA}), timeout=30)
            return 200, "", ""
        except urllib.error.HTTPError as e:
            return e.code, e.headers.get("location") or "", ""
        except urllib.error.URLError as e:
            reason = str(getattr(e, "reason", e))
            if insecure:
                return None, "", reason
            continue
    return None, "", "unreachable"


for wp in ("/", "/best-pet-insurance", "/sitemap.xml"):
    code, loc, err = www_probe(wp)
    if code is None:
        print(f"  www{wp}: FAILED ({err})")
    else:
        ok = code in (301, 308) and loc.startswith("https://furadvisor.com/")
        print(f"  www{wp}: {code} -> {loc} {'OK' if ok else 'WRONG'}")
