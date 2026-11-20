import re, html
import xml.etree.ElementTree as ET

NS = '{http://www.w3.org/1999/xhtml}'


def load(path):
    s = open(path, encoding='utf-8').read()
    s = re.sub(r'<\?xml[^>]*\?>', '', s)
    s = re.sub(r'<!DOCTYPE[^>]*>', '', s, flags=re.S)
    s = re.sub(r'&(?!amp;|lt;|gt;|quot;|apos;|#)(\w+);', lambda m: html.unescape(m.group(0)), s)
    return ET.fromstring(s.encode('utf-8'))


def tag(el):
    return el.tag.replace(NS, '')


def esc(t):
    # keep text literal in Markdown: escape < > only
    return t.replace('<', '&lt;').replace('>', '&gt;').replace('[', '\\[').replace(']', '\\]')


def inline(el, links='text', sup=None):
    """Render inline content of el to Markdown. sup: callback(text) -> str for <sup>."""
    parts = []

    def walk(e, em):
        t = tag(e)
        if t == 'br':
            parts.append(('br', ''))
        elif t == 'sup' and sup:
            parts.append(('raw', sup(''.join(e.itertext()))))
        else:
            is_em = em or t in ('em', 'i')
            if e.text:
                parts.append(('em' if is_em else 'txt', e.text))
            for c in e:
                walk(c, is_em)
                if c.tail:
                    parts.append(('em' if is_em else 'txt', c.tail))

    walk(el, False)
    # merge runs
    runs = []
    for k, v in parts:
        if k in ('txt', 'em'):
            v = re.sub(r'\s+', ' ', v)
        if runs and runs[-1][0] == k and k in ('txt', 'em'):
            runs[-1][1] += v
        else:
            runs.append([k, v])
    out = ''
    for k, v in runs:
        if k == 'txt':
            out += esc(v)
        elif k == 'em':
            if not v.strip():
                out += v
                continue
            lead = v[:len(v) - len(v.lstrip())]
            trail = v[len(v.rstrip()):]
            out += lead + '*' + esc(v.strip()) + '*' + trail
        elif k == 'br':
            out += '\n'
        else:
            out += v
    out = re.sub(r'[ \t]+', ' ', out)
    out = re.sub(r' *\n *', '\n', out)
    return out.strip()


def words(s):
    """Normalised word list for comparisons."""
    s = html.unescape(s)
    s = s.replace(' ', ' ').replace(' ', ' ').replace(' ', ' ')
    s = re.sub(r'\[\^[^\]]+\](:)?', ' ', s)          # footnote refs/defs
    s = re.sub(r'<[^>]+>', ' ', s)                    # html tags
    s = re.sub(r'\\(?=[^\w\s])', '', s)
    s = re.sub(r'[*_#>\\]', ' ', s)
    s = s.translate(str.maketrans({'‘': "'", '’': "'", '“': '"', '”': '"',
                                   '—': ' ', '–': '-', '…': '...'}))
    return s.split()
