# Web Research Project

This is a Claude Code project for structured web-based research.

## Project Structure

```
analyze/
├── CLAUDE.md              # Project configuration (this file)
├── commands/              # Command reference & documentation
├── skills/                # Reusable research skill prompts
├── .claude/
│   ├── commands/          # Slash commands (/plan, /implement, etc.)
│   └── settings/          # Project settings
├── scripts/               # Helper scripts for processing
├── input/                 # Research topics, URLs, questions (user-provided)
├── output/                # All generated output, organized by command
│   ├── plan/              # Plan command output
│   ├── implement/         # Implement command output
│   ├── research/          # Ad-hoc research output
│   ├── slides/            # PowerPoint presentations
│   └── data/              # Excel workbooks
└── templates/             # Reusable templates for output formatting
```

## Skills

Reusable research techniques in `skills/`. Apply during any research task:
- **evaluate-sources** — Assess source credibility (authority, currency, accuracy, purpose)
- **compare** — Structured comparison matrices with strengths/weaknesses
- **fact-check** — Verify claims against multiple independent sources
- **deep-dive** — Thorough investigation of a single source or subtopic

### Investment Research Skills
- **financial-statements** — Pull and analyze income statement, balance sheet, cash flow for public companies
- **stock-metrics** — Retrieve valuation and performance metrics (P/E, P/B, market cap, growth rates)
- **competitor-analysis** — Compare company against sector peers on financial and operational metrics
- **valuation** — Estimate intrinsic value using DCF, comparable companies, or other frameworks

## Workflow

1. **Plan** — Run `/plan` with a research topic. Produces a structured markdown plan in `output/plan/`.
2. **Implement** — Run `/implement` with a plan file path. Executes the plan steps and writes results to `output/implement/`.
3. **Analyze Stock** — Run `/analyze-stock TICKER` for comprehensive investment research on a public company.

## Conventions

- All output files use markdown format.
- Output filenames include a date prefix: `YYYY-MM-DD-<slug>.md`
- Plans reference their implementation output and vice versa.
- Input files in `input/` can be `.md`, `.txt`, or `.json`.
- When searching the web, always include source URLs in output.

## Tools Available

- `WebSearch` — Search the web for current information.
- `WebFetch` — Fetch and extract content from specific URLs.
- `Read`/`Write`/`Glob`/`Grep` — Local file operations.
- `Bash` — Run scripts from `scripts/` directory.

## MCP Servers

Configured in `.mcp.json` (project-scoped):
- **powerpoint** — Create and edit PowerPoint presentations via `office-powerpoint-mcp-server`. Requires `uvx` (install: `brew install uv`).
- **excel** — Read and write Excel workbooks via `excel-mcp-server`. Requires `uvx`.
- **yahoo-finance** — Stock prices, financial statements, metrics, news, and options data via [yahoo-finance-mcp](https://github.com/Alex2Yang97/yahoo-finance-mcp). Requires cloning the repo and `uv`.
- **sec-edgar** — SEC filings (10-K, 10-Q), XBRL-parsed financials, and insider trading data via [sec-edgar-mcp](https://github.com/stefanoamorelli/sec-edgar-mcp). Requires `uvx` and `SEC_EDGAR_USER_AGENT` env var. See `commands/setup-investment-research.md` for setup.
