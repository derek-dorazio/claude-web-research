# Setup: Search-Fund Roll-Up Research Capabilities

How to configure the data sources and scripts used by `/analyze-industry` and `/analyze-target` for healthcare-services and other-services roll-up research.

## What this adds

| Piece | Location | Purpose |
|---|---|---|
| `/analyze-industry` command | `.claude/commands/analyze-industry.md` | Roll-up thesis + fragmentation + sourcing map for a vertical |
| `/analyze-target` command | `.claude/commands/analyze-target.md` | Buy-box screen of a single acquisition candidate |
| `industry-fragmentation`, `rollup-thesis`, `target-screening`, `deal-sourcing` skills | `skills/` | Reusable techniques applied by the commands |
| `nppes_query.py`, `census_cbp.py` | `scripts/` | Pull free public data on provider density & establishment counts |

Output lands in `output/search-fund/industry/YYYY-MM-DD-<slug>/` and `output/search-fund/target/YYYY-MM-DD-<slug>/`. For the full deliverable set, templates, and folder layout, see `commands/search-fund-research-guide.md`.

## Prerequisites

- Python 3 (already required by the project's other scripts).
- The SEC EDGAR and Yahoo Finance MCP servers (already configured — see `setup-investment-research.md`). Used for public strategic acquirers and comparable valuation multiples.

## Free public data sources (wired in)

### 1. CMS NPPES NPI Registry — no key required
Counts and lists **organizational** healthcare providers by specialty (taxonomy) and geography. Used for fragmentation signals and proprietary target longlists.

```bash
python3 scripts/nppes_query.py --taxonomy "Home Health" --state FL --limit 100
python3 scripts/nppes_query.py --taxonomy "Physical Therapist" --state TX --city Austin --csv > targets.csv
python3 scripts/nppes_query.py --taxonomy "Skilled Nursing Facility" --state OH --json
```
- Filters to organizations (`NPI-2`), not individuals.
- The API caps results at ~1,200 per query; narrow with `--city` or `--postal` for complete counts in dense states.
- Common taxonomies: "Home Health", "Hospice", "Skilled Nursing Facility", "Physical Therapist", "Dentist", "Behavioral", "Pharmacy".

### 2. US Census County Business Patterns (CBP) — free key required
Establishment counts (`ESTAB`), employment (`EMP`), and payroll (`PAYANN`) by **NAICS** code — the generic path for *any* services vertical (healthcare or not).

1. Get a free, instant key: https://api.census.gov/data/key_signup.html
2. Add it to your shell profile (`~/.zshrc`):
   ```bash
   export CENSUS_API_KEY="your-key-here"
   ```
   Then `source ~/.zshrc`.
3. Query:
   ```bash
   python3 scripts/census_cbp.py --naics 6216 --geo "state:12"        # FL home health
   python3 scripts/census_cbp.py --naics 238220 --geo "us:*"          # US HVAC contractors
   python3 scripts/census_cbp.py --naics 561720 --geo "county:*&in=state:48"  # TX janitorial by county
   ```
- Geo syntax mirrors the Census `for=`/`in=` clauses. State FIPS: FL=12, TX=48, CA=06, NY=36.
- CBP data lags ~2 years; default year is 2022. Override with `--year`.
- Handy NAICS: home health `6216`, dental `6212`, HVAC `238220`, janitorial `561720`, residential property mgmt `531311`, vet services `541940`, laundry/dry-clean `8123`.

### 3. Deal marketplaces & brokers — via WebSearch / WebFetch (no API)
The `deal-sourcing` skill pulls live listings and active intermediaries from public marketplaces. No setup needed; the commands call WebSearch/WebFetch directly.
- **Marketplaces**: BizBuySell, Searchfunder, Axial, BizNexus, Kumo, BizQuest.
- **Healthcare-services M&A advisors** (examples surfaced in research): Mertz Taggart, VERTESS, MidCap Advisors.

## TLS / corporate-proxy note

The scripts auto-discover a working CA bundle (Homebrew/system) so they work without extra setup on most machines. If you're behind a TLS-inspecting proxy (e.g. Zscaler) that presents a certificate OpenSSL rejects, you have two options:
1. Point Python at your corporate CA bundle: `export SSL_CERT_FILE=/path/to/corp-ca-bundle.pem`
2. As a last resort, pass `--insecure` to a script to skip verification (off by default; use only on a trusted network).

## Optional paid platforms (not integrated)

These have no affordable API and aren't wired in. If you subscribe, export their lists/financials and drop them into `input/` so the commands can incorporate them:
- **Grata** / **SourceScrub** — private-company market mapping & off-market target lists.
- **PitchBook** — deal comps, transaction multiples, PE/strategic activity.
- **PrivCo** — private-company financials (US).
- **Definitive Healthcare** — deep healthcare provider/facility intelligence.
- Broker research (e.g. **Mertz Taggart** quarterly healthcare-services M&A reports).

## Test

```bash
# Healthcare path (no key needed):
python3 scripts/nppes_query.py --taxonomy "Home Health" --state FL --limit 20

# Any-services path (needs CENSUS_API_KEY):
python3 scripts/census_cbp.py --naics 6216 --geo "state:12"
```
Then run `/analyze-industry "home health agencies in Florida"` end-to-end.
