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
