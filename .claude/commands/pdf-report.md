# PDF Report: Convert a Markdown Report to PDF

You are a file converter. Your job is to convert a markdown `.md` file to a styled PDF using Pandoc and WeasyPrint.

## Instructions

1. **Identify the file**: The user may provide:
   - A path to an `.md` file
   - Just a filename — search recursively under `output/` (covers `general/`, `stock/`, `search-fund/industry/`, `search-fund/target/`)
   - No argument — find the most recent `.md` in `output/` (excluding `-plan.md` files)
2. **Convert to PDF**: Run the following command via Bash:
   ```
   pandoc <input-file> -o <output-file>.pdf --pdf-engine=weasyprint --css=templates/pdf-style.css
   ```
   - Save the PDF in the same directory as the source file.
   - The output filename should match the input but with `.pdf` extension.
   - `templates/pdf-style.css` is the project stylesheet (Lato typography, dark-blue/accent palette matching the decks, styled tables, running header/footer). Always pass it.
   - **Do not** pass `--metadata title=...`: these reports lead with their own `#` H1, which the stylesheet promotes to the title and the running header. A metadata title would print a duplicate. (A harmless "nonempty <title>" Pandoc warning is expected.)
   - Markdown authoring note: keep a blank line between a bold lead-in line and a following list, or the bullets render as one paragraph.
3. **Report back**: Tell the user the output PDF path and confirm success.

## Error Handling

- If Pandoc is not installed, tell the user to run: `brew install pandoc`
- If WeasyPrint is not installed, tell the user to run: `brew install weasyprint`
- If the file is not found, list available `.md` files in the output directories
- If conversion fails, show the error output and suggest fixes

## User Input

$ARGUMENTS
