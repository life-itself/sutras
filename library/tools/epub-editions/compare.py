"""Compare words of the raw conversion's main text with the draft's main text.
usage: compare.py raw.md RAW_START RAW_END draft.md DRAFT_START DRAFT_END"""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import re, difflib
from common import words


def cut(path, start, end):
    s = open(path, encoding='utf-8').read()
    a = re.search(start, s, re.M)
    b = re.search(end, s[a.end():], re.M)
    return s[a.start():a.end() + b.start()]


def norm(s):
    s = re.sub(r'!\[[^\]]*\]\([^)]*\)', ' ', s)
    s = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', s)
    s = re.sub(r'\{[^}]*\}', ' ', s)
    s = s.replace('&emsp;', ' ')
    w = words(s)
    w = [x.replace('\\', '') for x in w]
    return [x for x in w if x]


raw, rs, re_, draft, ds, de = sys.argv[1:7]
A = norm(cut(raw, rs, re_))
B = norm(cut(draft, ds, de))
print('raw main-text words:', len(A))
print('draft main-text words:', len(B))
sm = difflib.SequenceMatcher(None, A, B, autojunk=False)
n = 0
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op == 'equal':
        continue
    n += 1
    print(op, '| raw:', ' '.join(A[max(i1-3,0):i2+3]), '| draft:', ' '.join(B[max(j1-3,0):j2+3]))
print('differences:', n)
