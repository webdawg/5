#!/usr/bin/env python3
"""Generates the title page's age-censored format variant, per The Output
Format Interviewer's 2026-09-04 round (agents/output-format-interviewer.md,
SPEC.md's "Format variants" section) -- "output dedicated to age
censoring."

This builds the actual censoring *mechanism* -- CENSOR_REGIONS below is a
list of (box, reason) pairs to Gaussian-blur over the print composite --
rather than fabricating something age-inappropriate to demonstrate it on.
The title page's own content (a galaxy photo, a technical wireframe, a
red crayon drawing of a child reaching toward a destination) has nothing
in it that warrants censoring for any age group -- the design brief's own
theme is "the book is about hope, and children are part of that hope."
CENSOR_REGIONS is empty here on purpose, not left empty by oversight; a
future, more mature story input would populate it and get a real blurred
variant out of the same script, unchanged.

Usage: python3 generate_age_censored.py
Writes: ../render/age-censored/title-page-age-censored.png (archives the
        previous render first -- see generate.py's archive_existing())
"""
from PIL import Image, ImageFilter

import generate

RENDER_DIR = generate.RENDER_ROOT / "age-censored"
RENDER_NAME = "title-page-age-censored.png"

# Each entry: ((left, top, right, bottom) in print-canvas pixels, "reason").
# Empty for the title page -- see module docstring.
CENSOR_REGIONS: list[tuple[tuple[int, int, int, int], str]] = []


def apply_censor_regions(composed: Image.Image) -> Image.Image:
    """Heavily blurs each flagged region in place. A no-op when
    CENSOR_REGIONS is empty, which is the correct, honest output for a
    piece with nothing to censor -- not a placeholder for missing work."""
    if not CENSOR_REGIONS:
        return composed
    out = composed.copy()
    for box, _reason in CENSOR_REGIONS:
        region = out.crop(box).filter(ImageFilter.GaussianBlur(40))
        out.paste(region, box)
    return out


def main() -> None:
    RENDER_DIR.mkdir(parents=True, exist_ok=True)
    generate.archive_existing(RENDER_DIR, RENDER_NAME)

    composed = generate.build_composite().convert("RGB")
    censored = apply_censor_regions(composed)

    out_path = RENDER_DIR / RENDER_NAME
    censored.save(out_path, dpi=(generate.DPI, generate.DPI))
    note = "no regions flagged for this piece" if not CENSOR_REGIONS else f"{len(CENSOR_REGIONS)} region(s) blurred"
    print(f"Wrote {out_path} ({note})")


if __name__ == "__main__":
    main()
