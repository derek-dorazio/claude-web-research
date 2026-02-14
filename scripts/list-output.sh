#!/bin/bash
# List all research output files, organized by type
# Usage: ./scripts/list-output.sh [plan|implement|research]

BASE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
OUTPUT_DIR="$BASE_DIR/output"

if [ -n "$1" ]; then
    echo "=== $1 ==="
    ls -1t "$OUTPUT_DIR/$1"/*.md 2>/dev/null || echo "  (no files)"
else
    for dir in plan implement research; do
        echo "=== $dir ==="
        ls -1t "$OUTPUT_DIR/$dir"/*.md 2>/dev/null || echo "  (no files)"
        echo ""
    done
fi
