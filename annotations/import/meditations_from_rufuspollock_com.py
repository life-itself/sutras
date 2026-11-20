#!/usr/bin/env python3
"""One-off import: Rufus's Meditations notes (rufuspollock.com) -> annotations/meditations.yaml.

Usage: python3 annotations/import/meditations_from_rufuspollock_com.py [Meditations.md] [edition.md]
  defaults: ~/src/rufuspollock/rufuspollock.com/Meditations.md, library/meditations/edition-draft.md

Rufus's page is a run of headings, quoted passages of the Hays translation (bold italic, in
blockquotes) and his comments. Each quoted paragraph becomes a note; it is found in the edition and
its words are taken *from the edition* (so Rufus's own additions, such as wrapping quotation marks,
"[Homer, Iliad]" or "…" for Hays's ". . .", drop out), with the passage id it sits in. His comments
go on the first quote they belong to: the heading, the lines just before the quotes, and (after the
last quotes under a heading) the lines after them. A quoted passage that is not in the edition stays
in the comment as a quotation. Hays passages pasted as plain text are found too and become
highlights. Prints a report of everything that was not matched. Then run scripts/notes meditations.
"""
import importlib.machinery, importlib.util, os, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_loader("notes", importlib.machinery.SourceFileLoader("notes", str(ROOT / "scripts" / "notes")))
N = importlib.util.module_from_spec(spec); spec.loader.exec_module(N)

SRC = Path(sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser("~/src/rufuspollock/rufuspollock.com/Meditations.md"))
ED = Path(sys.argv[2] if len(sys.argv) > 2 else ROOT / "library/meditations/edition-draft.md")
OUT = ROOT / "annotations" / "meditations.yaml"


def loose(s):
    """For finding a quote only (the words written out come from the edition): ellipses too."""
    s = s.replace("…", ". . .")
    s = re.sub(r"\.\s*\.\s*\.", ". . .", s)
    return N.fold(s)


def folded_with_map(s):
    out, at = [], []
    for i, c in enumerate(s):
        f = loose(c) if c != "…" else ". . ."
        for ch in f:
            if ch == " " and (not out or out[-1] == " "):
                continue
            out.append(ch); at.append(i)
    return "".join(out), at


# ---------- the edition, split into passages ----------
ed = ED.read_text()
ed_body = ed[N.front_matter_end(ed):]
passages = []   # (id or None, plain text, folded, map)
ids = re.findall(r'<a\b[^>]*\bid="(\d+\.\d+a?)"', ed_body)
for pid in ids:
    t = N.plain(N.passage_region(ed_body, pid))
    t = re.sub(r"^\s*\d+a?\.\s", " ", t)          # the printed section number
    f, at = folded_with_map(t)
    passages.append((pid, t, f, at))
intro = re.search(r"\n## Introduction\n(.*?)(\n## Index of Persons\n|\Z)", ed_body, re.S)
if intro:
    t = N.plain(re.sub(r"\[\^[^\]]+\]", "", intro.group(1)))
    f, at = folded_with_map(t)
    passages.append((None, t, f, at))


# typos in the EPUB that Rufus copied and the edition corrects (library/meditations/NOTES.md)
EPUB_TYPOS = {"thewhole": "the whole", "upwithout": "up without"}


def clean_quote(q):
    q = re.sub(r"^\s*(>\s?)+", "", q, flags=re.M)
    for a, b in EPUB_TYPOS.items():
        q = q.replace(a, b)
    q = re.sub(r"\s*\[[^\]]*\]", "", q)                    # [Democritus fragment B115]
    q = q.strip().strip('"“” ').strip()
    q = re.sub(r"^\d+a?\.\s*", "", q)                       # his copied section number
    q = re.sub(r"(?<=[a-z]\.)\d+(?=\s)", "", q)             # a footnote digit from the introduction
    return q.strip().strip('"“” ').strip()


def find(q):
    """[(passage id, exact words from the edition)] or [] if not found."""
    lq = loose(q).strip()
    if len(lq) < 3:
        return []
    hits = []
    for pid, t, f, at in passages:
        i = f.find(lq)
        if i != -1:
            words = t[at[i]:at[i + len(lq) - 1] + 1]
            hits.append((pid, re.sub(r"\s+", " ", words).strip()))
    return hits


# ---------- Rufus's page, as blocks ----------
src = SRC.read_text()
src = src[N.front_matter_end(src):]
lines = src.split("\n")
blocks = []      # ("h", text) | ("q", [paragraph texts]) | ("p", text)
para, kind = [], None


def flush():
    global para, kind
    if para:
        text = "\n".join(para)
        if kind == "q":
            # a blockquote: its paragraphs are separated by '>' lines
            parts = [p for p in re.split(r"\n>\s*\n", text) if p.strip()]
            if blocks and blocks[-1][0] == "q":
                blocks[-1][1].extend(parts)
            else:
                blocks.append(("q", parts))
        else:
            blocks.append(("p", text))
    para, kind = [], None


for line in lines:
    s = line.strip()
    m = re.match(r"^(#{2,4})\s+(.*)$", s)
    if m:
        flush(); blocks.append(("h", m.group(2).replace("**", "").strip())); continue
    if not s:
        flush(); continue
    if s == "---" or s.startswith("!["):
        flush(); continue
    k = "q" if s.startswith(">") else "p"
    if kind and k != kind:
        flush()
    kind = k
    para.append(line)
