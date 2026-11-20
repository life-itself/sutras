# Verse and notes in the reading system: what we had to add

The reading system (v0.1) is built for prose. For a poem on Flowershow we added, all in `custom.css` and our copy of `js/reading.js`:

- **Verse:** one paragraph per stanza, lines ended with two spaces, inside `<div class="rs-verse">`. CSS turns off hyphenation and the Personal theme's small-caps first line. A hanging indent for wrapped lines is not possible this way (`text-indent` only reaches the first line of a paragraph, not lines after `<br>`); it would need one element per line.
- **Put the note marker at the end of a line,** after any dash: `…a flower in the sky —[^2]`. On a phone the note opens where the marker is; mid-line, it cuts the line in two.
- **Tap target:** upstream gives the note number `line-height: 0`, so its box is 9px by 0px. `custom.css` gives it padding on narrow screens.
- **Page-script safety:** `reading.js` adds window listeners and never removes them. Our copy removes them on `flowershow:page-leave` and returns early if the reader has already left (`sutras: 1` and `sutras: 3`).

These four, plus finding footnotes outside `.rs`, are worth sending upstream to `ux-patterns/reading-system` (Rufus's OK needed to edit that repo). Until then, when updating `css/reading.css` or `js/reading.js` from upstream, keep the lines marked `sutras:` in the script; the CSS file is an untouched copy.
