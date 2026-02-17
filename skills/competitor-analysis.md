# Skill: Competitor Analysis

Compare a company against its sector peers on key financial and operational metrics.

## When to Use

Apply this skill when evaluating a company's competitive position, relative valuation, or market share. Essential for investment decisions and industry research.

## Instructions

1. **Identify the target company**: Get ticker symbol and sector
2. **Identify competitors**:
   - Search for "{{COMPANY_NAME}} competitors" using WebSearch
   - Select 3-5 direct competitors in the same sector
   - Get ticker symbols for all competitors
3. **Pull metrics for all companies**: Use Yahoo Finance MCP `get_stock_info` for each ticker. If unavailable, use WebFetch on Yahoo Finance quote pages.
4. **Build comparison matrix** (follows the `compare` skill pattern):
   - **Size**: Market cap, revenue, employees
   - **Valuation**: P/E, P/B, EV/EBITDA
   - **Profitability**: Gross margin, operating margin, net margin, ROE
   - **Growth**: Revenue growth, earnings growth
   - **Risk**: Beta, debt-to-equity
   - **Performance**: 1-year return
5. **Identify leaders**: Note which company leads in each metric category
6. **Synthesize**: Summarize the target company's competitive position

## Output Format

```markdown
## Competitor Analysis: {{COMPANY_NAME}} ({{TICKER}})

**Analysis Date**: <date>
**Sector**: <industry sector>
**Peer Group**: <list of competitors>

### Companies Compared

1. **{{COMPANY_NAME}}** ({{TICKER}}) — Target company
2. **Competitor 1** (TICK1)
3. **Competitor 2** (TICK2)
4. **Competitor 3** (TICK3)

### Size & Scale

| Metric | {{TICKER}} | TICK1 | TICK2 | TICK3 | Leader |
|---|---|---|---|---|---|
| Market Cap | $XXX B | $XXX B | $XXX B | $XXX B | <ticker> |
| Revenue (TTM) | $XXX B | $XXX B | $XXX B | $XXX B | <ticker> |

### Valuation

| Metric | {{TICKER}} | TICK1 | TICK2 | TICK3 | Cheapest |
|---|---|---|---|---|---|
| P/E Ratio | XX.X | XX.X | XX.X | XX.X | <ticker> |
| P/B Ratio | X.X | X.X | X.X | X.X | <ticker> |
| EV/EBITDA | XX.X | XX.X | XX.X | XX.X | <ticker> |

### Profitability

| Metric | {{TICKER}} | TICK1 | TICK2 | TICK3 | Leader |
|---|---|---|---|---|---|
| Gross Margin | XX% | XX% | XX% | XX% | <ticker> |
| Operating Margin | XX% | XX% | XX% | XX% | <ticker> |
| Net Margin | XX% | XX% | XX% | XX% | <ticker> |
| ROE | XX% | XX% | XX% | XX% | <ticker> |

### Growth

| Metric | {{TICKER}} | TICK1 | TICK2 | TICK3 | Leader |
|---|---|---|---|---|---|
| Revenue Growth | +XX% | +XX% | +XX% | +XX% | <ticker> |
| Earnings Growth | +XX% | +XX% | +XX% | +XX% | <ticker> |

### Risk

| Metric | {{TICKER}} | TICK1 | TICK2 | TICK3 | Lowest Risk |
|---|---|---|---|---|---|
| Beta | X.X | X.X | X.X | X.X | <ticker> |
| Debt-to-Equity | X.X | X.X | X.X | X.X | <ticker> |

### Strengths & Weaknesses

**{{COMPANY_NAME}} ({{TICKER}})**
- **Strengths**: <metrics where target leads>
- **Weaknesses**: <metrics where target lags>

**Competitor 1 (TICK1)**
- **Strengths**: <key advantages>
- **Weaknesses**: <key disadvantages>

<repeat for each competitor>

### Competitive Positioning

**Market Leader**: <which company dominates on most metrics?>
**Best Value**: <which company offers best valuation?>
**Fastest Growing**: <which company has best growth trajectory?>
**Most Profitable**: <which company has best margins?>

**{{COMPANY_NAME}}'s Position**: <summary of where target company stands>

### Sources
- [Yahoo Finance - {{TICKER}}](https://finance.yahoo.com/quote/{{TICKER}})
- <Yahoo Finance links for each competitor>
```

## Placeholders

- `{{TICKER}}` — Target company ticker
- `{{COMPANY_NAME}}` — Target company name
