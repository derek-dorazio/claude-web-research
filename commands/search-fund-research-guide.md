# Search-Fund Roll-Up Research — Guide

End-to-end reference for the search-fund research capability: the commands, the output-document
templates, the folder structure, the data sources, and worked sample outputs. For one-time data
setup (API keys, TLS notes), see [setup-rollup-research.md](setup-rollup-research.md).

---

## 1. Commands

| Command | What it produces | Output folder |
|---|---|---|
| `/analyze-industry <vertical>` | Sector primer + market map + deal-pipeline workbook + sourcing map for a fragmented vertical | `output/search-fund/industry/<date>-<slug>/` |
| `/analyze-target <company>` | Company profile (tear sheet) + optional IC memo, screened against the buy box | `output/search-fund/target/<date>-<slug>/` |

Both are top-down/bottom-up halves of the same workflow: screen a vertical, build a target longlist,
then screen individual candidates.

```
/analyze-industry "home health agencies in Florida"
        │  (sector primer, market map, deal pipeline)
        ▼
/analyze-target "Acme Home Health"        # a name from the longlist
        │  (tear sheet, IC memo)
        ▼
/slides · /excel · /export pdf            # package for IC
```

These orchestrate four reusable skills in `skills/`: `industry-fragmentation`, `rollup-thesis`,
`target-screening`, `deal-sourcing`.

---

## 2. Output-document templates

Professional formats modeled on what PE shops and research houses produce. Templates live in `templates/`.

| Template | File | Format | Used by | Convention it follows |
|---|---|---|---|---|
| **Sector Primer** | `industry-primer.md` | Markdown → PDF | analyze-industry | McKinsey/Bain sector primer; PE diligence deck |
| **Market Map** | `market-map.md` | Markdown (or slide) | analyze-industry | PitchBook/CB Insights "landscape" — operators by sub-segment |
| **Deal Pipeline / Target Tracker** ("deal list") | `deal_pipeline_xlsx.py` | Excel (generator) | analyze-industry, /excel | M&A pipeline tracker — stage, probability, fit score, owner, next step |
| **Company Profile / Tear Sheet** ("company detail") | `company-profile.md` | Markdown one-pager | analyze-target | IB/PE six-block tear sheet + buy-box scorecard |
| **IC Memo** | `ic-memo.md` | Markdown → PDF | analyze-target | PE investment-committee memo — narrative, "what we must believe", buy-and-build plan |
| **Roll-Up Deck** | `rollup_slides.py` | PowerPoint (generator) | /slides | Industry-primer / IC deck |

### Generators (Python, standalone — `python-pptx` + `openpyxl`, no other deps)

```bash
# Deal pipeline workbook (Dashboard | Active Targets | Passed | Contacts)
python3 templates/deal_pipeline_xlsx.py --output <path>.xlsx            # blank, ready to fill
python3 templates/deal_pipeline_xlsx.py --data targets.json --output <path>.xlsx

# Roll-up / IC slide deck
python3 templates/rollup_slides.py --data deck.json --output <path>.pptx
```
The deal-pipeline workbook ships with Stage and Owner-Transition dropdowns, a Margin% formula,
conditional-formatted stages, and a Dashboard that counts pipeline by stage and computes
probability-weighted EBITDA. JSON shapes are documented in each script's docstring.

---

## 3. Folder structure

Roll-up output is grouped under a `search-fund/` parent so the top level stays clean alongside
`general/` and `stock/`:

```
output/
├── general/                         # /plan, /implement, /research
├── stock/                           # /analyze-stock
└── search-fund/
    ├── industry/<date>-<slug>/      # /analyze-industry
    │   ├── <slug>-primer.md
    │   ├── <slug>-market-map.md
    │   ├── <slug>-deal-pipeline.xlsx
    │   └── <slug>-deck.pptx          (optional, via /slides)
    └── target/<date>-<slug>/        # /analyze-target
        ├── <slug>-profile.md
        └── <slug>-ic-memo.md         (for serious platform candidates)
```

Naming follows the project convention: one folder per query, all files share the `<date>-<slug>`
base with a suffix per deliverable. List everything with `./scripts/list-output.sh` (filter with
e.g. `./scripts/list-output.sh search-fund`).

---

## 4. Data sources

| Source | Access | Role | Setup |
|---|---|---|---|
| CMS NPPES NPI Registry | `scripts/nppes_query.py` (free, no key) | Healthcare provider density + named target longlists | none |
| US Census County Business Patterns | `scripts/census_cbp.py` (free key) | Establishment counts by NAICS — any services vertical | `CENSUS_API_KEY` |
| SEC EDGAR (MCP) | existing MCP | Public strategics / consolidators as comps + exit evidence | existing |
| Yahoo Finance (MCP) | existing MCP | Public-comp multiples to frame entry-multiple arbitrage | existing |
| Deal marketplaces & brokers | WebSearch / WebFetch | Live listings + active intermediaries (BizBuySell, Searchfunder, Axial, BizNexus, Kumo) | none |

Premium platforms (Grata, SourceScrub, PitchBook, PrivCo, Definitive Healthcare) are **not**
integrated — no affordable API. If subscribed, export their data into `input/` and the commands
will incorporate it. Details and example queries: [setup-rollup-research.md](setup-rollup-research.md).

---

## 5. Worked samples

A complete, runnable example ships in the repo (operator names are real from NPPES; **financial
figures are illustrative placeholders**, clearly labeled):

