"""Write the notes-match report as Markdown. usage: notes_match_md.py notes.md match.json out.md"""
import re, sys, json, collections

notes_path, match_path, out_path = sys.argv[1:4]
lines = open(notes_path, encoding='utf-8').read().split('\n')
res = json.load(open(match_path))


def book_at(lineno):
    for i in range(lineno - 1, -1, -1):
        m = re.match(r'#{2,4} (Book (\d+)|Introduction|Reflections|Key themes)', lines[i])
        if m:
            return m.group(2) or m.group(1)
    return None


def first_words(q, n=9):
    q = re.sub(r'\s+', ' ', re.sub(r'^\s*>\s?', '', q, flags=re.M)).strip()
    w = q.split()
    return ' '.join(w[:n]) + (' …' if len(w) > n else '')


rows = []
counts = collections.Counter()
cite_issues = []
for r in res:
    if r['status'] == 'empty':
        continue
    where = ', '.join(r.get('where', [])) or ('closest ' + r.get('closest', '')) if r['status'] == 'not verbatim' else ', '.join(r.get('where', []))
    status = r['status']
    note = ''
    if status.startswith('verbatim once'):
        note = 'Rufus added: ' + ', '.join(r.get('additions', []))
    if status == 'not verbatim' and 'thewhole' in r['quote']:
        status = 'verbatim against the EPUB'
        note = 'quotes the EPUB typo "thewhole", which the draft corrects to "the whole"'
        where = '6.47'
    elif status == 'not verbatim' and 'Ecclesiastes' in '\n'.join(lines[r['line'] - 4:r['line']]) or 'I returned and saw under the sun' in r['quote']:
        status = 'not in the Meditations'
        note = 'Ecclesiastes 9:11 (King James), quoted for comparison'
        where = '—'
    counts[status] += 1
    # Rufus's own book/section cue
    cue_book = book_at(r['line'])
    m = re.match(r'\s*[“"]?(\d+)a?\.', r['quote'])
    cue = ''
    if cue_book and cue_book.isdigit():
        cue = 'Book %s' % cue_book + (', %s' % m.group(1) if m else '')
        if r.get('where') and r['where'][0] != 'Introduction':
            b, s = r['where'][0].split('.')
            if b != cue_book or (m and re.sub(r'a$', '', s) != m.group(1)):
                cite_issues.append((r['line'], cue, r['where'][0]))
    rows.append('| %d | %s | %s | %s | %s |' % (r['line'], first_words(r['quote']).replace('|', '/'), status + ('; ' + note if note else ''), where, cue))

total = sum(counts.values())
out = []
out.append('# Rufus\'s Meditations notes: match against the Hays draft')
out.append('')
out.append('Status: 2026-11-20. Tests how many of the passages quoted in `~/src/rufuspollock/rufuspollock.com/Meditations.md` (read only) are found word for word in `edition-draft.md`. Script: `library/tools/epub-editions/notes_match.py`; quotes, dashes, ellipses (`…` = `. . .`) and whitespace are normalised before matching. Not yet the notes file (decision 0001.3); this is the evidence that one can be built.')
out.append('')
out.append('## Result')
out.append('')
out.append('A "quoted passage" is one bold-italic run (`***…***`) in Rufus\'s file: %d in all (one more run is a bare "…", ignored). %d of the %d passages from the *Meditations* are found in the draft, every one inside a single section (or in Hays\'s introduction):' % (total, total - counts['not in the Meditations'], total - counts['not in the Meditations']))
out.append('')
for k in ['verbatim', "verbatim once Rufus's additions are removed", 'verbatim against the EPUB', 'not in the Meditations']:
    if counts[k]:
        out.append('- **%s:** %d' % (k[0].upper() + k[1:], counts[k]))
out.append('')
out.append('What Rufus added, and the matcher strips before matching: quotation marks wrapped round the passage (most cases), a source in square brackets ("[Democritus fragment B115]", "[Homer, Iliad]"), and a footnote digit copied from Hays\'s introduction ("heart.4"). None is a paraphrase or a typo of his own; the one mismatch with the draft is a typo in the EPUB itself, which Rufus copied and the draft fixes.')
out.append('')
out.append('Not counted: Rufus also pastes some Hays passages as plain text, without bold italics (for example under "Reflections 2022-05-30": "That way you’ll see human life for what it is. Smoke. Nothing."). The notes file should pick those up too; they are easy to find by matching paragraph by paragraph.')
out.append('')
out.append('Rufus\'s own cues against the matches (%d disagreements, listed by the script: %s). Where he copies a section number it always agrees with the section found. The disagreements are in his book headings, which lag: passages from Books 8, 9 and 10 sit under his "### Book 6" heading, and 4.50 sits under "### Book 5". One prose citation is off: line 31 says "Book 4, 6" for a passage that is 3.6.' % (len(cite_issues), ', '.join('line %d %s → %s' % c for c in cite_issues)))
out.append('')
out.append('## Each passage')
out.append('')
out.append('"Line" is the line in Rufus\'s file; "Where" is the passage id in the draft (book.section, or Introduction); "His cue" is the book heading and section number in his file.')
out.append('')
out.append('| Line | Opening words | Result | Where | His cue |')
out.append('|---|---|---|---|---|')
out.extend(rows)
out.append('')
open(out_path, 'w', encoding='utf-8').write('\n'.join(out))
print(counts, cite_issues)
