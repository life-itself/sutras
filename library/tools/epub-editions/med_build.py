"""Build library/meditations/edition-draft.md from the unpacked Hays EPUB.
usage: python3 -I med_build.py <unpacked-epub-dir> <out.md> <report.json>  (see library/meditations/NOTES.md)"""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import re, json
from med_parse import blocks, book_sections

BASE = sys.argv[1]
OUT = sys.argv[2]
REPORT = sys.argv[3]

BOOK_TITLES = {1: 'Debts and Lessons', 2: 'On the River Gran, Among the Quadi', 3: 'In Carnuntum'}

report = {'fixes': [], 'unplaced_notes': [], 'placed_notes': 0}


def esc_start(line):
    """Escape characters that would start Markdown block syntax at line start."""
    m = re.match(r'(\d+)([a-z]?)\. ', line)
    if m:
        return m.group(1) + m.group(2) + '\\.' + line[m.end() - 1:]
    if re.match(r'[-+#>|]', line):
        return '\\' + line
    return line


def render(paras):
    """Render a list of (cls, text) blocks to Markdown paragraphs."""
    out = []
    group = None  # ('list'|'verse', [lines])
    state = {'open_para': False}  # previous block is a plain paragraph that runs on into verse
    def flush():
        nonlocal group
        if group:
            kind, lines = group
            if kind == 'verse' and state['open_para']:
                out[-1] += '  \n' + '  \n'.join(esc_start(l) for l in lines)
            elif kind == 'verse':
                out.append('\n'.join('> ' + esc_start(l) + ('  ' if i < len(lines) - 1 else '') for i, l in enumerate(lines)))
            else:
                out.append('\n'.join(esc_start(l) + ('  ' if i < len(lines) - 1 else '') for i, l in enumerate(lines)))
        group = None
        state['open_para'] = False
    for cls, t in paras:
        if not t.strip():
            flush()
            continue
        kind = {'calibre_6': 'verse', 'calibre_10': 'list', 'calibre_11': 'list', 'calibre_13': 'list'}.get(cls)
        if kind:
            if group and group[0] != kind:
                flush()
            if not group:
                group = (kind, [])
            group[1].extend(t.split('\n'))
        else:
            flush()
            out.append('\n'.join(esc_start(l) for l in t.split('\n')))
            state['open_para'] = not re.search(r'[.?!:;”’)*]$', t.strip())
    flush()
    return out


# ---------- notes ----------
def parse_notes():
    notes = []  # dicts: key ('4.3' or 'book2'), lemma, body(list of paragraphs)
    cur_key = None
    for cls, t in blocks(BASE + '/index_split_030.html'):
        if not t.strip() or cls == 'calibre_2':
            continue
        m = re.match(r'(\d+)\.(\d+a?) (.*)$', t, re.S)
        mb = re.match(r'(\d+)\. (.*)$', t, re.S)
        if m:
            cur_key = '%s.%s' % (m.group(1), m.group(2))
            rest = m.group(3)
        elif mb:
            cur_key = 'book' + mb.group(1)
            rest = mb.group(2)
        else:
            rest = t
        lm = re.match(r'(\*.*?:\*|\*[^*]*\*[^*]*\*:\*|.*?:\*)\s*(.*)$', rest, re.S)
        if lm and (m or mb or rest.startswith('*') or rest.startswith('&lt;')):
            notes.append({'key': cur_key, 'lemma': lm.group(1), 'body': [lm.group(2)]})
        else:
            notes[-1]['body'].append(rest)
    return notes


BETWEEN = r"[\s*“”‘’\"'()\[\]\\&;ltg]*"


