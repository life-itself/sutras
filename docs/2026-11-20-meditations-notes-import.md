# Rufus's Meditations notes: import report

Date: 2026-11-20. Bead sutras-m2v.9.3. Source (read only): `~/src/rufuspollock/rufuspollock.com/Meditations.md` (page dated 2024-07-15; one section "Reflections 2022-05-30"). Result: `annotations/meditations.yaml`, shown on [/meditations](https://sutras.lifeitself.org/meditations). Importer: `annotations/import/meditations_from_rufuspollock_com.py` (one-off; the YAML is edited by hand from now on). An earlier match by the newtexts track (`library/meditations/rufus-notes-match.md`) found the same: every quotation from the *Meditations* is in the Hays text.

## Result

- **122 notes, 55 with Rufus's comments**, the rest plain highlights (the other paragraphs of the same quotation). Every quote is checked by `scripts/notes` against `meditations.md`, word for word.
- **Quoted paragraphs on his page:** 117 bold-italic quotations plus 5 Hays passages he pasted as plain text (e.g. "That way you’ll see human life for what it is. Smoke. Nothing."), which are now highlights too.
- **Not matched: 1.** Ecclesiastes 9:11 (King James), which Rufus quotes for comparison under "Dualities and concepts are traps for the unwary mind". It is not in the *Meditations*, so it stays in his comment as a quotation.
- **Shown on the page: 121 of 122.** Rufus's quote from 4.14 ("To the logos from which all things spring.") is in the text but the page shows "spring*.*" (an italic full stop Markdown cannot render), so the page cannot find it. Bead sutras-m2v.7.15 for the edition; the note appears once that is fixed.

## What was changed from Rufus's page, and why

- **The words of each quote come from the edition, not from his copy.** His copies differ only by additions, never by wording: wrapping quotation marks, a section number ("23."), a source in brackets ("[Democritus fragment B115]", "[Homer, Iliad]"), a footnote digit copied from Hays's introduction ("heart.4"), "…" for Hays's ". . .", and one ebook typo ("thewhole") that the edition corrects.
- **Each comment sits on the first quotation it belongs to:** the heading (in bold), the lines just before the quotes, and the lines after the last quote under that heading. The other paragraphs of a quotation are highlights without a note.
- **Left out:** the page's opening line ("Thoughts and commentary on Marcus Aurelius' Meditations in the Hays translation"), the image, "BTW this is all based on the Hays translation", the note "For some reason I seem to have made annotations here in two places. Oh well. Most of this commentary is just on book 4.", and two connecting words between quotations ("Or", "It continues:").
- **Kept as he wrote them:** his headings, emoji (👍, 🚩, 🔥, 🌷) and links to notes.lifeitself.org. His own citations are kept even where they are off: "Or on virtues see Book 4, 6" introduces a passage that is 3.6, and passages from Books 8, 9 and 10 sit under his "Book 6" heading (the passage ids in the notes file are right).
- **Repeats:** Rufus quotes 5.23–24 and 3.6 twice, under different headings, so those passages carry two notes each.
- **Choices among several:** "Remember:" occurs in 5.9, 5.24 and 8.15; it was placed in 5.24, the section number he copied.
- **Dates:** every note is dated 2024-07-15, the page's date; the "Reflections" notes may be from 2022-05-30.

## For Rufus

The notes are his words, lightly arranged; worth a look on the live page to see if the arrangement reads right (which comment sits on which quote), and whether 122 highlights are too many: most of his quotations are whole entries, so long stretches of the text are highlighted.
