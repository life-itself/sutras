"""Build library/dhammapada/edition-draft.md from the unpacked Thanissaro EPUB.
usage: python3 -I dhp_build.py <unpacked-epub>/OEBPS <out.md> <report.json>  (see library/dhammapada/NOTES.md)"""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import re, json
from common import load, tag, inline, NS
import dhp_parse as d

BASE = sys.argv[1]          # OEBPS dir
OUT = sys.argv[2]
REPORT = sys.argv[3]
d.BASE = BASE
EM = ' '


def indent(cls):
    m = re.match(r'v(-?\d+)$', cls or '')
    n = int(m.group(1)) if m else 0
    return '&emsp;' * max(n, 0)


def esc_start(line):
    m = re.match(r'(\d+)\. ', line)
    if m:
        return m.group(1) + '\\.' + line[m.end() - 1:]
    if re.match(r'[-+#>|]', line):
        return '\\' + line
    return line


def verse_lines(ps, prefix=''):
    """ps: list of (cls, p-element). Return Markdown lines with hard breaks."""
    lines = []
    for cls, p in ps:
        for t in inline(p).split('\n'):
            lines.append(indent(cls) + esc_start(t))
    return [prefix + l + ('  ' if i < len(lines) - 1 else '') for i, l in enumerate(lines)]


def render_blocks(el, prefix=''):
    """Render block children of el (front/back matter, notes) to Markdown paragraphs."""
    out = []
    for c in el:
        t = tag(c)
        cls = c.get('class') or ''
        if t == 'h1':
            continue
        if t in ('h2', 'h3', 'h4', 'h5'):
            out.append('### ' + inline(c).replace('\n', ' '))
        elif t == 'p':
            txt = inline(c)
            if not txt:
                continue
            if cls == 'blockquote':
                out.append('\n'.join(prefix + '> ' + l for l in txt.split('\n')))
            else:
                out.append(prefix + esc_start(txt.replace('\n', '\\\n' + prefix)))
        elif t == 'div' and 'verse' in cls.split():
            ps = [(p.get('class'), p) for p in c if tag(p) == 'p']
            out.append('\n'.join(verse_lines(ps, prefix + '> ')))
        elif t == 'div':
            out.extend(render_blocks(c, prefix))
        elif t == 'table':
            rows = [[inline(td) for td in tr if tag(td) in ('td', 'th')] for tr in c.iter(NS + 'tr')]
            out.append('\n'.join(['| | |', '|---|---|'] + ['| ' + ' | '.join(r) + ' |' for r in rows]))
        else:
            raise Exception('unhandled block ' + t)
    return out


def section(n):
    root = load(BASE + '/Text/Section%04d.xhtml' % n)
    body = root.find(NS + 'body')
    return render_blocks(body)


report = {'fixes': [], 'notes': {}, 'merged_groups': []}

# ---- endnotes ----
notes = []  # {label, paras}
nroot = load(BASE + '/Text/Section0033.xhtml').find(NS + 'body')
for c in nroot:
    if tag(c) == 'h1' or (c.get('class') == 'halfheight'):
        continue
    if tag(c) == 'p' and c.get('id', '').startswith('n-'):
        a = c.find(NS + 'a')
        label = ''.join(a.itertext()).strip()
        # drop the label link, keep the rest
        txt = inline(c)
        assert txt.startswith(label + ':'), txt[:40]
        notes.append({'label': label, 'paras': [txt[len(label) + 1:].strip()]})
    else:
        notes[-1].setdefault('els', []).append(c)

for n in notes:
    for c in n.pop('els', []):
        if tag(c) == 'p':
            txt = inline(c)
            if txt:
                n['paras'].append(txt.replace('\n', '\\\n'))
        elif tag(c) == 'div':
            stanzas = [x for x in c if tag(x) == 'div'] or [c]
            for st in stanzas:
                ps = [(p.get('class'), p) for p in st if tag(p) == 'p']
                assert ps, 'empty stanza in note ' + n['label']
                n['paras'].append('\n'.join(verse_lines(ps)))
        else:
            raise Exception('note block ' + tag(c))

# ---- chapters ----
note_by_end = {}
for n in notes:
    a, b = d.rng(n['label'])
    note_by_end.setdefault(b, []).append(n)

chapters = d.chapters()
out = []
ids = []
for title, groups in chapters:
    out.append('## ' + title + '\n')
    for g in groups:
        a, b = d.rng(g['label'])
        nverses = b - a + 1
        divs = g['divs']
        per_div = len(divs) == nverses
        if not per_div:
            report['merged_groups'].append({'label': g['label'], 'stanzas': len(divs)})
        block = []
        for i, dv in enumerate(divs):
            if per_div:
                vids = [a + i]
            else:
                vids = list(range(a, b + 1)) if i == 0 else []
            lines = verse_lines(dv['lines'])
            # footnotes: attach notes ending at this verse (per-div) or at group end (merged)
            ends = vids if per_div else (list(range(a, b + 1)) if i == len(divs) - 1 else [])
            refs = ''
            for v in ends:
                for n in note_by_end.get(v, []):
                    refs += '[^%s]' % n['label']
                    n['placed'] = True
            if refs:
                last = lines[-1]
                lines[-1] = last.rstrip() + refs + ('  ' if last.endswith('  ') else '')
            anchor = ''.join('<a id="%d"></a>' % v for v in vids)
            ids.extend(vids)
            block.append((anchor + '\n' if anchor else '') + '\n'.join(lines))
        out.append('\n\n'.join(block) + '\n\n<p class="cite">%s</p>\n' % g['label'])

unplaced = [n['label'] for n in notes if not n.get('placed')]
report['unplaced_notes'] = unplaced
report['ids'] = len(ids)
report['unique_ids'] = len(set(ids))
report['notes_total'] = len(notes)

# ---- front and back matter ----
matter = [
    ('Preface', 4), ('Introduction', 5), ('Historical Notes: The Text & the Translation', 32),
    ('Abbreviations', 3), ('Glossary', 34), ('Bibliography', 35), ('Copyright', 2),
]
for name, n in matter:
    out.append('## ' + name + '\n')
    out.append('\n\n'.join(section(n)) + '\n')

# ---- footnote definitions ----
defs = []
for n in notes:
    body = n['paras'][0]
    rest = n['paras'][1:]
    s = '[^%s]: %s' % (n['label'], body)
    for r in rest:
        s += '\n\n' + '\n'.join('    ' + l for l in r.split('\n'))
    defs.append(s)
out.append('\n\n'.join(defs) + '\n')

fm = '''---
title: Dhammapada
author: "Traditionally the Buddha; compiled in the Pāli Canon (Khuddaka Nikāya)"
translator: Thanissaro Bhikkhu (Geoffrey DeGraff)
date: "Verses attributed to the Buddha (5th century BCE); the anthology was fixed in the Pāli Canon, written down around the 1st century BCE"
tradition: Theravāda Buddhism
source: "Dhammapada: A Translation, by Thanissaro Bhikkhu (Metta Forest Monastery; © 1998, revised edition 2011). EPUB supplied by Rufus Pollock."
licence: "© 1998 Thanissaro Bhikkhu (revised edition 2011). For free distribution: may be copied and republished free of charge, if derivations state that they are derived and differ, and the full licence text is included (see Copyright below). Otherwise all rights reserved."
status: draft
---
'''
open(OUT, 'w', encoding='utf-8').write(fm + '\n' + '\n'.join(out))
json.dump(report, open(REPORT, 'w'), indent=1, ensure_ascii=False)
print(json.dumps({k: v for k, v in report.items() if k != 'notes'}, ensure_ascii=False))
