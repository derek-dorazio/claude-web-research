# Templates

Reusable output templates for professional-looking deliverables. Markdown templates are fill-in
skeletons (copy and replace `<placeholders>`); Python templates are generators run from the CLI or
imported. See [../commands/search-fund-research-guide.md](../commands/search-fund-research-guide.md)
for how each maps to a command and deliverable.

## Markdown templates

| File | Deliverable | Used by |
|---|---|---|
| [industry-primer.md](industry-primer.md) | Sector / industry primer (the deep report) | `/analyze-industry` |
| [market-map.md](market-map.md) | Market map — operators grouped by sub-segment | `/analyze-industry` |
| [company-profile.md](company-profile.md) | Company profile / tear sheet (one-pager) | `/analyze-target` |
| [ic-memo.md](ic-memo.md) | Investment-committee memo | `/analyze-target` |

## Print stylesheet

| File | Purpose | Used by |
|---|---|---|
| [pdf-style.css](pdf-style.css) | Markdown→PDF styling: Lato typography, dark-blue/accent palette (matches the decks), styled tables, blockquote callouts, running header (doc title) + footer (page numbers) | `/pdf-report`, `/export` (passed via `--css`) |

The PDF commands pass this automatically. Don't also pass `--metadata title=...` — the report's own `#` H1 becomes the title (the stylesheet promotes it and feeds the running header); a metadata title would duplicate it.

## Python generators

| File | Output | Run |
|---|---|---|
| [deal_pipeline_xlsx.py](deal_pipeline_xlsx.py) | Deal-pipeline Excel workbook (Dashboard / Active / Passed / Contacts) | `python3 templates/deal_pipeline_xlsx.py --output x.xlsx [--data targets.json]` |
| [rollup_slides.py](rollup_slides.py) | Roll-up / IC PowerPoint deck | `python3 templates/rollup_slides.py --data deck.json --output x.pptx` |
| [stock_analysis_slides.py](stock_analysis_slides.py) | Stock-analysis PowerPoint deck | `python3 templates/stock_analysis_slides.py --data d.json --output x.pptx` |

Generators depend on `python-pptx` and `openpyxl` (both already installed). Each file's docstring
documents its CLI flags and expected JSON shape.

## Branding / personalization

To apply the fund's colors, font, and logo across PDFs, decks, and workbooks, follow
**Personalization Options** in [../commands/search-fund-research-guide.md](../commands/search-fund-research-guide.md#7-personalization-options-fund-branding--logo)
— it lists the exact variables/constants to change in `pdf-style.css`, `rollup_slides.py`,
`stock_analysis_slides.py`, and `deal_pipeline_xlsx.py`, plus cover-page and logo snippets.

## Conventions
- Save generated files into the source query folder (`output/<type>/<date>-<slug>/`), sharing the
  `<date>-<slug>` base name with a deliverable suffix (`-primer.md`, `-deal-pipeline.xlsx`, `-deck.pptx`).
- Keep the dark-blue / accent color scheme consistent across decks and workbooks.
- Label any unverified or estimated figures.
