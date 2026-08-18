# Examples

Every other doc in this repo describes the input→output pattern in the abstract. This directory is the
one place that shows it concretely — a small, hand-authored, illustrative walkthrough, not a real case
and not a prescribed format. Phase 0 (`ROADMAP.md`) hasn't decided what a real input/output actually
looks like yet; this exists so "input, spec rule, output, trace" isn't purely theoretical while that's
still open. Treat everything under here as a toy, loudly, the same way `SPEC.md`'s eventual real
input/output format is expected to supersede it — do not build against this as if it were the contract.

## Layout

One numbered folder per example, each self-contained:

- `input.<ext>` — the raw arriving thing.
- `rule.md` — the tiny spec fragment that governs this specific transformation (a stand-in for a real
  `SPEC.md` section, kept local to the example since the real spec doesn't have rules like this yet).
- `output.<ext>` — what a Producer following `rule.md` should generate from `input.<ext>`.
- `trace.md` — what `PRD.md` requirement R8 (traceability) might record: which input, which rule/spec
  version, produced by what (here: a human, by hand — no Producer agent exists yet per `ROADMAP.md`
  Phase 1).

## Examples

- [`001-hello-uppercase/`](001-hello-uppercase/) — the simplest possible deterministic transformation
  (uppercase the text), used only to exercise the input→rule→output→trace shape end to end.
