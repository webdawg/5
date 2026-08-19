# Title Page — Design Brief

Settled decisions from the Creation Interview (see `INTENT.md`'s 2026-08-19 addenda and
`prompt-log/` for the full raw exchange). This stands in for a manuscript — front matter has no raw draft
to begin with, so this brief *is* the raw input `core-outputs/output-book/0-Title_Page/` builds from.

## Composition (back to front)

1. **NASA Milky Way photo** — public domain (NASA/Goddard Space Flight Center, 2003).
   Source: https://commons.wikimedia.org/wiki/File:Milky_Way_galaxy.jpg. Displayed black-and-white: its
   black background becomes white, then the whole photo is converted to grayscale. (The underlying color
   photo is still what the wireframe/crayon tracing works from — only the displayed layer changed.)
2. **Futuristic wireframe map** — code-generated, overlaid on the photo. Must actually trace the
   photo's real structure (traced from its brightness, not an abstract shape unrelated to it — a fixed
   circles-and-spokes grid reads as "a giant clock," not a galaxy map). The branching detail is the
   photo's actual topological **skeleton** (medial axis via Zhang-Suen thinning), branching wherever the
   real bright structure branches — not lines radiating from one point ("a rainbow"), not procedural/
   random generation. Color/tooling otherwise implementation's call ("whatever's easy").
3. **Crayon layer** — no longer traces the wireframe (see `future-ideas.md` for that superseded
   concept). Current composition, bright red throughout, every shape **hand-drawn-imperfect** (wobbly
   paths; circles that don't quite close — a real hand-drawn circle's start and end don't meet — see
   `_hand_drawn_circle()`), with a light waxy/grainy crayon texture pass (not a flat smooth vector line,
   but not the earlier heavy grain either):
   - A **small X at the galactic center**, no larger than ~5% of the page, with a hand-drawn circle
     around it — where the child wants to go. (Superseded an earlier "big X" instruction.)
   - A **circle in the bottom-left corner with a kid-drawn stick figure** inside it — "earth."
   - A **single leaping arc** ("jumps off the map, like an ellipse" — bulges out past the busy
     galaxy/wireframe area into open space before landing, not a multi-bounce path) connecting earth to
     the X, ending in a hand-drawn **arrowhead pointing at the X**.
   No signature/attribution note of any kind — explicitly removed.
4. **Title** — "INFINITY 0" (working title, not yet final), **all caps, monospace**, a custom-built 5x7
   stencil/dot-matrix font (not a vendored typeface — "can we make our own font" was answered yes; see
   `src/blockfont.py`), black, set level (no slant). Positioned **~12.5% down from the top of the
   page** (moved up from an earlier ~17.5%; clear of the galaxy/X entirely at that position), with a
   soft radial gradient (centered on the title block itself, fading outward, no hard edge) lightening
   whatever's directly behind it.
5. **Author** — "BY AGENT 0," same custom font, smaller, black. "Agent 0" itself is a confirmed
   pseudonym.

## Iteration log

Refining through repeated rounds against a rendered output, not settling everything upfront — see
`core-outputs/output-book/0-Title_Page/render/ARCHIVE/` for every prior version.

- v1 → v2: wireframe didn't trace the actual galaxy (looked like a clock), crayon needed to be bigger/
  bright red/textured, X needed to be bigger, signature needed real handwriting instead of italic type.
- v2 → v3: background's black regions become white, then the whole photo converts to black-and-white.
  (Side effect caught and flagged, not yet fixed at v3: white title text on the now-light galactic
  center was nearly illegible.)
- v3 → v4: title/author switched to a custom-built monospace all-caps font, and to black — which also
  fixed the v3 legibility problem, since black now reads clearly against the lightened area.
- v6: title/author block moved above the galactic center instead of straddling it, so the (now big) X
  stays fully visible below it. The legibility fade moved with it, staying centered on the title block.
- v7: title's vertical position now anchored to ~17.5% down from the top of the page (15-20% range)
  instead of relative to the galactic center — top-of-page is now the authoritative anchor.
- v8: wireframe now spawns recursive branching offshoots outward from the traced contour (a
  circuit-trace/root-system look), not just the two smooth closed contour loops from v2.
- v9: v8's branching was randomized (RNG-generated forks), not traced — reverted. Branching now comes
  entirely from 2D tracing: `radial_segments()` finds every separate contiguous bright run per ray
  across several threshold levels, so real gaps in the photo's structure produce the branching look.
- v10: v9's radial segments still read as rays fanned out from one point ("a rainbow"), not a skeleton.
  Replaced with `skeleton_segments()` — real medial-axis thinning (Zhang-Suen) of the photo's bright
  structure, branching wherever the shape itself branches.
- v11: title moved up 5 points, from ~17.5% down from the top of the page to ~12.5%.
- v13: crayon layer's wireframe-tracing concept dropped entirely (moved to `future-ideas.md`).
  Replaced with a big X + bounce-line-to-earth composition; signature removed; stroke rendering
  switched from waxy/grainy to smooth and thick.
- v16: v13's crayon shapes were too geometrically perfect to read as hand-drawn — added wobble to every
  path and switched circles to `_hand_drawn_circle()` (imperfect closure), reintroduced a lighter waxy
  texture pass (v13's "smooth" had gone too flat), shrank the X to ~5% of the page with its own
  hand-drawn circle around it (v13's X was too big), replaced the multi-bounce path with a single
  leaping arc that bulges out past the galaxy into open space ("jumps off the map, like an ellipse"),
  reversed its direction to run earth → X, and added a hand-drawn arrowhead pointing at the X.

## Theme

The book is about hope, and children are part of that hope — the crayon layer represents a child
reading along and participating, not just decoration.

## Open

- Title finality — "Infinity 0" may still change.
- Anything beyond title/author/background belonging on the title page itself (series name, edition
  line, publisher/imprint) — not yet raised.