def lemma_pattern(lemma):
    plain = re.sub(r'&lt;|&gt;', ' ', lemma).replace('*', ' ')
    plain = plain.strip().rstrip(':').strip()
    plain = re.sub(r" et al\.?$", "", plain)
    segs = [s for s in re.split(r'\.\s\.\s\.', plain) if re.search(r'\w', s)]
    if not segs:
        return None
    seg = segs[-1]
    toks = re.findall(r'\w+|[^\w\s“”‘’"\']', seg)
    toks = [t for t in toks if re.match(r'\w', t) or t in ',;!?-—']
    if not toks:
        return None
    return BETWEEN.join(re.escape(t) for t in toks)


def place(paras_md, pat, ref):
    for i, p in enumerate(paras_md):
        m = re.search(pat, p, re.I)
        if m:
            end = m.end()
            # step back over trailing junk the BETWEEN class may have eaten
            while end > m.start() and p[end - 1] in ' \n':
                end -= 1
            # don't break emphasis: if inside *...*, move past the closing *
            if p[:end].count('*') % 2 == 1:
                nxt = p.find('*', end)
                if nxt != -1:
                    end = nxt + 1
            # keep trailing punctuation before the ref
            m2 = re.match(r' ?&lt; ?(\*?\. \. \.\*?) ?&gt;', p[end:])
            if m2:
                end += m2.end()
            while end < len(p) and p[end] in '.,;:!?”’)]\\':
                end += 1
            paras_md[i] = p[:end] + ref + p[end:]
            return True
    return False


# ---------- build ----------
FIXES = [
    (1, '2', 'REPUTATIONf)', 'REPUTATION)', 'stray "f" in the EPUB heading'),
    (1, '15', 'MAXIMUSMaximus', 'MAXIMUS', 'heading doubled in the EPUB'),
    (4, '48', 'upwithout', 'up without', 'missing space in the EPUB'),
    (6, '47', 'thewhole', 'the whole', 'missing space in the EPUB'),
]
books, fixes = book_sections(BASE)
report['fixes'] += fixes
notes = parse_notes()
labels_used = {}
note_defs = []
book_note_refs = {}
sec_md = {}  # (book, label) -> list of md paragraphs
for b, secs in books.items():
    for lab, n, paras in secs:
        # fix known conversion damage
        fixed = []
        for cls, t in paras:
            for (fb, fs, old, new, why) in FIXES:
                if b == fb and lab == fs and old in t:
                    t = t.replace(old, new)
                    report['fixes'].append('%d.%s: "%s" -> "%s" (%s)' % (fb, fs, old, new, why))
            fixed.append((cls, t))
        sec_md[(b, lab)] = render(fixed)

for note in notes:
    k = note['key']
    labels_used[k] = labels_used.get(k, 0) + 1
    label = k if labels_used[k] == 1 else '%s-%d' % (k, labels_used[k])
    ref = '[^%s]' % label
    lemma = note['lemma']
    if '&lt;' in lemma:
        lemma = '*' + re.sub(r'\s+', ' ', lemma.replace('*', '')).strip() + '*'
    body = lemma + ' ' + '\n\n    '.join(note['body'])
    note_defs.append('[^%s]: %s' % (label, body.strip()))
    if k.startswith('book'):
        book_note_refs.setdefault(int(k[4:]), []).append(ref)
        report['placed_notes'] += 1
        continue
    b, s = k.split('.')
    key = (int(b), s)
    if key not in sec_md:
        report['unplaced_notes'].append((k, note['lemma'], 'no such section'))
        continue
    pat = lemma_pattern(note['lemma'])
    if pat and place(sec_md[key], pat, ref):
        report['placed_notes'] += 1
    else:
        sec_md[key][0] = sec_md[key][0] + ref
        report['unplaced_notes'].append((k, note['lemma'], 'lemma not found; ref put at end of first paragraph'))

# introduction
intro = []
skip_intro_heads = {'Introduction'}
in_notes = False
intro_notes = []
epigraph = []
paras = blocks(BASE + '/index_split_005.html', sup=lambda s: '[^i%s]' % s.strip())
buf = []
def flush_buf():
    global buf
    if buf:
        intro.extend(render(buf))
    buf = []
