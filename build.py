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
import os
import re
import uuid
from datetime import datetime, timezone
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "brands.json"
ARTICLES_PATH = ROOT / "data" / "articles.json"
TEMPLATE_DIR = ROOT / "templates"
SITE_DIR = ROOT / "site"

# 只允许品牌官网域名做来源；编辑型文章（articles.json）同样受此约束
OFFICIAL_HOSTS = {
    "lemonade.com", "www.lemonade.com",
    "spotpet.com", "www.spotpet.com",
    "spotpetins.com", "www.spotpetins.com",
    "fetchpet.com", "www.fetchpet.com",
    # 官方政策文档托管域：Nationwide 官网 + Spot 样例保单 PDF 的官方 CDN
    "petinsurance.com", "www.petinsurance.com",
    "assets.ctfassets.net",
    # 对标三家（@TOP3 2026-09-28 冻结）与它们指向的官方条款托管域（Embrace terms）
    "geico.com", "www.geico.com",
    "allstate.com", "www.allstate.com",
    "aspcapetinsurance.com", "www.aspcapetinsurance.com",
    "embracepetinsurance.com", "www.embracepetinsurance.com",
}

# 文章内 compare/facts/faqs/cards 块的默认小标题（可用块内 "h2" 覆盖，null = 不出标题）
BLOCK_HEADINGS = {
    "compare": "Side-by-side comparison - official published figures only",
    "facts": "Every figure with its official source",
    "faqs": "FAQ",
    "cards": "The plans compared, page by page",
    "related": "Related guides",
}

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


def asset_url(canonical: str, path: str) -> str:
    """Absolute URL for a static asset referenced from <head>.

    og:image / twitter:image must be absolute, so take the origin from the page's
    own canonical URL - that keeps the social crawler on the canonical host and
    never on a *.pages.dev preview domain.
    """
    from urllib.parse import urlparse
    origin = "{0.scheme}://{0.netloc}".format(urlparse(canonical))
    return f"{origin}{path}"


def llms_index(site: dict, brands: list[dict], articles: list[dict]) -> str:
    """llms.txt: a short, model-readable index of what this site answers.

    Only restates the site's own recorded facts and page purposes - no new claims.
    """
    lines = [
        f"# {site['name']}",
        "",
        f"> {site['tagline']}",
        "",
        "This site is a reference of pet insurance facts taken only from each brand's own "
        "official website and official policy pages. Every figure is published on this site "
        "with the official page it was read from and the date it was checked. Where a brand "
        "does not publish a figure, the page says so instead of estimating.",
        "",
        "## Guides",
        "",
    ]
    for a in articles:
        lines.append(f"- [{a['title']}]({page_url(site, '/' + a['slug'])}): {a['description']}")
    lines += ["", "## Brand pages", ""]
    for b in brands:
        lines.append(
            f"- [{b['name']} pet insurance facts]({page_url(site, '/' + b['slug'])}): "
            f"{b['price_line']}. {b['short_answer']}"
        )
    lines += [
        "",
        "## Optional",
        "",
        f"- [About this site]({page_url(site, '/about')}): who runs it, and how facts are sourced and dated.",
        f"- [Contact]({page_url(site, '/contact')}): report a fact that no longer matches a brand's official site.",
        f"- [Full fact list]({page_url(site, '/llms-full.txt')}): every recorded figure with its source page and check date.",
        "",
    ]
    return "\n".join(lines)


