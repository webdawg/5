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

Automatic: a `SessionEnd` hook (`.claude/settings.json`, running `.claude/hooks/dump-prompt-log.py`)
dumps every session's prompts when the session ends. It reads the session transcript directly rather
than re-typing anything, so captured text is exactly what was submitted — real prompts only (skips tool
results and injected skill/system content). A dump can still be taken manually at any other checkpoint
(e.g. whenever a batch of work is committed and pushed) by running that same script.
