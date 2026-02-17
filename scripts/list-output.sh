#!/bin/bash
# List all research output, organized by type and query
# Usage: ./scripts/list-output.sh [general|stock]

BASE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
OUTPUT_DIR="$BASE_DIR/output"

if [ -n "$1" ]; then
    echo "=== $1 ==="
    for dir in "$OUTPUT_DIR/$1"/*/; do
        [ -d "$dir" ] || continue
        echo "  $(basename "$dir")/"
        ls -1t "$dir" 2>/dev/null | sed 's/^/    /'
    done
    [ ! -d "$OUTPUT_DIR/$1" ] && echo "  (no output)"
else
    for type in general stock; do
        echo "=== $type ==="
        if [ -d "$OUTPUT_DIR/$type" ]; then
            for dir in "$OUTPUT_DIR/$type"/*/; do
                [ -d "$dir" ] || continue
                echo "  $(basename "$dir")/"
                ls -1t "$dir" 2>/dev/null | sed 's/^/    /'
            done
        else
            echo "  (no output)"
        fi
        echo ""
    done
fi
