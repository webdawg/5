# INTENT

## Why this exists

Most agentic coding setups treat "spec" as a one-time prompt and "input/output" as whatever happens to
flow through a single agent in a single session. This project inverts that: the spec is the persistent,
versioned source of truth (committed to git, evolving over time), and the system's job is to take
whatever shows up in `inputs/` and turn it into the matching `outputs/` — driven by that spec, not by
one-off improvisation per input.

The motivating constraint is speed and consistency: an input should become an output *instantly* and
*the same way every time*, because the transformation logic lives in a spec that agents read and follow,
not in ad hoc reasoning that varies run to run.

## Why multi-agent

A single agent doing "read spec, read input, write output" doesn't scale past trivial cases — it has no
separation between deciding *what* an input needs, *doing* the transformation, and *checking* the result
matches spec. Splitting these into distinct agent roles (see [`AGENTS.md`](AGENTS.md)) means:

- Each agent has a narrow, verifiable job instead of one agent silently doing everything.
- Work can run concurrently across multiple inputs instead of serially.
- A validation role can catch spec drift before a bad output lands, rather than trusting the producing
  agent's own judgment of its own work.

## What "done" looks like

An input lands in `inputs/`, the right output appears in `outputs/` shortly after with no manual
intervention, and the mapping between them is traceable back to a specific version of the spec that
produced it.

## Non-goals (for now)

- Not trying to support arbitrary unstructured input formats before the input/output contract itself is
  defined (see `SPEC.md`'s open questions).
- Not building a generic multi-agent framework — the agent roles here are specific to the
  input-to-output pipeline, not a reusable product.

## Capturing new intent

When a raw elaboration of the idea comes in (new scope, a changed motivator, a constraint), append it
here under a new `## Addenda` section as a dated entry, then pull anything concrete enough to act on
into `SPEC.md` (the contract), `AGENTS.md` (the roles), or `ROADMAP.md` (noted for later). This file is
the record of intent; the others are where it becomes actionable. See the raw material for this in
[`prompt-log/`](prompt-log/) if the exact original wording matters.

## Addenda

Later elaborations on the founding intent above, each captured a lightly-edited version first, then the
original raw text verbatim below it.

### 2026-08-18 — AI-controlled input/output, and MediaWiki as the first instance

**Edited for readability:**

Both the input and the output can be controlled by AI — not just a human dropping something in on one
side and reading it out the other. One of the first concrete pieces we're going to implement is an
input-and-output MediaWiki instance.

Later, further into the project, physical resources will eventually become available, and we'll raise
real instances at that point — but that's not a concern right now. Right now the goal is just to define
the why and the intent around this.

**Verbatim:**

AI can control both the input and output, and one of the first pieces we are going to implement is an
input, and output mediawiki instance - Later in the thick of things I will eventually provide access to
physical resources - we will raise these instances at this point, but we are not worried about doing
that right now, we just want to define the why, and the intent around this stuff

### 2026-08-18 — Input wiki vs. output wiki: things+instructions vs. rendered output or links

**Edited for readability:**

The input wiki will hold things and instructions. The output wiki will hold the rendered output, or
links to the output, etc. For example: if the input is "create a git repo," we can't really store a git
repo in MediaWiki — so instead the output wiki has a link to it.

**Verbatim:**

So the input wiki, will have things and instructions, and the output wiki will have the rendered output
or links to the outputs etc - like if the input is creating a git repo, we cant store that in mediawiki
really, so we have a link to all the outputs

### 2026-08-23 — One input, multiple outputs, each with its own agent and context window

**Edited for readability:**

A single input can fan out to multiple outputs, each a different type — not alternatives to pick
between, but outputs that can all exist at once from the same input. For example, a book input could
produce a LaTeX output for print typesetting, a webpage output for an interactive version of the story,
and a 3D model output for scene settings. Each output type gets its own agent, with its own context
window, rather than one agent holding the context for every output type at once.

**Verbatim:**

so for every input we may have multiple outputs, and we want an agent created for each output with its
own context window - for instance - if we process a book input, it could have a latex output for
typesetting for a published novel, a webpage output for a possible interactive story, a 3d model output
for scene settings

### 2026-08-24 — Naming the first two book-input agents: The Storyized Interviewer and The Exceptional Do-er

**Edited for readability:**

To start the first book input, we need an interview spec: an agent that logs inputs and asks what
outputs are needed. That agent is "The Storyized Interviewer" — its job is to collect all the inputs and
all the requirements for the outputs, then hand that off to the next agent, "The Exceptional Do-er,"
which does the actual work.

**Verbatim:**

Okay, so lets start our first book input - we need to create an interview spec for this - you need to
log my inputs, and ask me what outputs we need here - lets create an agent called "The Storyized
Interviewr" - it is there job to collect all the inputs, and all the reqirements for the ouputs, and
pass it off to the next Agent who is the "The Exceptional Do-er" - lets get these agents defined now in
the repo

### 2026-08-29 — A stateful, trainable agent: The Narrative Reviewer

**Edited for readability:**

Narrative review needs a dedicated agent, with its own subfolder, that remembers the user and past
decisions over time — not a stateless role invoked fresh each run like the others. The user intends to
train it directly. Full human review still happens alongside it, not instead of it.

**Verbatim:**

A dedicated narrative-review agent with its own agent subfolder - it remembers me and things and stuff -
we still go through a full human review together, but I am going to train it

### 2026-08-30 — Book input structure: core-inputs/input-book/, ordered by folder number and a priority file

**Edited for readability:**

Book inputs get a dedicated directory structure: `core-inputs/input-book/`, one folder per story, named
`<N>-<Story_Name>` where `N` is the order and `Story_Name` uses underscores for spaces. The real,
authoritative ordering mechanism is a `priority.txt` file inside each story's folder, containing a
number — not the folder name itself.

**Verbatim:**

so you will have book inputs lets create a core-inputs/input-book/0-#### spec structure for this book -
the numbers will be the order - the stuff after the - will be the name - the name will have underscores
- our system of ordering with be a priority text file inside of the last sub folder that will have a
number for priority

### 2026-08-19 — A Creation Interview, for outputs with no raw input behind them

**Edited for readability:**

The title page (`mediawiki-output/Infinity_0`) surfaced a gap: it was authored straight to output with
no raw input counterpart — front matter has no "unedited draft" the way a story has a manuscript, so
`The Storyized Interviewer`'s existing intake pattern (interview *about* an already-arrived raw input)
doesn't fit it. The plan is to work the title page next and log the actions taken along the way, then
distill that concrete trace into a repeatable **Creation Interview** — a second interview role/pattern
for inputs that start from nothing rather than from raw material.

**Verbatim:**

so lets log all the actions I do next so we can replicate this as a starting interview for creation - a
Creation Interview - how do I do this - what do I do?

### 2026-08-19 — Two-stage interview per asset: Creation Interview, then an output interview, then the Do-er

**Edited for readability:**

After the Creation Interview settled the title page's design (content: what it depicts, its layers,
theming), the natural next step wasn't to build it directly — it was a second interview, this time about
*output* requirements (format, where the rendered result lives, whether the generation code needs to be
reusable), before handing off to production. That second stage maps onto the pattern `The Storyized
Interviewer`/`The Exceptional Do-er` already established in `AGENTS.md` — just run at the granularity of
one asset (the title page) instead of the whole book input. So a single piece of front matter goes
through three stages: Creation Interview (input/design) → output interview (requirements) → Do-er
(production) — not two.

