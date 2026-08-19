# 0-Title_Page (output)

The title page's generation code (`src/`) and rendered deliverable(s) (`render/`), produced from
`core-inputs/input-book/0-Title_Page/design-brief.md`.

## Tooling

`src/generate.py` composites the four layers in Python/Pillow: the source photo (displayed
black-and-white), a wireframe traced from the photo's own brightness (`src/trace_galaxy.py` — a small
dependency-free "graphics plugin"; no numpy/opencv/pip was available in this environment, checked
directly), a procedurally generated crayon layer (no AI image-generation tool was available either — a
small X circled at the galactic center, a circle with a kid-drawn stick figure in the bottom-left
corner, and a leaping arc between them, every shape hand-drawn-imperfect via `_wobble()`/
`_hand_drawn_circle()`), and the title/author text in a custom-built monospace all-caps font
(`src/blockfont.py` — a 5x7 stencil glyph set drawn from scratch, not a vendored typeface).
Deterministic — rerunning `python3 src/generate.py` reproduces the same image byte-for-byte. No fonts
are vendored at all anymore — Liberation Serif and Patrick Hand were both used at earlier points and
removed once no longer needed (the title/author font is hand-built, and the signature that used Patrick
Hand was removed entirely) — no unused files left in the repo.

## Status

In active iteration — under active review, being refined round by round against the rendered output
(see `render/ARCHIVE/` for prior versions and `design-brief.md`'s "Iteration log" for what changed and
why at each round).
