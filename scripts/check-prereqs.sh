#!/usr/bin/env bash
# Prerequisite checker for the Web Research Project.
# Read-only: verifies the tools, Python packages, MCP clone, and env vars the
# project needs. Exits non-zero if a REQUIRED item is missing.
#
#   ./scripts/check-prereqs.sh
#
# See docs/setup-claude-code-cli.md or docs/setup-claude-code-desktop.md to fix anything missing.
set -u
G=$'\033[32m'; R=$'\033[31m'; Y=$'\033[33m'; B=$'\033[1m'; X=$'\033[0m'
ok=0; warn=0; miss=0
pass(){ printf "  ${G}✓${X} %-22s %s\n" "$1" "${2:-}"; ok=$((ok+1)); }
opt(){  printf "  ${Y}!${X} %-22s %s\n" "$1" "${2:-}"; warn=$((warn+1)); }
bad(){  printf "  ${R}✗${X} %-22s %s\n" "$1" "${2:-}"; miss=$((miss+1)); }
have(){ command -v "$1" >/dev/null 2>&1; }

printf "${B}Web Research Project — prerequisite check${X}\n\n"

echo "Core:"
have brew      && pass "Homebrew"   "$(brew --version | head -1)"        || bad "Homebrew" "install: https://brew.sh"
have git       && pass "git"        "$(git --version)"                   || bad "git"      "brew install git"
have python3   && pass "python3"    "$(python3 --version 2>&1)"          || bad "python3"  "brew install python"
have pip3      && pass "pip3"       "$(pip3 --version 2>&1 | cut -d' ' -f1-2)" || opt "pip3" "python3 -m ensurepip --upgrade"

echo; echo "MCP runtimes:"
have uv  && pass "uv"  "$(uv --version 2>&1)" || bad "uv"  "brew install uv"
have uvx && pass "uvx" ""                     || bad "uvx" "ships with uv (brew install uv)"
YF="$HOME/Tools/yahoo-finance-mcp"
[ -d "$YF" ] && pass "yahoo-finance-mcp" "$YF" || opt "yahoo-finance-mcp" "clone to $YF (see setup doc)"

echo; echo "Export tools:"
have pandoc     && pass "pandoc"     "$(pandoc --version | head -1)"                 || bad "pandoc"     "brew install pandoc"
have weasyprint && pass "weasyprint" "$(weasyprint --version 2>&1 | head -1)"        || bad "weasyprint" "brew install weasyprint"
if [ -x "/Applications/LibreOffice.app/Contents/MacOS/soffice" ] || have soffice; then
  pass "LibreOffice" "soffice"
else
  opt "LibreOffice" "brew install --cask libreoffice (only needed for /pdf-slides)"
fi

echo; echo "Python packages (slide/Excel generators):"
for mod in pptx openpyxl; do
  label=$mod; [ "$mod" = pptx ] && label="python-pptx"
  if python3 -c "import $mod" 2>/dev/null; then
    pass "$label" "$(python3 -c "import $mod,sys; print(getattr($mod,'__version__',''))" 2>/dev/null)"
  else
    bad "$label" "pip3 install $label  (or run scripts/setup-macos.sh)"
  fi
done

echo; echo "Environment variables:"
[ -n "${CENSUS_API_KEY:-}" ]       && pass "CENSUS_API_KEY" "set"       || opt "CENSUS_API_KEY"       "optional; free key: https://api.census.gov/data/key_signup.html"
[ -n "${SEC_EDGAR_USER_AGENT:-}" ] && pass "SEC_EDGAR_USER_AGENT" "set" || opt "SEC_EDGAR_USER_AGENT" "optional in env (already set in .mcp.json)"

echo; echo "Claude Code:"
have claude && pass "claude" "$(claude --version 2>/dev/null | head -1)" || opt "claude" "CLI optional here; see docs/setup-claude-code-cli.md"

echo
printf "${B}Summary:${X} ${G}%d ok${X}, ${Y}%d warning(s)${X}, ${R}%d missing${X}\n" "$ok" "$warn" "$miss"
if [ "$miss" -gt 0 ]; then
  echo "→ Run ./scripts/setup-macos.sh to install the missing required items (macOS)."
  exit 1
fi
echo "All required prerequisites present. ✓"
