#!/bin/bash
# Clean output query folders older than N days (default: 30)
# Removes entire query folders, not individual files
# Usage: ./scripts/clean-output.sh [days]

BASE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
OUTPUT_DIR="$BASE_DIR/output"
DAYS="${1:-30}"

echo "Cleaning output query folders older than $DAYS days..."
find "$OUTPUT_DIR" -mindepth 2 -maxdepth 2 -type d -mtime +"$DAYS" -print -exec rm -rf {} +
echo "Done."
