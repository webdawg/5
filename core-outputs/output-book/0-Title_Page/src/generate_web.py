#!/usr/bin/env python3
"""Generates the title page's web format variant, per The Output Format
Interviewer's 2026-09-04 round (agents/output-format-interviewer.md,
SPEC.md's "Format variants" section) -- "output dedicated to normal
website with regular web server," distinct from the print render already
built (generate.py).

Per that round's tooling decision, this is its own script rather than a
--format flag on generate.py -- but it reuses generate.py's
build_composite() rather than re-running the procedural generation at a
smaller canvas: the crayon/wireframe/font code draws in absolute pixel
widths tuned against CANVAS_SIZE, so composing fresh at a different size
would throw off their relative proportions and the web variant would
visibly drift from the print one. Same artwork, resampled down for
screen display -- not a second, independently-generated piece.

Usage: python3 generate_web.py
Reads:  ../../../../core-inputs/input-book/0-Title_Page/source-milky-way.jpg
        (via generate.py's build_composite())
Writes: ../render/web/title-page-web.png (archives the previous render
        first -- see generate.py's archive_existing())
"""
from PIL import Image

import generate

# A regular web server serving a full-page image, not a thumbnail --
# 1000px wide keeps the illustration and text legible at typical on-page
# display sizes while cutting file size well below the print render's
# 1650x2550. Aspect ratio matches CANVAS_SIZE exactly (5.5in x 8.5in).
WEB_WIDTH = 1000

RENDER_DIR = generate.RENDER_ROOT / "web"
RENDER_NAME = "title-page-web.png"


def main() -> None:
    RENDER_DIR.mkdir(parents=True, exist_ok=True)
    generate.archive_existing(RENDER_DIR, RENDER_NAME)

    composed = generate.build_composite().convert("RGB")
    scale = WEB_WIDTH / composed.width
    web_size = (WEB_WIDTH, round(composed.height * scale))
    resized = composed.resize(web_size, Image.LANCZOS)

    out_path = RENDER_DIR / RENDER_NAME
    resized.save(out_path, optimize=True)
    print(f"Wrote {out_path} ({web_size[0]}x{web_size[1]})")


if __name__ == "__main__":
    main()
