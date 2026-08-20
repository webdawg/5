#!/usr/bin/env python3
"""Generates the title page's AI-accessibility format variant, per The
Output Format Interviewer's 2026-09-04 round (agents/output-format-
interviewer.md, SPEC.md's "Format variants" section) -- "output
dedicated to AI accessibility."

Distinct from the human-accessibility variant (generate_human_accessible.py):
this one is structured data (JSON) for programmatic consumption -- fields,
coordinates, color values -- not prose. An AI agent reading this doesn't
need the pixels to know what the title page depicts, same way a sighted
human doesn't need alt text to know what an image shows.

Sourced from the same constants generate.py's composite is built from
(colors, canvas size, title/author strings, layout fractions) rather than
re-describing the image by inspecting pixels -- one source of truth for
the design, per CODEBOT.md.

Usage: python3 generate_ai_accessible.py
Writes: ../render/ai-accessible/title-page.json (archives the previous
        file first -- see generate.py's archive_existing())
"""
import json

import generate

RENDER_DIR = generate.RENDER_ROOT / "ai-accessible"
RENDER_NAME = "title-page.json"

TITLE = "Infinity 0"
AUTHOR = "Agent 0"


def build_description() -> dict:
    return {
        "title": TITLE,
        "author": AUTHOR,
        "author_is_pseudonym": True,
        "piece_type": "book title page (front matter)",
        "canvas": {
            "width_px": generate.CANVAS_SIZE[0],
            "height_px": generate.CANVAS_SIZE[1],
            "dpi": generate.DPI,
            "trim_size_in": [5.5, 8.5],
        },
        "layers_back_to_front": [
            {
                "name": "background",
                "type": "photograph",
                "source": "NASA/Goddard Space Flight Center Milky Way photo, public domain, 2003",
                "source_url": "https://commons.wikimedia.org/wiki/File:Milky_Way_galaxy.jpg",
                "display": "converted to black-and-white (black background lightened to white first)",
            },
            {
                "name": "wireframe",
                "type": "generated overlay",
                "description": (
                    "A futuristic wireframe map traced from the background photo's own "
                    "brightness structure -- two closed contour levels plus a topological "
                    "skeleton (medial-axis thinning) branching wherever the photo's bright "
                    "structure actually branches, not an abstract or randomly-generated shape."
                ),
                "color_rgb": list(generate.WIREFRAME_COLOR),
            },
            {
                "name": "crayon",
                "type": "generated overlay",
                "description": (
                    "A hand-drawn-imperfect crayon layer, all in one color: a small circled X "
                    "at the galactic center marking where a child wants to go, a circle in the "
                    "bottom-left corner containing a stick-figure child ('earth'), and a single "
                    "leaping arc connecting the two, ending in an arrowhead pointing at the X. "
                    "Represents a child reading along and participating, not just decoration -- "
                    "the book's theme is hope, and children are part of that hope."
                ),
                "color_rgb": list(generate.CRAYON_COLOR),
            },
            {
                "name": "title_text",
                "type": "text",
                "text": TITLE.upper(),
                "font": "custom-built monospace all-caps stencil font (not a vendored typeface)",
                "color_rgb": list(generate.TITLE_COLOR[:3]),
                "position_from_top_fraction": generate.TITLE_TOP_FRACTION,
                "note": "working title, not yet final",
            },
            {
                "name": "author_text",
                "type": "text",
                "text": f"BY {AUTHOR.upper()}",
                "font": "same custom font as title_text, smaller",
                "color_rgb": list(generate.TITLE_COLOR[:3]),
            },
        ],
        "semantic_summary": (
            "The title page for the science-fiction book Infinity 0 by Agent 0 (a pseudonym). "
            "A black-and-white NASA photo of the Milky Way fills the page, overlaid with a "
            "cyan technical wireframe tracing the galaxy's real structure, and a red hand-drawn "
            "crayon mark showing a child figure on Earth reaching toward a destination at the "
            "galactic center. The title and author appear near the top in a custom blocky "
            "monospace font."
        ),
    }


def main() -> None:
    RENDER_DIR.mkdir(parents=True, exist_ok=True)
    generate.archive_existing(RENDER_DIR, RENDER_NAME)

    out_path = RENDER_DIR / RENDER_NAME
    out_path.write_text(json.dumps(build_description(), indent=2) + "\n")
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
