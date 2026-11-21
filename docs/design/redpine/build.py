#!/usr/bin/env python3
"""Round 2 (2026-11-21): Faith in Mind set as near-copies of Emergence Magazine's Red Pine poem page.

Two variants, same layout and colour, different faces:
  open   the Red Pine page's faces swapped for open-licence ones (Archivo Expanded for GT America Extended,
         Fraunces for Ogg, Archivo for GT America, Newsreader for Reckless)
  seeds  the Seeds of Renaissance faces (Polyamine, Restora, Bricolage Grotesque, Apfel Grotezk). Polyamine
         and Restora are licensed to Seeds of Renaissance; they are read from ~/src/life-itself/sor-website at
         build time and inlined into the private mockup only. Not for the live site without a licence check.

Words: faith-in-mind.md as live (In brief, Introduction, the poem, the notes, About this translation's first
paragraph, credits). Chinese: the 信心銘 from zh.wikisource (景德傳燈錄 卷30), 146 phrases matching the
translation's 146 lines one for one; chinese.txt, one phrase per line.

  python3 docs/design/redpine/build.py            -> docs/design/redpine/out/{open,seeds}.html
"""
import base64, re, html, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SOR = pathlib.Path.home() / "src/life-itself/sor-website/public/fonts"
OUT = HERE / "out"


def b64(path, mime):
    return "data:%s;base64,%s" % (mime, base64.b64encode(pathlib.Path(path).read_bytes()).decode())


def inline(s):
    """The little Markdown the page uses: *italic*, [text](url), [^n] notes, typographic apostrophes kept."""
    s = re.sub(r"\[\^(\d+)\]", lambda m: '<sup class="nm"><a href="#n%s">%s</a></sup>' % (m.group(1), m.group(1)), s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"\*([^*]+)\*", r"<i>\1</i>", s)
    return s


def parse():
    md = (ROOT / "faith-in-mind.md").read_text()
    inbrief = re.search(r'<span class="rs-inbrief-label">In brief</span>\s*(.*?)</p>', md).group(1)
    intro = re.search(r"## Introduction\n\n(.*?)\n## The poem", md, re.S).group(1).strip().split("\n\n")
    verse = re.search(r'<div class="rs-verse">\n(.*?)\n</div>', md, re.S).group(1)
    stanzas = []
    for block in re.split(r'\n(?=<a class="v")', verse.strip()):
        n = re.match(r'<a class="v" id="(\d+)"', block).group(1)
        lines = [l.rstrip() for l in block.split("\n")[1:] if l.strip()]
        stanzas.append((int(n), lines))
    about = re.search(r"## About this translation\n\n(.*?)\n\n", md, re.S).group(1)
    notes = dict(re.findall(r"^\[\^(\d+)\]: (.*)$", md, re.M))
    return inbrief, intro, stanzas, about, notes


def chinese(stanzas):
    zh = [l.strip() for l in (HERE / "chinese.txt").read_text().split("\n") if l.strip()]
    assert len(zh) == sum(len(l) for _, l in stanzas) == 146, len(zh)
    out, i = [], 0
    for _, lines in stanzas:
        out.append(zh[i:i + len(lines)]); i += len(lines)
    return out


FACES = {
    "open": {
        "title": "Faith in Mind, Open Faces",
        "head": '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
                '<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&family=Fraunces:ital,opsz,wght@0,9..144,100..700;1,9..144,100..700'
                '&family=Newsreader:ital,opsz,wght@0,6..72,300..600;1,6..72,300..600&family=Noto+Serif+TC:wght@300;400&display=swap" rel="stylesheet">',
        "css": """
:root{--f-title:"Archivo",system-ui,sans-serif;--title-stretch:125%;--title-weight:600;--title-track:-.035em;
--f-display:"Fraunces",Georgia,serif;--display-weight:300;--display-style:normal;--display-vs:"opsz" 144,"SOFT" 0,"WONK" 0;
--f-body:"Archivo",system-ui,sans-serif;--body-weight:400;
--f-label:"Archivo",system-ui,sans-serif;--label-stretch:72%;--label-weight:500;
--f-poem:"Newsreader",Georgia,serif;--poem-weight:400;--poem-style:normal;--poem-size:19px;--poem-vs:"opsz" 16;
--f-num:"Fraunces",Georgia,serif;--num-weight:320;--num-vs:"opsz" 144}
""",
        "faces": "Archivo Expanded (for GT America Extended) · Fraunces (for Ogg) · Archivo (for GT America) · Newsreader (for Reckless) · Noto Serif TC",
    },
    "seeds": {
        "title": "Faith in Mind, Seeds Faces",
        "head": '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
                '<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,300..700&family=Noto+Serif+TC:wght@300;400&display=swap" rel="stylesheet">',
        "css": None,  # filled in build(): @font-face for the licensed faces
        "faces": "Polyamine (titles) · Restora (the display line, the poem, numerals) · Bricolage Grotesque (reading) · Apfel Grotezk (labels) · Noto Serif TC",
    },
}


