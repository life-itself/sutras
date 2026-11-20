#!/usr/bin/env python3
"""Build docs/design/<name>.html from <name>.src.html by inlining shots/*.jpg as data URIs.

Usage: python3 docs/design/build.py [name]   (default: brief; also: moodboard)
In brief.src.html write an image as: <img src="{{shot:NAME}}" alt="..."> (NAME.jpg lives in shots/).
Edit brief.src.html, never brief.html. Then republish brief.html to the same artifact URL (see README.md).
"""
import base64
import pathlib
import re
import sys

here = pathlib.Path(__file__).parent
name = sys.argv[1] if len(sys.argv) > 1 else "brief"
src = (here / f"{name}.src.html").read_text(encoding="utf-8")
missing = []


def inline(m):
    f = here / "shots" / (m.group(1) + ".jpg")
    if not f.exists():
        missing.append(m.group(1))
        return ""
    return "data:image/jpeg;base64," + base64.b64encode(f.read_bytes()).decode()


out = re.sub(r"\{\{shot:([a-z0-9-]+)\}\}", inline, src)
if missing:
    sys.exit("missing shots: " + ", ".join(missing))
(here / f"{name}.html").write_text(out, encoding="utf-8")
print(f"{name}.html written, {len(out) / 1e6:.2f} MB")
