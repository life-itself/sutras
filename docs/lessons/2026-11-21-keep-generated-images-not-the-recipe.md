# A generated image differs between machines: keep the image, redraw it only when its inputs change

The EPUB covers are drawn with Pillow. The same Pillow version, the same font and the same code gave different anti-aliasing on a Mac and on the Action's Linux runner (pixel differences up to 177 in the letter edges), so the Action re-committed all nine EPUBs after a Mac build. Every local rebuild would then show nine changed files to whichever track ran it.

The fix: keep each cover as a file (`downloads/covers/<slug>.png`, committed), with a hash of what it is drawn from (words, colours, font, the drawing function's source) in a PNG text chunk, and redraw only when the hash changes. Whichever machine draws it first, everyone else reuses it, and the EPUBs are byte-identical again.

Pinning the library is not enough. For anything rasterised (images, PDFs, fonts) in a build that is meant to be reproducible, commit the output and key it on its inputs.
