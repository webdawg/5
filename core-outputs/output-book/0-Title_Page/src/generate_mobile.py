#!/usr/bin/env python3
"""Generates the title page's mobile format variant, per The Output
Format Interviewer's 2026-09-04 round (agents/output-format-interviewer.md,
SPEC.md's "Format variants" section) -- "an output for mobile," distinct
from the print (generate.py) and standard web (generate_web.py) variants
already built.

Same reuse rationale as generate_web.py: resamples generate.py's shared
build_composite() rather than re-running the procedural generation at a
smaller canvas, so this stays the same artwork as every other variant,
not an independently drifting one.

Sized narrower than generate_web.py's 1000px "regular web server" target
but at a 2x-equivalent pixel density -- mobile viewports are physically
smaller than desktop but commonly render at 2x/3x device pixel ratio, so
a naively small image reads soft on-device. 750px wide is a common
"mobile @2x" asset-width convention for a page designed around a ~375px
logical viewport width.

Usage: python3 generate_mobile.py
Reads:  ../../../../core-inputs/input-book/0-Title_Page/source-milky-way.jpg
        (via generate.py's build_composite())
Writes: ../render/mobile/title-page-mobile.png (archives the previous
        render first -- see generate.py's archive_existing())
"""
from PIL import Image

import generate

MOBILE_WIDTH = 750

RENDER_DIR = generate.RENDER_ROOT / "mobile"
RENDER_NAME = "title-page-mobile.png"


def main() -> None:
    RENDER_DIR.mkdir(parents=True, exist_ok=True)
    generate.archive_existing(RENDER_DIR, RENDER_NAME)

    composed = generate.build_composite().convert("RGB")
    scale = MOBILE_WIDTH / composed.width
    mobile_size = (MOBILE_WIDTH, round(composed.height * scale))
    resized = composed.resize(mobile_size, Image.LANCZOS)

    out_path = RENDER_DIR / RENDER_NAME
    resized.save(out_path, optimize=True)
    print(f"Wrote {out_path} ({mobile_size[0]}x{mobile_size[1]})")


if __name__ == "__main__":
    main()