def llms_full(site: dict, brands: list[dict], articles: list[dict]) -> str:
    """llms-full.txt: every recorded fact with its official source URL and check date."""
    out = [
        f"# {site['name']} - full fact list",
        "",
        f"> {site['tagline']}",
        "",
        f"Every entry below was read from the official page named in its source URL and "
        f"checked on the date shown. Figures are quoted as published; conditions are stated "
        f"because the number usually depends on them.",
        "",
    ]
    for b in brands:
        out += [f"## {b['name']} pet insurance", "", f"URL: {page_url(site, '/' + b['slug'])}", ""]
        out += [f"- **{b['price_line']}** - {b['price_condition']}",
                f"  Source: {b['price_source']} (checked {site['checked']})", ""]
        out.append("### Facts")
        out.append("")
        for f in b["facts"]:
            out.append(f"- {f['fact']} (condition: {f['condition']})")
            out.append(f"  Source: {f['source_url']} (checked {f['checked']})")
        out += ["", "### FAQ", ""]
        for f in b["faqs"]:
            out.append(f"- **{f['q']}** {f['a']}")
            out.append(f"  Source: {f['source_url']} (checked {f['checked']})")
        out.append("")
    for a in articles:
        out += [f"## {a['title']}", "", f"URL: {page_url(site, '/' + a['slug'])}", "",
                f"Keyword: {a.get('keyword', '')}", "", "### Facts", ""]
        for f in a["facts"]:
            out.append(f"- {f['fact']} (condition: {f['condition']})")
            out.append(f"  Source: {f['source_url']} (checked {f['checked']})")
        out += ["", "### FAQ", ""]
        for f in a["faqs"]:
            out.append(f"- **{f['q']}** {f['a']}")
            out.append(f"  Source: {f['source_url']} (checked {f['checked']})")
        out.append("")
    out += [
        "## About this data",
        "",
        f"- Every fact carries the official page it was read from and the date it was checked.",
        f"- No figure is estimated, rounded or filled in from memory.",
        f"- Where a brand publishes no figure, the page states that rather than guessing.",
        f"- This site is not affiliated with, endorsed by, or compensated by any insurer it covers.",
        f"- Site: {page_url(site, '/')} · Repository: {site['repo']}",
        "",
    ]
    return "\n".join(out)


