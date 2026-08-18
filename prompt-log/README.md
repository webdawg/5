# Prompt Log

Raw, unedited history of the prompts given to the AI assistant working on this project. Deliberately
separate from `SPEC.md`/`INTENT.md`: those curate prompts into organized, analyzed decisions; this
directory preserves the actual, verbatim input as given — typos, shorthand, mid-turn interruptions, and
all — including prompts that never became a formal spec change (status checks, questions, one-off asks).

This convention showed up independently in two other repos before landing here — worth noting because
this project is *about* the input/output pattern: this log is itself an instance of it. The raw prompt
is the input; a curated `INTENT.md`/`SPEC.md` update is one possible output produced from it. Treat this
directory as a live example of what `inputs/` conceptually holds, not just incidental process hygiene.

## Why

- **The curated docs are edited, this is not.** `INTENT.md`/`SPEC.md` summarize *what was decided* and
  *why*. This log preserves *what was actually typed*, unfiltered — if a future session needs the exact
  original wording of something rather than a paraphrase, this is where to look.
- **Not everything becomes a spec change.** Status checks, clarifying questions, and small one-off
  requests are real project history but don't warrant their own `SPEC.md`/`AGENTS.md` section. They
  still belong somewhere.

## Format

One file per dump, named `YYYY-MM-DD_HHMMSS<_optional-label>.txt` (or `.md`), containing the ordered,
verbatim list of user prompts covered by that dump. Prompts are numbered and separated by `---`, with a
one-line header noting when the dump was taken and what it covers. Nothing is corrected, reworded, or
summarized — copy-paste accuracy is the point. Files are never edited after being written (append a new
dump instead) and never deleted.

## Cadence

No automatic trigger — a dump happens when asked. Reasonable default: whenever a batch of work is
committed and pushed, since that's already the natural checkpoint. For fully automatic capture, a Claude
Code `Stop`/`SessionEnd` hook could trigger this — not set up here unless asked for.
