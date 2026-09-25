# STEP:4 compare old vs new project page by page: status + body md5 + title
import hashlib, re, subprocess, sys, time

OLD = "https://pet-insurance-decisions.pages.dev"
NEW = "https://furwell.pages.dev"

PAGES = ["/", "/lemonade-pet-insurance", "/spot-pet-insurance", "/fetch-pet-insurance",
         "/best-pet-insurance", "/pet-insurance-cost", "/lemonade-vs-spot",
         "/about", "/privacy", "/contact",
         "/sitemap.xml", "/robots.txt", "/assets/style.css", "/assets/favicon.svg"]


def fetch(base, path, follow=False):
    # follow=False: 取首跳状态码，防止 301 到旧站后正文相同、把跳转伪装成"对上了"
    cmd = ["curl", "-s", "-L" if follow else "", "-o", "-", "-w", "\n__CODE__%{http_code} %{redirect_url}",
           "--max-time", "30", base + path]
    out = subprocess.run([c for c in cmd if c], capture_output=True).stdout
    if b"__CODE__" in out:
        body, meta = out.rsplit(b"__CODE__", 1)
        return body, meta.decode().strip()
    return out, "ERR"


rows = []
mismatch = []
for p in PAGES:
    ob, ometa = fetch(OLD, p)
    nb, nmeta = fetch(NEW, p)
    oc = ometa.split()[0] if ometa != "ERR" else "ERR"
    nc = nmeta.split()[0] if nmeta != "ERR" else "ERR"
    oh = hashlib.md5(ob).hexdigest()[:12]
    nh = hashlib.md5(nb).hexdigest()[:12]
    # title of each side (html pages only)
    def title(b):
        m = re.search(rb"<title>(.*?)</title>", b, re.S)
        return m.group(1).decode("utf-8", "replace") if m else "-"
    same = "SAME" if ob == nb else "DIFF"
    if oc != nc or ob != nb:
        mismatch.append((p, oc, nc, oh, nh))
    rows.append((p, oc, nc, oh, nh, same, title(nb)[:60]))

print(f"{'path':<28} {'old':>4} {'new':>4} {'old_md5':>13} {'new_md5':>13} {'body':>5}  title")
for r in rows:
    print(f"{r[0]:<28} {r[1]:>4} {r[2]:>4} {r[3]:>13} {r[4]:>13} {r[5]:>5}  {r[6]}")

# 404 behaviour on new host
for path in ["/no-such-page", "/404.html"]:
    nb, nmeta = fetch(NEW, path)
    print(f"404-check {path}: new_status={nmeta} title={title(nb)[:50]}")

# html extension redirect on new host (should stay on furwell domain)
code, body = subprocess.run(
    ["curl", "-s", "-o", "-", "-w", "\n%{http_code} %{redirect_url}", "--max-time", "30",
     NEW + "/about.html"], capture_output=True).stdout.decode().rsplit("\n", 1)[-1]
print("about.html redirect:", code)

print("RESULT:", "ALL SAME" if not mismatch else f"{len(mismatch)} MISMATCH -> {mismatch}")
