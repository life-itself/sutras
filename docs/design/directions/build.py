#!/usr/bin/env python3
"""Build the three sample sites (directions A, B, C) from snapshots of the live reading pages.

Usage: python3 docs/design/directions/build.py            -> docs/design/directions/out/{a,b,c}/*.html + img/
       python3 docs/design/directions/build.py a          -> one direction

Each page is the live page's .rs block (dom/*.html, captured from sutras.lifeitself.org after its scripts ran,
so verse lines, stanza numbers and margin notes are the real ones) with: the site's css/reading.css,
css/notes.css and the .rs parts of custom.css inlined; base.css and the direction's css on top; a minimal
nav and footer; one open-licence image per text above the title; the home page rebuilt as a shelf.
Nothing here edits the live site. The chosen direction's CSS is what gets applied to custom.css later.
"""
import pathlib, re, shutil, sys

here = pathlib.Path(__file__).parent
root = here.parents[2]  # repo root
out_root = here / "out"
which = sys.argv[1:] or ["a", "b", "c"]

reading_css = (root / "css/reading.css").read_text()
notes_css = (root / "css/notes.css").read_text()
custom_css = (root / "custom.css").read_text()
custom_css = re.sub(r'@import[^\n]*\n', '', custom_css)  # fonts and reading.css are loaded here instead
base_css = (here / "base.css").read_text()

FONTS = {
    "a": "Literata:ital,opsz,wght@0,7..72,400;0,7..72,500;1,7..72,400&family=Instrument+Sans:wght@400;500&family=Ma+Shan+Zheng&family=Noto+Serif+TC:wght@400;600",
    "b": "Spectral:ital,wght@0,300;0,400;0,500;1,300;1,400&family=Instrument+Sans:wght@400;500&family=Noto+Serif+TC:wght@400;600",
    "c": "Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&family=Instrument+Sans:wght@400;500&family=Noto+Serif+TC:wght@400;600",
}
NAMES = {"a": "A · Warm red", "b": "B · Blue", "c": "C · Gold on indigo"}
MARK = "慧"  # the character for wisdom (hui, prajñā); an option, not a decision

# one open-licence image per text, and the label above the title
ART = {
    "fim": ("img/sesshu.jpg", "Sesshū Tōyō, Haboku Sansui, 1495. Tokyo National Museum, public domain", "Zen · a poem"),
    "seneca": ("img/aldus.jpg", "A page from Aldus Manutius’s Virgil, Venice 1501: the pocket editions the Roman authors were read in. Public domain", "Stoicism · an essay"),
    "about": (None, None, "About"),
}
SHELF = [  # slug, image, label on the shelf
    ("faith-in-mind", "img/sesshu-sq.jpg"), ("shodoka", "img/sengai.jpg"), ("gateless-gate-mumonkan", "img/hakuin.jpg"),
    ("diamond", "img/diamond.jpg"), ("diamond-red-pine", "img/jingoji-sq.jpg"), ("dhammapada", "img/song.jpg"),
    ("seneca-on-the-shortness-of-life", "img/aldus.jpg"), ("meditations", "img/xylander.jpg"),
]
LOCAL = {"faith-in-mind": "faith-in-mind.html", "seneca-on-the-shortness-of-life": "seneca.html"}

def page(d, key, title, body, home=False):
    css = reading_css + "\n" + notes_css + "\n" + custom_css + "\n" + base_css + "\n" + (here / f"{d}.css").read_text()
    cur = {"home": "index.html", "fim": "faith-in-mind.html", "seneca": "seneca.html", "about": "about.html"}[key]
    def nav_a(href, label):
        current = ' aria-current="page"' if href == cur else ''
        return f'<a href="{href}"{current}>{label}</a>'
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title if title != "Sutras" else "Sutras"} · sample site {NAMES[d]}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family={FONTS[d]}&display=swap">
<style>{css}</style>
</head><body class="{'sd-home' if home else ''}">
<nav class="sd-nav"><a class="sd-brand" href="index.html"><span class="sd-mark" aria-hidden="true">{MARK}</span><span class="sd-word">Sutras</span></a><span class="sd-links">{nav_a('index.html', 'Texts')}{nav_a('about.html', 'About')}</span></nav>
{body}
<footer class="sd-foot"><span>Sutras · a library of wisdom texts</span><a href="https://lifeitself.org">Life Itself</a><a href="https://github.com/life-itself/sutras/issues">Report a mistake</a><span>Sample site, direction {NAMES[d]}, {MARK} is a mark option</span></footer>
</body></html>"""

def relink(html):
    """Links to the live site's pages: local where this sample has the page, absolute otherwise."""
    def sub(m):
        slug = m.group(1)
        return f'href="{LOCAL[slug]}"' if slug in LOCAL else f'href="https://sutras.lifeitself.org/{slug}"'
    html = re.sub(r'href="/([a-z0-9-]+)"', sub, html)
    html = html.replace('href="/"', 'href="index.html"')
    return html

