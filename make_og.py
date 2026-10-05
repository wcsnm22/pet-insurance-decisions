# ILANG
# TYPE:tool ROLE:og-image-generator PROJECT:pet-insurance-decisions
# ::RULE{图片只是页面标题和站内既有数字的排版 不引入任何新事实 不做品牌 logo 拼贴}
# ::BOUNDARY{never:改 site 输出目录之外的文件 用非系统字体 依赖网络|scope:file}
"""为每个页面生成一张 1200x630 的社交分享图（og:image）。

输出到 templates/assets/og-<slug>.png，由 build.py 原样拷进 site/assets/。
build.py 本身保持零依赖，所以生图这一步单独跑：

    python make_og.py

图上只有两样东西：页面标题，以及该页已经在渲染的 stats 里印出来的那个数字。
不新增任何站内没有的事实。

版式自下而上固定：页脚和数字条的位置是常量，标题只拿到剩下的高度，并且在
横向折行的同时按高度反推字号，最后断言标题底边没有压到数字条。
"""
from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "templates" / "assets"
FONT_DIR = Path("C:/Windows/Fonts")

W, H = 1200, 630
SCALE = 2
PAD = 84

# 画布上的固定锚点（未缩放坐标）：改这里必须让下面的断言重新通过
BRAND_Y = 86
TITLE_TOP = 186
STAT_H = 92
STAT_GAP = 26          # 数字条与标题之间的最小空隙
FOOT_LINE_Y = 520
FOOT_TEXT_Y = 544

BG = (10, 13, 19)
PANEL = (18, 25, 38)
LINE = (33, 44, 61)
TEXT = (233, 239, 248)
MUTED = (147, 163, 184)
DIM = (125, 142, 166)
ACCENT = (246, 130, 31)
ACCENT_2 = (255, 180, 107)

STAT_TOP = FOOT_LINE_Y - 34 - STAT_H          # 数字条自下而上定位
TITLE_MAX_W = W - PAD * 2
TITLE_MAX_H = STAT_TOP - STAT_GAP - TITLE_TOP  # 标题能用的全部高度
LINE_RATIO = 1.22


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONT_DIR / name), size * SCALE)


def wrap(draw: ImageDraw.ImageDraw, text: str, f: ImageFont.FreeTypeFont, max_w: int) -> list[str]:
    """按像素宽度折行；单个超长单词也不许溢出给定宽度。"""
    lines, cur = [], ""
    for word in text.split():
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=f) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def fit_title(draw: ImageDraw.ImageDraw, title: str) -> tuple[ImageFont.FreeTypeFont, list[str], float]:
    """在 3 行以内同时满足宽和高，取能放下的最大字号。"""
    for size in range(62, 33, -2):
        f = font("segoeuib.ttf", size)
        lines = wrap(draw, title, f, TITLE_MAX_W)
        if len(lines) <= 3 and len(lines) * size * LINE_RATIO <= TITLE_MAX_H:
            return f, lines, size * LINE_RATIO
    raise SystemExit(f"TITLE DOES NOT FIT AT ANY SIZE: {title!r}")