- **Industry**: `output/search-fund/industry/2026-05-31-home-health-rhode-island/`
  — sector primer, market map, deal-pipeline workbook (`.xlsx`), and a 9-slide deck (`.pptx`).
- **Target**: `output/search-fund/target/2026-05-31-access-healthcare-ri/`
  — company profile and IC memo for the platform candidate.

Regenerate the workbook/deck from their JSON to see the generators in action (see each script's docstring).

---

## 6. Quick start

```bash
# 1. (optional) free Census key for non-healthcare sizing
export CENSUS_API_KEY="..."        # https://api.census.gov/data/key_signup.html

# 2. screen a vertical
/analyze-industry "home health agencies in Florida"

# 3. screen a candidate from the longlist
/analyze-target "Acme Home Health"

# 4. package for IC
/slides   <industry folder>        # rollup_slides.py deck
/export pdf <primer or ic-memo>
```

---

## 7. Personalization Options

*Apply the fund's branding — colors, font, and logo — across PDFs, decks, and workbooks.*

All deliverables share one palette and font stack. When you have the fund's brand guidelines, change
them in the places below — no other edits needed. Keep the three sources in sync so PDFs, decks, and
workbooks match.

### 7.1 Brand colors

**PDF** — edit the CSS variables at the top of `templates/pdf-style.css` (`:root { … }`):

| Variable | Controls | Default |
|---|---|---|
| `--dark-blue` | Headings, table header fill, title rule | `#1b2a4a` |
| `--accent` | H2 bar, H3 text, links, list markers | `#2e75b6` |
| `--accent-2` | Positive/secondary accent | `#27ae60` |
| `--row-alt` | Table zebra striping | `#eef5fb` |
| `--muted` | Header/footer text | `#8a9097` |
| `--callout-bg` / `--callout-br` | ⚠️ disclaimer box | `#fef9e7` / `#f39c12` |

```css
/* example: replace with the fund's hex values */
:root { --dark-blue: #0E2A47; --accent: #C8102E; --accent-2: #1F8A70; }
```

**Decks** — edit the `RGBColor(...)` constants near the top of `templates/rollup_slides.py`
(and `templates/stock_analysis_slides.py` to match): `DARK_BLUE`, `ACCENT_BLUE`, `ACCENT_GREEN`,
`ACCENT_RED`, `ACCENT_AMBER`. Use the same hex as the CSS, e.g. `DARK_BLUE = RGBColor(0x0E, 0x2A, 0x47)`.

**Workbook** — edit the hex string constants at the top of `templates/deal_pipeline_xlsx.py`:
`DARK_BLUE`, `ACCENT_BLUE`, `ROW_ALT`, `GREEN`/`RED`/`AMBER` (these are plain strings like `"1B2A4A"`,
no `#`).

### 7.2 Brand font

1. Install the font on the machine (e.g. drop the `.ttf`/`.otf` in `~/Library/Fonts/`); confirm with
   `fc-list | grep -i "<FontName>"`.
2. **PDF** — set it first in the `--sans` (and optionally `--mono`) stack in `templates/pdf-style.css`,
   keeping fallbacks: `--sans: "<Fund Font>", "Lato", "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji";`
3. **Decks** — the generators pass `font_name="Calibri"` in their text helpers; change those to the
   brand font (search `font_name=` and the `.font.name =` lines in `rollup_slides.py`).

### 7.3 Logo

Drop the logo (PNG with transparency, or SVG) in `templates/` as e.g. `fund-logo.png`.

**In the PDF running header** — add a margin-box image to the `@page` rule in `pdf-style.css`
(WeasyPrint resolves the `url()` relative to the CSS file):

```css
@page { @top-left { content: url("fund-logo.png"); } }
/* tip: pad the logo's height to align with the title block */
```

**On a deck title slide** — add an image in `build_title_slide()` in `rollup_slides.py`:

```python
slide.shapes.add_picture("templates/fund-logo.png", Inches(0.5), Inches(0.4),
                         height=Inches(0.6))
```

### 7.4 Cover page (optional)

For an IC/LP-facing cover, add a first-page rule to `pdf-style.css`. WeasyPrint supports `:first`
and named pages:

```css
@page :first {
  margin: 0;
  @top-right { content: none; }          /* hide the running header on the cover */
  @bottom-left { content: none; }
  @bottom-right { content: none; }
}
/* style the document's title block as the cover */
h1 { /* already the title; enlarge / center for a cover if desired */ }
```

For a richer cover (logo + title + date centered on a full page), put an HTML block at the very top of
the markdown — Pandoc passes inline HTML through — and target it with a `.cover` class in the CSS:

```html
<div class="cover">
  <img src="templates/fund-logo.png" alt="">
  <h1>Sector Primer: …</h1>
  <p>Confidential · 2026-05-31</p>
</div>
```
```css
.cover { break-after: page; text-align: center; padding-top: 35vh; }
.cover img { height: 64px; margin-bottom: 1em; }
```

After any change, re-render a sample to check: `/export pdf <path>` or
`pandoc <file>.md -o <file>.pdf --pdf-engine=weasyprint --css=templates/pdf-style.css`.

---

See also: [README](README.md) (all commands) · [../skills/README.md](../skills/README.md) (skills) ·
[setup-rollup-research.md](setup-rollup-research.md) (data setup) · [../templates/README.md](../templates/README.md) (templates).
