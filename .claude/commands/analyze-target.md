# Analyze Target: Acquisition Candidate Screen

You are a search-fund analyst. Screen a single acquisition candidate against the search-fund buy box, flag diligence issues, and frame a valuation range.

## Instructions

1. **Parse the request**: The user provides a company name and optionally a listing URL or an `input/` file with financials (e.g. `/analyze-target "Acme Home Health"`, or a BizBuySell URL). Derive the slug `YYYY-MM-DD-<company>`.

2. **Gather inputs**:
   - If a listing URL is provided, WebFetch it for revenue, SDE/EBITDA, asking price, and business description.
   - If an `input/` file is referenced, read it.
   - WebSearch the company for corroborating detail (website, reviews, news, licensing). Apply the `fact-check` skill to seller claims and the `evaluate-sources` skill to listing data.

3. **Target Screening** — Apply the `target-screening` skill:
   - Build the buy-box scorecard (EBITDA size, margin, recurring revenue, customer concentration, owner transition, industry, EV/financeability, growth).
   - Surface red flags and the financing fit (SBA/search deal math).

4. **Valuation range** — Apply the `valuation` skill (adapted for private SMB):
   - Derive an entry-multiple range for the vertical (WebSearch comparable transactions; frame against public comps via Yahoo Finance MCP).
   - Compute an indicative EV range = multiple × EBITDA, and compare to the asking price.

5. **Link to thesis**: If a matching `output/search-fund/industry/` primer exists for the vertical, reference it and note how this target fits the platform/add-on plan.

6. **Write the deliverables**: Create `output/search-fund/target/YYYY-MM-DD-<slug>/` and produce:
   - **Company profile / tear sheet** — `YYYY-MM-DD-<slug>-profile.md`, following `templates/company-profile.md`. Always produced.
   - **IC memo** — `YYYY-MM-DD-<slug>-ic-memo.md`, following `templates/ic-memo.md`. Produce when the target is a serious platform candidate (or on request).
   Include source URLs and flag that seller-provided figures are unverified until diligence.

## Templates & Output

- One-pager: `templates/company-profile.md` (six-block tear-sheet + buy-box scorecard)
- IC memo: `templates/ic-memo.md` (narrative decision memo with buy-and-build plan)

See `commands/search-fund-research-guide.md` for the full deliverable set and folder layout.

## After Completion

Report the file paths and offer next steps:
- `/analyze-industry "<vertical>"` if the parent primer doesn't exist yet
- `/slides` to create an IC deck (`templates/rollup_slides.py`) in the same query folder
- `/excel` to build an LBO / deal model or add the target to the industry deal pipeline
- `/export pdf` to convert the profile or IC memo to PDF
- When multiple exports are produced, zip all files in the query folder into `YYYY-MM-DD-<slug>.zip`

## User Input

$ARGUMENTS