def glow(base: Image.Image, cx: float, cy: float, r: float, color: tuple[int, int, int], alpha: int) -> None:
    """柔和径向光斑：画在独立图层上再高斯模糊，叠回底色。"""
    layer = Image.new("RGB", base.size, (0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.ellipse([(cx - r) * SCALE, (cy - r) * SCALE, (cx + r) * SCALE, (cy + r) * SCALE], fill=color)
    layer = layer.filter(ImageFilter.GaussianBlur(r * SCALE * 0.55))
    base.paste(Image.blend(base, layer, alpha / 255), (0, 0))


def render(title: str, stat_value: str, stat_label: str, out: Path) -> None:
    img = Image.new("RGB", (W * SCALE, H * SCALE), BG)
    glow(img, 120, 20, 520, (58, 30, 8), 150)
    glow(img, 1120, 40, 460, (22, 33, 62), 150)

    d = ImageDraw.Draw(img)
    f_brand = font("segoeuib.ttf", 30)
    f_foot = font("segoeui.ttf", 25)
    f_label = font("segoeui.ttf", 26)

    d.rectangle([PAD * SCALE, 60 * SCALE, (PAD + 46) * SCALE, 68 * SCALE], fill=ACCENT)
    d.text((PAD * SCALE, BRAND_Y * SCALE), "Pet Insurance Decisions", font=f_brand, fill=TEXT)

    f_title, lines, line_h = fit_title(d, title)
    y = TITLE_TOP * SCALE
    for ln in lines:
        d.text((PAD * SCALE, y), ln, font=f_title, fill=TEXT)
        y += int(line_h * SCALE)
    title_bottom = y / SCALE

    if stat_value:
        top = STAT_TOP * SCALE
        f_stat = font("segoeuib.ttf", 50)
        vw = d.textlength(stat_value, font=f_stat)
        box_w = min(int(vw) + 72 * SCALE, TITLE_MAX_W)
        d.rounded_rectangle(
            [PAD * SCALE, top, PAD * SCALE + box_w, top + STAT_H * SCALE],
            radius=20 * SCALE, fill=PANEL, outline=LINE, width=2 * SCALE,
        )
        d.text((PAD * SCALE + 36 * SCALE, top + (STAT_H - 50) / 2 * SCALE + 4 * SCALE),
               stat_value, font=f_stat, fill=ACCENT_2)
        lx = PAD * SCALE + box_w + 30 * SCALE
        ly = top + 22 * SCALE
        for ln in wrap(d, stat_label, f_label, (W - PAD) * SCALE - lx)[:2]:
            d.text((lx, ly), ln, font=f_label, fill=MUTED)
            ly += 34 * SCALE

    d.line([PAD * SCALE, FOOT_LINE_Y * SCALE, (W - PAD) * SCALE, FOOT_LINE_Y * SCALE],
           fill=LINE, width=2 * SCALE)
    d.text((PAD * SCALE, FOOT_TEXT_Y * SCALE), "furadvisor.com", font=f_foot, fill=TEXT)
    note = "Every figure taken from the brand's own official page"
    nw = d.textlength(note, font=f_foot)
    d.text(((W - PAD) * SCALE - nw, FOOT_TEXT_Y * SCALE), note, font=f_foot, fill=DIM)

    # 断言：标题不能被数字条压住，数字条不能被页脚压住
    assert title_bottom <= STAT_TOP - STAT_GAP + 1, (title, title_bottom, STAT_TOP)
    assert STAT_TOP + STAT_H <= FOOT_LINE_Y, (title, STAT_TOP + STAT_H, FOOT_LINE_Y)

    img.resize((W, H), Image.LANCZOS).save(out, "PNG", optimize=True)


def main() -> None:
    data = json.loads((ROOT / "data" / "brands.json").read_text(encoding="utf-8"))
    site = data["site"]
    articles = json.loads((ROOT / "data" / "articles.json").read_text(encoding="utf-8"))["articles"]

    jobs = [
        ("og-home.png", site.get("meta_title", site["name"]),
         "$10/mo", "lowest published starting price (Lemonade)"),
    ]
    for b in data["brands"]:
        jobs.append((f'og-{b["slug"]}.png', b.get("meta_title", b["name"]),
                     b["price_line"], b["price_condition"]))
    for a in articles:
        stats = a.get("stats") or []
        jobs.append((f'og-{a["slug"]}.png', a.get("meta_title", a["title"]),
                     stats[0]["value"] if stats else "", stats[0]["label"] if stats else ""))

    for name, title, value, label in jobs:
        out = ASSETS / name
        render(title, value, label, out)
        print(f"{out.name:52} {out.stat().st_size // 1024:4} KB  {title}")

    print(f"\n{len(jobs)} og images -> {ASSETS}")
    print(f"layout: title {TITLE_TOP}-{STAT_TOP - STAT_GAP}px, stat bar {STAT_TOP}-{STAT_TOP + STAT_H}px, footer {FOOT_LINE_Y}px")


if __name__ == "__main__":
    main()