def seeds_css():
    ff = lambda fam, f, mime, fmt, extra="": '@font-face{font-family:"%s";%ssrc:url(%s) format("%s");font-display:swap}' % (fam, extra, b64(SOR / f, mime), fmt)
    return "\n".join([
        ff("Polyamine", "Polyamine-Regular.woff2", "font/woff2", "woff2", "font-weight:400;"),
        ff("Restora", "Restora-ExtraLight.woff2", "font/woff2", "woff2", "font-weight:100 900;font-style:normal;"),
        ff("Restora", "Restora-ThinItalic.woff2", "font/woff2", "woff2", "font-weight:100 900;font-style:italic;"),
        ff("Apfel Grotezk", "ApfelGrotezk-Regular.otf", "font/otf", "opentype", "font-weight:400;"),
        ff("Apfel Grotezk", "ApfelGrotezk-Mittel.otf", "font/otf", "opentype", "font-weight:500;"),
    ]) + """
:root{--f-title:"Polyamine",Georgia,serif;--title-stretch:100%;--title-weight:400;--title-track:-.01em;
--f-display:"Restora",Georgia,serif;--display-weight:300;--display-style:normal;--display-vs:normal;
--f-body:"Bricolage Grotesque",system-ui,sans-serif;--body-weight:400;
--f-label:"Apfel Grotezk",system-ui,sans-serif;--label-stretch:100%;--label-weight:500;
--f-poem:"Restora",Georgia,serif;--poem-weight:430;--poem-style:normal;--poem-size:20px;--poem-vs:normal;
--f-num:"Restora",Georgia,serif;--num-weight:300;--num-vs:normal}
html .title .by{font-size:clamp(24px,3.6vw,48px)}
"""


