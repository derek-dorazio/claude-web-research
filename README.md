# Web Research Project

A structured Claude Code project for web-based research. Inputs go in, organized and source-cited
deliverables come out — markdown reports, slide decks, spreadsheets, and styled PDFs, all grouped by
query under `output/`.

The project supports three research capabilities. Each has a dedicated detail page covering its
commands, skills, input/output structure, templates, and data sources.

## Research capabilities

| Capability | What it does | Detail page |
|---|---|---|
| **General research** | Plan-first web research on any topic → cited markdown report (with quick one-shot and summarize modes) | [docs/general-research.md](docs/general-research.md) |
| **Investment / stock research** | Full analysis of a public company — metrics, financials, peers, valuation, recommendation | [docs/stock-research.md](docs/stock-research.md) |
| **Search-fund / roll-up research** | Industry consolidation theses and private acquisition-target screens for a search fund | [docs/search-fund-research.md](docs/search-fund-research.md) |

## How it works

```
your prompt (topic · ticker · vertical)  →  /command clarifies scope if needed  →  applies skills + web/MCP tools  →  output/<type>/<date>-<slug>/  →  /export (pptx · xlsx · pdf)
```

Just prompt the command with what you want researched — the prompt is the primary input, and a command will ask a few clarifying questions if it needs more shaping. An `input/` file is optional for adding extra context.

- **Commands** (`/plan`, `/analyze-stock`, `/analyze-industry`, …) orchestrate the work — see [commands/README.md](commands/README.md).
- **Skills** are reusable techniques (source evaluation, valuation, fragmentation analysis, …) — see [skills/README.md](skills/README.md).
- **Templates** standardize professional output (slide/Excel generators, markdown skeletons, PDF stylesheet) — see [templates/README.md](templates/README.md).
- **Tools**: `WebSearch`/`WebFetch`, MCP servers (PowerPoint, Excel, Yahoo Finance, SEC EDGAR), helper scripts in `scripts/`, and Pandoc + WeasyPrint for PDF.

## Quick start

**Prerequisites**: [Claude Code](https://docs.anthropic.com/en/docs/claude-code), and [uv](https://docs.astral.sh/uv/) (`brew install uv`) for the MCP servers. For PDFs: `brew install pandoc weasyprint`. Some capabilities need extra setup ([investment](commands/setup-investment-research.md), [roll-up](commands/setup-rollup-research.md)).

```
# general
/research What are the top JavaScript frameworks in 2026?
# stock
/analyze-stock AAPL
# search-fund
/analyze-industry "home health agencies in Florida"
```
Results land in `output/`. List them with `./scripts/list-output.sh`.

## Project structure

```
analyze/
├── README.md / CLAUDE.md     # this overview / Claude Code project config
├── docs/                     # per-capability detail pages
├── commands/                 # command reference, setup docs & guides
├── .claude/commands/         # executable slash commands
├── skills/                   # reusable research skills
├── templates/                # output templates (md skeletons + .py generators + pdf-style.css)
├── scripts/                  # helper scripts & data-source clients
├── input/                    # your topics, tickers, verticals (user-provided)
└── output/                   # generated deliverables, grouped by type & query
    ├── general/  ├── stock/  └── search-fund/{industry,target}/
```

## Conventions

| Convention | Detail |
|---|---|
| Output grouping | All artifacts for one query live in `output/<type>/YYYY-MM-DD-<slug>/` |
| File naming | Files share the `YYYY-MM-DD-<slug>` base; plans get `-plan`, deliverables get a suffix (`-primer`, `-profile`, …) |
| Multi-file export | When exporting 2+ files, they are zipped into `YYYY-MM-DD-<slug>.zip` |
| Sources | Every report cites source URLs |
| Input formats | `.md`, `.txt`, or `.json` files in `input/` |

## Helper scripts

```bash
./scripts/list-output.sh [filter]   # list output (e.g. filter "search-fund", "stock")
./scripts/clean-output.sh [days]     # remove query folders older than N days (default 30)
```

## Reference

- Commands: [commands/README.md](commands/README.md) · Skills: [skills/README.md](skills/README.md) · Templates: [templates/README.md](templates/README.md)
- Setup: [investment research](commands/setup-investment-research.md) · [roll-up research](commands/setup-rollup-research.md)
- Deep guide: [search-fund research](commands/search-fund-research-guide.md)
- Project config for Claude Code: [CLAUDE.md](CLAUDE.md)
