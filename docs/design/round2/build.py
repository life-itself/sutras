#!/usr/bin/env python3
"""Sutras round 2 sample site (2026-11-21): the Red Pine direction in the Seeds of Renaissance faces.

Rufus, after the two Red Pine copies: "i think i want to go with seeds of renaissance approach… it's quite
elaborate… maybe we want just a simplified version when we just have text… side notes… a three-column version
[original, translation, commentary]… some elegant table of contents… a bit like LessWrong… good to see more of
the site."

Pages, from the live Markdown:
  index.html          home: the picture, the name, a teaching's first lines, the shelf
  faith-in-mind.html  the feature register (../redpine/build.py, Seeds faces)
  seneca.html         the reading register: contents rail, the text, notes in the margin
  mumonkan.html       the parallel register: Chinese | English | notes (preface and cases 1-7)

  python3 docs/design/round2/build.py   -> docs/design/round2/out/ (not committed; publish index.html with the rest as files)
Fonts: Polyamine and Restora are licensed to Seeds of Renaissance and are copied from ~/src/life-itself/sor-website
into out/ for the private mockup only.
"""
import html, json, pathlib, re, shutil, subprocess, sys
from bs4 import BeautifulSoup
from PIL import Image, ImageOps

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OUT = HERE / "out"
SOR = pathlib.Path.home() / "src/life-itself/sor-website/public/fonts"
PAPER = (236, 233, 228)
SLATE, CORAL = (70, 100, 122), (226, 98, 72)

GOOGLE = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
          '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,300..700&family=Noto+Serif+TC:wght@300;400&display=swap">')


def top(here):
    links = [("index.html", "Library"), ("seneca.html", "Reading"), ("mumonkan.html", "Parallel"), ("faith-in-mind.html", "Feature")]
    nav = "".join('<a href="%s"%s>%s</a>' % (h, ' aria-current="page"' if h == here else "", t) for h, t in links)
    return '<header class="top"><a href="index.html"><span class="mark" lang="zh-Hant">慧</span><span class="name">Sutras</span></a><nav>%s</nav></header>' % nav


FOOT = '<footer class="foot"><span>Sutras · a library of wisdom texts · Life Itself</span><span>Round 2 sample · Seeds of Renaissance faces · not the live site</span></footer>'


def doc(title, body, here, main=False):
    head = '<title>%s</title><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">%s<link rel="stylesheet" href="site.css">' % (title, GOOGLE)
    page = head + top(here) + body + FOOT + '<script src="toc.js"></script>'
    if main:  # the artifact's own page is wrapped by the publisher
        return page
    return '<!doctype html><html lang="en"><head><meta charset="utf-8">%s</head><body>%s</body></html>' % (head, top(here) + body + FOOT + '<script src="toc.js"></script>')


# ---------- images: every picture toned in one of the two inks ----------
def tone(src, dest, ink, crop=None, cut=176, gamma=1.35, width=1000):
    im = Image.open(src).convert("L")
    if crop:
        w, h = im.size
        im = im.crop((int(crop[0] * w), int(crop[1] * h), int(crop[2] * w), int(crop[3] * h)))
    im = ImageOps.autocontrast(im, cutoff=(1, 0.5))
    hist = im.histogram(); total = sum(hist); acc = 0
    for level, count in enumerate(hist):  # the paper: the level below which 60% of pixels fall, less a margin
        acc += count
        if acc >= total * 0.6: break
    cut = min(cut, max(120, int(level * 0.93)))
    im = im.point(lambda v: 255 if v > cut else int(255 * (v / cut) ** gamma))
    im = ImageOps.colorize(im, black=ink, white=(255, 255, 255))  # white, so multiply leaves the page's own paper
    if im.width > width:
        im = im.resize((width, int(im.height * width / im.width)), Image.LANCZOS)
    im.save(dest, quality=74, optimize=True, progressive=True)


SHELF = [  # slug, page in this sample (or None), ink
    ("faith-in-mind", "faith-in-mind.html", CORAL), ("shodoka", None, SLATE), ("gateless-gate-mumonkan", "mumonkan.html", CORAL),
    ("diamond", None, SLATE), ("diamond-red-pine", None, CORAL), ("dhammapada", None, SLATE),
    ("tao-te-ching", None, CORAL), ("seneca-on-the-shortness-of-life", "seneca.html", SLATE), ("meditations", None, CORAL),
]


