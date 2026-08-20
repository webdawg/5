# The Output Format Interviewer

## Responsibility

Runs after an output type is already decided (by **The Output Interviewer**, or — not yet
confirmed, see "Open questions" — **The Storyized Interviewer**) and before **The Exceptional
Do-er**. Interviews the human on every distinct **format/audience variant** that single, already-decided
output type needs — not alternate output *types* (that's `SPEC.md`'s "Fan-out", decided upstream), but
different packagings of the same conceptual deliverable for different consumers: accessibility, platform,
interactivity, audience filtering. Added 2026-09-04 to close a gap The Output Interviewer's own first
interview round exposed but didn't resolve — see `SPEC.md`'s "Format variants" section and `INTENT.md`'s
2026-09-04 addendum.

Doesn't produce any rendered output itself — its job ends once the list of format variants for the
output type is captured and handed off, one per variant, to The Exceptional Do-er.

## Consumes

- The already-decided output type and its requirements, from The Output Interviewer (or The Storyized
  Interviewer, at whole-book granularity — see "Open questions").
- The human's answers during the interview: which format/audience variants are actually needed for this
  output type, right now vs. deferred.

## Produces

- A list of format variants for the output type, each one ready to hand to The Exceptional Do-er as its
  own generation run — per `SPEC.md`'s tooling convention, its own script and its own subfolder under
  `render/`.

## Handoff

Passes to **The Exceptional Do-er**, once per format variant identified (mirrors `SPEC.md`'s Fan-out:
"one Producer per (input, output type)" — this splits a single output type further, one Do-er run per
format variant of it).

## Interview log — what this actually looked like (title page, 2026-09-04)

Three questions were asked, against the already-completed title page print render:

1. **Which format/audience variants does this output type need, beyond what's already built?**
   Answered with a wide list, not a narrow one — captured verbatim in `INTENT.md`'s 2026-09-04 addendum:
   an AI-accessibility-facing output, a human-accessibility-facing output, an animated/interactive
   version a user can move, a puzzle version, a standard web-hosted version, an age-censored version, a
   mobile version — plus, in the same breath, output-*type*-level examples that belong to `SPEC.md`'s
   Fan-out instead (a 3D model in TypeScript/WebGL, a source-code-and-servers output for technical
   "hacker" users, a text-to-speech audio output). Also surfaced: the pipeline needs to reach a genuinely
   *published* end, not stop at `render/` — the print render itself still isn't anywhere a real consumer
   would reach it. See `SPEC.md`'s "Publishing" section.
2. **Shared pipeline or separate script per variant?** Answered: separate script per format — each
   variant gets its own generation script rather than one shared parametrized pipeline.
3. **Where do variants live on disk?** Answered: subfolder per format under `render/` (e.g.
   `render/print/`, `render/web/`), mirroring `render/ARCHIVE/`'s existing subfolder convention.

**Not yet done as of this round:** this interview captured *what's needed*, same as The Output
Interviewer's own round did for deliverable scope — building each variant is separate Exceptional Do-er
work, not done inline here.

**Update:** The Exceptional Do-er built every variant from this round's list (2026-09-04 through
2026-09-07) — see `core-outputs/output-book/0-Title_Page/README.md`'s "Format variants" section for the
full set (print, web, mobile, AI-accessible JSON, human-accessible long description, an interactive
pan/zoom HTML page, a tile-swap puzzle HTML page, and the age-censoring mechanism itself, with zero
regions flagged for this piece). Two judgment calls worth flagging, not asked about upfront:

- The animated/interactive and puzzle variants stayed self-contained single HTML files (embedded PNG,
  vanilla CSS/JS, no external requests) rather than reaching for a real web/JS framework, since no
  technology stack has been decided for the project generally — that's `SPEC.md`'s Fan-out territory (a
  new output *type*), not this role's job. If a real interactive webpage output type gets scoped later,
  these may get superseded by it rather than extended.
- The age-censored variant builds the actual mechanism (a list of regions to blur) rather than
  fabricating age-inappropriate content to demonstrate it on a children's-hope-themed title page — the
  list is empty for this piece on purpose.

Only the separate "published, not just rendered" gap (`SPEC.md`'s "Publishing" section) remains
untouched — explicitly out of scope for this pass.

**Correction, 2026-09-08:** the "web" answer from this round's list was wrong in kind, not just
underspecified — a resized static image wasn't what "an output dedicated to normal website with regular
web server" meant. It's actually the webpage output *type* (`SPEC.md`'s "Webpage output" section, a
click-through directory of HTML pages spanning the whole book, `publish-output/web-book/` — moved there
2026-09-09, `SPEC.md`'s "Publishing" section), not a format variant scoped to one asset. This resolves
this doc's own "some items raised in this round's answer... read as output types" open question below —
confirmed, at least for "web." The already-built `render/web/title-page-web.png` wasn't wasted work,
though: it's now the embedded image inside the title page's actual book-page HTML
(`publish-output/web-book/render/pages/page-000-title-page.html`).

## Activation

Conversational, same as every other role in this chain right now — no automatic trigger. See
`AGENTS.md`'s "Activation" note.

## Open questions

- Does this role apply to the whole-book chain (after The Storyized Interviewer) as well as the asset
  chain (after The Output Interviewer) it was scoped to when introduced? The human's original ask named
  only "after the output interviewer" — whether whole-book output types (LaTeX, webpage, 3D model) also
  need a format/audience-variant pass, or that's out of scope for them, isn't decided.
- Is the 2026-09-04 list of variants (AI accessibility, human accessibility, animated/interactive,
  puzzle, age-censored, mobile — "web" removed 2026-09-08, see "Correction" above) a universal checklist
  every output type gets run against, or decided fresh per output type? See `SPEC.md`'s matching open
  question.
- Some items raised in this round's answer (3D model, hacker source+servers, audio/TTS, and — confirmed
  2026-09-08 — "web") read as output *types* per `SPEC.md`'s Fan-out, not format variants of one type.
  The line held up on its first real test: a *format variant* changes how the same conceptual piece is
  packaged for a consumer (accessibility, platform, censorship); a *type* changes the underlying
  technology/medium (image vs. webpage vs. 3D scene vs. audio) — "web" needed a real output type because
  a directory of click-through pages isn't a repackaging of the title page image, it's a different kind
  of thing entirely. Worth applying this test to 3D model, hacker source+servers, and audio/TTS too
  before assuming they're settled the same way.
- The "published, not just rendered" gap this round surfaced is real but distinct from this role's core
  job — tracked as its own open question in `SPEC.md`'s "Publishing" section and
  `agents/exceptional-doer.md`, not resolved here.
