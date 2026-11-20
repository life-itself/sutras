"""Match Rufus's bold-italic quotes (***...***) in Meditations.md against the draft.
usage: notes_match.py notes.md draft.md out.json"""
import re, sys, json, difflib, bisect

notes_path, draft_path, out_path = sys.argv[1:4]


def norm(s):
    s = s.replace('\u2026', ' . . . ')
    s = re.sub(r'\.\s*\.\s*\.', ' ... ', s)
    s = s.translate(str.maketrans({'\u2018': "'", '\u2019': "'", '\u201c': '"', '\u201d': '"',
                                   '\u2014': ' - ', '\u2013': ' - ', '\u00a0': ' '}))
    s = re.sub(r'(?<=\w)-(?=\w)', '-', s)
    s = re.sub(r'\s*-\s*', ' - ', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip()


# ---- draft: split into labelled chunks ----
draft = open(draft_path, encoding='utf-8').read()
draft = draft.split('\n---\n', 1)[1]
main, rest = draft.split('\n## Introduction\n', 1)
intro = rest.split('\n## Index of Persons\n', 1)[0]
chunks = []  # (label, normalized text)
for m in re.finditer(r'<a id="(\d+\.\d+a?)"></a>\n(.*?)(?=<a id="|\Z)', main, re.S):
    chunks.append((m.group(1), m.group(2)))
chunks.append(('Introduction', intro))


def clean_draft(t):
    t = re.sub(r'\[\^[^\]]+\]', '', t)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = re.sub(r'^## .*$', ' ', t, flags=re.M)
    t = t.replace('&lt;', '<').replace('&gt;', '>').replace('&emsp;', ' ')
    t = re.sub(r'\\(?=[^\w\s])', '', t)
    t = re.sub(r'^> ?', '', t, flags=re.M)
    t = t.replace('*', '')
    t = re.sub(r'^\d+a?\. ', '', t)   # section number at start of chunk
    return norm(t)


big = ''
starts = []
labels = []
for lab, t in chunks:
    starts.append(len(big))
    labels.append(lab)
    big += clean_draft(t) + ' '


def label_at(pos):
    return labels[bisect.bisect_right(starts, pos) - 1]


# ---- quotes ----
notes = open(notes_path, encoding='utf-8').read()
lines = notes.split('\n')
quotes = []
for m in re.finditer(r'\*\*\*(.+?)\*\*\*', notes, re.S):
    lineno = notes.count('\n', 0, m.start()) + 1
    q = m.group(1)
    q = re.sub(r'^\s*>\s?', '', q, flags=re.M)  # continuation lines inside blockquote
    quotes.append((lineno, q))

def book_cue(lineno):
    for i in range(lineno - 1, -1, -1):
        m = re.match(r'#{2,4} Book (\d+)', lines[i])
        if m:
            return m.group(1)
    return None


def find_best(nq, lineno, raw):
    occ = []
    i = big.find(nq)
    while i != -1:
        occ.append(i)
        i = big.find(nq, i + 1)
    if not occ:
        return -1
    lead = re.match(r'\s*[\u201c"]?(\d+)a?\.', raw)
    cue = book_cue(lineno)
    def score(i):
        lab = label_at(i)
        b, _, sec = lab.partition('.')
        sec = sec.rstrip('a')
        return ((lead is not None and sec == lead.group(1)) * 2 + (cue is not None and b == cue), -i)
    return max(occ, key=score)


results = []
for lineno, q in quotes:
    raw = q
    q = re.sub(r'^\s*\d+a?\.\s*', '', q.strip())
    nq = norm(q)
    rec = {'line': lineno, 'quote': raw.strip()}
    if not re.search(r'\w', nq):
        rec['status'] = 'empty'
        results.append(rec)
        continue
    i = find_best(nq, lineno, raw)
    if i != -1:
        rec['status'] = 'verbatim'
        rec['where'] = sorted(set([label_at(i), label_at(i + len(nq) - 1)]), key=lambda x: (x == 'Introduction', x))
        results.append(rec)
        continue
    # Rufus's own additions: wrapping quotation marks, section numbers, [bracketed] sources, footnote digits
    q2 = re.sub(r'\s*\[[^\]]*\]', '', q)
    q2 = re.sub(r'^\s*>\s*', '', q2, flags=re.M).strip()
    q2 = q2.strip('"\u201c\u201d ')
    q2 = re.sub(r'^\d+a?\.\s*', '', q2)
    q2 = re.sub(r'(?<=[a-z]\.)\d+(?=\s)', '', q2)
    nq2 = norm(q2)
    i = find_best(nq2, lineno, raw)
    if i != -1:
        rec['status'] = 'verbatim once Rufus\'s additions are removed'
        rec['additions'] = [x for x in (('quotation marks' if q.strip()[:1] in '"\u201c' or q.strip()[-1:] in '"\u201d' else ''), ('bracketed source' if '[' in q else ''), ('footnote digit' if re.search(r'[a-z]\.\d+\s', q) else '')) if x]
        rec['where'] = sorted(set([label_at(i), label_at(i + len(nq2) - 1)]), key=lambda x: (x == 'Introduction', x))
        results.append(rec)
        continue
    nq = nq2
    # try ellipsis fragments in order
    frags = [f.strip() for f in nq.split('...') if len(f.strip().split()) >= 2]
    pos = 0
    found = []
    for f in frags:
        j = big.find(f, pos)
        if j == -1:
            found = None
            break
        found.append(j)
        pos = j + len(f)
    if found and len(frags) > 1:
        rec['status'] = 'verbatim with elision'
        rec['where'] = sorted(set([label_at(found[0]), label_at(pos - 1)]))
        results.append(rec)
        continue
    # closest match by words
    qw = nq.split()
    bw = big.split()
    sm = difflib.SequenceMatcher(None, qw, bw, autojunk=False)
    mt = sm.find_longest_match(0, len(qw), 0, len(bw))
    lo = max(0, mt.b - mt.a - 5)
    hi = min(len(bw), mt.b + (len(qw) - mt.a) + 5)
    window = bw[lo:hi]
    sm2 = difflib.SequenceMatcher(None, qw, window, autojunk=False)
    diffs = []
    for op, a1, a2, b1, b2 in sm2.get_opcodes():
        if op != 'equal' and not (b1 == 0 or b2 == len(window)) or (op in ('replace', 'delete')):
            diffs.append('%s: notes "%s" / text "%s"' % (op, ' '.join(qw[a1:a2]), ' '.join(window[b1:b2])))
    charpos = len(' '.join(bw[:mt.b]))
    rec['status'] = 'not verbatim'
    rec['closest'] = label_at(charpos)
    rec['ratio'] = round(sm2.ratio(), 2)
    rec['diffs'] = diffs[:6]
    results.append(rec)

json.dump(results, open(out_path, 'w'), indent=1, ensure_ascii=False)
from collections import Counter
print(Counter(r['status'] for r in results), len(results))
for r in results:
    if r['status'] == 'not verbatim':
        print(r['line'], r['closest'], r['ratio'], r['quote'][:70].replace('\n', ' '))
        for d in r['diffs']:
            print('     ', d[:160])
