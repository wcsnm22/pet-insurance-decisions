# ILANG
# TYPE:module ROLE:builder PROJECT:pet-insurance-decisions
# ::RULE{每条事实必须带 source_url 和 checked 才能渲染 否则构建直接报错}
# ::RULE{每页必须有 canonical 和 JSON-LD sitemap.xml 和 robots.txt 由本文件生成 不手写}
# ::BOUNDARY{never:编价格 编条款 编折扣 中文出现在输出页|scope:file}
"""读 data/brands.json -> 渲染静态站到 site/（含 JSON-LD、canonical、sitemap）

零依赖：只用 Python 标准库。
用法：python build.py
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "brands.json"
TEMPLATE_DIR = ROOT / "templates"
SITE_DIR = ROOT / "site"

# Cloudflare Pages 高级模式脚本：全量接管请求。
# ::RULE{非规范主机名 301 到主域 不留两个活地址}
# ::RULE{不在白名单的路径返回真实 404 不让 Pages 回退首页}
WORKER_TEMPLATE = """// ILANG
// TYPE:worker ROLE:canonical-host-and-real-404
const CANONICAL_HOST = "__CANONICAL_HOST__";
const VALID_PATHS = new Set(__VALID_PATHS__);

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (url.hostname !== CANONICAL_HOST) {
      return Response.redirect(new URL(url.pathname + url.search, `https://${CANONICAL_HOST}`).toString(), 301);
    }

    const path = url.pathname.replace(/\\/+$/, "") || "/";

    if (path.endsWith(".html")) {
      const bare = path === "/index.html" ? "/" : path.slice(0, -5);
      if (VALID_PATHS.has(bare)) {
        return Response.redirect(new URL(bare + url.search, `https://${CANONICAL_HOST}`).toString(), 308);
      }
    }

    if (VALID_PATHS.has(path)) {
      return env.ASSETS.fetch(request);
    }

    const notFound = await env.ASSETS.fetch(new URL("/404.html", url));
    return new Response(notFound.body, {
      status: 404,
      headers: {
        "content-type": "text/html; charset=utf-8",
        "cache-control": "no-store",
        "x-robots-tag": "noindex",
      },
    });
  },
};
"""


# ------------------------------------------------------------------ 小工具
def render(template: str, values: dict[str, str]) -> str:
    def replace(match: re.Match) -> str:
        return values.get(match.group(1).strip(), "")

    return re.sub(r"\{\{\s*([a-zA-Z0-9_]+)\s*\}\}", replace, template)


def template(name: str) -> str:
    html = (TEMPLATE_DIR / name).read_text(encoding="utf-8")
    return re.sub(r"\s*<style>.*?</style>", "", html, flags=re.S)


def jsonld(payload: dict | list) -> str:
    return json.dumps(payload, ensure_ascii=False, separators=(",", ":"))


def iso_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def page_url(site: dict, path: str) -> str:
    base = site["base_url"].rstrip("/")
    return base if path == "/" else f"{base}{path}"


def fact_rows(facts: list[dict]) -> str:
    cols = ["Fact", "Condition to get it", "Official source page", "Checked"]
    rows = []
    for f in facts:
        cells = [
            escape(f["fact"]),
            escape(f["condition"]),
            f'<a href="{escape(f["source_url"])}" rel="nofollow noopener" target="_blank">{escape(f["source_url"])}</a>',
            escape(f["checked"]),
        ]
        rows.append(
            "<tr>"
            + "".join(
                f'<td data-th="{escape(c, quote=True)}">{v}</td>'
                for c, v in zip(cols, cells)
            )
            + "</tr>"
        )
    return "".join(rows)


def fact_jsonld_items(facts: list[dict]) -> list[dict]:
    return [
        {
            "@type": "ClaimReview",
            "claimReviewed": f["fact"],
            "author": {"@type": "Organization", "name": "brand's own official site"},
            "url": f["source_url"],
            "datePublished": f["checked"],
        }
        for f in facts
    ]


def head_block(title: str, description: str, canonical: str, jsonld_blocks: list[str]) -> str:
    parts = [
        f'<meta name="description" content="{escape(description, quote=True)}">',
        f'<link rel="canonical" href="{escape(canonical, quote=True)}">',
        '<meta property="og:type" content="website">',
        f'<meta property="og:title" content="{escape(title, quote=True)}">',
        f'<meta property="og:description" content="{escape(description, quote=True)}">',
        f'<meta property="og:url" content="{escape(canonical, quote=True)}">',
        '<meta property="og:site_name" content="Pet Insurance Decisions">',
        '<meta name="twitter:card" content="summary">',
        '<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">',
        '<link rel="stylesheet" href="/assets/style.css?v=1">',
    ]
    for block in jsonld_blocks:
        parts.append(f'<script type="application/ld+json">{block}</script>')
    return "\n  ".join(parts)


FOOTER_LINKS = (
    '<a href="/">Home</a> · <a href="/about">About</a> · <a href="/privacy">Privacy</a> · '
    '<a href="/contact">Contact</a> · <a href="/sitemap.xml">Sitemap</a>'
)


# ------------------------------------------------------------------ 构建
def build() -> None:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    site = data["site"]
    brands = data["brands"]

    # FAQ 条目统一挂上站点复核日期（FAQ 与 facts 同批读取，同日复核）
    for b in brands:
        for item in b["faqs"]:
            item.setdefault("checked", site["checked"])
    for item in data["home_faqs"]:
        item.setdefault("checked", site["checked"])

    # 事实完整性：缺 source_url 或 checked 的条目直接让构建失败，不许渲染出去
    for group_name, group in [("brand", [f for b in brands for f in b["facts"]]),
                              ("brand faq", [f for b in brands for f in b["faqs"]]),
                              ("home", data["home_facts"] + data["home_faqs"])]:
        for item in group:
            if not item.get("source_url") or not item.get("checked"):
                raise SystemExit(f"FACT MISSING SOURCE/DATE in {group_name}: {item}")

    SITE_DIR.mkdir(exist_ok=True)
    (SITE_DIR / "assets").mkdir(exist_ok=True)
    generated_at = iso_now()
    brand_tpl = template("brand.html")
    nav = ' · '.join(f'<a href="/{b["slug"]}">{escape(b["name"])}</a>' for b in brands)

    # ---- 首页
    home_jsonld = [
        jsonld({
            "@context": "https://schema.org",
            "@type": "WebSite",
            "name": site["name"],
            "url": page_url(site, "/"),
            "description": site["tagline"],
            "inLanguage": site["locale"],
        }),
        jsonld({
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": f["q"],
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": f["a"],
                        "url": f["source_url"],
                    },
                }
                for f in data["home_faqs"]
            ],
        }),
    ]
    home_head = head_block(
        "Pet Insurance: Coverage, Cost and Waiting Periods - Facts from Lemonade, Spot and Fetch",
        site["tagline"],
        page_url(site, "/"),
        home_jsonld,
    )
    cards = "".join(
        f'<div class="card"><h3><a href="/{b["slug"]}">{escape(b["name"])} pet insurance</a></h3>'
        f'<p class="price big">{escape(b["price_line"])}</p>'
        f'<p class="muted">{escape(b["price_condition"])}</p>'
        f'<p class="muted">Source: <a href="{escape(b["price_source"])}" rel="nofollow noopener" target="_blank">'
        f'{escape(b["price_source"])}</a> · checked {escape(site["checked"])}</p>'
        f'<p>{escape(b["short_answer"])}</p></div>'
        for b in brands
    )
    faq_html = "".join(
        f'<details open><summary>{escape(f["q"])}</summary><p>{escape(f["a"])}</p>'
        f'<p class="muted">Source: <a href="{escape(f["source_url"])}" rel="nofollow noopener" target="_blank">'
        f'{escape(f["source_url"])}</a> · checked {escape(f["checked"])}</p></details>'
        for f in data["home_faqs"]
    )
    home = render(template("index.html"), {
        "lang": "en",
        "title": "Pet Insurance: Coverage, Cost and Waiting Periods - Facts from Lemonade, Spot and Fetch",
        "head": home_head,
        "brand": site["name"],
        "nav": f'<a href="/">Home</a> · {nav}',
        "tagline": site["tagline"],
        "cards": cards,
        "fact_table_rows": fact_rows(data["home_facts"]),
        "faqs": faq_html,
        "footer": FOOTER_LINKS,
        "generated_at": generated_at,
    })
    (SITE_DIR / "index.html").write_text(home, encoding="utf-8")

    # ---- 品牌页：一个品牌一页，整族说法都进 title/H1/FAQ/JSON-LD
    for b in brands:
        title = (
            f'{b["name"]} Pet Insurance: Review, Cost, Quote and Promo Code Facts '
            f'(Sources Inside)'
        )
        description = (
            f'{b["name"]} pet insurance in plain facts: cost, coverage, waiting periods, '
            f'quote flow and any official discounts - every line linked to {b["official_site"].split("//")[1]} '
            f"and checked {site['checked']}."
        )
        canonical = page_url(site, f'/{b["slug"]}')
        jsonld_blocks = [
            jsonld({
                "@context": "https://schema.org",
                "@type": "FAQPage",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": f["q"],
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": f["a"],
                            "url": f["source_url"],
                        },
                    }
                    for f in b["faqs"]
                ],
            }),
            jsonld({
                "@context": "https://schema.org",
                "@type": "Article",
                "headline": title,
                "description": description,
                "url": canonical,
                "dateModified": site["checked"],
                "publisher": {"@type": "Organization", "name": site["name"]},
                "about": {"@type": "Thing", "name": f'{b["name"]} pet insurance'},
            }),
            jsonld({
                "@context": "https://schema.org",
                "@type": "ClaimReview",
                "itemReviewed": {"@type": "Thing", "name": f'{b["name"]} pet insurance facts'},
                "claimReviewed": f'Facts about {b["name"]} pet insurance as published on its official site',
                "url": b["official_site"],
                "datePublished": site["checked"],
                "author": {"@type": "Organization", "name": site["name"]},
            }),
        ]
        head = head_block(title, description, canonical, jsonld_blocks)
        faq_html = "".join(
            f'<details open><summary>{escape(f["q"])}</summary><p>{escape(f["a"])}</p>'
            f'<p class="muted">Source: <a href="{escape(f["source_url"])}" rel="nofollow noopener" target="_blank">'
            f'{escape(f["source_url"])}</a> · checked {escape(site["checked"])}</p></details>'
            for f in b["faqs"]
        )
        html = render(brand_tpl, {
            "lang": "en",
            "title": title,
            "head": head,
            "brand": site["name"],
            "nav": f'<a href="/">Home</a> · {nav}',
            "name": b["name"],
            "h1": f'{b["name"]} pet insurance: review, cost, quote and promo code facts',
            "short_answer": b["short_answer"],
            "price_line": b["price_line"],
            "price_condition": b["price_condition"],
            "price_source": b["price_source"],
            "official_site": b["official_site"],
            "quote_url": b["quote_url"],
            "fact_table_rows": fact_rows(b["facts"]),
            "faqs": faq_html,
            "checked": site["checked"],
            "footer": FOOTER_LINKS,
        })
        (SITE_DIR / f'{b["slug"]}.html').write_text(html, encoding="utf-8")

    # ---- 通用页
    for page in ("about", "privacy", "contact", "404"):
        tpl = template(f"{page}.html")
        canonical = page_url(site, "/" if page == "404" else f"/{page}")
        blocks = [jsonld({
            "@context": "https://schema.org",
            "@type": "WebPage",
            "name": page.capitalize(),
            "url": canonical,
            "isPartOf": {"@type": "WebSite", "name": site["name"], "url": page_url(site, "/")},
        })]
        head = head_block(
            f'{page.capitalize()} - {site["name"]}',
            f"{page.capitalize()} page of {site['name']}.",
            canonical,
            blocks,
        )
        html = render(tpl, {
            "lang": "en",
            "title": f'{page.capitalize()} - {site["name"]}',
            "head": head,
            "brand": site["name"],
            "nav": f'<a href="/">Home</a> · {nav}',
            "repo": site["repo"],
            "checked": site["checked"],
            "footer": FOOTER_LINKS,
        })
        (SITE_DIR / f"{page}.html").write_text(html, encoding="utf-8")

    # ---- 资源
    import shutil
    for asset in (TEMPLATE_DIR / "assets").iterdir():
        shutil.copy2(asset, SITE_DIR / "assets" / asset.name)

    # ---- sitemap.xml / robots.txt
    urls = [("/", "1.0")]
    urls += [(f'/{b["slug"]}', "0.9") for b in brands]
    urls += [("/about", "0.5"), ("/privacy", "0.5"), ("/contact", "0.5")]
    sitemap_items = "".join(
        f"<url><loc>{escape(page_url(site, path))}</loc>"
        f"<lastmod>{site['checked']}</lastmod>"
        f"<priority>{pri}</priority></url>"
        for path, pri in urls
    )
    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{sitemap_items}\n</urlset>\n"
    )
    (SITE_DIR / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    robots = f"User-agent: *\nAllow: /\n\nSitemap: {page_url(site, '/sitemap.xml')}\n"
    (SITE_DIR / "robots.txt").write_text(robots, encoding="utf-8")

    # ---- _worker.js（规范主机 + 真 404）
    from urllib.parse import urlparse
    host = urlparse(site["base_url"]).netloc
    valid_paths = sorted({"/"} | {path for path, _ in urls})
    worker = (
        WORKER_TEMPLATE
        .replace("__CANONICAL_HOST__", host)
        .replace("__VALID_PATHS__", json.dumps(valid_paths))
    )
    (SITE_DIR / "_worker.js").write_text(worker, encoding="utf-8")

    print(f"built {len(urls) + 1} pages -> {SITE_DIR} at {generated_at}")


if __name__ == "__main__":
    build()
