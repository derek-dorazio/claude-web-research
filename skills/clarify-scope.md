# Skill: Clarify Scope (Intake)

Turn a user's prompt into a well-shaped research brief — and ask a few targeted questions only when
the prompt is too thin to proceed confidently.

## When to Use

At the **start of any research command** (`/research`, `/plan`, `/analyze-stock`, `/analyze-industry`,
`/analyze-target`). It standardizes how input is taken and when to interview the user.

## Input model

1. **The prompt is the primary input.** Whatever the user typed after the command is the brief —
   parse the target (topic / ticker / vertical / company), any focus area, and any constraints from it.
2. **Derive a `<slug>`** — a short kebab-case identifier for this search, taken from the prompt
   (e.g. `AAPL` → `aapl`; "home health agencies in Florida" → `home-health-florida`). The `<slug>` is
   the search's identity: it names both the optional input lookup and the output folder. It's the only
   per-search "instance" concept in the project.
3. **`input/` is optional.** Check `input/<slug>.{md,txt,json}` for additional context, and read any
   file the user explicitly references. Treat whatever you find as *extra context*, never a
   requirement — never block on a missing input file.

## Instructions

1. **Parse the prompt** into a working brief: subject, scope/boundaries, intended depth, key questions,
   source/recency expectations, output focus, and any stated constraints.

2. **Assess sufficiency.** You have enough to proceed when the subject is clear and at least the rough
   scope and intended output are inferable. Sensible defaults are fine — fill obvious gaps yourself
   (e.g., default to recent/authoritative sources, US market unless implied otherwise) rather than asking.

3. **Interview only if needed.** If material ambiguity remains — something that would genuinely change
   the research direction or output — ask **1–3 concise clarifying questions** (max 4) using the
   `AskUserQuestion` tool before doing the work. Draw from, but don't exhaust, these dimensions:
   - **Scope / boundaries** — geography, time frame, sub-segment, breadth vs. depth, what to exclude.
   - **Sources** — preferred or required sources, recency cutoff, primary vs. secondary, anything to avoid.
   - **Focus / angle** — the decision the research supports, the audience, comparison set, specific questions.
   - **Output** — format/length, level of detail, deliverables expected.

   Offer concrete options with a recommended default first, so the user can answer in one click. Ask
   only what changes the outcome — don't interrogate, and don't re-ask anything the prompt already answered.

4. **State the plan before executing.** In one line, tell the user: the derived `<slug>`, that you'll
   check `input/<slug>` for extra context (note whether a matching file was found), and where results
   will be saved — `output/<type>/YYYY-MM-DD-<slug>/`. For example:
   > *"Slug: `home-health-florida`. I'll fold in `input/home-health-florida.md` if present and save the
   > report to `output/search-fund/industry/2026-05-31-home-health-florida/`."*
   Fold this into the same turn as any clarifying questions — it's transparency, not a separate gate.

5. **Otherwise proceed.** If the prompt is specific enough, don't interrupt with questions; the one-line
   plan from step 4 plus a brief note of key assumptions (scope, sources, output) is enough.

6. **Carry the brief forward.** Use the (possibly clarified) brief and the `<slug>` to drive the rest
   of the command.

## Notes
- Prefer one well-designed `AskUserQuestion` call with a few questions over multiple round-trips.
- This skill produces no file output — it shapes the brief the calling command executes.
