# Investment / Stock Research

Comprehensive analysis of a public company — metrics, financial statements, peer comparison, and
valuation — compiled into an investment report with a recommendation, and exportable to an
investor deck, financial model, or PDF.

← Back to [README](../README.md) · See also [general-research.md](general-research.md) ·
[search-fund-research.md](search-fund-research.md)

## When to use it
Evaluating a publicly traded company (a ticker). For private SMB acquisition targets and industry
roll-up theses, use [search-fund research](search-fund-research.md) instead.

> **Setup required.** This capability depends on the Yahoo Finance and SEC EDGAR MCP servers — see
> [commands/setup-investment-research.md](../commands/setup-investment-research.md).

## Commands
| Command | Purpose | File |
|---|---|---|
| `/analyze-stock <TICKER>` | Full investment analysis (metrics → financials → peers → valuation → recommendation) | [.claude/commands/analyze-stock.md](../.claude/commands/analyze-stock.md) |
| `/slides` | Investor deck via the stock slide template | [.claude/commands/slides.md](../.claude/commands/slides.md) |
| `/excel`, `/export pdf` | Financial-model workbook / PDF report | [export.md](../.claude/commands/export.md) |

## Skills applied
Investment skills in [`skills/`](../skills/README.md) (plus general skills like `compare`, `fact-check`):

| Skill | Purpose |
|---|---|
| [stock-metrics](../skills/stock-metrics.md) | Valuation & performance metrics (P/E, P/B, market cap, growth) |
| [financial-statements](../skills/financial-statements.md) | Income statement, balance sheet, cash flow analysis |
| [competitor-analysis](../skills/competitor-analysis.md) | Peer comparison matrix |
| [valuation](../skills/valuation.md) | DCF, comparable-company, and weighted fair value |

## Input structure
A ticker, optionally with a focus area, e.g. `/analyze-stock AAPL`, `/analyze-stock MSFT valuation`,
`/analyze-stock GOOGL vs competitors`. No input file needed; data is pulled live from the MCP servers.

## Output structure
One folder per analysis under `output/stock/`:
```
output/stock/YYYY-MM-DD-<ticker>/
├── YYYY-MM-DD-<ticker>-analysis.md     # the report
├── YYYY-MM-DD-<ticker>-analysis.pptx   # /slides (optional)
├── YYYY-MM-DD-<ticker>-analysis.xlsx   # /excel (optional)
├── YYYY-MM-DD-<ticker>-analysis.pdf    # /export pdf (optional)
└── YYYY-MM-DD-<ticker>.zip             # when 2+ export files are produced
```

## Templates
- Deck: [`templates/stock_analysis_slides.py`](../templates/stock_analysis_slides.py) — pre-built slide
  builders (title, exec summary, valuation, financials, peers, sensitivity, bull/bear, recommendation).
- PDF styling: [`templates/pdf-style.css`](../templates/pdf-style.css).

## Data sources & tools
- **Yahoo Finance MCP** — prices, financial statements, metrics, news, holders, analyst ratings.
- **SEC EDGAR MCP** — 10-K/10-Q filings, XBRL financials, insider trading.
- **Web**: `WebSearch`/`WebFetch` for catalysts and recent developments.
- Setup & tool list: [commands/setup-investment-research.md](../commands/setup-investment-research.md).

## Workflow
```
/analyze-stock <TICKER>  →  /slides · /excel · /export pdf  →  (zip if multiple)
```
