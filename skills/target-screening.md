# Skill: Target Screening

Score a single acquisition candidate against the search-fund buy box and surface diligence red flags.

## When to Use

Apply when evaluating a specific company — whether a broker listing, an off-market prospect, or a name from an industry target longlist — to decide whether it merits deeper diligence and an IOI/LOI. Pairs with `valuation` for the price range and `fact-check` for verifying seller claims.

## Instructions

1. **Gather the inputs**: From the user's input (company name, a listing URL to WebFetch, or an `input/` file), extract revenue, EBITDA (or SDE), margins, revenue mix, customer concentration, owner role, age of business, and asking price if disclosed. Note what's missing — gaps are themselves findings.

2. **Score against the buy box** (the standard search-fund criteria):

   | Criterion | Target | Weight |
   |---|---|---|
   | EBITDA | $1–3M (sweet spot); $0.75–5M acceptable | High |
   | EBITDA margin | ≥ 10% | Medium |
   | Recurring / contracted revenue | ≥ 60% recurring or repeat | High |
   | Customer concentration | No customer > 15–20% | High |
   | Owner transition | Owner willing to exit / not the rainmaker | High |
   | Industry | Fragmented, non-cyclical, low tech-disruption risk | Medium |
   | Enterprise value | < $50M (financeable with SBA/search economics) | Medium |
   | Growth | Stable to growing; positive FCF conversion | Medium |

   Rate each Strong / Adequate / Weak / Unknown, and assign a 0–5 score. Justify each from the evidence.

3. **Surface red flags**: customer/payor concentration, owner-as-rainmaker, declining revenue, add-back-inflated EBITDA, deferred maintenance/capex, licensing/regulatory exposure, litigation, or thin/ messy financials. Distinguish dealbreakers from diligence items.

4. **Note the financing fit**: rough SBA 7(a) / search-fund deal math — can the cash flow service debt at a plausible purchase multiple? Flag if the asking multiple looks rich vs. the vertical's norm.

5. **Render a fit verdict** with a clear recommendation (Pursue / Pursue-with-conditions / Pass) and the top 3 diligence questions to resolve next.

## Output Format

```markdown
## Target Screen: {{COMPANY}}

**Date**: <date>
**Vertical**: <industry> | **Location**: <geo>
**Source**: <listing URL / off-market / longlist>

### Snapshot
| Field | Value |
|---|---|
| Revenue (TTM) | $X.XM |
| EBITDA / SDE | $X.XM (XX% margin) |
| Recurring revenue | XX% |
| Largest customer | XX% of revenue |
| Owner role | <description> |
| Asking price | $X.XM (X.Xx EBITDA) |

### Buy-Box Scorecard
| Criterion | Rating | Score (0–5) | Notes |
|---|---|---|---|
| EBITDA size | <rating> | X | <note> |
| Margin | <rating> | X | <note> |
| Recurring revenue | <rating> | X | <note> |
| Customer concentration | <rating> | X | <note> |
| Owner transition | <rating> | X | <note> |
| Industry attractiveness | <rating> | X | <note> |
| Enterprise value / financeability | <rating> | X | <note> |
| Growth / cash conversion | <rating> | X | <note> |
| **Total** | | **XX / 40** | |

### Red Flags
- 🚩 <dealbreaker or diligence item>
- 🚩 <...>

### Financing Fit
<rough SBA/search deal math; debt-service coverage at plausible multiple>

### Verdict
**<Pursue / Pursue with conditions / Pass>** — <rationale>

**Top diligence questions**
1. <question>
2. <question>
3. <question>

### Sources
- <listing URL, company site, any verifying sources>
```

## Placeholders
- `{{COMPANY}}` — target company name
