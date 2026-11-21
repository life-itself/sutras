import sys
from playwright.sync_api import sync_playwright
CH="/Users/rgrp/Library/Caches/ms-playwright/chromium-1234/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing"
outdir=sys.argv[1]; files=sys.argv[2:]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path=CH)
    for f in files:
        name=f.rsplit("/",1)[-1].replace(".html","")
        for w,h,mob in [(1280,800,False),(390,844,True)]:
            ctx=b.new_context(viewport={"width":w,"height":h},device_scale_factor=1 if not mob else 2,is_mobile=mob,has_touch=mob)
            import pathlib as _pl
            w_=_pl.Path(f).with_suffix(".wrapped.htm"); w_.write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"></head><body>'+_pl.Path(f).read_text()+'</body></html>')
            pg=ctx.new_page(); pg.goto("file://"+str(w_)); pg.wait_for_timeout(2500)
            sw=pg.evaluate("document.documentElement.scrollWidth")
            pg.screenshot(path=f"{outdir}/{name}-{w}.png",full_page=True)
            print(name,w,"scrollWidth",sw,"height",pg.evaluate("document.body.scrollHeight"))
            ctx.close()
    b.close()