def fact_rows(facts: list[dict]) -> str:
    cols = ["Fact", "Condition to get it", "Official source page", "Checked"]
    rows = []
    for f in facts:
        cells = [
            escape(f["fact"]),
            escape(f["condition"]),
            f'<a href="{escape(f["source_url"])}" rel="noopener" target="_blank">{escape(f["source_url"])}</a>',
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


def official_host(url: str) -> str:
    parts = url.split("/")
    return parts[2] if url.startswith("http") and len(parts) > 2 else ""


def faq_details(items: list[dict]) -> str:
    return "".join(
        f'<details open><summary>{escape(f["q"])}</summary><p>{escape(f["a"])}</p>'
        f'<p class="muted">Source: <a href="{escape(f["source_url"])}" rel="noopener" target="_blank">'
        f'{escape(f["source_url"])}</a> · checked {escape(f["checked"])}</p></details>'
        for f in items
    )


def compare_table(article: dict) -> str:
    """并排对比表：每格自带官方来源链接；没发布的格子写 not published on the official site。"""
    heads = "".join(
        f'<th><a href="{escape(c["url"])}">{escape(c["name"])}</a></th>'
        for c in article["columns"]
    )
    rows = []
    for r in article["rows"]:
        sources = r.get("sources", [])
        cells = [f'<td data-th="What we compare"><strong>{escape(r["label"])}</strong></td>']
        for i, text in enumerate(r["cells"]):
            src = sources[i] if i < len(sources) else ""
            inner = escape(text)
            if src:
                inner += (
                    f'<br><a class="muted" href="{escape(src)}" rel="noopener" '
                    f'target="_blank">source: {escape(official_host(src))}</a>'
                )
            cells.append(f'<td data-th="{escape(article["columns"][i]["name"], quote=True)}">{inner}</td>')
        rows.append("<tr>" + "".join(cells) + "</tr>")
    return (
        "<table><thead><tr><th>What we compare</th>"
        + heads
        + "</tr></thead><tbody>"
        + "".join(rows)
        + "</tbody></table>"
    )


def article_body(article: dict, brands: list[dict], brand_cards: str) -> str:
    """按 blocks 顺序拼正文；未知块类型直接让构建失败。"""
    parts: list[str] = []
    for blk in article["blocks"]:
        kind = blk.get("type")
        if kind == "section":
            parts.append(f'<h2>{escape(blk["h2"])}</h2>' + blk["html"])
            continue
        heading = blk["h2"] if "h2" in blk else BLOCK_HEADINGS.get(kind)
        if kind == "compare":
            parts.append(((f"<h2>{escape(heading)}</h2>") if heading else "") + compare_table(article))
        elif kind == "facts":
            table = (
                "<table><thead><tr><th>Fact</th><th>Condition to get it</th>"
                "<th>Official source page</th><th>Checked</th></tr></thead>"
                f"<tbody>{fact_rows(article['facts'])}</tbody></table>"
            )
            parts.append(((f"<h2>{escape(heading)}</h2>") if heading else "") + table)
        elif kind == "faqs":
            parts.append(((f"<h2>{escape(heading)}</h2>") if heading else "") + faq_details(article["faqs"]))
        elif kind == "cards":
            cards = "".join(brand_cards) if isinstance(brand_cards, list) else brand_cards
            parts.append(((f"<h2>{escape(heading)}</h2>") if heading else "") + f'<div class="grid">{cards}</div>')
        elif kind == "related":
            links = blk.get("links", [])
            if not links:
                raise SystemExit(f"RELATED BLOCK WITH NO LINKS in {article['slug']}")
            items = []
            for link in links:
                href = link["url"]
                if not href.startswith("http"):
                    href = link["url"]
                items.append(
                    f'<li><a href="{escape(href, quote=True)}">{escape(link["text"])}</a>'
                    f' <span class="muted">{escape(link["why"])}</span></li>'
                )
            parts.append(
                ((f"<h2>{escape(heading)}</h2>") if heading else "")
                + f'<ul class="related">{"".join(items)}</ul>'
            )
        else:
            raise SystemExit(f"UNKNOWN ARTICLE BLOCK in {article['slug']}: {kind}")
    return "".join(parts)


def _css_v() -> str:
    """Cache-bust the stylesheet: version = short hash of the real CSS file,
    so a style change always ships a new ?v= and browsers never keep stale CSS."""
    import hashlib
    import pathlib
    p = pathlib.Path(__file__).parent / "templates" / "assets" / "style.css"
    return hashlib.sha1(p.read_bytes()).hexdigest()[:8]


def latest_checked(items: list[dict]) -> str:
    """Most recent check date among a page's own facts/FAQs.

    Pages are rechecked in batches, so the honest "last updated" is the newest
    date actually recorded on that page - not the site-wide build date.
    """
    dates = [i["checked"] for i in items if i.get("checked")]
    return max(dates) if dates else ""


INDEXNOW_KEY_PATH = ROOT / "indexnow-key.txt"


def security_txt_expiry() -> str:
    """RFC 9116 requires an Expires field. Pin it to the end of next year.

    Computing it as "now + 365 days" would rewrite the file on every build and
    make an unchanged site look modified; a yearly fixed date stays valid for
    12-24 months and only changes once a year.
    """
    return f"{datetime.now(timezone.utc).year + 1}-12-31T00:00:00Z"


def indexnow_key() -> str:
    """The IndexNow key, generated once and then kept stable in the repo.

    Regenerating it on every build would orphan URLs already submitted under the
    old key, so it is read from a file and only created if that file is absent.
    """
    if INDEXNOW_KEY_PATH.exists():
        key = INDEXNOW_KEY_PATH.read_text(encoding="utf-8").strip()
    else:
        key = uuid.uuid4().hex
        INDEXNOW_KEY_PATH.write_text(key, encoding="utf-8")
    if not re.fullmatch(r"[0-9a-f]{8,128}", key):
        raise SystemExit(f"INDEXNOW KEY IS NOT A HEX STRING: {key!r}")
    return key


def byline_html(updated: str) -> str:
    """Visible byline: who maintains the page, when its facts were last checked.

    Rendered into the page, not just declared in JSON-LD - the E-E-A-T signals
    Google reads are on the page itself.
    """
    return (
        '<p class="byline">'
        f'By <a href="/about">tangshoufu</a><span class="sep">·</span>'
        'built and maintained from the brands\' own official pages<span class="sep">·</span>'
        f'<time datetime="{escape(updated)}">Facts last checked {escape(updated)}</time>'
        '</p>'
    )


def author_jsonld(site: dict) -> dict:
    """The Person behind the site, tied to the repo account stated on /about."""
    return {
        "@type": "Person",
        "name": "tangshoufu",
        "url": page_url(site, "/about"),
        "sameAs": ["https://github.com/wcsnm22"],
    }


def publisher_jsonld(site: dict) -> dict:
    """Article.publisher must be an Organization, so the site itself carries it."""
    return {
        "@type": "Organization",
        "name": site["name"],
        "url": page_url(site, "/"),
        "founder": author_jsonld(site),
    }


def head_block(title: str, description: str, canonical: str, jsonld_blocks: list[str],
               og_slug: str = "og-home", og_type: str = "article") -> str:
    """共享 <head>：社交卡片、robots 指令、canonical、JSON-LD。

    og:image 由 make_og.py 预生成到 templates/assets/og-<slug>.png；这里只负责引用，
    所以缺图时构建必须报错而不是发出一页没图的卡片。
    """
    og_path = TEMPLATE_DIR / "assets" / f"{og_slug}.png"
    if not og_path.exists():
        raise SystemExit(f"OG IMAGE MISSING (run python make_og.py): {og_path.name}")
    og_url = asset_url(canonical, f"/assets/{og_path.name}")
    parts = [
        # Admitad/Mitgo ad-space ownership verification (site owner action)
        '<meta name="mitgo-verification" content="525da73b-6632-4867-a8b7-3f78725eee42">',
        # Impact.com publisher site-ownership verification (site owner action)
        '<meta name="impact-site-verification" value="2385d48f-31d9-4d68-93cb-707ce4d312fe">',
        f'<meta name="description" content="{escape(description, quote=True)}">',
        f'<link rel="canonical" href="{escape(canonical, quote=True)}">',
        # 允许大图预览：不写这条时 Google 只会拿小缩略图
        '<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">',
        '<meta property="og:type" content="{}">'.format(og_type),
        f'<meta property="og:title" content="{escape(title, quote=True)}">',
        f'<meta property="og:description" content="{escape(description, quote=True)}">',
        f'<meta property="og:url" content="{escape(canonical, quote=True)}">',
        '<meta property="og:site_name" content="Pet Insurance Decisions">',
        f'<meta property="og:image" content="{escape(og_url, quote=True)}">',
        f'<meta property="og:image:alt" content="{escape(title, quote=True)}">',
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        f'<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{escape(title, quote=True)}">',
        f'<meta name="twitter:description" content="{escape(description, quote=True)}">',
        f'<meta name="twitter:image" content="{escape(og_url, quote=True)}">',
        '<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">',
        f'<link rel="stylesheet" href="/assets/style.css?v={_css_v()}">',
    ]
    for block in jsonld_blocks:
        parts.append(f'<script type="application/ld+json">{block}</script>')
    return "\n  ".join(parts)


def breadcrumb_jsonld(name: str, url: str, site: dict) -> str:
    """BreadcrumbList for content pages (Google breadcrumb rich-result shape)."""
    return jsonld({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": page_url(site, "/")},
            {"@type": "ListItem", "position": 2, "name": name, "item": url},
        ],
    })


