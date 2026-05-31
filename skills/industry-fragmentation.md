# Skill: Industry Fragmentation Analysis

Quantify how fragmented a services vertical is — the core precondition for a roll-up thesis.

## When to Use

Apply when screening an industry for roll-up / buy-and-build potential. A fragmented market (many small operators, no dominant player, low barriers to a national footprint) is what makes consolidation and multiple arbitrage possible. Pairs with the `rollup-thesis` and `deal-sourcing` skills.

## Instructions

1. **Define the vertical precisely**: Convert the user's plain-English vertical into the right codes.
   - **NAICS code** for any services business (used by Census). E.g. home health = `6216`, dental offices = `6212`, HVAC = `238220`, janitorial = `561720`, residential property management = `531311`.
   - **NPPES taxonomy description** for healthcare verticals (used by the NPI registry). E.g. "Home Health", "Physical Therapist", "Skilled Nursing Facility", "Hospice".

2. **Pull establishment counts** (works for ANY services vertical) using the Census County Business Patterns script:
   ```bash
   python3 scripts/census_cbp.py --naics <NAICS> --geo "us:*"          # national
   python3 scripts/census_cbp.py --naics <NAICS> --geo "state:12"      # a state (FIPS)
   ```
   Requires a free `CENSUS_API_KEY` (see `commands/setup-rollup-research.md`). Capture `ESTAB` (number of establishments), `EMP` (employment), `PAYANN` (annual payroll). Establishments / firm size = the fragmentation base.

3. **For healthcare verticals, add provider density** using the NPPES script (no key needed):
   ```bash
   python3 scripts/nppes_query.py --taxonomy "<taxonomy>" --state <ST> --csv > targets.csv
   ```
   The organizational provider count corroborates Census and yields a named target longlist for `deal-sourcing`.

4. **Estimate top-player concentration**: WebSearch for "largest <vertical> companies market share" and trade-association/IBISWorld-style summaries. Estimate the combined share of the top 4 players (CR4). Note if the market is led by a few nationals or thousands of independents.

5. **Size the buy-box band**: Estimate how many establishments fall in the search-fund target range ($1–3M EBITDA ≈ rough revenue band given typical margins). Use average employees/establishment and revenue-per-employee benchmarks (from WebSearch) to translate establishment counts into a count of acquirable targets.

6. **Render a verdict**: Classify as **Fragmented** (CR4 < 40%, thousands of small operators — ideal), **Consolidating** (CR4 40–60%, active PE roll-ups underway), or **Concentrated** (CR4 > 60% — limited roll-up runway).

## Output Format

```markdown
## Industry Fragmentation: {{VERTICAL}}

**Geography**: {{GEO}}
**NAICS**: {{NAICS}} | **NPPES taxonomy**: {{TAXONOMY}}
**Analysis Date**: <date>

### Market Structure

| Metric | Value | Source |
|---|---|---|
| Establishments (CBP) | XX,XXX | Census CBP <year> |
| Total employment | XXX,XXX | Census CBP <year> |
| Avg employees / establishment | XX | derived |
| Annual payroll | $XXX M | Census CBP <year> |
| Organizational providers (healthcare only) | XX,XXX | NPPES |
| Est. firms in buy-box band ($1–3M EBITDA) | X,XXX | derived |

### Concentration

- **Top 4 players (CR4)**: ~XX% combined share — <named players>
- **Largest operator**: <name> (~XX% share)
- **PE / strategic roll-ups already active**: <yes/no — examples>

### Fragmentation Verdict

**<Fragmented / Consolidating / Concentrated>** — <1–2 sentence justification: how many targets, who dominates, how much runway remains>

### Sources
- Census County Business Patterns: https://www.census.gov/programs-surveys/cbp.html
- NPPES NPI Registry: https://npiregistry.cms.hhs.gov/
- <market-share / trade sources with URLs>
```

## Placeholders
- `{{VERTICAL}}` — the industry being screened
- `{{GEO}}` — geographic scope (national, state, metro)
- `{{NAICS}}` — NAICS code used
- `{{TAXONOMY}}` — NPPES taxonomy (healthcare only)
