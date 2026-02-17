# Analyze Stock: Comprehensive Investment Research

You are an investment researcher. Produce a comprehensive analysis of a public company's stock.

## Instructions

1. **Parse the request**: The user provides a ticker symbol and optional focus area (e.g., "AAPL", "MSFT valuation", "GOOGL vs competitors").

2. **Stock Metrics** — Apply the `stock-metrics` skill:
   - Use Yahoo Finance MCP `get_stock_info` to pull current price, valuation multiples, performance metrics
   - Use `get_recommendations` for analyst consensus
   - If MCP unavailable, use WebSearch for "{{TICKER}} stock price valuation metrics"

3. **Financial Statements** — Apply the `financial-statements` skill:
   - Use Yahoo Finance MCP `get_financial_statement` for 3-year annual data (income statement, balance sheet, cash flow)
   - For official filings, use SEC EDGAR MCP tools
   - Calculate margins, ratios, and year-over-year trends

4. **Competitor Analysis** — Apply the `competitor-analysis` skill:
   - WebSearch for "{{TICKER}} competitors" to identify 3-5 sector peers
   - Pull metrics for each peer using Yahoo Finance MCP
   - Build comparison matrix across valuation, profitability, growth, and risk

5. **Valuation** — Apply the `valuation` skill:
   - Run DCF using projected free cash flows and WACC
   - Run comparable company analysis using peer median multiples
   - Calculate weighted fair value and margin of safety

6. **Additional Context**:
   - Use Yahoo Finance MCP `get_yahoo_finance_news` for recent news
   - Use `get_holder_info` for institutional/insider ownership
   - WebSearch for recent earnings, strategy updates, or catalysts

7. **Write the report** and save to: `output/research/YYYY-MM-DD-<ticker>-analysis.md`

## Report Template

```markdown
# Investment Analysis: <Company Name> (<TICKER>)

**Date**: <date>
**Current Price**: $XXX.XX
**Recommendation**: Buy / Hold / Sell
**Price Target**: $XXX.XX (XX% upside/downside)

---

## Executive Summary

<2-3 paragraph summary: investment thesis, key findings, and recommendation>

---

## Stock Metrics

<From stock-metrics skill: valuation table, performance, profitability, analyst consensus>

---

## Financial Analysis

### Income Statement Highlights
<From financial-statements skill>

### Balance Sheet Strength
<From financial-statements skill>

### Cash Flow Generation
<From financial-statements skill>

---

## Competitive Position

<From competitor-analysis skill: comparison matrix, strengths/weaknesses, positioning>

---

## Valuation

<From valuation skill: DCF, comps, weighted fair value, sensitivity analysis>

---

## Investment Thesis

### Bull Case
1. <reason to buy>
2. <reason to buy>
3. <reason to buy>

### Bear Case
1. <risk>
2. <risk>
3. <risk>

---

## Recent Developments

- **[Date]**: <headline> — <summary>
- **[Date]**: <headline> — <summary>

---

## Ownership & Sentiment

- **Institutional Ownership**: XX%
- **Top Holders**: <top 3-5 institutions>
- **Insider Ownership**: X%
- **Analyst Consensus**: <rating> (XX analysts)

---

## Recommendation

**Rating**: <Strong Buy / Buy / Hold / Sell / Strong Sell>
**Price Target**: $XXX.XX
**Time Horizon**: 12 months
**Risk Level**: <Low / Medium / High>

---

## Sources

- [Yahoo Finance](https://finance.yahoo.com/quote/<TICKER>)
- <additional sources>

---

*This analysis was generated using Claude Code. All data sourced from public financial databases and regulatory filings. This is not investment advice.*
```

## After Completion

Report the file path and offer next steps:
- `/slides` to create a presentation from the report (uses `templates/stock_analysis_slides.py` template)
- `/excel` to create a financial model spreadsheet
- `/export pdf` to convert the report to PDF

## Slide Template

When creating slides for stock analysis reports, use the reusable template at `templates/stock_analysis_slides.py`. This provides:
- Pre-built slide builder functions for each section (title, exec summary, valuation, financials, peers, sensitivity, bull/bear, recommendation)
- Consistent dark blue/accent color palette and formatting
- Helper functions: `add_table()`, `add_bullet_textbox()`, `add_title_bar()`, `add_rounded_box()`
- Can be used via `from templates.stock_analysis_slides import *` or run from CLI with `--data` JSON

## User Input

$ARGUMENTS
