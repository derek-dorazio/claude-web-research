# Skill: Deal Sourcing

Map the deal-flow landscape for a vertical — intermediaries, marketplaces, and proprietary outreach targets — into an actionable sourcing tracker.

## When to Use

Apply once a vertical passes the `rollup-thesis` screen and you need to build a pipeline. Covers both **on-market** channels (brokers, M&A advisors, marketplaces) and **off-market / proprietary** outreach (named operators from `industry-fragmentation`).

## Instructions

1. **Identify active intermediaries** for the vertical via WebSearch (e.g. "<vertical> M&A advisors lower middle market", "<vertical> business brokers recent deals"):
   - **Marketplaces**: BizBuySell, Searchfunder, Axial, BizNexus, Kumo, BizQuest. WebFetch listing pages for live, on-market deals in the vertical + geography.
   - **Boutique M&A advisors / brokers** specializing in the vertical (e.g. for healthcare services: Mertz Taggart, VERTESS, etc.). Note their recent transaction activity and typical deal size.
   - **Industry associations & trade shows**: a channel for relationship-based, off-market origination.

2. **Pull live on-market listings**: WebFetch BizBuySell/marketplace search results for the vertical + geography; capture business name (or blind teaser), revenue/SDE, asking price, broker, and URL.

3. **Build the proprietary longlist**: For healthcare verticals, use `scripts/nppes_query.py` to produce a named list of operators by taxonomy + geography. For other services, use establishment data and WebSearch/company directories. These are off-market outreach candidates.

4. **Assemble a sourcing tracker**: combine on-market listings + proprietary targets into one table with a status column for outreach tracking. Recommend a sourcing cadence (broker NDAs, direct-mail/email outreach volume, follow-up rhythm) appropriate to a roll-up search.

## Output Format

```markdown
## Deal Sourcing Map: {{VERTICAL}}

**Geography**: {{GEO}}
**Date**: <date>

### Intermediaries & Marketplaces

| Channel | Type | Vertical focus | Recent activity | Link |
|---|---|---|---|---|
| <name> | Broker / Advisor / Marketplace | <yes/no> | <notes> | <url> |

### Live On-Market Listings

| Business | Revenue | SDE/EBITDA | Asking | Broker | Link |
|---|---|---|---|---|---|
| <name/teaser> | $X.XM | $X.XM | $X.XM | <broker> | <url> |

### Proprietary Outreach Longlist (off-market)

| Company | Location | NPI / source | Notes |
|---|---|---|---|
| <name> | <city, ST> | <NPI> | <from NPPES/directory> |

*Full longlist exported via `scripts/nppes_query.py ... --csv`.*

### Recommended Sourcing Plan
- **On-market**: sign NDAs with <N> brokers covering the vertical; monitor <marketplaces> weekly.
- **Off-market**: outreach to ~<N> proprietary targets/month via <channel>; expect <conversion> response.
- **Cadence**: <weekly/monthly rhythm and follow-up>.

### Sources
- <marketplace and advisor URLs>
- NPPES NPI Registry: https://npiregistry.cms.hhs.gov/
```

## Placeholders
- `{{VERTICAL}}` — industry being sourced
- `{{GEO}}` — geographic scope
