import re, sys
D = set(w.strip().lower() for w in open('/usr/share/dict/words'))
FW = ['the', 'and', 'of', 'to', 'in', 'that', 'it', 'is', 'was', 'for', 'with', 'as', 'his', 'be', 'not', 'but', 'on', 'you', 'your', 'up', 'out', 'what', 'all', 'from', 'by', 'or', 'are', 'we', 'he', 'she', 'they', 'an', 'at', 'so', 'if', 'no', 'one', 'who', 'this']
txt = open(sys.argv[1], encoding='utf-8').read()
txt = re.sub(r'\[\^[^\]]+\]', ' ', txt)
for w in sorted(set(re.findall(r"\b[a-z]{5,}\b", txt))):
    if w in D:
        continue
    for f in FW:
        if w.startswith(f) and w[len(f):] in D and len(w) - len(f) >= 3:
            print(w, '=', f, w[len(f):])
            break
        if w.endswith(f) and w[:-len(f)] in D and len(w) - len(f) >= 3:
            print(w, '=', w[:-len(f)], f)
            break
