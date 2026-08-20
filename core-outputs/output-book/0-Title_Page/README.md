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
but the three image variants all reuse `generate.py`'s `build_composite()` rather than re-running the
procedural generation at a different canvas size — the crayon/wireframe/font code draws in absolute pixel
widths tuned against `CANVAS_SIZE`, so a fresh composite at a smaller size would visibly drift from the
print one. `src/generate_web.py` and `src/generate_mobile.py` resample it (Pillow `LANCZOS`) down to
their own target width; `src/generate_age_censored.py` runs it through a (currently empty) censor-region
pass. The two interactive variants (`src/generate_interactive.py`, `src/generate_puzzle.py`) are each a
single self-contained HTML file — one already-rendered PNG embedded as base64, vanilla CSS/JS, no
external requests or framework — since no web/JS technology stack has been decided for the project
generally (`SPEC.md`'s Fan-out territory) and this role only owns format variants of the already-decided
title page image, not a new output type. The two accessibility variants
(`src/generate_ai_accessible.py`, `src/generate_human_accessible.py`) are text, not images — structured
JSON for machine consumption vs. WCAG-style prose for a screen reader — both sourced from the same
design constants `generate.py` uses, not by inspecting pixels.

## Format variants

- **`render/print/`** (`src/generate.py`) — 1650x2550 (5.5"x8.5" at 300 DPI), the original high-res
  print deliverable.
- **`render/web/`** (`src/generate_web.py`) — 1000x1545, resampled from the same composite. **Not** the
  webpage output itself (that was a 2026-09-04 misclassification, corrected 2026-09-08 — see `SPEC.md`'s
  "Webpage output" section) — this PNG is now the embedded image inside this piece's actual book page,
  `publish-output/web-book/render/pages/page-000-title-page.html` (moved there 2026-09-09, `SPEC.md`'s
  "Publishing" section). Kept as its own format
  variant regardless, since a plain web-resolution image is still independently useful (thumbnails,
  social previews, embedding).
- **`render/mobile/`** (`src/generate_mobile.py`) — 750x1159, resampled narrower than the web variant
  but at a 2x-equivalent pixel density (a common "mobile @2x" asset-width convention for a ~375px
  logical viewport), so it stays crisp on typical mobile device pixel ratios rather than just being a
  smaller web image.
- **`render/ai-accessible/`** (`src/generate_ai_accessible.py`) — `title-page.json`, a structured
  machine-readable description (layers, colors, text, layout) for AI/programmatic consumption.
- **`render/human-accessible/`** (`src/generate_human_accessible.py`) — `title-page-description.txt`, a
  WCAG-1.1.1-style plain-language long description, written for a screen reader.
- **`render/interactive/`** (`src/generate_interactive.py`) — a self-contained HTML page: the web PNG,
  pannable by drag, zoomable by scroll/pinch, with a slow continuous ambient zoom animation. Answers
  "a moving animated version that users can move if they want."
- **`render/puzzle/`** (`src/generate_puzzle.py`) — a self-contained HTML tap-to-swap tile puzzle (4x5
  grid) built from the mobile PNG via CSS background-position slicing — no server-side image slicing, no
  game framework. The generated file is deterministic; the shuffle re-randomizes every page load, on
  purpose.
- **`render/age-censored/`** (`src/generate_age_censored.py`) — the actual censoring *mechanism*
  (flagged regions get Gaussian-blurred), not a demonstration on fabricated content. `CENSOR_REGIONS` is
  empty for this piece on purpose: the title page's own content (a galaxy photo, a wireframe, a child
  reaching toward a destination) has nothing in it that warrants censoring for any age group. A more
  mature story input would populate the same list and get a real blurred variant from the same script,
  unchanged.

Still open, not attempted here: the separate "published, not just rendered" gap (`SPEC.md`'s "Publishing"
section) — none of the built variants have reached an externally-reachable location, only `render/`.

## Status

Format-variant set complete per The Output Format Interviewer's 2026-09-04 list (2026-09-07). The
underlying artwork itself is still in active iteration — refined round by round against the rendered
output (see `render/print/ARCHIVE/`, `render/web/ARCHIVE/`, `render/mobile/ARCHIVE/`, and the other
variants' own `ARCHIVE/` folders for prior versions; `design-brief.md`'s "Iteration log" for what changed
and why at each round). The interactive and puzzle HTML files were checked structurally (valid output,
no unresolved template placeholders) but not opened in a live browser — worth a manual check before
treating either as done.
