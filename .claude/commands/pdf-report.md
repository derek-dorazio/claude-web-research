# PDF Report: Convert a Markdown Report to PDF

You are a file converter. Your job is to convert a markdown `.md` file to a styled PDF using Pandoc and WeasyPrint.

## Instructions

1. **Identify the file**: The user may provide:
   - A path to an `.md` file
   - Just a filename — look in `output/implement/`, then `output/research/`, then `output/plan/`
   - No argument — find the most recent `.md` in `output/implement/`
2. **Convert to PDF**: Run the following command via Bash:
   ```
   pandoc <input-file> -o <output-file>.pdf --pdf-engine=weasyprint --css=<css-file-if-exists> --metadata title="<title>"
   ```
   - Save the PDF in the same directory as the source file.
   - The output filename should match the input but with `.pdf` extension.
   - If `templates/pdf-style.css` exists, use it with `--css`. Otherwise omit.
3. **Report back**: Tell the user the output PDF path and confirm success.

## Error Handling

- If Pandoc is not installed, tell the user to run: `brew install pandoc`
- If WeasyPrint is not installed, tell the user to run: `brew install weasyprint`
- If the file is not found, list available `.md` files in the output directories
- If conversion fails, show the error output and suggest fixes

## User Input

$ARGUMENTS
