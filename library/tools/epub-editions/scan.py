"""Scan a draft for likely conversion damage."""
import re, sys, collections
txt = open(sys.argv[1], encoding='utf-8').read()
body = txt.split('\n---\n', 1)[1]
checks = {
    'glued caps': r'\b[A-Z]{3,}[A-Z][a-z]+',
    'lower-Upper join': r'\b[a-z]{2,}[A-Z][a-z]+',
    'letter-digit join': r'\b[A-Za-z]{3,}\d+\b',
    'double space': r'\S  \S',
    'space before punct': r'\w [,;:!?](?!\S)',
    'hyphen at word end + space': r'\w- [a-z]',
    'odd chars': r'[�­​﻿]',
    'html tag (non-a)': r'<(?!a id|/a>)[a-z/][^>]*>',
    'repeated word': r'\b(\w+) \1\b',
}
for name, pat in checks.items():
    hits = [(m.start(), m.group(0)) for m in re.finditer(pat, body)]
    if hits:
        print('==', name, len(hits))
        for pos, h in hits[:25]:
            ln = body.count('\n', 0, pos)
            ctx = body[max(0, pos - 40):pos + 40].replace('\n', '/')
            print('   ', repr(h), '|', ctx)