flush()
# blank lines inside one blockquote split it into several "q" blocks: join them back up
merged = []
for b in blocks:
    if b[0] == "q" and merged and merged[-1][0] == "q":
        merged[-1][1].extend(b[1])
    else:
        merged.append(b)
blocks = merged

# a plain paragraph that is Hays's words pasted without formatting is a quote too
pasted = []
for i, b in enumerate(blocks):
    if b[0] == "p" and "***" not in b[1] and not b[1].lstrip().startswith(("-", "*")):
        txt = b[1].strip()
        if len(txt) > 40 and find(clean_quote(txt)):
            blocks[i] = ("q", [txt]); pasted.append(txt[:70])

# ---------- notes ----------
notes, report, used_ids = [], {"unmatched": [], "pasted": pasted, "dropped": []}, {}


def nid(pid):
    base = "rp-" + (pid if pid else "intro")
    used_ids[base] = used_ids.get(base, 0) + 1
    return base if used_ids[base] == 1 else "%s-%d" % (base, used_ids[base])


def md_note(parts):
    out = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        if re.match(r"^\s*[-*]\s", p):
            p = "\n\n".join("• " + re.sub(r"^\s*[-*]\s+", "", l).strip() for l in p.splitlines() if l.strip())
        out.append(p)
    return "\n\n".join(out)


def choose(hits, raw, prev):
    """Several passages hold these words (e.g. "Remember:"): prefer the section number Rufus copied,
    then the passage he quoted just before, then the next one after it, then the same book."""
    lead = re.match(r"\s*[\u201c\"]?(\d+)a?\.", raw)
    pb, ps = (prev.split(".") + [""])[:2] if prev else ("", "")
    def score(h):
        pid = h[0] or ""
        b, _, sec = pid.partition(".")
        sec = sec.rstrip("a")
        near = b == pb and sec.isdigit() and ps.rstrip("a").isdigit() and 0 <= int(sec) - int(ps.rstrip("a")) <= 1
        return ((lead is not None and sec == lead.group(1)) * 4 + near * 2 + (b == pb))
    return max(hits, key=score)


prev_pid = None
heading, pending, last_group = None, [], None
for b in blocks:
    if b[0] == "h":
        if last_group is not None and pending:
            last_group["trail"].extend(pending)
        elif pending:
            report["dropped"].append((heading, " / ".join(x[:60] for x in pending)))
        heading, pending, last_group = b[1], [], None
        continue
    if b[0] == "p":
        pending.append(b[1]); continue
    # a group of quoted paragraphs
    group = {"heading": heading if last_group is None else None, "lead": pending, "trail": [], "quotes": [], "missing": []}
    pending = []
    for q in b[1]:
        runs = re.findall(r"\*\*\*(.+?)\*\*\*", q, flags=re.S) or [q]
        for r in runs:
            cq = clean_quote(r)
            if not re.search(r"\w", cq):
                continue
            hits = find(cq)
            if not hits:
                group["missing"].append(cq); report["unmatched"].append(cq[:90]); continue
            pid, words = choose(hits, r, prev_pid)
            if len(hits) > 1:
                report.setdefault("chosen among several", []).append((cq[:40], [h[0] for h in hits], pid))
            prev_pid = pid
            group["quotes"].append((pid, words))
    notes.append(group)
    last_group = group
if last_group is not None and pending:
    last_group["trail"].extend(pending)

# ---------- write YAML ----------
def yq(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


out = ["# Rufus Pollock's notes on Marcus Aurelius, Meditations (Hays translation).",
       "# Imported 2026-11-20 from rufuspollock.com/Meditations (written 2022-05-30 to 2024-07-15) by",
       "# annotations/import/meditations_from_rufuspollock_com.py; edit by hand from now on.",
       "# Format: see scripts/notes. Check and rebuild: scripts/notes meditations",
       "text: %s" % ED.relative_to(ROOT), "notes:"]
count = 0
prev_g = None
for g in notes:
    comment = []
    if g["heading"]:
        comment.append("**%s.**" % g["heading"].rstrip(".…:"))
    comment.extend(g["lead"])
    comment.extend("> " + m for m in g["missing"])
    comment.extend(g["trail"])
    g["body"], g["extra"] = md_note(comment), []
    if not g["quotes"]:
        if g["body"] and prev_g is not None:
            prev_g["extra"].append(g["body"])
        elif g["body"]:
            report["dropped"].append((g["heading"], g["body"][:80]))
        continue
    prev_g = g
for g in notes:
    if not g["quotes"]:
        continue
    body = "\n\n".join(x for x in [g["body"]] + g["extra"] if x)
    for k, (pid, words) in enumerate(g["quotes"]):
        out.append("")
        out.append("  - id: %s" % nid(pid))
        if pid:
            out.append('    passage: "%s"' % pid)
        out.append("    quote: %s" % yq(words))
        if k == 0 and body:
            out.append("    note: |")
            out.extend(("      " + l) if l else "" for l in body.split("\n"))
        out.append("    by: Rufus Pollock")
        out.append("    date: 2024-07-15")
        count += 1
OUT.write_text("\n".join(out) + "\n")
print("wrote %s: %d notes" % (OUT.relative_to(ROOT), count))
for k, v in report.items():
    print("%s: %d" % (k, len(v)))
    for x in v:
        print("   ", x)
