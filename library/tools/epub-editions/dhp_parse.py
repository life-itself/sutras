import re, html
import xml.etree.ElementTree as ET

NS = '{http://www.w3.org/1999/xhtml}'
BASE = None


def load(path):
    s = open(BASE + '/' + path, encoding='utf-8').read()
    s = re.sub(r'<!DOCTYPE[^>]*>', '', s, flags=re.S)
    s = re.sub(r'&(?!amp;|lt;|gt;|quot;|apos;)(\w+);', lambda m: html.unescape(m.group(0)), s)
    return ET.fromstring(s.encode('utf-8'))


def text(el):
    return ''.join(el.itertext())


def chapters():
    """Return list of (title, groups); group = {label, href, divs:[{id, lines:[(cls, el)]}]}."""
    out = []
    for n in range(6, 32):
        root = load('Text/Section%04d.xhtml' % n)
        h1 = root.find('.//' + NS + 'h1')
        title = text(h1).strip()
        groups = []
        cur = []
        for div in root.iter(NS + 'div'):
            if div.get('class') != 'verse':
                continue
            lines = []
            label = href = None
            for p in div:
                if p.tag != NS + 'p':
                    raise Exception('non-p in verse: %s %s' % (p.tag, title))
                cls = p.get('class') or ''
                if cls == 'cite':
                    label = text(p).strip()
                    a = p.find(NS + 'a')
                    href = a.get('href') if a is not None else None
                else:
                    lines.append((cls, p))
            cur.append({'id': div.get('id'), 'lines': lines})
            if label:
                groups.append({'label': label, 'href': href, 'divs': cur})
                cur = []
        if cur:
            raise Exception('trailing divs in ' + title)
        out.append((title, groups))
    return out


def rng(label):
    a, _, b = label.partition('-')
    return int(a), int(b or a)