def images():
    (OUT / "img").mkdir(parents=True, exist_ok=True)
    for slug, _, ink in SHELF:
        tone(ROOT / "assets/images" / (slug + ".jpg"), OUT / "img" / (slug + ".jpg"), ink, width=700)
    tone(pathlib.Path.home() / "src/life-itself/sutras/docs/design/redpine/img/hero-coral.jpg" if False else HERE.parent / "redpine/img/hero-coral.jpg", OUT / "img/hero-coral.jpg", CORAL, cut=200, gamma=1.0, width=1100)
    tone(ROOT / "assets/images/seneca-on-the-shortness-of-life.jpg", OUT / "img/seneca-head.jpg", SLATE, cut=170, width=900)
    tone(ROOT / "assets/images/gateless-gate-mumonkan.jpg", OUT / "img/mumonkan-head.jpg", CORAL, cut=190, gamma=1.1, width=900)


# ---------- Markdown to HTML, notes into the margin ----------
def front_and_body(slug):
    md = (ROOT / (slug + ".md")).read_text()
    fm, body = re.match(r"---\n(.*?)\n---\n(.*)", md, re.S).groups()
    return fm, body


def pandoc(md):
    return subprocess.run(["pandoc", "-f", "markdown+smart-raw_attribute", "-t", "html5", "--wrap=none"], input=md, capture_output=True, text=True, check=True).stdout


def sidenotes(soup):
    """Footnotes become Tufte-style margin notes: a number in the text, the note floated into the right rail."""
    notes = {}
    sec = soup.find("section", class_="footnotes")
    if sec:
        for li in sec.find_all("li"):
            for back in li.find_all("a", class_="footnote-back"):
                back.decompose()
            inner = "".join(str(c) for c in li.children).strip()
            inner = re.sub(r"</?p>", " ", inner).strip()
            inner = inner.replace("<em>Editors’ note.</em> ", "").replace("<em>Editors' note.</em> ", "")
            notes[li["id"]] = inner
        sec.decompose()
    n = 0
    for ref in soup.find_all("a", class_="footnote-ref"):
        n += 1
        fid = ref["href"][1:]
        label = ref.get_text()
        new = BeautifulSoup('<label for="sn-%s" class="snr">%s</label><input type="checkbox" id="sn-%s" class="snt"><span class="sn"><b>%s</b>%s</span>'
                            % (fid, label, fid, label, notes.get(fid, "")), "html.parser")
        ref.replace_with(new)
    return soup


def editor_notes(htmltext, slug):
    """The editors' highlights (js/notes/<slug>.js): the passage underlined in coral, the note in the margin."""
    js = (ROOT / "js/notes" / (slug + ".js")).read_text()
    data = json.loads(re.search(r"=\s*(\{.*\})\s*;?\s*$", js, re.S).group(1))
    for i, note in enumerate(data["notes"]):
        q = note["quote"]
        body = note.get("note") or ""
        if q not in htmltext:
            continue
        if not body:
            htmltext = htmltext.replace(q, '<mark class="hl">%s</mark>' % q, 1)
            continue
        mark = '<mark class="hl">%s</mark><label for="ed-%d" class="snr">✦</label><input type="checkbox" id="ed-%d" class="snt"><span class="sn ed">%s<span class="by">%s</span></span>' % (
            q, i, i, body, note.get("by", "Editors"))
        htmltext = htmltext.replace(q, mark, 1)
    return htmltext


def toc_html(items, title):
    lis = "".join('<li class="%s"><a href="#%s">%s</a></li>' % (c, i, t) for i, t, c in items)
    rail = '<aside class="toc" aria-label="Contents"><p>%s</p><ol>%s</ol></aside>' % (title, lis)
    phone = '<details class="toc-phone"><summary>Contents</summary><ol>%s</ol></details>' % lis
    return rail, phone


# ---------- the reading register: Seneca ----------
def seneca():
    fm, body = front_and_body("seneca-on-the-shortness-of-life")
    art = re.search(r'<article class="rs-text">\n(.*)</article>', body, re.S).group(1)
    inbrief = re.search(r'<p class="rs-inbrief"><span class="rs-inbrief-label">In brief</span>\s*(.*?)</p>', art, re.S).group(1)
    art = re.sub(r'<p class="rs-inbrief">.*?</p>', "", art, flags=re.S)
    art = re.sub(r"\n## Download.*", "", art, flags=re.S) if "## Download" in art else art
    notes_tail = body[body.find("[^1]:"):] if "[^1]:" in body else ""
    h = pandoc(art + "\n\n" + notes_tail)
    soup = sidenotes(BeautifulSoup(h, "html.parser"))
    # sections: h2 ids, roman chapters as h3 with ids already
    items = []
    for el in soup.find_all(["h2", "h3"]):
        if el.name == "h2":
            if not el.get("id"):
                el["id"] = re.sub(r"[^a-z]+", "-", el.get_text().lower()).strip("-")
            items.append((el["id"], el.get_text(), ""))
        elif el.get("id", "").isdigit():
            nxt = el.find_next("p")
            plain = BeautifulSoup(str(nxt), "html.parser") if nxt else None
            if plain:
                for x in plain.select(".snr, .sn, .snt"): x.decompose()
            words = " ".join(re.sub(r"\s+", " ", plain.get_text()).split(" ")[:5]).rstrip(",;:.") if plain else ""
            items.append((el["id"], "%s · %s…" % (el.get_text(), words), "sub"))
    text = editor_notes(str(soup), "seneca-on-the-shortness-of-life")
    rail, phone = toc_html(items, "On the Shortness of Life")
    head = f"""<section class="head"><div class="art"><img src="img/seneca-head.jpg" alt="A page of italic type from Aldus Manutius's Virgil, Venice 1501."></div>
<p class="label">Stoicism · an essay</p>
<h1>On the Shortness of Life</h1><p class="by">Seneca</p></section>
<p class="stand">{inbrief}<span class="meta">Translated by John W. Basore, 1932 · about an hour · notes in the margin</span></p>
<div class="thread"></div>"""
    page = head + '<main class="page">%s<article class="text">%s%s</article></main>' % (rail, phone, text)
    return doc("On the Shortness of Life", page, "seneca.html")


