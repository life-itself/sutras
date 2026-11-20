#!/usr/bin/env python3
"""Parse the sacred-texts Mumonkan page into a structure: preface, 48 cases, postscript.

Usage: python3 library/gateless-gate-mumonkan/parse_source.py    (from the repo root; prints JSON)

Used by extract.py (to make the first version of the edition) and compare.py (to check the
edition against the source). Each section is a list of parts (text, comment, verse); each part is a
list of paragraphs; each paragraph is a list of (chinese, english) sentence pairs, as the source
pairs them. Paragraph breaks are the source's empty paragraphs. No words are changed here.
"""
import html, json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "sacred-texts-mumonkan.htm"
# "—" counts as Chinese: the source has one inside a Chinese sentence (case 1, 打成—片, for 一)
CJK = re.compile(r"[　-〿㐀-鿿豈-﫿＀-￯□—]")


def paragraphs():
    h = SOURCE.read_text(encoding="utf-8")
    for p in re.findall(r"(?is)<p\b[^>]*>(.*?)</p>", h):
        bold = " ".join(re.findall(r"(?is)<b>(.*?)</b>", p))
        p = re.sub(r"(?is)<span style='mso-tab-count:[^']*'>.*?</span>", "\t", p)
        t = html.unescape(re.sub(r"<[^>]+>", "", p)).replace("\xa0", " ")
        t = re.sub(r"[ \r\n]+", " ", t).strip()
        yield t, html.unescape(re.sub(r"<[^>]+>", "", bold)).strip()


def split_zh(t):
    """Split a paragraph into its leading Chinese and trailing English."""
    i = 0
    while i < len(t) and (CJK.match(t[i]) or t[i] in " \t"):
        i += 1
    return t[:i].strip(), t[i:].strip()


def parse():
    sections, sec, part, para = [], None, None, None
    started = False
    for t, bold in paragraphs():
        if not started:
            started = t.startswith("Mumon's Preface")
            if not started:
                continue
        if t == "Source" or t.startswith("Source "):
            break
        head = re.match(r"Case (\d+)\s+(.*)$", t) if bold.startswith("Case") else None
        if t.startswith("Mumon's Preface") or t.startswith("Mumon's Postscript") or head:
            if head:
                title, zh = split_title(head.group(2))
                sec = {"id": head.group(1), "label": "Case " + head.group(1), "title": title, "zh": zh, "parts": []}
            else:
                name, zh = split_title(t)
                sec = {"id": "preface" if "Preface" in t else "postscript", "label": name, "title": "", "zh": zh, "parts": []}
            sections.append(sec)
            part = {"kind": "text", "label": "", "paras": []}
            sec["parts"].append(part)
            para = None
            continue
        if t.startswith("Mumon's Comment") or re.match(r"(Mumon's )?Verse", t):
            kind = "comment" if "Comment" in t else "verse"
            part = {"kind": kind, "label": t, "paras": []}
            sec["parts"].append(part)
            para = None
            continue
        if not t:
            para = None
            continue
        zh, en = split_zh(t)
        if para is None:
            para = []
            part["paras"].append(para)
        if zh and en:
            para.append([zh, en])          # a verse line, or a line given side by side
        elif zh:
            para.append([zh, ""])
        else:
            if para and para[-1][1] == "":
                para[-1][1] = en
            elif para and part["kind"] == "verse":
                para[-1][1] += " " + en     # a verse line the source wrapped
            else:
                para.append(["", en])
    # drop empty leading parts (a section that opens with a part heading)
    for s in sections:
        s["parts"] = [p for p in s["parts"] if p["paras"] or p["kind"] != "text"]
    return sections


def split_title(t):
    zh_at = next((i for i, ch in enumerate(t) if CJK.match(ch) and ch != "　"), len(t))
    return t[:zh_at].strip(), t[zh_at:].strip()


if __name__ == "__main__":
    print(json.dumps(parse(), ensure_ascii=False, indent=1))
