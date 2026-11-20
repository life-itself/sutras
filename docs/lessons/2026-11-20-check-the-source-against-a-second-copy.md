# A web source can be wrong in ways only a second copy shows

The Terebess page for *Faith in Mind* looked clean, and the edition matched it word for word. A second copy (the DharmaNet 1994 electronic edition, found through the NTU Buddhist library) showed two things the comparison with the source alone could not:

- Terebess had dropped five line-end dashes from the poem (the same page still has them where the talks quote the lines).
- The two copies word five lines differently ("as far apart" / "as far from it", "Nothing is not included" / "Nothing is excluded"). Neither is a typo; they look like two states of the translation. We kept the named source and listed the other readings in `library/faith-in-mind/NOTES.md`.

So: for each edition, find one other copy and diff the text against it, even when the source is HTML and not a scan. Twenty minutes. List what differs; change the text only where the source is plainly broken and the second copy (or the source itself) shows the right reading. The front matter of the second copy also gave the copyright line and the co-translator, which the source page lacks.

The script for the first half is `scripts/compare-source` (written for this one text; generalise it for the second edition).
