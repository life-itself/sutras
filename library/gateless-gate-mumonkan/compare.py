#!/usr/bin/env python3
"""Compare the Gateless Gate edition with its source, word for word (English) and character by
character (Chinese).

Usage: python3 library/gateless-gate-mumonkan/compare.py      (from the repo root)

Reads gateless-gate-mumonkan.md and the source as fetched (sacred-texts-mumonkan.htm, through
parse_source.py) and prints every difference, section by section. Quote style, dashes, whitespace,
the macrons (ō for the source's õ) and footnote markers are normalised first, so only real changes
show. Exit status 1 if there is a difference not in EXPECTED; each expected one is in NOTES.md.

A copy of scripts/compare-source's approach for this text: that script is written for Faith in Mind
only (bead filed for the site track to generalise it).
"""
import difflib, html, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from parse_source import parse
from compare_chinese import box_fills
from fixes import EN_FIXES, ZH_FIXES

EDITION = HERE.parent.parent / "gateless-gate-mumonkan.md"

# English: (source words, edition words), all listed in NOTES.md (from fixes.EN_FIXES)
EXPECTED_EN = {("Destitude", "Destitute")}
# Chinese: the corrections in fixes.ZH_FIXES are applied to the source before comparing, and the
# boxes in the body must be filled with the Taishō characters in order. Beyond those: (section, source, edition)
EXPECTED_ZH = {("40", "□", "趯")}   # the box in case 40's title, as in the Taishō contents list


def norm_en(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("ō", "õ").replace("ū", "û").replace("Ō", "Õ").replace("—", " - ").replace("\\.", ".")
    return re.sub(r"\s+", " ", s).strip()


def zh_chars(s):
    return re.sub(r"[\s　]", "", s)


def source():
    out = {}
    fills = box_fills()
    for s in parse():
        en = [s["title"]] if s["title"] else []
        zh = [s["zh"]]
        for part in s["parts"]:
            for para in part["paras"]:
                for c, e in para:
                    en.append(e)
                    zh.append(c)
        zh = zh_chars("|".join(zh))
        for sid, a, b in ZH_FIXES:
            if sid == s["id"]:
                zh = zh.replace(a, b)
        out[s["id"]] = (norm_en(" ".join(en)), zh.replace("|", ""), fills.get(s["id"], []))
    return out


def edition():
    t = EDITION.read_text(encoding="utf-8")
    t = t[t.index("## The text"):t.index("## About this translation")]
    out = {}
    for block in re.split(r'(?=<h3 class="koan-title")', t)[1:]:
        sid = re.match(r'<h3 class="koan-title" id="([^"]+)"', block).group(1)
        head, body = block.split("</h3>", 1)
        head = re.sub(r'<span class="koan-num">.*?</span>', "", head)
        title = re.sub(r"<[^>]+>", "", re.sub(r'<span class="koan-title-zh" lang="zh">[^<]*</span>', "", head.split(">", 1)[1]))
        title = "" if sid in ("preface", "postscript") else title.strip()
        title_zh = re.search(r'<span class="koan-title-zh" lang="zh">([^<]*)</span>', block.split("</h3>", 1)[0])
        zh = (title_zh.group(1) if title_zh else "") + "".join(re.findall(r'<p class="orig" lang="zh">(.*?)</p>', body))
        body = re.sub(r'<p class="orig" lang="zh">.*?</p>', "", body)
        body = re.sub(r'<p class="koan-label[^>]*>.*?</p>', "", body)
        body = re.sub(r"\[\^[^\]]+\]", "", body)
        body = html.unescape(re.sub(r"<[^>]+>", "", body))
        out[sid] = (norm_en(title + " " + body), zh_chars(re.sub(r"<br\s*/?>", "", zh)))
    return out


def main():
    src, ed = source(), edition()
    problems = 0
    if list(src) != list(ed):
        print("Sections differ:", list(src), list(ed))
        return 1
    filled = 0
    for sid in src:
        s_en, s_zh, fills = src[sid]
        e_en, e_zh = ed[sid]
        a, b = s_en.split(), e_en.split()
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
            if op == "equal":
                continue
            x, y = " ".join(a[i1:i2]), " ".join(b[j1:j2])
            ok = (x.strip('.,;:!?"'), y.strip('.,;:!?"')) in EXPECTED_EN
            problems += not ok
            print("%s %s  English: %r -> %r" % ("  expected" if ok else "UNEXPECTED", sid, x, y))
        todo = list(fills)
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, s_zh, e_zh, autojunk=False).get_opcodes():
            if op == "equal":
                continue
            x, y = s_zh[i1:i2], e_zh[j1:j2]
            if op == "replace" and set(x) == {"□"} and len(x) == len(y) and list(y) == todo[:len(y)]:
                todo = todo[len(y):]
                filled += len(y)
                continue
            ok = (sid, x, y) in EXPECTED_ZH
            problems += not ok
            print("%s %s  Chinese: %r -> %r" % ("  expected" if ok else "UNEXPECTED", sid, x, y))
        if todo:
            problems += 1
            print("UNEXPECTED %s  boxes not filled: %r" % (sid, todo))
    words = sum(len(v[0].split()) for v in ed.values())
    print("%d sections, %d English words, %d Chinese characters, %d boxes filled from the Taishō, %d unexpected differences"
          % (len(ed), words, sum(len(v[1]) for v in ed.values()), filled, problems))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
