# core-inputs

The raw, "core" side of an input: actual raw source content, organized by input type. Distinct from
`mediawiki-input/`'s wiki-representation layer (things + instructions, per `SPEC.md`) and the generic,
still-unused `inputs/` scaffold — a `mediawiki-input/` page points here for the real material; this
directory holds the material itself. Its output-side counterpart is `core-outputs/` — what gets produced
from this material (generation code/scripts plus the rendered result) lives there, not here.

## Layout

- `input-book/` — the book-input case. See `input-book/README.md` for its structure.

More input types get their own subdirectory here as they come up — nothing beyond `input-book/` exists
yet, and this directory isn't meant to be a generic catch-all ahead of an actual second type showing up.