FOOTER_LINKS = (
    '<a href="/">Home</a> · <a href="/about">About</a> · <a href="/privacy">Privacy</a> · '
    '<a href="/contact">Contact</a> · <a href="/sitemap.xml">Sitemap</a>'
)


# ------------------------------------------------------------------ 构建
def build() -> None:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    site = data["site"]
    brands = data["brands"]
    articles = (
        json.loads(ARTICLES_PATH.read_text(encoding="utf-8"))["articles"]
        if ARTICLES_PATH.exists()
        else []
    )

    # FAQ 条目统一挂上站点复核日期（FAQ 与 facts 同批读取，同日复核）
    for b in brands:
        for item in b["faqs"]:
            item.setdefault("checked", site["checked"])
    for item in data["home_faqs"]:
        item.setdefault("checked", site["checked"])
    for a in articles:
        for item in a["faqs"]:
            item.setdefault("checked", site["checked"])

    # 事实完整性：缺 source_url 或 checked 的条目直接让构建失败，不许渲染出去
    for group_name, group in [("brand", [f for b in brands for f in b["facts"]]),
                              ("brand faq", [f for b in brands for f in b["faqs"]]),
                              ("article", [f for a in articles for f in a["facts"] + a["faqs"]]),
                              ("home", data["home_facts"] + data["home_faqs"])]:
        for item in group:
            if not item.get("source_url") or not item.get("checked"):
                raise SystemExit(f"FACT MISSING SOURCE/DATE in {group_name}: {item}")

    # 文章：来源必须是品牌官网域名；对比表的行列数量必须和 columns 对齐
    for a in articles:
        ncols = len(a["columns"])
        for f in a["facts"] + a["faqs"]:
            if official_host(f["source_url"]) not in OFFICIAL_HOSTS:
                raise SystemExit(f"NON-OFFICIAL SOURCE in article {a['slug']}: {f['source_url']}")
        for r in a["rows"]:
            if len(r["cells"]) != ncols or len(r.get("sources", [])) != ncols:
                raise SystemExit(f"COMPARE SHAPE MISMATCH in article {a['slug']}: {r['label']}")
            for u in r.get("sources", []):
                if u and official_host(u) not in OFFICIAL_HOSTS:
                    raise SystemExit(f"NON-OFFICIAL COMPARE SOURCE in article {a['slug']}: {u}")

    SITE_DIR.mkdir(exist_ok=True)
    (SITE_DIR / "assets").mkdir(exist_ok=True)
    generated_at = iso_now()
    brand_tpl = template("brand.html")
    article_tpl = template("article.html")
    nav = ' · '.join(
        [f'<a href="/{b["slug"]}">{escape(b["name"])}</a>' for b in brands]
        + [f'<a href="/{a["slug"]}">{escape(a.get("nav_label") or a["title"])}</a>' for a in articles]
    )
    article_cards = "".join(
        f'<div class="card"><h3><a href="/{a["slug"]}">{escape(a["title"])}</a></h3>'
        f'<p>{escape(a["description"])}</p>'
        f'<p class="muted">Type: {escape(a.get("type", ""))} · keyword: {escape(a.get("keyword", ""))} · '
        f'facts checked {escape(site["checked"])}</p></div>'
        for a in articles
    )

    # ---- 首页
    home_updated = latest_checked(data["home_facts"] + data["home_faqs"])
    home_jsonld = [
        jsonld({
            "@context": "https://schema.org",
            "@type": "WebSite",
            "name": site["name"],
            "url": page_url(site, "/"),
            "description": site["tagline"],
            "inLanguage": site["locale"],
            "publisher": publisher_jsonld(site),
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
    home_title = site.get(
        "meta_title",
        "Pet Insurance: Coverage, Cost and Waiting Periods",
    )
    home_desc = site.get("meta_description", site["tagline"])
    home_head = head_block(
        home_title,
        home_desc,
        page_url(site, "/"),
        home_jsonld,
        og_slug="og-home",
        og_type="website",
    )
    cards = "".join(
        f'<div class="card"><h3><a href="/{b["slug"]}">{escape(b["name"])} pet insurance</a></h3>'
        f'<p class="price big">{escape(b["price_line"])}</p>'
        f'<p class="muted">{escape(b["price_condition"])}</p>'
        f'<p class="muted">Source: <a href="{escape(b["price_source"])}" rel="noopener" target="_blank">'
        f'{escape(b["price_source"])}</a> · checked {escape(site["checked"])}</p>'
        f'<p>{escape(b["short_answer"])}</p></div>'
        for b in brands
    )
    faq_html = "".join(
        f'<details open><summary>{escape(f["q"])}</summary><p>{escape(f["a"])}</p>'
        f'<p class="muted">Source: <a href="{escape(f["source_url"])}" rel="noopener" target="_blank">'
        f'{escape(f["source_url"])}</a> · checked {escape(f["checked"])}</p></details>'
        for f in data["home_faqs"]
    )
    home = render(template("index.html"), {
        "lang": "en",
        "title": home_title,
        "head": home_head,
        "brand": site["name"],
        "nav": f'<a href="/">Home</a> · {nav}',
        "tagline": site["tagline"],
        "byline": byline_html(home_updated),
        "cards": cards,
        "article_cards": article_cards,
        "fact_table_rows": fact_rows(data["home_facts"]),
        "faqs": faq_html,
        "footer": FOOTER_LINKS,
        "generated_at": generated_at,
    })
    (SITE_DIR / "index.html").write_text(home, encoding="utf-8")

    # ---- 品牌页：一个品牌一页，整族说法都进 title/H1/FAQ/JSON-LD
    for b in brands:
        title = b.get(
            "meta_title",
            f'{b["name"]} Pet Insurance: Review, Cost and Promo Code Facts',
        )
        description = b.get(
            "meta_description",
            f'{b["name"]} pet insurance in plain facts: cost, coverage, waiting periods, '
            f'quote flow and any official discounts, every line linked to '
            f'{b["official_site"].split("//")[1]}.',
        )
        canonical = page_url(site, f'/{b["slug"]}')
        b_updated = latest_checked(b["facts"] + b["faqs"])
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
                "inLanguage": site["locale"],
                # 只声明可核对的 dateModified（= 该页事实最近一次复核日）。
                # 站上从未记录过首发日，所以不写 datePublished，不编一个日期出去。
                "dateModified": b_updated,
                "author": author_jsonld(site),
                "publisher": publisher_jsonld(site),
                "mainEntityOfPage": canonical,
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
        jsonld_blocks.append(breadcrumb_jsonld(b["name"], canonical, site))
        head = head_block(title, description, canonical, jsonld_blocks, og_slug=f'og-{b["slug"]}')
        faq_html = "".join(
            f'<details open><summary>{escape(f["q"])}</summary><p>{escape(f["a"])}</p>'
            f'<p class="muted">Source: <a href="{escape(f["source_url"])}" rel="noopener" target="_blank">'
            f'{escape(f["source_url"])}</a> · checked {escape(site["checked"])}</p></details>'
            for f in b["faqs"]
        )
        related = b.get("related", [])
        related_html = ""
        if related:
            items = "".join(
                f'<li><a href="/{escape(r["slug"], quote=True)}">{escape(r["text"])}</a>'
                + (f' <span class="muted">{escape(r["why"])}</span>' if r.get("why") else "")
                + "</li>"
                for r in related
            )
            related_html = (
                f'<h2>More on {escape(b["name"])}</h2>\n'
                f'    <ul class="related">{items}</ul>'
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
            "related": related_html,
            "checked": site["checked"],
            "byline": byline_html(b_updated),
            "footer": FOOTER_LINKS,
        })
        (SITE_DIR / f'{b["slug"]}.html').write_text(html, encoding="utf-8")

    # ---- 文章页（排期表里的编辑型选题：build 时校验来源，缺来源即失败）
    brands_by_path = {f'/{b["slug"]}': b for b in brands}
    for a in articles:
        canonical = page_url(site, f'/{a["slug"]}')
        a_updated = latest_checked(a["facts"] + a["faqs"])
        stats_html = "".join(
            f'<div><b>{escape(s["value"])}</b><span class="muted">{escape(s["label"])}</span></div>'
            for s in a.get("stats", [])
        )
        jsonld_blocks = [
            jsonld({
                "@context": "https://schema.org",
                "@type": "Article",
                "headline": a["title"],
                "description": a["description"],
                "url": canonical,
                "inLanguage": site["locale"],
                # 同上：只有事实复核日是可核对的，不编首发日
                "dateModified": a_updated,
                "author": author_jsonld(site),
                "publisher": publisher_jsonld(site),
                "mainEntityOfPage": canonical,
                "about": {"@type": "Thing", "name": a.get("keyword", a["title"])},
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
                    for f in a["faqs"]
                ],
            }),
        ]
        # 对比类文章再给一个 ItemList（列出被比较的官方页面，描述取各品牌官网口径）
        if a.get("columns"):
            jsonld_blocks.append(jsonld({
                "@context": "https://schema.org",
                "@type": "ItemList",
                "name": a["title"],
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": i + 1,
                        "name": c["name"],
                        # 列可以是本页路径，也可以是被比较品牌的官方页（绝对 URL 原样用）
                        "url": c["url"] if c["url"].startswith("http") else page_url(site, c["url"]),
                        "description": brands_by_path.get(c["url"], {}).get("short_answer", ""),
                    }
                    for i, c in enumerate(a["columns"])
                ],
            }))
        jsonld_blocks.append(breadcrumb_jsonld(a["title"], canonical, site))
        head = head_block(a["title"], a["description"], canonical, jsonld_blocks, og_slug=f'og-{a["slug"]}')
        html = render(article_tpl, {
            "lang": "en",
            "title": a["title"],
            "head": head,
            "brand": site["name"],
            "nav": f'<a href="/">Home</a> · {nav}',
            "h1": a.get("h1", a["title"]),
            "lede": a["lede"],
            "facts_note": a.get("facts_note", "Every figure on this page was read from the brand's own official site and carries its source link and check date."),
            "stats": stats_html,
            "body": article_body(a, brands, "".join(
                f'<div class="card"><h3><a href="/{b["slug"]}">{escape(b["name"])}</a></h3>'
                f'<p class="price big">{escape(b["price_line"])}</p>'
                f'<p class="muted">{escape(b["price_condition"])}</p>'
                f'<p>{escape(b["short_answer"])}</p>'
                f'<p class="muted"><a href="/{b["slug"]}">Full {escape(b["name"])} facts</a></p></div>'
                for b in brands
            )),
            "disclaimer": a.get("disclaimer", ""),
            "checked": site["checked"],
            "byline": byline_html(a_updated),
            "footer": FOOTER_LINKS,
        })
        (SITE_DIR / f'{a["slug"]}.html').write_text(html, encoding="utf-8")

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
            og_slug="og-home",
            og_type="website",
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
    # lastmod 用每页自己记录的最近复核日，而不是全站同一个日期：全站日期会让
    # 每一页在每次构建时都宣称"刚改过"，反而让真正的更新看不出来。
    urls = [("/", "1.0", home_updated)]
    urls += [(f'/{b["slug"]}', "0.9", latest_checked(b["facts"] + b["faqs"])) for b in brands]
    urls += [(f'/{a["slug"]}', "0.8", latest_checked(a["facts"] + a["faqs"])) for a in articles]
    urls += [("/about", "0.5", site["checked"]),
             ("/privacy", "0.5", site["checked"]),
             ("/contact", "0.5", site["checked"])]
    missing_lastmod = [p for p, _, d in urls if not d]
    if missing_lastmod:
        raise SystemExit(f"SITEMAP ENTRY WITHOUT A REAL DATE: {missing_lastmod}")
    sitemap_items = "".join(
        f"<url><loc>{escape(page_url(site, path))}</loc>"
        f"<lastmod>{lastmod}</lastmod>"
        f"<priority>{pri}</priority></url>"
        for path, pri, lastmod in urls
    )
    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{sitemap_items}\n</urlset>\n"
    )
    (SITE_DIR / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    robots = f"User-agent: *\nAllow: /\n\nSitemap: {page_url(site, '/sitemap.xml')}\n"
    (SITE_DIR / "robots.txt").write_text(robots, encoding="utf-8")

    # ---- llms.txt / llms-full.txt（生成式引擎的可读索引，内容取自站内既有事实）
    (SITE_DIR / "llms.txt").write_text(llms_index(site, brands, articles), encoding="utf-8")
    (SITE_DIR / "llms-full.txt").write_text(llms_full(site, brands, articles), encoding="utf-8")

    # ---- IndexNow key file
    # IndexNow 要求把 <key>.txt 放在站点根目录、内容就是 key 本身，提交时用它证明
    # 我们拥有这个域。key 存在仓库里而不是每次构建重新生成，否则轮换 key 会让
    # 之前提交的 URL 关联失效。
    # ::RULE{key 必须可公开访问，worker 白名单必须包含它，否则 404}
    key = indexnow_key()
    (SITE_DIR / f"{key}.txt").write_text(key, encoding="utf-8")

    # ---- ads.txt
    # 站上目前没有任何广告或联盟链接（见 privacy 页）。空的 ads.txt 是合法且常见的
    # 声明：它明确表示"本站不授权任何广告系统售卖这里的广告位"，比 404 更清楚。
    (SITE_DIR / "ads.txt").write_text(
        "# This site does not currently sell advertising inventory and has no\n"
        "# authorized digital sellers. See /privacy for the current advertising status.\n",
        encoding="utf-8",
    )

    # ---- .well-known/security.txt（RFC 9116）
    # 只写真实存在的信息：联系地址就是站上公开的地址，没有 PGP key 就不编一个。
    wk = SITE_DIR / ".well-known"
    wk.mkdir(exist_ok=True)
    contact = site.get("contact_email", "")
    (wk / "security.txt").write_text(
        "Contact: "
        + (f"mailto:{contact}" if contact else page_url(site, "/contact"))
        + "\n"
        + f"Expires: {security_txt_expiry()}\n"
        + f"Canonical: {page_url(site, '/.well-known/security.txt')}\n"
        + "Policy: "
        + page_url(site, "/about")
        + "\nPreferred-Languages: en\n",
        encoding="utf-8",
    )

    # ---- _worker.js（规范主机 + 真 404）
    from urllib.parse import urlparse
    # 本机构建可用 PET_SITE_CANONICAL_HOST 覆盖 worker 的规范域名（只影响路由跳转，不改任何页面内容）
    host = os.environ.get("PET_SITE_CANONICAL_HOST") or urlparse(site["base_url"]).netloc
    assets = sorted(
        f"/assets/{p.name}" for p in (SITE_DIR / "assets").iterdir() if p.is_file()
    )
    valid_paths = sorted(
        {"/"} | {path for path, _, _ in urls} | {"/sitemap.xml", "/robots.txt", "/llms.txt", "/llms-full.txt", "/ads.txt", "/.well-known/security.txt", f"/{key}.txt"} | set(assets)
    )
    worker = (
        WORKER_TEMPLATE
        .replace("__CANONICAL_HOST__", host)
        .replace("__VALID_PATHS__", json.dumps(valid_paths))
    )
    (SITE_DIR / "_worker.js").write_text(worker, encoding="utf-8")

    print(f"built {len(urls) + 1} pages -> {SITE_DIR} at {generated_at}")


if __name__ == "__main__":
    build()
