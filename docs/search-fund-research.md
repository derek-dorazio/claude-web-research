# Search-Fund / Roll-Up Research

Top-down and bottom-up research for consolidating fragmented industries: screen a vertical for
roll-up potential (sector primer, fragmentation, market map, target longlist, sourcing), then screen
individual acquisition candidates against the search-fund buy box (tear sheet, IC memo).

← Back to [README](../README.md) · See also [general-research.md](general-research.md) ·
[stock-research.md](stock-research.md)

## When to use it
Building a consolidation thesis in healthcare services or any fragmented "other services" vertical,
and evaluating private SMB acquisition targets. For public equities use
[stock research](stock-research.md).

> **Deep guide & setup.** This page is the reference card. For the full walkthrough, worked samples,
> and **fund-branding personalization**, see [commands/search-fund-research-guide.md](../commands/search-fund-research-guide.md).
> For data-source setup (API keys, TLS notes), see [commands/setup-rollup-research.md](../commands/setup-rollup-research.md).

## Commands
| Command | Purpose | File |
|---|---|---|
| `/analyze-industry <vertical>` | Sector primer + fragmentation + market map + deal pipeline + sourcing map | [.claude/commands/analyze-industry.md](../.claude/commands/analyze-industry.md) |
| `/analyze-target <company>` | Buy-box screen → company profile (+ IC memo for serious candidates) | [.claude/commands/analyze-target.md](../.claude/commands/analyze-target.md) |
| `/slides`, `/excel`, `/export pdf` | IC deck, deal-pipeline workbook, PDF | [export.md](../.claude/commands/export.md) |

## Skills applied
Roll-up skills in [`skills/`](../skills/README.md) (plus reused `valuation`, `competitor-analysis`, `fact-check`):

| Skill | Purpose |
|---|---|
| [industry-fragmentation](../skills/industry-fragmentation.md) | Quantify fragmentation (establishment/provider counts, concentration) |
| [rollup-thesis](../skills/rollup-thesis.md) | Why-now, value-creation levers, exit pathways, risks |
| [target-screening](../skills/target-screening.md) | Score a candidate against the buy box; red flags |
| [deal-sourcing](../skills/deal-sourcing.md) | Map brokers, marketplaces & proprietary outreach into a tracker |

## Input structure
- **Industry**: a vertical, optionally with geography — `/analyze-industry "home health agencies in Florida"`.
- **Target**: a company name and/or a listing URL — `/analyze-target "Acme Home Health"` or a BizBuySell URL.
- Optional [`input/`](../input) file for detailed briefs; paste exports from paid platforms (Grata, PitchBook, etc.) into `input/` to fold them in.

## Output structure
Roll-up output is grouped under the `search-fund/` parent:
```
output/search-fund/
├── industry/YYYY-MM-DD-<slug>/
│   ├── <slug>-primer.md / .pdf        # sector primer
│   ├── <slug>-market-map.md / .pdf    # market map
│   ├── <slug>-deal-pipeline.xlsx      # target tracker ("deal list")
│   └── <slug>-deck.pptx               # IC/industry deck (optional)
└── target/YYYY-MM-DD-<slug>/
    ├── <slug>-profile.md / .pdf       # company tear sheet
    └── <slug>-ic-memo.md / .pdf       # investment-committee memo
```
Worked samples ship in the repo: `output/search-fund/industry/2026-05-31-home-health-rhode-island/`
and `output/search-fund/target/2026-05-31-access-healthcare-ri/`.

## Templates
| Template | Deliverable |
|---|---|
| [industry-primer.md](../templates/industry-primer.md) | Sector primer |
| [market-map.md](../templates/market-map.md) | Market map (segment grid) |
| [company-profile.md](../templates/company-profile.md) | Company tear sheet (one-pager) |
| [ic-memo.md](../templates/ic-memo.md) | Investment-committee memo |
| [deal_pipeline_xlsx.py](../templates/deal_pipeline_xlsx.py) | Deal-pipeline Excel generator |
| [rollup_slides.py](../templates/rollup_slides.py) | Roll-up / IC deck generator |
| [pdf-style.css](../templates/pdf-style.css) | PDF styling (rebrandable — see the guide) |

## Data sources & tools
| Source | Access | Role |
|---|---|---|
| CMS NPPES NPI Registry | [`scripts/nppes_query.py`](../scripts/nppes_query.py) (free, no key) | Healthcare provider density + target longlists |
| US Census County Business Patterns | [`scripts/census_cbp.py`](../scripts/census_cbp.py) (free `CENSUS_API_KEY`) | Establishment counts by NAICS — any services vertical |
| SEC EDGAR MCP / Yahoo Finance MCP | existing MCP servers | Public strategics & comps for exit/arbitrage framing |
| Deal marketplaces & brokers | `WebSearch`/`WebFetch` | Live listings + active intermediaries |

Premium platforms (Grata, SourceScrub, PitchBook, Definitive Healthcare) are not integrated — paste
exports into `input/`. Details: [setup-rollup-research.md](../commands/setup-rollup-research.md).

## Workflow
```
/analyze-industry <vertical>  →  /analyze-target <longlist name>  →  /slides · /excel · /export pdf
```