# ---------- the parallel register: Mumonkan ----------
def mumonkan(last_case=7):
    fm, body = front_and_body("gateless-gate-mumonkan")
    art = re.search(r'<article class="rs-text">\n(.*)</article>', body, re.S).group(1)
    inbrief = re.search(r'<p class="rs-inbrief"><span class="rs-inbrief-label">In brief</span>\s*(.*?)</p>', art, re.S).group(1)
    titles = re.findall(r'<li><a href="#(\d+)">(.*?)</a></li>', art)
    intro = re.search(r"## Introduction\n\n(.*?)\n(?=<details|## |<h3)", art, re.S)
    intro = intro.group(1) if intro else ""
    start = art.find('<h3 class="koan-title" id="preface">')
    end = art.find('<h3 class="koan-title" id="%d">' % (last_case + 1))
    cases = art[start:end]
    notes_tail = "\n\n".join(re.findall(r"^\[\^[a-z]+\]:.*$", body, re.M))
    h = pandoc(cases + "\n\n" + notes_tail)
    soup = sidenotes(BeautifulSoup(h, "html.parser"))
    out = []
    for el in soup.find_all(recursive=False):
        out.append(el)
    parts = []

    def pairs(container, verse=False):
        """Within a case's part: each English paragraph with the Chinese that follows it."""
        res, en = [], None
        for el in container.find_all(recursive=False):
            if el.name == "p" and "koan-label" in (el.get("class") or []):
                lab = el.decode_contents()
                res.append('<p class="part">%s</p>' % lab)
            elif el.name == "p" and "orig" in (el.get("class") or []):
                zh = str(el).replace(' class="orig"', "")
                res.append('<div class="pair%s"><div class="zh" lang="zh-Hant">%s</div><div class="en">%s</div></div>' % (" verse" if verse else "", zh, en or ""))
                en = None
            else:
                if en:
                    res.append('<div class="pair solo"><div class="en">%s</div></div>' % en)
                en = str(el)
        if en:
            res.append('<div class="pair solo"><div class="en">%s</div></div>' % en)
        return "".join(res)

    items = [("introduction", "Introduction", "")]
    for el in out:
        if el.name == "h3":
            cid = el["id"]
            num = el.find("span", class_="koan-num")
            zh = el.find("span", class_="koan-title-zh")
            ztext = zh.get_text().split("　")[-1] if zh else ""
            if num: num.extract()
            if zh: zh.extract()
            title = el.decode_contents().strip()
            n = num.get_text().replace("Case ", "") if num else ""
            parts.append('<div class="case-head" id="%s"><div class="zh-title" lang="zh-Hant">%s</div><div>%s<h3>%s</h3></div></div>' % (
                cid, ztext, '<span class="n">%s</span>' % n if n else "", title))
            items.append((cid, ("%s. " % n if n else "") + re.sub("<.*?>", "", title), "sub" if n else ""))
        elif el.name == "div":
            cls = el.get("class") or []
            parts.append(pairs(el, verse="koan-verse" in cls))
        elif el.name == "p" and "orig" in (el.get("class") or []):
            parts.append('<div class="pair"><div class="zh" lang="zh-Hant">%s</div><div class="en"></div></div>' % el.decode_contents())
        elif el.name == "p":
            parts.append('<div class="pair solo"><div class="en">%s</div></div>' % str(el))
        else:
            parts.append(str(el))
    seen = {i for i, _, _ in items}
    for n, t in titles:
        if n not in seen:
            pass
    items.append(("rest", "Cases %d to 48 on the full page" % (last_case + 1), "sub off"))
    body_html = editor_notes("".join(parts), "gateless-gate-mumonkan")
    intro_html = str(sidenotes(BeautifulSoup(pandoc(intro), "html.parser")))
    rail, phone = toc_html(items, "The Gateless Gate")
    head = f"""<section class="head"><div class="art"><img src="img/mumonkan-head.jpg" alt="Hakuin's brushed character for virtue, a single large character."></div>
<p class="label">Zen · koans</p>
<h1>The Gateless Gate</h1><p class="by">Wumen Huikai</p><p class="orig" lang="zh-Hant">無門關</p></section>
<p class="stand">{inbrief}<span class="meta">Translated by Katsuki Sekida · with the Chinese of 1228 · this sample has the preface and cases 1 to {last_case}</span></p>
<div class="thread"></div>"""
    legend = '<div class="par-legend"><span class="label">The Chinese, 1228</span><span class="label">Katsuki Sekida’s translation</span></div>'
    text = '%s<h2 id="introduction">Introduction</h2><div class="wide">%s</div><hr>%s%s<p class="small wide" style="margin-top:80px">Cases %d to 48 continue on the full page.</p>' % (phone, intro_html, legend, body_html, last_case + 1)
    page = head + '<main class="page par">%s<article class="text">%s</article></main>' % (rail, text)
    return doc("The Gateless Gate", page, "mumonkan.html")


