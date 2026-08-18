# input-book

Raw, per-story source content for a book input. One folder per story, directly under here — no
book-name layer for now, since there's only one book (`Infinity 0`, see
`mediawiki-input/Infinity_0`); revisit if a second book shows up.

## Layout (illustrative — not real story titles)

```
input-book/
├── 0-Some_Story_Title/
│   ├── priority.txt
│   └── manuscript.txt
├── 1-Another_Story_Title/
│   ├── priority.txt
│   └── manuscript.txt
└── ...
```

- **Folder name** — `<N>-<Story_Title>`: `N` is a rough, human-sortable order hint; `Story_Title` uses
  underscores for spaces, matching the same convention as `mediawiki-input/`'s page filenames.
- **`priority.txt`** — a single integer. This is the **authoritative** order, not the folder-name
  number. Reordering a story means editing this file, not renaming the folder, so reordering never
  breaks anything that references the folder by name. If the folder-name number and `priority.txt` ever
  disagree, `priority.txt` wins.
- **`manuscript.txt`** — the raw, unedited story text itself.

## Status

No real story folders exist here yet. `Infinity 0`'s 495+ pages haven't been split into individually
named/titled stories yet — that's exactly the split this structure is for. Folders get added here as
individual stories are identified out of the corpus, not all at once upfront.
