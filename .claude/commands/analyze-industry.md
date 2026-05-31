# Analyze Industry: Roll-Up Thesis & Target Landscape

You are a search-fund analyst. Produce a roll-up / consolidation thesis for a fragmented services vertical, with a fragmentation analysis, target longlist, and deal-sourcing map.

## Instructions

1. **Intake & clarify scope** — Apply the `clarify-scope` skill. The user's prompt is the primary input: a vertical and optional geography (e.g. "home health agencies in Florida", "residential HVAC", "dental support organizations Texas"); an `input/` file is optional extra context (read it only if referenced or an obvious match). If shaping is missing — geography, sub-segment, target size band, or which sources to lean on — ask a couple of clarifying questions before proceeding; otherwise state your assumptions and continue. Derive the slug `YYYY-MM-DD-<vertical>-<geo>`.

2. **Map to codes**: Determine the NAICS code (any services vertical) and, for healthcare, the NPPES taxonomy description. State your mapping so the user can correct it.

3. **Industry Fragmentation** — Apply the `industry-fragmentation` skill:
   - Run `scripts/census_cbp.py --naics <NAICS> --geo <geo>` for establishment counts (needs `CENSUS_API_KEY`; if unset, tell the user how to get one and fall back to WebSearch estimates).
   - For healthcare, run `scripts/nppes_query.py --taxonomy "<taxonomy>" --state <ST>` for provider density and a named longlist.
   - Estimate top-player concentration (CR4) via WebSearch. Render a fragmentation verdict.

4. **Roll-Up Thesis** — Apply the `rollup-thesis` skill:
   - Establish why-this-industry / why-now / value-creation levers / risks.
   - Find public strategics and PE platforms (exit pathways + multiple-arbitrage frame) using the SEC EDGAR MCP, Yahoo Finance MCP, and WebSearch.

5. **Deal Sourcing** — Apply the `deal-sourcing` skill:
   - WebSearch + WebFetch active brokers, M&A advisors, and marketplace listings (BizBuySell, Searchfunder, Axial, BizNexus, Kumo) for the vertical + geo.
   - Build the proprietary outreach longlist (NPPES for healthcare; directories otherwise).

6. **Write the deliverables**: Create `output/search-fund/industry/YYYY-MM-DD-<slug>/` and produce:
   - **Sector primer** — `YYYY-MM-DD-<slug>-primer.md`, following `templates/industry-primer.md`. This is the main report; fill every section from the skills above.
   - **Market map** — `YYYY-MM-DD-<slug>-market-map.md`, following `templates/market-map.md` (operators grouped by sub-segment).
   - **Deal pipeline** — `YYYY-MM-DD-<slug>-deal-pipeline.xlsx`, generated with `python3 templates/deal_pipeline_xlsx.py --data <targets.json> --output <path>` from the longlist.
   Always include source URLs. Label any unverified/estimated figures.

## Templates & Output

Use the templates rather than re-inventing structure:
- Report: `templates/industry-primer.md`
- Market map: `templates/market-map.md`
- Deal list (Excel): `templates/deal_pipeline_xlsx.py` (tabs: Dashboard, Active Targets, Passed, Contacts)
- Deck (PowerPoint): `templates/rollup_slides.py`

See `commands/search-fund-research-guide.md` for the full deliverable set, folder layout, and data sources.

## After Completion

Report the file paths and offer next steps:
- `/analyze-target "<name>"` to screen a longlist candidate (output goes to `output/search-fund/target/`)
- `/slides` to build an industry/IC deck via `templates/rollup_slides.py` (saved in the same query folder)
- `/excel` to extend or refresh the deal-pipeline workbook
- `/export pdf` to convert the primer to PDF
- When multiple exports are produced, zip all files in the query folder into `YYYY-MM-DD-<slug>.zip`

## User Input

$ARGUMENTS
