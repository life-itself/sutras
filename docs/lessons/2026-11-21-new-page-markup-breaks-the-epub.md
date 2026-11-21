# New markup on an edition page can break the EPUB, and nobody sees it

The design added `<figure class="sd-art"><img src="/assets/images/<slug>.jpg" alt="">` above every edition's title. The site was fine; the EPUB Action failed on the next six pushes and the downloads quietly went stale, because nobody watches a red run on a workflow they did not touch.

Two faults, both from passing raw HTML through Pandoc:

- Pandoc writes a raw `alt=""` back as a bare `alt` (the HTML form), which is not XML, so epubcheck stops with a fatal RSC-016 on that chapter. Any empty attribute in raw HTML does this.
- A site path (`/assets/...`) is not a file path, so Pandoc cannot fetch the image and leaves a dead reference.

The fix was to turn the figure into a Markdown image resolved from the repo root (`--resource-path`), so Pandoc packages it, and to move it onto the title page afterwards.

**When you add markup to edition pages, run `scripts/epub <one slug>` before pushing,** or at least look at `gh run list --workflow=epub.yml` after. A new kind of element needs a line in `to_book()` in `scripts/epub`.
