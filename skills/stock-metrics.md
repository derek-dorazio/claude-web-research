# Skill: Stock Metrics

Retrieve key valuation and performance metrics for a public company's stock.

## When to Use

Apply this skill for quick fundamental analysis, screening stocks, or comparing valuation levels. Essential for initial research or building a stock comparison matrix.

## Instructions

1. **Get the ticker**: Verify the correct ticker symbol for the company
2. **Pull comprehensive stock data**: Use Yahoo Finance MCP `get_stock_info` tool. If unavailable, use WebFetch on the Yahoo Finance quote page.
3. **Extract valuation metrics**:
   - P/E ratio (trailing and forward)
   - P/B ratio (Price-to-Book)
   - EV/EBITDA (Enterprise Value to EBITDA)
   - PEG ratio (P/E to Growth)
   - Dividend yield (if applicable)
4. **Extract performance metrics**:
   - Market cap
   - Beta (volatility vs market)
   - 52-week high/low and current price vs range
   - Average volume
   - Revenue growth (YoY)
   - Earnings growth (YoY)
5. **Extract profitability metrics**:
   - Gross margin, operating margin, net margin
   - ROE (Return on Equity), ROA (Return on Assets)
6. **Get analyst consensus**: Use Yahoo Finance MCP `get_recommendations` for analyst ratings
7. **Interpret the data**: Note whether valuation is high/low relative to growth and sector norms

## Output Format

```markdown
## Stock Metrics: {{COMPANY_NAME}} ({{TICKER}})

**Analysis Date**: <date>
**Current Price**: $XXX.XX
**Data Source**: Yahoo Finance

### Valuation Metrics

| Metric | Value | Interpretation |
|---|---|---|
| P/E Ratio (TTM) | XX.XX | <vs industry average> |
| Forward P/E | XX.XX | <expected valuation> |
| P/B Ratio | X.XX | <vs book value> |
| EV/EBITDA | XX.XX | <enterprise value multiple> |
| PEG Ratio | X.XX | <growth-adjusted valuation> |
| Dividend Yield | X.XX% | <if applicable, else "N/A"> |

### Company Size & Risk

| Metric | Value |
|---|---|
| Market Cap | $XXX.XX B |
| Enterprise Value | $XXX.XX B |
| Beta | X.XX |
| Average Volume | XX.XX M shares |

### Performance

| Metric | Value |
|---|---|
| 52-Week Range | $XXX.XX - $XXX.XX |
| % from 52-Week High | -XX.X% |
| % from 52-Week Low | +XX.X% |
| Revenue Growth (YoY) | +XX.X% |
| Earnings Growth (YoY) | +XX.X% |

### Profitability

| Metric | Value |
|---|---|
| Gross Margin | XX.X% |
| Operating Margin | XX.X% |
| Net Profit Margin | XX.X% |
| ROE (Return on Equity) | XX.X% |
| ROA (Return on Assets) | XX.X% |

### Analyst Consensus

- **Rating**: Strong Buy / Buy / Hold / Sell / Strong Sell
- **Number of Analysts**: XX
- **Price Target**: $XXX.XX (upside/downside: +/-XX%)

### Key Observations

**Valuation**: <Is the stock expensive, cheap, or fairly valued?>
**Growth**: <Is the company growing revenue and earnings?>
**Risk**: <Beta interpretation and volatility assessment>
**Momentum**: <Recent price action vs 52-week range>

### Sources
- [Yahoo Finance - {{TICKER}}](https://finance.yahoo.com/quote/{{TICKER}})
```

## Placeholders

- `{{TICKER}}` — Stock ticker symbol
- `{{COMPANY_NAME}}` — Full company name
