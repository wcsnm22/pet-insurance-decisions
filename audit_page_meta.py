# 只读：检查可能让 Google「抓取后不收录」的页面级技术问题（标题/描述/H1 唯一性、结构化数据、内链锚文本）。
import re, glob, os, json
from collections import Counter


def txt(s):
    s = re.sub(r'<[^>]+>', '', s or '')
    return re.sub(r'\s+', ' ', s).strip()


def main():
    rows = []
    for f in sorted(glob.glob('site/*.html')):
        h = open(f, encoding='utf-8').read()
        slug = os.path.basename(f)[:-5]
        title = re.search(r'<title>(.*?)</title>', h, flags=re.S | re.I)
        desc = re.search(r'<meta name="description" content="([^"]*)"', h, flags=re.I)
        h1 = re.findall(r'<h1[^>]*>(.*?)</h1>', h, flags=re.S | re.I)
        ld = re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, flags=re.S | re.I)
        rows.append({
            'slug': slug,
            'title': txt(title.group(1)) if title else '',
            'desc': txt(desc.group(1)) if desc else '',
            'h1': [txt(x) for x in h1],
            'ld_blocks': len(ld),
            'ld_types': re.findall(r'"@type"\s*:\s*"([^"]+)"', ' '.join(ld)),
        })

    print('=== 唯一性检查（%d 个页面）===' % len(rows))
    for key, label in (('title', 'title'), ('desc', 'meta description')):
        c = Counter(r[key] for r in rows if r[key])
        dup = {k: v for k, v in c.items() if v > 1}
        missing = [r['slug'] for r in rows if not r[key]]
        print('%-18s unique=%d/%d  missing=%s  dup=%s' % (
            label, len(c), len(rows), missing or '-',
            ([(k[:60], v) for k, v in dup.items()]) or '-'))
    h1count = Counter(len(r['h1']) for r in rows)
    print('%-18s H1 count distribution: %s' % ('h1', dict(h1count)))
    h1dup = {k: v for k, v in Counter(r['h1'][0] for r in rows if r['h1']).items() if v > 1}
    print('%-18s duplicate H1: %s' % ('', h1dup or '-'))

    print()
    print('=== 结构化数据类型 ===')
    for r in rows:
        print('  %-46s ld=%-2d %s' % (r['slug'], r['ld_blocks'], ','.join(sorted(set(r['ld_types'])))))

    print()
    print('=== 标题长度 / 描述长度（Google 截断约 580px / 155 字符）===')
    for r in rows:
        flag = ''
        if len(r['title']) > 65:
            flag += ' TITLE_LONG'
        if not (70 <= len(r['desc']) <= 165):
            flag += ' DESC_OUT_OF_RANGE'
        if len(r['h1']) != 1:
            flag += ' H1_NOT_ONE'
        if flag:
            print('  %-46s t=%-3d d=%-3d%s' % (r['slug'], len(r['title']), len(r['desc']), flag))

    print()
    print('=== 内链锚文本（站内指向每页的锚文本）===')
    anchors = {}
    for f in sorted(glob.glob('site/*.html')):
        h = open(f, encoding='utf-8').read()
        for m in re.finditer(r'<a\s+[^>]*href="(/[^"#?]*)"[^>]*>(.*?)</a>', h, flags=re.S | re.I):
            href, a = m.group(1), txt(m.group(2))
            if not href or href.startswith('/sitemap') or href.startswith('/privacy'):
                continue
            anchors.setdefault(href.lstrip('/') or 'index', []).append(a)
    for slug in sorted(anchors):
        vs = anchors[slug]
        uniq = sorted(set(vs))
        print('  %-46s n=%-3d distinct=%-2d %s' % (
            slug, len(vs), len(uniq), ' | '.join(u[:38] for u in uniq[:3])))

    json.dump(rows, open('audit_page_meta.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('\nwritten audit_page_meta.json')


if __name__ == '__main__':
    main()
