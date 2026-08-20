#!/usr/bin/env python3
"""Generates the title page's human-accessibility format variant, per The
Output Format Interviewer's 2026-09-04 round (agents/output-format-
interviewer.md, SPEC.md's "Format variants" section) -- "output
dedicated human accessibility."

Distinct from the AI-accessibility variant (generate_ai_accessible.py):
this one is plain-language prose, written the way a WCAG 1.1.1 long
description is meant to read to someone using a screen reader -- not
structured data, sentences a person listens to and understands.

Usage: python3 generate_human_accessible.py
Writes: ../render/human-accessible/title-page-description.txt (archives
        the previous file first -- see generate.py's archive_existing())
"""
import generate

RENDER_DIR = generate.RENDER_ROOT / "human-accessible"
RENDER_NAME = "title-page-description.txt"

DESCRIPTION = """\
Title page for the book "Infinity 0" by Agent 0 (a pen name).

This is a full-page illustration in black, white, and gray, with red
accents. It shows a real photograph of the Milky Way galaxy, our home
galaxy, converted to black and white -- a bright, cloudy band of stars
stretching diagonally across the page, darkest at the edges and brightest
along a dense central strip.

Layered over the photo is a thin, light-blue technical outline -- like a
map or diagram -- that traces the actual shape of the galaxy's bright
regions, branching and forking the way the galaxy's own structure does,
rather than a generic or invented pattern.

Drawn on top of that, in red crayon with a hand-drawn, imperfect look
(wobbly lines, a circle that doesn't quite close), are three things: a
small circle with an "X" inside it near the center of the galaxy,
marking a destination; a circle in the bottom-left corner containing a
simple stick figure, representing a child, standing in for Earth; and a
single curved line leaping from that circle out and up toward the X,
ending in an arrowhead. Together they suggest a child reaching from home
toward the center of the galaxy -- a visual for the book's theme of
hope, with children imagined as part of that hope and part of the
journey, not just decoration.

Near the top of the page, in bold, blocky, all-capital-letters monospace
lettering (a custom-built typeface, not a licensed font), is the book's
title: "INFINITY 0". Below it, smaller, in the same lettering: "BY AGENT
0". A soft, glowing light patch sits behind the title and author text so
they stay easy to read against the busy galaxy image behind them.

No other text, logos, or decoration appears on the page.
"""


def main() -> None:
    RENDER_DIR.mkdir(parents=True, exist_ok=True)
    generate.archive_existing(RENDER_DIR, RENDER_NAME)

    out_path = RENDER_DIR / RENDER_NAME
    out_path.write_text(DESCRIPTION)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
