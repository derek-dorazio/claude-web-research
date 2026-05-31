# Skill: Clarify Scope (Intake)

Turn a user's prompt into a well-shaped research brief — and ask a few targeted questions only when
the prompt is too thin to proceed confidently.

## When to Use

At the **start of any research command** (`/research`, `/plan`, `/analyze-stock`, `/analyze-industry`,
`/analyze-target`). It standardizes how input is taken and when to interview the user.

## Input model

1. **The prompt is the primary input.** Whatever the user typed after the command is the brief —
   parse the target (topic / ticker / vertical / company), any focus area, and any constraints from it.
2. **`input/` is optional.** Only read a file from `input/` if the user references one, or if a file
   in `input/` is an obvious match for the prompt. Use it as *additional context*, never a requirement.
3. **Never block on missing input files.** Absence of an input file is normal.

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

4. **Otherwise proceed.** If the prompt is specific enough, do **not** interrupt. Briefly state the key
   assumptions you're making (scope, sources, output) at the top of your work so the user can course-correct.

5. **Carry the brief forward.** Use the (possibly clarified) brief to drive the rest of the command.

## Notes
- Prefer one well-designed `AskUserQuestion` call with a few questions over multiple round-trips.
- This skill produces no file output — it shapes the brief the calling command executes.