for cls, t in paras:
    if not t.strip():
        buf.append((cls, t))
        continue
    if in_notes:
        m = re.match(r'(\d+)\. (.*)$', t, re.S)
        if m:
            intro_notes.append('[^i%s]: %s' % (m.group(1), m.group(2)))
        else:
            intro_notes[-1] += '\n\n    ' + t
        continue
    if cls == 'calibre_2':
        if t in skip_intro_heads:
            continue
        if t.startswith('States will never') or t.startswith('—PLATO'):
            flush_buf()
            if t.startswith('—PLATO'):
                intro[-1] += '  \n> ' + t
            else:
                intro.append('> ' + t)
            continue
        if t == '*Gregory Hays*':
            flush_buf()
            intro.append(t)
            continue
        flush_buf()
        intro.append('### ' + t)
        continue
    if cls == 'calibre_6' and (re.fullmatch(r'\*[^*]+\*', t) or t.isupper()):
        flush_buf()
        if t == 'INTRODUCTION NOTES':
            in_notes = True
            continue
        intro.append(('#### ' + t.strip('*')) if t.startswith('*') else ('### ' + t))
        continue
    buf.append((cls, t))
flush_buf()

# index of persons, about the translator, copyright
def simple(fname, drop_first_heading=True):
    out = []
    for md in render([(c, t) for c, t in blocks(BASE + '/' + fname) if c != 'calibre_2' or not drop_first_heading]):
        out.append(md)
    return out

index = render([(('calibre_8' if c == 'calibre_11' else c), t) for c, t in blocks(BASE + '/index_split_031.html') if c != 'calibre_2'])
about = [t for c, t in blocks(BASE + '/index_split_032.html') if t.strip() and t.strip() != 'ABOUT THE TRANSLATOR']
copyright = [esc_start(t) for c, t in blocks(BASE + '/index_split_034.html') if t.strip()]

fm = '''---
title: Meditations
author: Marcus Aurelius
translator: Gregory Hays
date: "Written in Greek, probably in the 170s CE (Marcus died in 180)"
tradition: Stoicism
source: "Marcus Aurelius, Meditations: A New Translation, with an Introduction, by Gregory Hays (Modern Library, 2002; e-ISBN 1-58836-173-X). EPUB supplied by Rufus Pollock."
licence: "In copyright: Introduction and notes © 2002 Gregory Hays; all rights reserved (Modern Library). Reproduced in full without permission."
status: draft
---
'''

lines = [fm]
for b, secs in books.items():
    title = 'Book %d' % b + (': ' + BOOK_TITLES[b] if b in BOOK_TITLES else '')
    lines.append('<a id="%d"></a>\n\n## %s%s\n' % (b, title, ''.join(book_note_refs.get(b, []))))
    for lab, n, paras in secs:
        md = sec_md[(b, lab)]
        md[0] = '<a id="%d.%s"></a>\n' % (b, lab) + md[0]
        lines.append('\n\n'.join(md) + '\n')

lines.append('## Introduction\n')
lines.append('\n\n'.join(intro) + '\n')
lines.append('## Index of Persons\n')
lines.append('\n\n'.join(index) + '\n')
lines.append('## About the Translator\n')
lines.append('\n\n'.join(about) + '\n')
lines.append('## Copyright\n')
lines.append('\n\n'.join(copyright) + '\n')
lines.append('\n\n'.join(intro_notes) + '\n')
lines.append('\n\n'.join(note_defs) + '\n')
open(OUT, 'w', encoding='utf-8').write('\n'.join(lines))
report['notes_total'] = len(notes)
report['intro_notes'] = len(intro_notes)
json.dump(report, open(REPORT, 'w'), indent=1, ensure_ascii=False)
print(json.dumps({k: (v if not isinstance(v, list) else len(v)) for k, v in report.items()}))
