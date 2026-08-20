# input-book

Raw, per-story source content for a book input, plus front-matter pieces that have no raw manuscript to
begin with (authored straight to output — see `IDEAS.md`'s "A Creation Interview" entry). One folder per
story or front-matter piece, directly under here — no book-name layer for now, since there's only one
book (`Infinity 0`, see `mediawiki-input/Infinity_0`); revisit if a second book shows up.

Its output-side counterpart is `core-outputs/output-book/` — folder names match 1:1 for traceability, but
what lives in each is different: this side holds the *input* to production (a manuscript, or for
front matter, the design brief the Creation Interview produced, plus any actual raw source material used
as an ingredient). The generation code/scripts and the rendered result itself are outputs, not inputs —
they live on the other side, in `core-outputs/output-book/`, even for a piece that was authored rather
than edited from a draft.

## Layout (illustrative — not real story titles)

```
input-book/
├── 0-Title_Page/
│   ├── priority.txt
│   └── design-brief.md
├── 1-Some_Story_Title/
│   ├── priority.txt
│   └── manuscript.txt
├── 2-Another_Story_Title/
│   ├── priority.txt
│   └── manuscript.txt
└── ...
```

- **Folder name** — `<N>-<Title>`: `N` is a rough, human-sortable order hint; `Title` uses underscores
  for spaces, matching the same convention as `mediawiki-input/`'s page filenames. Matches the
  corresponding `core-outputs/output-book/` folder name exactly.
- **Every folder** holds **`priority.txt`** (a single integer — the **authoritative** order, not the
  folder-name number; reordering means editing this file, not renaming the folder, so reordering never
  breaks anything that references the folder by name) — extended 2026-09-08 (`SPEC.md`'s "Webpage
  output" section) from story folders to *every* folder, front matter included, so the webpage output's
  page-ordering has one source across every kind of asset rather than special-casing front matter as
  "always first."
- **Story folders** additionally hold **`manuscript.txt`** (the raw, unedited story text itself).
- **Front-matter folders** hold no manuscript — there's no raw draft, so the Creation Interview's settled
  decisions stand in for one: a design brief (what the piece depicts/contains, and why), which is this
  piece's actual raw input. May also hold true raw source material pulled in as an ingredient (e.g. a
  reference image), but not generation code or rendered output — see `core-outputs/output-book/`.

## Status

`0-Title_Page/` holds the book's title page's design brief (`design-brief.md`) — the Creation Interview's
settled decisions: background image layers, a code-generated wireframe map, title typography (see
`mediawiki-output/Infinity_0` too). No story folders exist yet: `Infinity 0`'s 495+ pages haven't been
split into individually named/titled stories. Folders get added here as pieces are ready, not all at
once upfront.
