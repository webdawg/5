# The Exceptional Do-er

## Responsibility

Takes the completed input + requirements record from **The Storyized Interviewer** (whole-book input)
or **The Output Format Interviewer** (a single asset within one, per
`agents/output-format-interviewer.md`) and does the actual work: produces every output type/variant the
interview identified. This is where "turn input into output" actually happens for the book-input
pipeline, per `SPEC.md`'s "Fan-out" and "Format variants" sections.

Runs at either granularity: once per book-level input, or once per individual asset within one, or once
per format variant of one asset (added 2026-09-04 — see `agents/output-format-interviewer.md`). Proven
2026-08-19 producing the title page's print render (`core-outputs/output-book/0-Title_Page/`, built as a
real generation tool, not a one-off script, per that round's output interview) — but as of 2026-09-04,
that's still the *only* variant actually built; the rest of that round's format list (web, accessibility,
animated, etc.) is documented, not produced yet. At asset granularity, the chain leading here starts with
**The Input Creation Interviewer** → **The Output Interviewer** → **The Output Format Interviewer**
instead of The Storyized Interviewer against raw `mediawiki-input/` material — see `AGENTS.md`'s "Named
agents" section.

## Consumes

- The input + requirements record handed off by The Storyized Interviewer or The Output Format
  Interviewer: the input material (or, at asset granularity, a design brief from The Input Creation
  Interviewer), plus the list of output types and their per-type/per-variant requirements.

## Produces

- One output per output type identified in the interview — e.g. a LaTeX output, a webpage output, and a
  3D-model output, all from the same book input — and, within one output type, one output per format
  variant identified by The Output Format Interviewer (2026-09-04 — e.g. a print render and a separate
  web render of the same title page), each its own script per `SPEC.md`'s tooling convention.
- Not yet doing: publishing any of these to a genuinely reached, final location — see "Open questions."

## Handoff

Not yet decided — does each output type get checked by a Validator (`AGENTS.md`) before landing in
`mediawiki-output/`/`outputs/`, or does The Exceptional Do-er own that too? See `AGENTS.md`'s open
questions.

## Open questions

- Is The Exceptional Do-er one agent per input that fans out internally across output types, or does it
  split into one instance per (input, output type) pair — matching the Producer role's "own context
  window per output type" (`SPEC.md`'s Fan-out, `AGENTS.md`'s Producer)?
- Relationship to Producer/Validator (`AGENTS.md`): is this just this project's name for the Producer
  role, or something broader that also self-validates its own output?
- Publishing gap (2026-09-04, `SPEC.md`'s "Publishing" section): does The Exceptional Do-er own getting
  an output to a genuinely published/reached location too, or does that need its own downstream role?
  Not resolved — even the completed title page print render hasn't been published anywhere yet, only
  generated into `render/`.
