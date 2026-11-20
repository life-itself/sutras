"""Check passage ids in an edition draft.
usage: check_ids.py dhammapada|meditations draft.md"""
import re, sys, collections

kind, path = sys.argv[1:3]
txt = open(path, encoding='utf-8').read()
ids = re.findall(r'<a id="([^"]+)"></a>', txt)
dupes = [k for k, v in collections.Counter(ids).items() if v > 1]
print('ids found:', len(ids), '| unique:', len(set(ids)), '| duplicates:', dupes or 'none')
fm = txt.split('---\n')[1]
for key in ('title', 'author', 'translator', 'date', 'tradition', 'source', 'licence', 'status'):
    if not re.search(r'^%s: .+' % key, fm, re.M):
        print('MISSING frontmatter:', key)
refs = set(re.findall(r'\[\^([^\]]+)\](?!:)', txt))
defs = set(re.findall(r'^\[\^([^\]]+)\]:', txt, re.M))
print('footnotes: refs', len(refs), '| defs', len(defs), '| refs without def', sorted(refs - defs) or 'none', '| defs without ref', sorted(defs - refs) or 'none')
if kind == 'dhammapada':
    nums = [int(i) for i in ids]
    missing = sorted(set(range(1, 424)) - set(nums))
    extra = sorted(set(nums) - set(range(1, 424)))
    print('verses 1-423: missing', missing or 'none', '| out of range', extra or 'none',
          '| in order', nums == sorted(nums))
    print('chapters:', len(re.findall(r'^## [IVXL]+ : ', txt, re.M)))
else:
    std = [17, 17, 16, 51, 37, 59, 75, 61, 42, 38, 39, 36]
    books = [i for i in ids if '.' not in i]
    print('book ids:', books)
    for b in range(1, 13):
        secs = [i.split('.')[1] for i in ids if i.startswith('%d.' % b)]
        main = [int(s) for s in secs if s.isdigit()]
        extra = [s for s in secs if not s.isdigit()]
        ok = main == list(range(1, std[b - 1] + 1))
        print('Book %2d: %2d sections (standard %2d) %s%s' % (b, len(main), std[b - 1], 'OK' if ok else 'MISMATCH',
              ('; plus Hays\'s split entries ' + ', '.join('%d.%s' % (b, s) for s in extra)) if extra else ''))
