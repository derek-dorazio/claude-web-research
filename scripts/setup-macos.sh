#!/usr/bin/env bash
# One-shot setup for the Web Research Project on a fresh macOS machine.
# Installs Homebrew + project dependencies, clones the Yahoo Finance MCP server,
# installs the Python packages, and (optionally) configures the env block the
# Claude Code Desktop app needs. Re-runnable: skips anything already present.
#
#   ./scripts/setup-macos.sh                    # install all project dependencies
#   ./scripts/setup-macos.sh --configure-desktop  # also write .claude/settings.local.json env (PATH + CENSUS_API_KEY) for the Desktop app
#
# This installs the project's LIBRARIES. It does not install the Claude Code app
# itself — see docs/setup-claude-code-cli.md / docs/setup-claude-code-desktop.md.
set -euo pipefail

CONFIGURE_DESKTOP=0
[ "${1:-}" = "--configure-desktop" ] && CONFIGURE_DESKTOP=1
REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
YF_DIR="$HOME/Tools/yahoo-finance-mcp"
say(){ printf "\n\033[1m== %s\033[0m\n" "$1"; }

[ "$(uname)" = "Darwin" ] || { echo "This installer targets macOS. See the setup docs for other platforms."; exit 1; }

say "1/6  Homebrew"
if ! command -v brew >/dev/null 2>&1; then
  echo "Installing Homebrew (may prompt for your password)…"
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  eval "$(/opt/homebrew/bin/brew shellenv 2>/dev/null || /usr/local/bin/brew shellenv)"
else
  echo "already installed: $(brew --version | head -1)"
fi

say "2/6  CLI tools (python, uv, pandoc, weasyprint, git)"
brew install python uv pandoc weasyprint git

say "3/6  LibreOffice (for /pdf-slides — large download, optional but recommended)"
if brew list --cask libreoffice >/dev/null 2>&1; then echo "already installed"; else brew install --cask libreoffice; fi

say "4/6  Python packages (python-pptx, openpyxl)"
# Homebrew's Python is 'externally managed'; fall back to --break-system-packages.
python3 -m pip install --user python-pptx openpyxl 2>/dev/null \
  || python3 -m pip install --break-system-packages python-pptx openpyxl

say "5/6  Yahoo Finance MCP server"
if [ -d "$YF_DIR" ]; then
  echo "already cloned: $YF_DIR"
else
  mkdir -p "$HOME/Tools"
  git clone https://github.com/Alex2Yang97/yahoo-finance-mcp.git "$YF_DIR"
fi
# Keep .mcp.json's path in sync if the user cloned elsewhere previously — informational only:
grep -q "$YF_DIR" "$REPO_DIR/.mcp.json" 2>/dev/null || echo "  note: ensure .mcp.json 'yahoo-finance' --directory points to $YF_DIR"

say "6/6  Desktop env (optional)"
if [ "$CONFIGURE_DESKTOP" = 1 ]; then
  BREW_BIN="$(brew --prefix)/bin"
  python3 - "$REPO_DIR/.claude/settings.local.json" "$BREW_BIN" <<'PY'
import json, os, sys
settings, brew_bin = sys.argv[1], sys.argv[2]
data = {}
if os.path.exists(settings):
    try: data = json.load(open(settings))
    except json.JSONDecodeError: data = {}
env = data.setdefault("env", {})
candidates = [brew_bin, brew_bin.replace("/bin", "/sbin"),
              os.path.expanduser("~/.local/bin"),
              "/usr/local/bin", "/usr/bin", "/bin", "/usr/sbin", "/sbin"]
seen = set(); path = [p for p in candidates if not (p in seen or seen.add(p))]
env["PATH"] = ":".join(path)
env.setdefault("CENSUS_API_KEY", "")  # <-- paste your free key here
os.makedirs(os.path.dirname(settings), exist_ok=True)
json.dump(data, open(settings, "w"), indent=2)
print(f"  wrote env.PATH to {settings}")
print("  → add your CENSUS_API_KEY value in that file (free: https://api.census.gov/data/key_signup.html)")
PY
else
  echo "  skipped. For the Desktop app, re-run with --configure-desktop (see docs/setup-claude-code-desktop.md)."
fi

say "Verifying"
"$REPO_DIR/scripts/check-prereqs.sh" || true
cat <<EOF

Next steps:
  • Install the Claude Code app — docs/setup-claude-code-cli.md or docs/setup-claude-code-desktop.md
  • Get a free CENSUS_API_KEY — https://api.census.gov/data/key_signup.html
  • Open this folder in Claude Code and approve the .mcp.json servers, then try:  /research <a question>
EOF
