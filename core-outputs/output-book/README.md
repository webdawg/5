# output-book

What gets produced for each piece of the book input — one folder per story or front-matter piece,
directly under here, named to match its `core-inputs/input-book/` counterpart exactly. No book-name
layer for now, same reasoning as the input side: only one book (`Infinity 0`) exists.

Per `SPEC.md`'s "Fan-out" section, one input piece isn't limited to one output — the title page alone
could reasonably need a print-resolution render, a web-optimized version, and more, each a distinct
deliverable. A piece could end up needing anywhere from one output to several; this layout doesn't
presume a fixed number.

## Layout (illustrative)

```
output-book/
├── 0-Title_Page/
│   ├── src/              -- generation code/scripts: the tool, not a one-off
│   └── render/            -- current rendered deliverable(s)
│       ├── title-page-print.png
│       └── ARCHIVE/       -- superseded versions, kept not overwritten
│           ├── title-page-print-v1.png
│           └── title-page-print-v2.png
└── ...
```

- **Folder name** — `<N>-<Title>`, matching the corresponding `core-inputs/input-book/` folder.
- **`src/`** — the generation code/scripts that produce the piece. Built as a real, reusable tool for
  this output, not a throwaway script — per the 2026-08-19 output interview on `0-Title_Page`.
- **`render/`** — the current rendered deliverable(s). One piece may have several (different formats,
  resolutions, or purposes), added as they're actually needed rather than all upfront.
- **`render/ARCHIVE/`** — every superseded version, versioned (`-v1`, `-v2`, ...), never overwritten or
  deleted. Whenever a piece's generation tool produces a new render, the file it replaces moves here
  first — per the 2026-08-19 versioning instruction. This is production iteration history, not the same
  thing as `prompt-log/`'s prompt history or `INTENT.md`'s decision history, though all three overlap in
  what they explain about how a piece ended up the way it did.

Exact internal shape (subfolder names, how multiple deliverables get distinguished) isn't fixed by this
layout — `src/`/`render/` here is illustrative, not a hard requirement, and may get revised once a real
piece has gone all the way through production.

## Status

`0-Title_Page/` is reserved — the output interview settled what belongs here (a real generation tool
plus a high-res render first, other formats later) but production hasn't started, so nothing exists yet.