# ---------- home ----------
def home():
    md = (ROOT / "README.md").read_text()
    entries = re.findall(r'<li><a href="/([^"]+)"><img[^>]*><h3>(.*?)</h3><span class="sd-kind">(.*?)</span><span class="rs-quiet">(.*?)</span><span class="sd-line">(.*?)</span></a></li>', md)
    pages = {s: p for s, p, _ in SHELF}
    lis = []
    for slug, title, kind, quiet, line in entries:
        who = quiet.split(" · ")[0]
        href = pages.get(slug)
        tag = 'a href="%s"' % href if href else 'a href="#" class="soon" title="Not in this sample"'
        lis.append('<li><%s><span class="pic"><img src="img/%s.jpg" alt=""></span><span class="kind">%s</span><h3>%s</h3><p class="who">%s</p><p class="line">%s</p></a></li>' % (tag, slug, kind, title, who, line))
    body = f"""<section class="home-hero"><div><div class="art"><img src="img/hero-coral.jpg" alt="Sesshū's splashed-ink landscape, toned coral."></div>
<h1>Sutras</h1><p class="tag">texts worth reading slowly</p></div></section>
<section class="opening"><p class="lines"><span>There is the leisurely one,</span><span>Walking the Tao, beyond philosophy,</span></p><p class="src">The first lines of the Shodoka, a Zen song</p></section>
<p class="intro">A small library of texts worth reading slowly, from Zen poems to the Stoics. Each is here complete and free, with a link to every passage and an EPUB; most have notes in the margin.</p>
<ul class="shelf">{''.join(lis)}</ul>
<p class="colophon">Made by Rufus Pollock, with AI assistants, as part of Life Itself. In this sample, three texts open: <a href="faith-in-mind.html">Faith in Mind</a> as a feature, <a href="seneca.html">Seneca</a> as a plain reading page, and <a href="mumonkan.html">the Gateless Gate</a> with its Chinese beside the translation.</p>"""
    return doc("Sutras Round Two", body, "index.html", main=True)


# ---------- the feature page: the Red Pine copy in Seeds faces, given the site line ----------
def feature():
    sys.path.insert(0, str(HERE.parent / "redpine"))
    import importlib
    rp = importlib.import_module("build")
    rp.build("seeds")
    page = (HERE.parent / "redpine/out/seeds.html").read_text()
    page = page.replace('<nav class="top"><a href="#">', '<nav class="top"><a href="index.html">').replace('<a href="#">Library</a>', '<a href="index.html">Library</a>')
    title = re.search(r"<title>.*?</title>", page).group(0)
    return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">%s</head><body>%s</body></html>' % (
        title.replace("Faith in Mind, Seeds Faces", "Faith in Mind"), page.replace(title, ""))


def main():
    OUT.mkdir(exist_ok=True)
    (OUT / "fonts").mkdir(exist_ok=True)
    for f in ["Polyamine-Regular.woff2", "Restora-ExtraLight.woff2", "Restora-ThinItalic.woff2", "ApfelGrotezk-Regular.otf", "ApfelGrotezk-Mittel.otf"]:
        shutil.copy(SOR / f, OUT / "fonts" / f)
    shutil.copy(HERE / "site.css", OUT / "site.css")
    shutil.copy(HERE / "toc.js", OUT / "toc.js")
    images()
    (OUT / "index.html").write_text(home())
    (OUT / "seneca.html").write_text(seneca())
    (OUT / "mumonkan.html").write_text(mumonkan())
    (OUT / "faith-in-mind.html").write_text(feature())
    for p in sorted(OUT.rglob("*")):
        if p.is_file(): print(p.relative_to(OUT), p.stat().st_size // 1024, "KB")


if __name__ == "__main__":
    main()