CSS = """
:root{--paper:#ece9e4;--slate:#5a7a8f;--ink:#46657a;--soft:#8aa0ae;--coral:#ee8a70;--hair:#e7b8a6;--hair2:#b9c6cf;color-scheme:light}
*{box-sizing:border-box}
html,body{margin:0;background:var(--paper);color:var(--ink)}
body{font-family:var(--f-body);font-weight:var(--body-weight);-webkit-font-smoothing:antialiased;overflow-x:hidden}
a{color:inherit;text-decoration-thickness:1px;text-underline-offset:.2em;text-decoration-color:var(--hair)}
a:hover{text-decoration-color:var(--coral)}
.label{font-family:var(--f-label);font-stretch:var(--label-stretch);font-weight:var(--label-weight);text-transform:uppercase;letter-spacing:.07em;font-size:15px;color:var(--slate)}

/* the site's own line: the name, small, and the way back */
.top{position:absolute;inset:0 0 auto 0;display:flex;justify-content:space-between;align-items:center;padding:18px 24px;z-index:3}
.top a{text-decoration:none;font-family:var(--f-body);font-size:15px;color:var(--slate)}
.top .mark{font-family:"Noto Serif TC",serif;font-size:17px;margin-right:.45em;color:var(--coral)}

/* opening: the picture alone on the paper, a coral sun across it, the kind of text beneath */
.hero{min-height:100svh;display:grid;grid-template-rows:1fr auto;justify-items:center;padding:80px 20px 28px}
.hero .art{position:relative;align-self:center;width:min(64vw,760px)}
.hero .art img{display:block;width:100%;height:auto;max-height:76svh;object-fit:contain;mix-blend-mode:multiply}
.hero .art .band{position:absolute;inset:0;-webkit-mask-image:linear-gradient(180deg,transparent 22%,#000 30%,#000 40%,transparent 47%);mask-image:linear-gradient(180deg,transparent 22%,#000 30%,#000 40%,transparent 47%)}
.hero .sun{position:absolute;width:23%;aspect-ratio:1;border-radius:50%;background:var(--coral);mix-blend-mode:multiply;right:-6%;top:46%;opacity:.92}
.hero .wash{position:absolute;left:-14%;right:30%;top:14%;height:7%;background:var(--coral);mix-blend-mode:multiply;opacity:.55;border-radius:40% 60% 50% 50%/50%}
.hero .label{margin:24px 0 0}

/* title */
.title{text-align:center;padding:12vh 20px 0;max-width:1180px;margin:0 auto}
.title h1{font-family:var(--f-title);font-stretch:var(--title-stretch);font-weight:var(--title-weight);letter-spacing:var(--title-track);font-size:clamp(44px,7.5vw,96px);line-height:1.02;margin:0;color:var(--slate)}
.title .by{font-family:var(--f-display);font-weight:var(--display-weight);font-style:var(--display-style);font-variation-settings:var(--display-vs);font-size:clamp(34px,6.6vw,90px);line-height:1.08;margin:.06em 0 0;color:var(--slate);letter-spacing:-.01em}
.title .zh{font-family:"Noto Serif TC",serif;font-weight:300;font-size:clamp(18px,2vw,24px);letter-spacing:.5em;margin:28px 0 0;color:var(--soft)}
.stand{max-width:750px;margin:9vh auto 0;padding:0 20px;font-size:clamp(19px,1.9vw,25px);line-height:1.42;color:var(--slate);text-wrap:pretty}

/* threads: hairlines that cross the page, as on the Red Pine page */
.thread{width:1px;background:var(--hair2);margin:0 auto}
.thread.t1{height:120px;margin-top:9vh}
.cue{position:relative;text-align:center;font-size:16px;line-height:1.4;color:var(--slate);margin:22px 0}
.cue::before{content:"";position:absolute;left:0;top:.7em;width:calc(50% - 120px);height:1px;background:var(--hair)}

/* the poem: number, English, the Chinese down the centre thread; pictures bleed off an edge */
.poem{position:relative;padding:40px 0 120px}
.poem::before{content:"";position:absolute;left:50%;top:0;bottom:0;width:1px;background:var(--hair)}
.st{position:relative;display:grid;grid-template-columns:minmax(0,1fr) auto minmax(0,1fr);column-gap:clamp(20px,3vw,48px);align-items:start;padding:clamp(72px,14vh,140px) 0;scroll-margin-top:24px}
.st .en{grid-column:1;grid-row:1;justify-self:end;width:min(100%,25em);padding-left:20px}
.st .zh{grid-column:2;grid-row:1;position:relative;z-index:1;background:var(--paper);padding:10px 0}
.st.flip .en{grid-column:3;grid-row:1;justify-self:start;padding:0 20px 0 0}
.st .num{display:block;font-family:var(--f-num);font-weight:var(--num-weight);font-variation-settings:var(--num-vs);font-size:clamp(64px,7vw,104px);line-height:.9;color:var(--slate);text-decoration:none;margin:0 0 .9em}
.st .lines{font-family:var(--f-poem);font-weight:var(--poem-weight);font-style:var(--poem-style);font-variation-settings:var(--poem-vs);font-size:var(--poem-size);line-height:1.5;color:var(--ink);margin:0}
.st .lines span{display:block;padding-left:1.2em;text-indent:-1.2em}
.st .zh p{writing-mode:vertical-rl;font-family:"Noto Serif TC",serif;font-weight:400;font-size:22px;line-height:1.9;letter-spacing:.24em;margin:0;color:var(--slate);white-space:nowrap}
.st .zh p span{display:block}
.st .zh p span:nth-child(2n){margin-bottom:0}
.after .note{font-size:16px !important;font-family:var(--f-body);font-size:14px;line-height:1.45;color:var(--slate);margin:1.4em 0 0;max-width:24em;opacity:.9}
.st .note b{font-weight:500;color:var(--coral)}
.nm a{color:var(--coral);text-decoration:none;font-family:var(--f-body);font-size:.6em;margin-left:.15em}
.st .bleed{position:absolute;top:0;bottom:0;margin:0;pointer-events:none;z-index:0;overflow:hidden}
.st .bleed img{height:100%;width:100%;object-fit:cover;mix-blend-mode:multiply;display:block;-webkit-mask-image:linear-gradient(transparent,#000 18%,#000 82%,transparent);mask-image:linear-gradient(transparent,#000 18%,#000 82%,transparent)}
.st .bleed.r{right:0;width:34vw}
.st .bleed.l{left:0;width:34vw}
.st .rule{position:absolute;height:1px;background:var(--hair);left:0}
.st .rule.r{left:auto;right:0}
.st:target .num{color:var(--coral)}

/* afterwards: the introduction and the credits, quieter, in the reading face */
.after{max-width:750px;margin:0 auto;padding:40px 20px 80px;color:var(--slate)}
.after h2{font-family:var(--f-display);font-weight:var(--display-weight);font-style:var(--display-style);font-variation-settings:var(--display-vs);font-size:clamp(34px,4.4vw,54px);line-height:1.1;margin:0 0 28px;text-align:center}
.after p{font-size:19px;line-height:1.55;margin:0 0 1em;text-wrap:pretty;color:var(--ink)}
.credits{max-width:450px;margin:0 auto;padding:60px 20px 100px;text-align:center;color:var(--slate)}
.credits .label{font-size:13px;margin:0 0 10px}
.credits h3{font-family:var(--f-display);font-weight:var(--display-weight);font-style:var(--display-style);font-variation-settings:var(--display-vs);font-size:16px;margin:28px 0 4px;letter-spacing:.02em}
.credits .who{font-size:24px;margin:0 0 8px}
.credits p{font-size:13.5px;line-height:1.5;margin:0}
.dl{display:inline-block;margin-top:40px;font-family:var(--f-label);font-stretch:var(--label-stretch);text-transform:uppercase;letter-spacing:.07em;font-size:14px;border:1px solid var(--hair2);padding:12px 22px;text-decoration:none}
.foot{border-top:1px solid var(--hair2);padding:22px 24px 40px;font-size:13px;color:var(--soft);display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}

/* phones */
@media (max-width:720px){
  .hero{min-height:72svh;padding:64px 16px 20px}
  .hero .label{margin-top:32px}
  .stand{font-size:19px;line-height:1.45}
  .st .lines{font-size:calc(var(--poem-size) - 2px)}
  .hero .art{width:min(84vw,420px)}
  .title{padding-top:8vh}
  .poem::before{left:16px}
  .st{grid-template-columns:minmax(0,1fr);padding:52px 0 52px 0}
  .st .en,.st.flip .en{grid-column:1;grid-row:auto;justify-self:start;width:auto;padding:0 16px 0 36px}
  .st .zh{grid-column:1;grid-row:auto;justify-self:start;margin:28px 0 0 36px;padding:6px 0;max-width:calc(100vw - 52px);overflow-x:auto}
  .st .zh p{font-size:19px;line-height:1.75;letter-spacing:.22em}
  .st .bleed{position:relative;width:auto !important;height:64vw;margin:0 0 36px 36px;inset:auto;grid-row:1}
  .st .bleed.l{margin:0 36px 36px 0}
  .st .rule{display:none}
  .cue::before{display:none}
  .stand{margin-top:7vh}
  .after p{font-size:18px}
}
"""


