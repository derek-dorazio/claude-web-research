# Skill: Valuation

Estimate a company's intrinsic value using fundamental valuation methodologies.

## When to Use

Apply this skill when determining if a stock is overvalued or undervalued. Essential for investment decision-making and price target estimation. Best used after running the `financial-statements` and `stock-metrics` skills.

## Instructions

1. **Gather financial data**:
   - Use `financial-statements` skill output for income statement, balance sheet, cash flow
   - Use `stock-metrics` skill output for current price, shares outstanding, market cap
   - Use `competitor-analysis` skill output for peer group multiples (if available)
2. **Run DCF (Discounted Cash Flow)**:
   - Start with current free cash flow
   - Project FCF growth for 5-10 years (use historical growth + analyst estimates)
   - Apply a terminal growth rate (typically 2-3%)
   - Discount at WACC (weighted average cost of capital, typically 8-12%)
   - Sum present values + terminal value = enterprise value
   - Subtract net debt to get equity value
   - Divide by shares outstanding for per-share value
3. **Run Comparable Company Analysis (Comps)**:
   - Use peer group median P/E, EV/EBITDA, P/B multiples
   - Apply each multiple to target company's corresponding metric
   - Average the results for a comps-based fair value
4. **Calculate weighted average**: Blend DCF and comps (typically 50/50 or weighted by confidence)
5. **Determine margin of safety**: Compare intrinsic value to current market price
6. **Document assumptions**: Every assumption must be stated explicitly
7. **Sensitivity analysis**: Show how fair value changes with different growth/discount rates

## Output Format

```markdown
## Valuation: {{COMPANY_NAME}} ({{TICKER}})

**Analysis Date**: <date>
**Current Stock Price**: $XXX.XX
**Shares Outstanding**: XXX.XX M
**Market Cap**: $XXX.XX B

---

### Method 1: Discounted Cash Flow (DCF)

**Assumptions**:
- Free Cash Flow (Current): $XX.XX B
- Growth Rate (Years 1-5): X%
- Growth Rate (Years 6-10): X%
- Terminal Growth Rate: X%
- Discount Rate (WACC): X%

**Projections**:

| Year | FCF Projection | Present Value |
|---|---|---|
| Year 1 | $XX.XX B | $XX.XX B |
| Year 2 | $XX.XX B | $XX.XX B |
| Year 3 | $XX.XX B | $XX.XX B |
| Year 4 | $XX.XX B | $XX.XX B |
| Year 5 | $XX.XX B | $XX.XX B |
| Terminal Value | $XXX.XX B | $XXX.XX B |

**Enterprise Value**: $XXX.XX B
**Less Net Debt**: $XX.XX B
**Equity Value**: $XXX.XX B
**DCF Fair Value Per Share**: $XXX.XX

---

### Method 2: Comparable Company Analysis

**Peer Multiples**:

| Multiple | {{TICKER}} | Peer Median |
|---|---|---|
| P/E (TTM) | XX.X | XX.X |
| EV/EBITDA | XX.X | XX.X |
| P/B | X.X | X.X |

**Implied Values**:

| Method | Calculation | Implied Value |
|---|---|---|
| P/E Multiple | Peer Median P/E x EPS | $XXX.XX |
| EV/EBITDA Multiple | Peer Median EV/EBITDA x EBITDA / Shares | $XXX.XX |

**Comps Fair Value Per Share**: $XXX.XX (average)

---

### Valuation Summary

| Method | Fair Value | vs Current Price | Weight |
|---|---|---|---|
| DCF | $XXX.XX | +/-XX% | 50% |
| Comps | $XXX.XX | +/-XX% | 50% |
| **Weighted Average** | **$XXX.XX** | **+/-XX%** | |

### Margin of Safety: +/- XX%

---

### Sensitivity Analysis

| | WACC 8% | WACC 10% | WACC 12% |
|---|---|---|---|
| Growth 5% | $XXX | $XXX | $XXX |
| Growth 8% | $XXX | $XXX | $XXX |
| Growth 12% | $XXX | $XXX | $XXX |

---

### Investment Recommendation

**Rating**: Strong Buy / Buy / Hold / Sell / Strong Sell
**Price Target**: $XXX.XX
**Risk Level**: Low / Medium / High

**Rationale**: <2-3 sentences explaining the recommendation>

**Key Risks**:
- <risk 1>
- <risk 2>

**Key Catalysts**:
- <catalyst 1>
- <catalyst 2>

### Sources
- Financial data from Yahoo Finance and/or SEC EDGAR
- Peer data from competitor analysis
```

## Placeholders

- `{{TICKER}}` — Stock ticker symbol
- `{{COMPANY_NAME}}` — Full company name
