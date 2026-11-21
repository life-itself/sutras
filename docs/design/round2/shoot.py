"""Screenshot the round 2 pages at 1280 and 390 (device emulation) and report horizontal overflow."""
import pathlib, sys
from playwright.sync_api import sync_playwright
CH = "/Users/rgrp/Library/Caches/ms-playwright/chromium-1234/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing"
OUT = pathlib.Path(__file__).parent / "out"
dest = pathlib.Path(sys.argv[1]); pages = sys.argv[2:] or ["index", "faith-in-mind", "seneca", "mumonkan", "faces"]
(OUT / "_index.html").write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"></head><body>' + (OUT / "index.html").read_text() + "</body></html>")
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CH)
    for name in pages:
        f = OUT / ("_index.html" if name == "index" else name + ".html")
        for w, h, mob in [(1280, 800, False), (1440, 900, False), (390, 844, True)]:
            ctx = b.new_context(viewport={"width": w, "height": h}, device_scale_factor=1, is_mobile=mob, has_touch=mob)
            pg = ctx.new_page(); pg.goto(f.as_uri(), wait_until="domcontentloaded", timeout=60000); pg.wait_for_timeout(2500)
            sw = pg.evaluate("document.documentElement.scrollWidth")
            wide = pg.evaluate("""() => [...document.querySelectorAll('body *')].filter(e => e.getBoundingClientRect().right > innerWidth + 1 && getComputedStyle(e).position !== 'fixed').slice(0,5).map(e => e.tagName + '.' + e.className)""")
            pg.screenshot(path=str(dest / f"{name}-{w}.png"), full_page=True)
            print(name, w, "scrollWidth", sw, "height", pg.evaluate("document.body.scrollHeight"), "overflow:", wide if sw > w else "none")
            ctx.close()
    b.close()
