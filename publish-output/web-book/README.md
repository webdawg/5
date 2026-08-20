# web-book (output)

The book's webpage output type (`SPEC.md`'s "Webpage output" section) — a directory of static HTML
pages a reader clicks through sequentially, like flipping pages in a physical book. Added 2026-09-08,
correcting an earlier mistake: a resized static image (`core-outputs/output-book/0-Title_Page/render/
web/title-page-web.png`) had been built and documented as "the web format variant," but that's not what
a webpage output actually is — see `INTENT.md`'s 2026-09-08 addendum.

Lives under `publish-output/` (moved here 2026-09-09), spanning the whole book, rather than nested
inside any single asset's own `core-outputs/output-book/<N>-<Name>/` folder — this output type isn't
scoped to one asset. `publish-output/` holds final, ready-to-publish deliverables only (`SPEC.md`'s
"Publishing" section); `core-outputs/` still holds the generation code and iteration history for
everything else, unchanged. web-book moved here whole (source and render together) since, unlike a
hand-tuned image, it has no iteration history to leave behind.

## Tooling

`src/build.py` scans `core-inputs/input-book/*/priority.txt` for every asset (story or front matter),
sorts by that authoritative order, and for each one finds its already-rendered web-resolution image at
`core-outputs/output-book/<N>-<Name>/render/web/*.png` — for the title page, the file `generate_web.py`
already produces. Generates one self-contained HTML page per asset (image embedded as base64, no
external requests — same dependency-free approach as `render/interactive/` and `render/puzzle/`, since
no real web/JS framework has been decided for the project generally), with "← Previous" / "Next →" links
between consecutive pages (present only where a neighbor actually exists — no disabled buttons, no
auto-redirects). `render/pages/index.html` links to the first page.

Only produces the *directory* — matches `SPEC.md`'s "Publishing" section: this is a render, not yet
published anywhere a reader would actually reach it.

Usage: `python3 src/build.py`. Deterministic given the same ordered set of assets and the same source
images; rerunning regenerates every page (all pages depend on the full ordered set for their prev/next
links, so there isn't a meaningful "only rebuild what changed" version yet — fine at one asset, worth
revisiting once there are many).

## Open

- A future story's page needs real page content (typeset prose), not just an embedded image the way the
  title page's page works — `SPEC.md`'s open question, not resolved here.
- No per-page `ARCHIVE/` versioning (unlike `0-Title_Page/render/print/ARCHIVE/` etc.) — this is a
  mechanical rebuild from already-rendered assets and current ordering, not an iteratively hand-tuned
  artifact, so versioning every page on every asset addition seemed like more overhead than value. Worth
  reconsidering if that turns out wrong.
