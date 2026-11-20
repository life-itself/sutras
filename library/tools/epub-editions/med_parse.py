import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import re, sys
from common import load, tag, inline, NS

BOOK_FILES = ['index_split_%03d.html' % n for n in range(7, 30, 2)]


def blocks(path, sup=None):
    """Yield (cls, markdown_text) for each top-level div of a calibre file; '' text = spacer."""
    root = load(path)
    body = root.find(NS + 'body')
    out = []
    for d in body:
        if tag(d) != 'div':
            continue
        cls = d.get('class') or ''
        if cls in ('mbp_pagebreak',):
            continue
        ps = d.findall(NS + 'p')
        if not ps:
            continue
        txt = '\n'.join(inline(p, sup=sup) for p in ps).strip()
        out.append((cls, txt))
    return out


def book_sections(base):
    """Return {book: [(label, num, [(cls, text), ...])]}; label like '49' or '49a'.
    Also returns list of repairs made."""
    books = {}
    fixes = []
    for b, f in enumerate(BOOK_FILES, 1):
        secs = []
        cur = None
        for cls, txt in blocks(base + '/' + f):
            m = re.match(r'(\d+)(a?)\.( ?)', txt)
            if m:
                n = int(m.group(1))
                last = secs[-1][1] if secs else 0
                ok = (not m.group(2) and n == last + 1) or (m.group(2) and n == last)
                if ok:
                    if not m.group(3):
                        fixes.append('%d.%s: added missing space after "%s"' % (b, m.group(1), m.group(0)))
                        txt = m.group(0) + ' ' + txt[m.end():]
                    cur = (m.group(1) + m.group(2), n, [])
                    secs.append(cur)
            if cur is None:
                if txt:
                    print('PRE-SECTION', b, repr(txt[:60]), file=sys.stderr)
                continue
            cur[2].append((cls, txt))
        books[b] = secs
    return books, fixes


if __name__ == '__main__':
    bs, fixes = book_sections(sys.argv[1])
    std = [17, 17, 16, 51, 37, 59, 75, 61, 42, 38, 39, 36]
    for b, secs in bs.items():
        main = [s for s in secs if not s[0].endswith('a')]
        print(b, len(main), std[b - 1], [('%d.%s' % (b, s[0])) for s in secs if s[0].endswith('a')])
    print(fixes)
    for b, secs in bs.items():
        for lab, n, paras in secs:
            for cls, t in paras[1:]:
                if re.match(r'\d+a?\.', t):
                    print('NUMLIKE', b, lab, t[:60])
