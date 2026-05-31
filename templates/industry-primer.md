<!--
TEMPLATE: Industry / Sector Primer
Used by: /analyze-industry  (output/search-fund/industry/YYYY-MM-DD-<slug>/)
The deep narrative deliverable — the "sector primer" a PE deal team or research house
produces before committing to a vertical. Fill every <placeholder>; delete guidance comments.
Mirrors the structure of McKinsey/Bain sector primers and PE diligence decks.
-->
# Sector Primer: <Vertical> <Geography>

**Prepared by**: <Fund / Analyst>
**Date**: <YYYY-MM-DD>
**Classification**: Confidential — Internal Use Only
**NAICS**: <code> | **NPPES taxonomy**: <if healthcare>
**Thesis verdict**: <Compelling / Conditional / Pass>

---

## 1. Executive Summary
<3–5 sentences: the opportunity, why the vertical is attractive for consolidation, the
headline fragmentation/sizing numbers, and the verdict. Write this last; lead with the punchline.>

**Key takeaways**

<!-- NOTE: keep a blank line between a bold lead-in and a list, or Pandoc renders the bullets as one paragraph in the PDF. -->
- <takeaway 1 — quantified>
- <takeaway 2 — quantified>
- <takeaway 3 — quantified>

---

## 2. Market Overview & Sizing
<What the industry does, the customer, and how revenue is earned. Then size it.>

| Measure | Value | Source / Year |
|---|---|---|
| Total market size (revenue) | $<X>B | <source> |
| Establishments / operators | <N> | Census CBP / NPPES |
| Market growth (CAGR) | <X>% | <source> |
| Avg revenue per establishment | $<X>M | derived |
| Geographic scope | <national / regional> | — |

---

## 3. Market Map
<Insert or reference the one-page market map (see templates/market-map.md). Summarize the
segmentation here: how the market divides into sub-segments and who plays in each.>

See: `<slug>-market-map.md`

---

## 4. Competitive Landscape & Fragmentation
<The core of the roll-up case. Use scripts/census_cbp.py + scripts/nppes_query.py.>

| Concentration metric | Value |
|---|---|
| Top-4 share (CR4) | ~<X>% |
| Largest operator | <name> (~<X>%) |
| # operators in buy-box band ($1–3M EBITDA) | <N> |
| PE / strategic roll-ups already active | <yes/no — examples> |

**Fragmentation verdict**: <Fragmented / Consolidating / Concentrated> — <justification>

---

## 5. Value Chain & Economics
<Where margin sits in the value chain; typical unit economics of a single operator;
fixed vs. variable cost structure; what scale changes.>

---

## 6. Demand Drivers — Why Now
- <driver 1 — demographic / regulatory / technological, with source>
- <driver 2 — with source>
- <driver 3 — with source>

---

## 7. Regulatory & Reimbursement Environment
<Licensing, payor mix, reimbursement exposure, certificate-of-need, key regulatory risks.
For healthcare verticals this section is often decisive.>

---

## 8. Roll-Up Thesis
<From the rollup-thesis skill.>

**One-line thesis**: <…>

| Value-creation lever | Mechanism | Magnitude |
|---|---|---|
| Multiple arbitrage | Buy ~<X>x → exit ~<X>x | +<X>% on value |
| Margin expansion | Shared G&A / procurement | +<X> bps |
| Organic growth | <cross-sell / density> | +<X>% |
| Add-on cadence | <N> tuck-ins/yr | <runway> |

**Exit pathways**: <strategics / PE platforms — named>

---

## 9. Target Landscape
<Summary of the longlist + how it was built. Full list lives in the deal pipeline workbook.>

| Segment | # targets | Representative names | Source |
|---|---|---|---|
| <segment> | <N> | <names> | NPPES / listings |

See: `<slug>-deal-pipeline.xlsx`

---

## 10. Deal Sourcing Plan
<From the deal-sourcing skill: intermediaries, marketplaces, proprietary outreach cadence.>

---

## 11. Risks & Mitigants
| Risk | Severity | Mitigant |
|---|---|---|
| <risk> | <H/M/L> | <mitigant> |

---

## 12. Recommendation & Next Steps
**Verdict**: <Compelling / Conditional / Pass>
**Ideal platform profile**: <size, geography, characteristics>
**Next actions**: <screen N targets, sign broker NDAs, outreach volume>

---

## Appendix
- A. Data methodology (NPPES / Census queries run, dates)
- B. Full source list with URLs
- C. Glossary

---

## Sources
- Census County Business Patterns: https://www.census.gov/programs-surveys/cbp.html
- NPPES NPI Registry: https://npiregistry.cms.hhs.gov/
- <market, regulatory, acquirer sources with URLs>

---

*Generated using Claude Code. Data from public registries and web sources. Not investment advice.*
