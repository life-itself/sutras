#!/usr/bin/env python3
"""Compare the Chinese of the source (sacred-texts, from an Iwanami Bunko edition) with the Taishō
text (CBETA T48n2005), section by section.

Usage: python3 library/gateless-gate-mumonkan/compare_chinese.py [--boxes | --kept]    (from the repo root)

Punctuation is dropped and common variant forms of the same character are treated as equal (VARIANTS),
so what is printed is a difference of reading, a slip, or an empty box (□) in the source. With
--boxes, prints only the boxes and the Taishō character at each. With --kept, applies the
corrections in fixes.py first and leaves out the boxes and the 頌曰 ("the verse says") that the
source prints as a heading: what is left is the differences of reading kept as in the source
(saved as chinese-differences.txt).
"""
import difflib, pathlib, re, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from parse_source import parse

HERE = pathlib.Path(__file__).resolve().parent
CBETA = HERE / "cbeta-T48n2005.xml"

# Pairs of forms of one character (Japanese or older form first, Taishō form second).
VARIANTS = dict(p for p in "衆眾 説說 爲為 徳德 眞真 歩步 擧舉 脱脫 絶絕 黄黃 倶俱 渉涉 虚虛 税稅 縁緣 万萬 惣總 峰峯 殻殼 敍敘 内內 晩晚 並并 顔顏 腸膓 刹剎 捏揑 掲揭 黒黑 録錄 歴歷 厮廝 呑吞 覚覺 嵒巖 祗祇 廻迴 唖啞 彦彥 毎每 着著 傚俲 啓啟 雙双 撃擊 涙淚 茘荔 剥剝 没沒 状狀 贓贜 偸偷 獻献 舎舍 蟹蠏 渓溪 栢柏 撿檢 値值 敕勅 悦悅 乗乘 馳駞 款欵 剰剩 佗他 戸戶 時旹 納衲 你爾".split())  # pairs of forms of one character: source form, Taishō form


def k(ch):
    return VARIANTS.get(ch, ch)


def strip(s):
    return [c for c in s if re.match(r"[\u3400-\u9fff\uf900-\ufaff\U00020000-\U0003ffff□]", c)]


def cbeta_sections():
    x = CBETA.read_text(encoding="utf-8")
    b = x[x.index("<body"):x.index("</body>")]
    b = re.sub(r"<note\b.*?</note>", "", b, flags=re.S)
    b = re.sub(r"<lb\b[^>]*/>\n?", "", b)
    divs = re.findall(r"<cb:div[^>]*>(.*?)</cb:div>", b, flags=re.S)
    out = []
    for d in divs:
        head = re.search(r"<head>(.*?)</head>", d)
        body = re.sub(r"<head>.*?</head>|<cb:mulu.*?</cb:mulu>", "", d, flags=re.S)
        out.append((re.sub(r"<[^>]+>", "", head.group(1)) if head else "", re.sub(r"<[^>]+>", "", body)))
    return out


def source_sections(fixed=False):
    from fixes import ZH_FIXES
    for s in parse():
        zh = "|".join(re.sub(r"[ \u3000]", "", c) for part in s["parts"] for para in part["paras"] for c, e in para)
        if fixed:
            for sid, a, b in ZH_FIXES:
                if sid == s["id"]:
                    zh = zh.replace(a, b)
        yield s["id"], s["zh"], zh.replace("|", "")


def pairs(fixed=False):
    """(source id, source title, source Chinese), (Taishō head, Taishō text), section by section."""
    cb = cbeta_sections()
    # the Taishō has a preface by Xi'an (習菴) and a memorial first; the cases follow the contents list
    cases = [d for d in cb if d[0] not in ("禪宗無門關", "目錄")]
    preface = [d for d in cb if d[0] == "禪宗無門關"][1]
    src = list(source_sections(fixed))
    pairs = [(src[0], preface)] + list(zip(src[1:49], cases[:48]))
    # the postscript is the text after case 48 in the last div, up to 禪箴
    last = cases[47][1]
    pairs[-1] = (src[48], (cases[47][0], last[:last.index("無門曰")] + last[last.index("無門曰"):last.find("頌曰")]))
    post_div = next((d for d in cb if "從上佛祖垂示機緣" in d[1]), None)
    post_text = post_div[1] if post_div else last
    post_text = post_text[post_text.index("從上佛祖"):]
    post_text = post_text[:post_text.find("禪箴")] if "禪箴" in post_text else post_text
    pairs.append((src[49], ("後序", post_text)))
    return pairs


def align(s, c):
    a, b = strip(s), strip(c)
    sm = difflib.SequenceMatcher(None, [k(x) for x in a], [k(x) for x in b], autojunk=False)
    return a, b, sm.get_opcodes()


def box_fills():
    """For each section, the Taishō character at each empty box (□) of the source, in order
    (None where the alignment does not give a single character)."""
    fills = {}
    for (sid, stitle, s), (ctitle, c) in pairs():
        a, b, ops = align(s, c)
        got = []
        for op, i1, i2, j1, j2 in ops:
            for n, ch in enumerate(a[i1:i2]):
                if ch == "□":
                    got.append(b[j1 + n] if op == "replace" and i2 - i1 == j2 - j1 else None)
        if got:
            fills[sid] = got
    return fills


def main(boxes_only=False, kept=False):
    for (sid, stitle, s), (ctitle, c) in pairs(kept):
        a, b, ops = align(s, c)
        diffs = [(op, "".join(a[i1:i2]), "".join(b[j1:j2]), "".join(a[max(0, i1 - 3):i1]))
                 for op, i1, i2, j1, j2 in ops if op != "equal"]
        if boxes_only:
            diffs = [d for d in diffs if "□" in d[1]]
        if kept:
            diffs = [d for d in diffs if "□" not in d[1] and d[2] != "頌曰" and not (sid == "48" and len(d[1]) > 20)]
        if diffs:
            print("== %s %s / %s" % (sid, stitle, ctitle))
            for op, x, y, ctx in diffs:
                print("   %-7s source %s|%s|  Taishō |%s|" % (op, ctx, x, y))


if __name__ == "__main__":
    main("--boxes" in sys.argv, "--kept" in sys.argv)
