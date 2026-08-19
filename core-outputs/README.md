# core-outputs

The "core" side of an output: generation code/scripts plus the actual rendered result, organized by
input type — the output-side counterpart to `core-inputs/`. Distinct from `mediawiki-output/`'s
wiki-representation layer (rendered content or a link, per `SPEC.md`) and the generic, still-unused
`outputs/` scaffold — a `mediawiki-output/` page links here for non-wiki-shaped material (an image, a
script); this directory holds the material itself.

## Layout

- `output-book/` — the book-output case. See `output-book/README.md` for its structure. Folder names
  mirror `core-inputs/input-book/`'s 1:1, for traceability back to what each piece was produced from.

More output types get their own subdirectory here as they come up — nothing beyond `output-book/` exists
yet, and this directory isn't meant to be a generic catch-all ahead of an actual second type showing up.
