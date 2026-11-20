#!/usr/bin/env python3
"""Make the first version of the text section of gateless-gate-mumonkan.md from the source.

Usage: python3 library/gateless-gate-mumonkan/extract.py > /tmp/text.md    (from the repo root)

Run once, on 2026-11-20; the edition has been edited by hand since (notes added), so do not
overwrite it with this output. Kept as the record of how the text was made: what it does to the
words is listed in NOTES.md. In short: the source's sentence pairs are joined into paragraphs, the
English first and its Chinese after; quotation marks made curly; õ, û, Õ made ō, ū, Ō; fixes listed
in FIXES below.
"""
import re, sys

sys.path.insert(0, __import__("os").path.dirname(__file__))
from parse_source import parse
from compare_chinese import box_fills
from fixes import EN_FIXES, ZH_FIXES

TITLE_BOXES = {"40": "趯"}   # the box in case 40's Chinese title, as in the Taishō contents list


def macrons(s):
    return s.replace("õ", "ō").replace("û", "ū").replace("Õ", "Ō")


def curly(s):
    s = re.sub(r'(^|[\s(\[—])"', r"\1“", s)
    s = s.replace('"', "”")
    s = re.sub(r"(^|[\s(\[—“])'", r"\1‘", s)
    s = s.replace("'", "’")
    return s


def zh_spans(s):
    return re.sub(r"([㐀-鿿□]+)", r'<span lang="zh">\1</span>', s)


def fix(s):
    for sid, a, b in EN_FIXES:
        s = s.replace(a, b)
    return s


def fill_boxes(sections):
    """Fill the source's empty boxes (□) from the Taishō text, in order, section by section."""
    fills = box_fills()
    for s in sections:
        todo = list(fills.get(s["id"], []))
        for part in s["parts"]:
            for para in part["paras"]:
                for pair in para:
                    while "□" in pair[0]:
                        pair[0] = pair[0].replace("□", todo.pop(0), 1)
                    # the source's stray spaces inside sentences (從　前, 驚天　動地) dropped; slips fixed
                    pair[0] = re.sub(r"[ \u3000]", "", pair[0])
                    for sid, a, b in ZH_FIXES:
                        if sid == s["id"]:
                            pair[0] = pair[0].replace(a, b)
        assert not todo, s["id"]
        if s["id"] in TITLE_BOXES:
            s["zh"] = s["zh"].replace("□", TITLE_BOXES[s["id"]])
        for sid, a, b in ZH_FIXES:
            if sid == s["id"]:
                s["zh"] = s["zh"].replace(a, b)
    return sections


def en(s):
    return zh_spans(curly(macrons(fix(s))))


def zh(s):
    return s


def label(part):
    if part["kind"] == "comment":
        return '<p class="koan-label rs-label">Mumon’s comment</p>'
    if part["kind"] == "verse":
        return '<p class="koan-label rs-label">Mumon’s verse <span lang="zh">頌曰</span></p>'
    return ""


def prose(paras, sec_id):
    out = []
    for para in paras:
        lines, zhs = [], []
        for c, e in para:
            if c:
                zhs.append(zh(c))
            if e:
                lines.append(en(e))
        if sec_id == "24":                     # Fuketsu's quoted poem: the source sets it as lines
            text = lines[0] + "\n\n" + "  \n".join(lines[1:])
        elif sec_id == "postscript" and lines[0].startswith("The change of era"):   # date and signature
            text = "  \n".join(l.replace("\t", "  \n") for l in lines)
            zhs = ["<br />".join(zhs)]
        elif sec_id == "postscript" and lines[0].startswith("Wu-wen kuan"):
            text = lines[0].replace("\t", "  \n")
        elif sec_id == "47":                   # the three barriers: one paragraph each
            text, chunks = "", []
            for l in lines:
                if re.match(r"\d\. ", l):
                    chunks.append([l.replace(". ", "\\. ", 1)])
                elif chunks:
                    chunks[-1].append(l)
                else:
                    chunks.append([l])
            text = "\n\n".join(" ".join(c) for c in chunks)
        else:
            text = " ".join(lines)
        out.append(text)
        if zhs:
            out.append('<p class="orig" lang="zh">' + "".join(zhs) + "</p>")
    return out


def verse(paras):
    out = []
    for para in paras:
        out.append("  \n".join(en(e) for c, e in para))
        out.append('<p class="orig" lang="zh">' + "<br />".join(zh(c) for c, e in para) + "</p>")
    return out


def section(s):
    if s["id"] in ("preface", "postscript"):
        name = "Mumon’s preface" if s["id"] == "preface" else "Mumon’s postscript"
        zh_title = ' <span class="koan-title-zh" lang="zh">%s</span>' % s["zh"] if s["zh"] else ""
        head = '<h3 class="koan-title" id="%s"><a href="#%s">%s%s</a></h3>' % (s["id"], s["id"], name, zh_title)
    else:
        head = ('<h3 class="koan-title" id="%s"><a href="#%s"><span class="koan-num">Case %s</span> %s <span class="koan-title-zh" lang="zh">%s</span></a></h3>'
                % (s["id"], s["id"], s["id"], en(s["title"]), s["zh"]))
    out = [head]
    for part in s["parts"]:
        kind = {"text": "koan-case", "comment": "koan-comment", "verse": "koan-verse rs-verse"}[part["kind"]]
        if s["id"] in ("preface", "postscript"):
            kind = {"text": "koan-prose", "verse": "koan-verse rs-verse"}[part["kind"]]
        body = [label(part)] if label(part) else []
        body += verse(part["paras"]) if part["kind"] == "verse" else prose(part["paras"], s["id"])
        out.append('<div class="%s">\n\n%s\n\n</div>' % (kind, "\n\n".join(body)))
    return "\n\n".join(out)


if __name__ == "__main__":
    print("\n\n".join(section(s) for s in fill_boxes(parse())))
