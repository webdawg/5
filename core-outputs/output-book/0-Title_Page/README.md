# 0-Title_Page (output)

The title page's generation code (`src/`) and rendered deliverable(s) (`render/`), produced from
`core-inputs/input-book/0-Title_Page/design-brief.md`. As of 2026-09-04, per The Output Format
Interviewer's round (`agents/output-format-interviewer.md`, `SPEC.md`'s "Format variants" section), this
piece has more than one format variant — `render/` holds one subfolder per variant, each with its own
`ARCHIVE/`, rather than a single flat render.

## Tooling

`src/generate.py`'s `build_composite()` composites the four layers in Python/Pillow: the source photo
(displayed black-and-white), a wireframe traced from the photo's own brightness (`src/trace_galaxy.py` —
a small dependency-free "graphics plugin"; no numpy/opencv/pip was available in this environment, checked
directly), a procedurally generated crayon layer (no AI image-generation tool was available either — a
small X circled at the galactic center, a circle with a kid-drawn stick figure in the bottom-left
corner, and a leaping arc between them, every shape hand-drawn-imperfect via `_wobble()`/
`_hand_drawn_circle()`), and the title/author text in a custom-built monospace all-caps font
(`src/blockfont.py` — a 5x7 stencil glyph set drawn from scratch, not a vendored typeface).
Deterministic — rerunning `python3 src/generate.py` reproduces the same image byte-for-byte. No fonts
are vendored at all anymore — Liberation Serif and Patrick Hand were both used at earlier points and
removed once no longer needed (the title/author font is hand-built, and the signature that used Patrick
Hand was removed entirely) — no unused files left in the repo.

Each format variant is its own script (per The Output Format Interviewer's 2026-09-04 tooling decision),
but every variant reuses `generate.py`'s `build_composite()` rather than re-running the procedural
generation at a different canvas size — the crayon/wireframe/font code draws in absolute pixel widths
tuned against `CANVAS_SIZE`, so a fresh composite at a smaller size would visibly drift from the print
one. `src/generate_web.py` and `src/generate_mobile.py` both build the same composite and resample it
(Pillow `LANCZOS`) down to their own target width instead.

## Format variants

- **`render/print/`** (`src/generate.py`) — 1650x2550 (5.5"x8.5" at 300 DPI), the original high-res
  print deliverable.
- **`render/web/`** (`src/generate_web.py`) — 1000x1545, resampled from the same composite, for a
  standard web-hosted page (the "output dedicated to normal website with regular web server" answer).
- **`render/mobile/`** (`src/generate_mobile.py`) — 750x1159, resampled narrower than the web variant
  but at a 2x-equivalent pixel density (a common "mobile @2x" asset-width convention for a ~375px
  logical viewport), so it stays crisp on typical mobile device pixel ratios rather than just being a
  smaller web image.

Still only documented, not built, from The Output Format Interviewer's full 2026-09-04 list: an
AI-accessibility variant, a human-accessibility variant, an animated/interactive variant, a puzzle
variant, and an age-censored variant — plus the separate, still-open "published, not just rendered" gap
(`SPEC.md`'s "Publishing" section) none of the built variants have reached yet.

## Status

In active iteration — under active review, being refined round by round against the rendered output
(see `render/print/ARCHIVE/`, `render/web/ARCHIVE/`, `render/mobile/ARCHIVE/` for prior versions and
`design-brief.md`'s "Iteration log" for what changed and why at each round).
