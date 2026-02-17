# PDF Slides: Convert a PowerPoint Presentation to PDF

You are a file converter. Your job is to convert a `.pptx` file to PDF using LibreOffice.

## Instructions

1. **Identify the file**: The user may provide:
   - A path to a `.pptx` file
   - Just a filename — search recursively in `output/general/*/` and `output/stock/*/`
   - No argument — find the most recent `.pptx` in `output/`
2. **Convert to PDF**: Run the following command via Bash:
   ```
   /Applications/LibreOffice.app/Contents/MacOS/soffice --headless --convert-to pdf --outdir <output-dir> <input-file>
   ```
   Save the PDF alongside the original `.pptx` in the same query folder.
3. **Report back**: Tell the user the output PDF path and confirm success.

## Error Handling

- If LibreOffice is not installed, tell the user to run: `brew install --cask libreoffice`
- If the file is not found, search for `.pptx` files recursively in `output/`
- If conversion fails, show the error output

## User Input

$ARGUMENTS
