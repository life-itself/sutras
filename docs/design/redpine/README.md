# Round 2: the Red Pine page, copied closely

Rufus, 2026-11-21: "the site isn't bad, but it's not great… compared to Emergence it's not nearly as beautiful… I'd like a page which is really almost copying Emergence style… find substitute fonts for what it has, or use the fonts that Seeds of Renaissance had."

*Faith in Mind* set twice on the layout and colours of Emergence Magazine's [Red Pine poem page](https://emergencemagazine.org/poem/red-pine), changing only the faces:

- [Open faces](https://claude.ai/artifact/1EWyZdNMhjruSC3YTUN7Ta): Archivo Expanded for GT America Extended, Fraunces for Ogg, Archivo for GT America, Newsreader for Reckless.
- [Seeds faces](https://claude.ai/artifact/HDLYRfSpMtc2Sn8C13mxnh): Polyamine, Restora, Bricolage Grotesque, Apfel Grotezk. Polyamine and Restora are licensed to Seeds of Renaissance; `build.py` reads them from `~/src/life-itself/sor-website` and inlines them in the private mockup only. Using them on Sutras needs a licence check.

What was measured on the Red Pine page (Playwright, 1440 wide): all text slate blue `#5a7a8f` on paper about `#ece9e4`; title GT America Extended Bold 90px, tracked -4px; "translated by Red Pine" Ogg 90px; label GT America Condensed capitals; standfirst GT America 26px; credits in Reckless; images duotoned coral and slate; hairline rules; the Chinese set vertically beside the English.

What these pages take from it: the picture alone on the first screen; the extended grotesque over a fine display serif; everything in slate; a coral thread down the centre of the poem with each stanza's Chinese on it (zh.wikisource 信心銘, 146 phrases matching the translation's 146 lines); stanzas alternating sides; coral and slate duotones of Sesshū's *Haboku Sansui* bleeding off the edge. An art-director critique (Opus) was applied before showing: the coral sun disc was dropped as clip-art, the Chinese enlarged, the pictures faded into the paper, the notes gathered after the poem. Its seal-stamp idea was not taken (Rufus turned down the seals on the first board).

Build: `python3 docs/design/redpine/build.py` writes `out/open.html` and `out/seeds.html` (not committed); `shoot.py <dir> <files>` screenshots them at 1280 and 390. `img/` holds the duotones, made from the Commons scan (see `../images.md`).
