# 只读诊断：量化站内页面之间的正文重复，找出最可能被 Google 当成重复内容的页面对。
import re, glob, os, itertools

WORD = re.compile(r"[a-z0-9'\-]+")


def body_words(path):
    html = open(path, encoding='utf-8').read()
    m = re.search(r'<main[^>]*>(.*?)</main>', html, flags=re.S | re.I)
    chunk = m.group(1) if m else html
    chunk = re.sub(r'<script.*?</script>', ' ', chunk, flags=re.S | re.I)
    chunk = re.sub(r'<[^>]+>', ' ', chunk)
    chunk = re.sub(r'&[a-z]+;|&#\d+;', ' ', chunk)
    chunk = re.sub(r'\s+', ' ', chunk).strip().lower()
    return WORD.findall(chunk)


def main():
    pages = {}
    for f in sorted(glob.glob('site/*.html')):
        w = body_words(f)
        if len(w) > 400:
            pages[os.path.basename(f)[:-5]] = w

    grams = {k: set(tuple(w[i:i + 7]) for i in range(len(w) - 6)) for k, w in pages.items()}
    pairs = []
    for a, b in itertools.combinations(sorted(grams), 2):
        ga, gb = grams[a], grams[b]
        inter = len(ga & gb)
        if inter < 60:
            continue
        pairs.append((inter, 100.0 * inter / min(len(ga), len(gb)), a, b))
    pairs.sort(reverse=True)
    print('%-7s %6s  %-40s %s' % ('shared', 'pctmin', 'page A', 'page B'))
    for inter, pct, a, b in pairs[:16]:
        print('%7d %5.1f%%  %-40s %s' % (inter, pct, a, b))

    print()
    print('worst offenders (max shared % against any other page):')
    worst = {}
    for inter, pct, a, b in pairs:
        for x, y in ((a, b), (b, a)):
            if pct > worst.get(x, (0, ''))[0]:
                worst[x] = (pct, y)
    for p, (pct, other) in sorted(worst.items(), key=lambda kv: -kv[1][0]):
        print('  %-42s %5.1f%% shared with %s' % (p, pct, other))


if __name__ == '__main__':
    main()
