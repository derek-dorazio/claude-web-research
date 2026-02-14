#!/bin/bash
# Clean output files older than N days (default: 30)
# Usage: ./scripts/clean-output.sh [days]

BASE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
OUTPUT_DIR="$BASE_DIR/output"
DAYS="${1:-30}"

echo "Cleaning output files older than $DAYS days..."
find "$OUTPUT_DIR" -name "*.md" -mtime +"$DAYS" -print -delete
echo "Done."
