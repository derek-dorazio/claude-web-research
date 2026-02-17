# Skill: Financial Statements

Pull and analyze income statement, balance sheet, and cash flow statement for a public company.

## When to Use

Apply this skill when researching a company's financial health, profitability, liquidity, or capital structure. Essential for valuation, credit analysis, or investment decision-making.

## Instructions

1. **Identify the company**: Get the ticker symbol from user input or search for it
2. **Pull the statements**:
   - Use Yahoo Finance MCP `get_financial_statement` for quick access (annual or quarterly)
   - For official regulatory filings, use SEC EDGAR MCP tools (10-K for annual, 10-Q for quarterly)
   - If MCP tools are unavailable, use WebSearch/WebFetch from Yahoo Finance or SEC EDGAR websites
3. **Extract key line items**:
   - **Income Statement**: Revenue, gross profit, operating income, net income, EPS
   - **Balance Sheet**: Total assets, total liabilities, shareholders' equity, current assets/liabilities, cash, debt
   - **Cash Flow**: Operating cash flow, investing cash flow, financing cash flow, free cash flow
4. **Calculate derived metrics**:
   - Gross margin = Gross Profit / Revenue
   - Operating margin = Operating Income / Revenue
   - Net margin = Net Income / Revenue
   - Current ratio = Current Assets / Current Liabilities
   - Debt-to-equity = Total Debt / Shareholders' Equity
5. **Analyze trends**: Compare year-over-year or quarter-over-quarter changes (3 years minimum)
6. **Flag red flags**: Declining margins, increasing debt, negative cash flow, revenue deceleration

## Output Format

```markdown
## Financial Statements: {{COMPANY_NAME}} ({{TICKER}})

**Analysis Date**: <date>
**Period**: <e.g., "Annual 2022-2024" or "Q1-Q4 2024">
**Data Source**: Yahoo Finance / SEC EDGAR

### Income Statement

| Line Item | {{YEAR1}} | {{YEAR2}} | {{YEAR3}} | YoY Change |
|---|---|---|---|---|
| Revenue | $X.XX B | $X.XX B | $X.XX B | +X.X% |
| Gross Profit | $X.XX B | $X.XX B | $X.XX B | +X.X% |
| Operating Income | $X.XX B | $X.XX B | $X.XX B | +X.X% |
| Net Income | $X.XX B | $X.XX B | $X.XX B | +X.X% |
| EPS (Diluted) | $X.XX | $X.XX | $X.XX | +X.X% |

**Margins**:
- Gross Margin: XX.X%
- Operating Margin: XX.X%
- Net Margin: XX.X%

### Balance Sheet

| Line Item | {{YEAR1}} | {{YEAR2}} | {{YEAR3}} |
|---|---|---|---|
| Total Assets | $X.XX B | $X.XX B | $X.XX B |
| Current Assets | $X.XX B | $X.XX B | $X.XX B |
| Cash & Equivalents | $X.XX B | $X.XX B | $X.XX B |
| Total Liabilities | $X.XX B | $X.XX B | $X.XX B |
| Total Debt | $X.XX B | $X.XX B | $X.XX B |
| Shareholders' Equity | $X.XX B | $X.XX B | $X.XX B |

**Key Ratios**:
- Current Ratio: X.XX
- Debt-to-Equity: X.XX

### Cash Flow Statement

| Line Item | {{YEAR1}} | {{YEAR2}} | {{YEAR3}} |
|---|---|---|---|
| Operating Cash Flow | $X.XX B | $X.XX B | $X.XX B |
| Investing Cash Flow | ($X.XX B) | ($X.XX B) | ($X.XX B) |
| Financing Cash Flow | ($X.XX B) | ($X.XX B) | ($X.XX B) |
| Free Cash Flow | $X.XX B | $X.XX B | $X.XX B |

### Analysis

**Strengths**:
- <observation about positive trends>

**Concerns**:
- <observation about negative trends or risks>

**Overall Assessment**: <brief summary of financial health>

### Sources
- [Yahoo Finance - {{TICKER}}](https://finance.yahoo.com/quote/{{TICKER}})
- [SEC EDGAR - {{COMPANY_NAME}}](URL if applicable)
```

## Placeholders

- `{{TICKER}}` — Stock ticker symbol (e.g., AAPL, MSFT)
- `{{COMPANY_NAME}}` — Full company name
- `{{YEAR1}}`, `{{YEAR2}}`, `{{YEAR3}}` — Fiscal years or quarters
