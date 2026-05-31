# General Research

Plan-first web research on any topic: a question or brief goes in, an organized, source-cited
markdown report comes out — optionally exported to slides, a spreadsheet, or PDF.

← Back to [README](../README.md) · See also [stock-research.md](stock-research.md) ·
[search-fund-research.md](search-fund-research.md)

## When to use it
Market overviews, competitive landscapes, technology comparisons, due-diligence background, or any
"what's the current state of X?" question. For public-company financials use
[stock research](stock-research.md); for industry roll-up theses use
[search-fund research](search-fund-research.md).

## Commands
| Command | Purpose | File |
|---|---|---|
| `/plan <topic>` | Draft a structured research plan (objectives, questions, phased search strategy) | [.claude/commands/plan.md](../.claude/commands/plan.md) |
| `/implement <plan>` | Execute a plan into a full, cited report | [.claude/commands/implement.md](../.claude/commands/implement.md) |
| `/research <question>` | Quick one-shot research (skips the plan step) | [.claude/commands/research.md](../.claude/commands/research.md) |
| `/summarize <file>` | Condense any output into a 1-page executive summary | [.claude/commands/summarize.md](../.claude/commands/summarize.md) |
| `/slides`, `/excel`, `/export pdf` | Package a report as PowerPoint, Excel, or PDF | [export.md](../.claude/commands/export.md) |

## Skills applied
General-purpose techniques in [`skills/`](../skills/README.md):

| Skill | Purpose |
|---|---|
| [evaluate-sources](../skills/evaluate-sources.md) | Assess source authority, currency, accuracy, purpose |
| [compare](../skills/compare.md) | Structured comparison matrices |
| [fact-check](../skills/fact-check.md) | Verify claims against multiple independent sources |
| [deep-dive](../skills/deep-dive.md) | Thorough investigation of a single source/subtopic |

## Input structure
Provide a topic inline (`/plan <topic>`) or, for richer context, an input file in [`input/`](../input)
(`.md`, `.txt`, or `.json`). Recommended shape:

```markdown
# <Topic>
## Topic
<detailed description>
## Questions I Want Answered
- <question 1>
- <question 2>
## Notes
- <constraints, focus areas, preferences>
```
Then: `/plan See input/<your-file>.md`. See [`input/example-topic.md`](../input/example-topic.md).

## Output structure
One folder per query under `output/general/`:
```
output/general/YYYY-MM-DD-<slug>/
├── YYYY-MM-DD-<slug>-plan.md     # from /plan
├── YYYY-MM-DD-<slug>.md          # from /implement or /research (the report)
├── YYYY-MM-DD-<slug>-summary.md  # from /summarize (optional)
├── YYYY-MM-DD-<slug>.pptx/.xlsx/.pdf   # from /slides, /excel, /export (optional)
└── YYYY-MM-DD-<slug>.zip         # when 2+ export files are produced
```

## Templates
- PDF styling: [`templates/pdf-style.css`](../templates/pdf-style.css) (applied automatically by `/pdf-report` and `/export`).
- Slides/workbooks are built ad hoc via the MCP servers (no fixed template for general research).

## Data sources & tools
- **Web**: `WebSearch`, `WebFetch` (every report cites source URLs).
- **MCP**: PowerPoint (`/slides`) and Excel (`/excel`) servers.
- **PDF**: Pandoc + WeasyPrint (`brew install pandoc weasyprint`).

## Workflow
```
/plan <topic>  →  review & edit the plan  →  /implement <plan>  →  /summarize (optional)  →  /slides · /export pdf
```
For simple questions, skip straight to `/research <question>`.