**Verbatim:**

lets generate our ouputs for 0, and start this as a new output intervier just like we just did input
interviewer, and then the output interviewer will hand off to the doer

### 2026-09-04 — A missing stage: format/audience variants of one output type, and a publishing gap

**Edited for readability:**

The Output Interviewer's own first interview question for the title page ("one master render now, or
several formats/resolutions up front?") got answered by deferring the question ("high-res first,
everything else later"), not by giving format multiplicity a real stage. That's a gap: a new role, **The
Output Format Interviewer**, gets inserted into the asset chain between The Output Interviewer and The
Exceptional Do-er — given one already-decided output type, interview the human on every distinct
format/audience variant that single deliverable needs.

Running that interview for real against the already-completed title page print render surfaced a wide
list of variants to plan for across the pipeline generally, not just the title page: an
AI-accessibility-facing output, a human-accessibility-facing output, an animated/interactive version a
user can move, a puzzle version, a standard web-hosted version, an age-censored version, a mobile
version — alongside output-*type*-level examples raised in the same breath (a 3D model built in
TypeScript/WebGL, a source-code-and-servers output aimed at technical/"hacker" users, a text-to-speech
audio output). Whether every one of these applies to every output type, or this is the general universe
to check each output type against, is open — see `SPEC.md`.

The same round also surfaced a related, distinct gap: the pipeline as built stops at a
generation/render step (`core-outputs/<piece>/render/`), which is a work product, not a genuinely
*published*, externally-reachable final artifact — even the completed title page print render doesn't
live anywhere a real consumer would reach it yet. The chain needs to reach all the way to a published
end, not just a rendered one.

Tooling/layout decided for the format-variant axis: each variant gets its own separate generation
script (not one shared parametrized pipeline, to avoid one script accumulating every variant's
special-casing), and lives in its own subfolder under `render/` (e.g. `render/print/`, `render/web/`),
mirroring `render/ARCHIVE/`'s existing subfolder convention for prior versions.

**Verbatim:**

so we need to work on the output interviewer - we did not talk about multiple formats here, and that is
a problem, so we need to insert an output multiple formats interviewer before the doer and after the
output interviewer - lets construct, and document, and spec, and intent that, and go through an
interview, save it as an example, and get this done

Interview answer (format variants needed): get this into the spec: output dedicated to AI accessibility,
output dedicated human accessibility, a moving animated version that users can move if they want, a
puzzle version, we just did the print version and we need to create a chain that goes to the end so for
the print version we even need to add to the final published dir, output dedicated to normal website with
regular web server, an output dedicated to age censoring, an output of 3d model built on typescript and
web gl, an output for hackers that is source code and servers, an audio output using some cool text to
speech voice, an output for mobile

Interview answer (tooling shape): Separate script per format.

Interview answer (storage layout): Subfolder per format under render/.
