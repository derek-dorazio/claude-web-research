#!/bin/bash
# List all research output, organized by type and query.
# Query folders are named YYYY-MM-DD-<slug> and may sit one or two levels deep
# (e.g. output/general/<query> or output/search-fund/industry/<query>).
# Usage: ./scripts/list-output.sh [path-filter]
#   path-filter: optional substring to limit results, e.g. "search-fund", "stock", "industry"

BASE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
OUTPUT_DIR="$BASE_DIR/output"
FILTER="$1"

[ -d "$OUTPUT_DIR" ] || { echo "(no output)"; exit 0; }

# Find dated query folders at any depth, print path relative to output/ + contents.
find "$OUTPUT_DIR" -type d -name '20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]-*' \
    | sort \
    | while read -r dir; do
        rel="${dir#"$OUTPUT_DIR"/}"
        if [ -n "$FILTER" ] && [[ "$rel" != *"$FILTER"* ]]; then
            continue
        fi
        echo "$rel/"
        ls -1t "$dir" 2>/dev/null | sed 's/^/    /'
    done

# If nothing matched, say so.
if [ -z "$(find "$OUTPUT_DIR" -type d -name '20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]-*' 2>/dev/null)" ]; then
    echo "(no output)"
fi