def stanza_html(n, lines, zh, notes, opts):
    flip = n % 2 == 0
    en_lines = "".join("<span>%s</span>" % inline(html.escape(l, quote=False)) for l in lines)
    note_ids = re.findall(r"\[\^(\d+)\]", "\n".join(lines))
    note_html = ""
    # Chinese: one column per couplet, read right to left, as the Red Pine page sets Cold Mountain
    cols = ["%s　　%s" % tuple(zh[i:i + 2]) if i + 1 < len(zh) else zh[i] for i in range(0, len(zh), 2)]
    zh_html = '<p lang="zh-Hant">%s</p>' % "".join("<span>%s</span>" % c for c in cols)
    extra = opts.get(n, "")
    cls = "st flip" if flip else "st"
    return ('<section class="%s" id="%d">%s<div class="en"><a class="num" href="#%d">%d</a><p class="lines">%s</p>%s</div>'
            '<div class="zh">%s</div></section>') % (cls, n, extra, n, n, en_lines, note_html, zh_html)


def build(variant):
    inbrief, intro, stanzas, about, notes = parse()
    zh = chinese(stanzas)
    face = FACES[variant]
    css = face["css"] or seeds_css()
    side = b64(HERE / "img/side-coral.jpg", "image/jpeg")
    hero = b64(HERE / "img/hero-slate.jpg", "image/jpeg")
    coralhero = b64(HERE / "img/hero-coral.jpg", "image/jpeg")
    # the pictures inside the poem: a coral Sesshū beside the first stanza (bleeding right, as Red Pine's
    # coral mountain does), the slate one beside stanza 8 (bleeding left); hairlines from the page edge elsewhere
    opts = {
        1: '<figure class="bleed r"><img src="%s" alt="" style="object-position:50%% 60%%"></figure>' % hero,
        4: '<span class="rule" style="top:38%%;width:22vw"></span>',
        6: '<span class="rule r" style="top:64%%;width:30vw"></span>',
        9: '<figure class="bleed l"><img src="%s" alt=""></figure>' % side,
        11: '<span class="rule" style="top:20%%;width:14vw"></span>',
        13: '<span class="rule r" style="top:52%%;width:18vw"></span>',
    }
    body = "".join(stanza_html(n, l, z, notes, opts) for (n, l), z in zip(stanzas, zh))
    page = f"""<title>{face['title']}</title>{face['head']}<style>{css}{CSS}</style>
<nav class="top"><a href="#"><span class="mark" lang="zh-Hant">慧</span>Sutras</a><a href="#">Library</a></nav>
<section class="hero"><div class="art"><img src="{coralhero}" alt="An ink landscape: a few dark strokes of trees and rock, most of the paper empty."></div><p class="label">Poem</p></section>
<header class="title"><h1>Faith in Mind</h1><p class="by">translated by Master <span style="white-space:nowrap">Sheng-yen</span></p><p class="zh" lang="zh-Hant">信心銘</p></header>
<p class="stand">{inline(inbrief)}</p>
<div class="thread t1"></div>
<p class="cue">A poem attributed to<br>Seng Ts’an</p>
<div class="poem">{body}</div>
<section class="after notes"><h2>Notes</h2>{''.join('<p class="note" id="n%s"><b>%s</b> %s</p>' % (i, i, inline(t.replace("*Editors’ note.* ", ""))) for i, t in sorted(notes.items()))}</section>
<section class="after"><h2>Introduction</h2>{''.join('<p>%s</p>' % inline(p) for p in intro)}
<h2 style="margin-top:72px">About this translation</h2><p>{inline(about)}</p></section>
<section class="credits"><p class="label">Credits</p>
<h3>Translation</h3><p class="who">Master Sheng-yen</p><p>with Paul Kennedy. From <i>Faith in Mind: A Guide to Ch’an Practice</i>, Dharma Drum Publications, 1987. In copyright.</p>
<h3>Chinese text</h3><p class="who">信心銘</p><p>From the <i>Jingde Record of the Transmission of the Lamp</i>, fascicle 30, via Wikisource. Public domain.</p>
<h3>Image</h3><p class="who">Sesshū Tōyō</p><p><i>Haboku Sansui</i>, 1495. Tokyo National Museum. Public domain; toned here in two inks.</p>
<a class="dl" href="#">Download the EPUB</a></section>
<footer class="foot"><span>Sutras · a library of wisdom texts · Life Itself</span><span>Mockup, {face['faces']}</span></footer>"""
    OUT.mkdir(exist_ok=True)
    (OUT / f"{variant}.html").write_text(page)
    print(OUT / f"{variant}.html", len(page) // 1024, "KB")


if __name__ == "__main__":
    for v in sys.argv[1:] or ["open", "seeds"]:
        build(v)