def with_art(html, key, d):
    img, credit, label = ART[key]
    art = f'<figure class="sd-art"><img src="{img}" alt=""><figcaption>{credit}</figcaption></figure>' if img else ""
    # the kicker says what kind of text this is, not the site name (the nav says that)
    html = re.sub(r'<a class="rs-kicker" href="[^"]*">Sutras</a>', f'<span class="rs-kicker">{label}</span>', html, count=1)
    head = re.search(r'<header class="rs-head">.*?</header>', html, re.S)
    front = f'<div class="sd-front">{art}{head.group(0)}</div>'
    return html.replace(head.group(0), front, 1)

def home(html, d):
    """Rebuild the home list as a shelf: one image per text, title, author line."""
    inbrief = re.search(r'<p class="rs-inbrief">.*?</p>', html, re.S).group(0)
    inbrief = re.sub(r'<span class="rs-inbrief-label">.*?</span>\s*', '', inbrief)
    items = []
    for chunk in re.split(r'<h3[^>]*>', html)[1:]:
        m = re.search(r'<a href="/([a-z0-9-]+)"[^>]*>(.*?)</a>', chunk, re.S)
        if not m: continue
        slug, title = m.group(1), re.sub(r'<[^>]+>', '', m.group(2)).strip()
        by = re.search(r'<p class="rs-quiet">(.*?)</p>', chunk, re.S)
        line = re.search(r'</p>\s*<p>(.*?)</p>', chunk, re.S)
        by = by.group(1) if by else ""
        line = line.group(1) if line else ""
        img = dict(SHELF).get(slug, "img/moonjar.jpg")
        href = LOCAL.get(slug, f"https://sutras.lifeitself.org/{slug}")
        items.append(f'<li><a href="{href}"><img class="sd-thumb" src="{img}" alt=""><h3>{title}</h3><span class="sd-by">{by}</span><span class="sd-line">{line}</span></a></li>')
    sections = re.findall(r'<h2[^>]*>(.*?)</h2>', html, re.S)
    sections = [re.sub(r'<[^>]+>', '', s).strip() for s in sections]
    body = f'''<div class="rs" data-rs-theme="personal" data-rs-rail="off" data-rs-dropcap="off">
<div class="sd-front"><header class="rs-head"><div class="rs-wrap"><div class="rs-head-text">
<span class="rs-kicker">A library of wisdom texts</span><h1>Sutras</h1>
{inbrief}
</div></div></header></div>
<div class="rs-body"><div class="rs-wrap"><article class="rs-text">
<ul class="sd-shelf">{''.join(items)}</ul>
</article></div></div></div>'''
    return body

for d in which:
    out = out_root / d
    out.mkdir(parents=True, exist_ok=True)
    if (out / "img").exists(): shutil.rmtree(out / "img")
    shutil.copytree(here / "img", out / "img")
    dom = {k: (here / "dom" / f"{k}.html").read_text() for k in ("home", "fim", "seneca", "about")}
    (out / "index.html").write_text(page(d, "home", "Sutras", home(dom["home"], d), home=True))
    (out / "faith-in-mind.html").write_text(page(d, "fim", "Faith in Mind", relink(with_art(dom["fim"], "fim", d))))
    (out / "seneca.html").write_text(page(d, "seneca", "On the Shortness of Life", relink(with_art(dom["seneca"], "seneca", d))))
    (out / "about.html").write_text(page(d, "about", "About", relink(with_art(dom["about"], "about", d))))
    print(d, [p.name for p in out.glob("*.html")])
