# input-book

Raw, per-story source content for a book input, plus front-matter pieces that have no raw manuscript to
begin with (authored straight to output — see `IDEAS.md`'s "A Creation Interview" entry). One folder per
story or front-matter piece, directly under here — no book-name layer for now, since there's only one
book (`Infinity 0`, see `mediawiki-input/Infinity_0`); revisit if a second book shows up.

## Layout (illustrative — not real story titles)

```
input-book/
├── 0-Title_Page/
│   └── (generation code + source assets, once produced — see Status)
├── 1-Some_Story_Title/
│   ├── priority.txt
│   └── manuscript.txt
├── 2-Another_Story_Title/
│   ├── priority.txt
│   └── manuscript.txt
└── ...
```

- **Folder name** — `<N>-<Title>`: `N` is a rough, human-sortable order hint; `Title` uses underscores
  for spaces, matching the same convention as `mediawiki-input/`'s page filenames.
- **Story folders** hold **`priority.txt`** (a single integer — the **authoritative** order, not the
  folder-name number; reordering a story means editing this file, not renaming the folder, so reordering
  never breaks anything that references the folder by name) and **`manuscript.txt`** (the raw, unedited
  story text itself).
- **Front-matter folders** hold no manuscript — there's no raw draft, the content is authored directly.
  Instead: whatever was actually used to produce the piece (generation code, source assets like images
  or fonts), so it's reproducible from what's in the repo, not just the rendered result living on the
  output side.

## Status

`0-Title_Page/` is reserved for the book's title page — design is still being interviewed (background
image layers, a code-generated wireframe map, title typography; see `mediawiki-output/Infinity_0` for
the settled parts) — nothing generated yet, so the folder holds no code/assets so far. No story folders
exist either yet: `Infinity 0`'s 495+ pages haven't been split into individually named/titled stories.
Folders get added here as pieces are ready, not all at once upfront.
