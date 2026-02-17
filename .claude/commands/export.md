# Export: Convert a Markdown Report to Other Formats

You are a format exporter. Your job is to take an existing markdown report and convert it to one or more output formats.

## Supported Formats

| Format | What It Does | Tool Used |
|--------|-------------|-----------|
| `pdf-report` | Converts markdown to a styled PDF | Pandoc + WeasyPrint |
| `slides` | Creates a PowerPoint presentation from the content | PowerPoint MCP server |
| `pdf-slides` | Creates a PowerPoint presentation, then converts it to PDF | PowerPoint MCP + LibreOffice |

## Instructions

1. **Identify the source file**: The user may provide:
   - A path to an `.md` file
   - Just a filename — search recursively in `output/general/*/` and `output/stock/*/`
   - No file specified — find the most recent `.md` in `output/` (excluding `-plan.md` files)

2. **Identify requested formats**: Parse the user's input for one or more of: `pdf-report`, `slides`, `pdf-slides`, `pdf`, `all`.
   - If no format specified, ask the user which formats they want.
   - `pdf` is shorthand for `pdf-report`.
   - `all` means all three formats.

3. **Execute each format in order**:

   ### pdf-report
   Convert markdown to PDF:
   ```bash
   pandoc <input.md> -o <output-dir>/<basename>.pdf --pdf-engine=weasyprint --metadata title="<title>"
   ```
   - If `templates/pdf-style.css` exists, add `--css=templates/pdf-style.css`
   - Save to the same directory as the source file

   ### slides
   Create a PowerPoint presentation from the report content:
   - Read the source markdown file
   - Plan a slide deck (title, overview, key content slides, summary)
   - Use the PowerPoint MCP tools: `create_presentation`, `add_slide`, `add_textbox`, `add_table`, `save_presentation`
   - Follow the design guidelines from the `/slides` command: one idea per slide, bullets not paragraphs, 5-6 bullets max, tables for comparisons
   - Save the `.pptx` in the same query folder as the source file

   ### pdf-slides
   Run `slides` first (if not already done), then convert the `.pptx` to PDF:
   ```bash
   /Applications/LibreOffice.app/Contents/MacOS/soffice --headless --convert-to pdf --outdir <same-query-folder> <pptx-file>
   ```

4. **Zip if multiple outputs**: If more than one file was generated, zip all output files in the query folder:
   ```bash
   cd <query-folder> && zip YYYY-MM-DD-<slug>.zip *.md *.pdf *.pptx *.xlsx 2>/dev/null
   ```

5. **Report back**: List all generated files with their paths. If zipped, report the zip path.

## Error Handling

- If Pandoc is missing: `brew install pandoc`
- If WeasyPrint is missing: `brew install weasyprint`
- If LibreOffice is missing: `brew install --cask libreoffice`
- If the PowerPoint MCP server is unavailable, skip `slides` and `pdf-slides` and notify the user
- If any conversion fails, continue with remaining formats and report errors at the end

## Examples

```
/export my-report.md as pdf-report slides
/export 2026-02-14-australia-restaurants-report.md all
/export pdf
/export slides pdf-slides
```

## User Input

$ARGUMENTS
