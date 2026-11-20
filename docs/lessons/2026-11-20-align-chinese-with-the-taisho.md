# Align a web transcription of Chinese with the Taishō

The sacred-texts Mumonkan gives the Chinese from a Japanese website, and that site's typist could not enter 36 rare characters (empty boxes) and mistyped about 40 others as characters of similar shape: 堅 for 竪 "raise" (so "Gutei Raises a Finger" read "Gutei Firm Finger"), 方 for 法 in 正法眼藏, 問 for 門 in 無門曰, a dash for 一. None of this shows when you compare the page with its own source.

What worked: CBETA publishes the Taishō canon as TEI XML on GitHub (`cbeta-org/xml-p5`, e.g. `T/T48/T48n2005.xml`). Strip tags (keep `<g>` contents, drop `<note>`), drop punctuation from both texts, and align them section by section with `difflib.SequenceMatcher` on characters. Then:

- boxes: take the Taishō character at each box; it came out one-for-one for all 36;
- the rest: list every difference, treat common variant forms (爲/為, 説/說, 衆/眾) as equal, and read what is left. Fix only where the source's character is a look-alike that makes no sense and the translator's English needs the Taishō's; keep real differences of reading (the Japanese edition is not the Taishō) and list them.

Twenty minutes of script for 7,900 characters. Some Taishō characters are outside the Basic Multilingual Plane (𦗚, 𣔻, 𨁝): a regex over `㐀-鿿` misses them; add `\U00020000-\U0003ffff`. Scripts: `library/gateless-gate-mumonkan/compare_chinese.py`, fixes in `fixes.py`.
