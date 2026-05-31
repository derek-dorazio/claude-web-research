# Setup — Claude Code CLI (macOS, fresh machine)

Get this project running from a terminal on a brand-new Mac with nothing installed. The CLI runs
inside your shell, so once your shell profile has the tools and env vars, everything "just works."
(For the GUI app, see [setup-claude-code-desktop.md](setup-claude-code-desktop.md).)

← Back to [README](../README.md)

## What you'll install
Homebrew · git · Python 3 + `python-pptx`/`openpyxl` · `uv`/`uvx` (MCP runtime) · `pandoc` + `weasyprint`
(PDF) · LibreOffice (PPTX→PDF) · the Yahoo Finance MCP server · the Claude Code CLI.

A helper script does the heavy lifting; the manual equivalents are listed if you'd rather see each step.

## 1. Get the project
```bash
# install Xcode command line tools (provides git) if prompted:
xcode-select --install 2>/dev/null || true
git clone https://github.com/derek-dorazio/claude-web-research.git
cd claude-web-research
```
(If you don't yet have `git`, install Homebrew first — step 2 — then `brew install git`.)

## 2. Install dependencies (one command)
```bash
./scripts/setup-macos.sh
```
This installs Homebrew (if missing), `python uv pandoc weasyprint git`, LibreOffice, the Python
packages, and clones the Yahoo Finance MCP server to `~/Tools/yahoo-finance-mcp`. It's re-runnable.

<details>
<summary>Manual equivalent</summary>

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python uv pandoc weasyprint git
brew install --cask libreoffice
python3 -m pip install --break-system-packages python-pptx openpyxl
git clone https://github.com/Alex2Yang97/yahoo-finance-mcp.git ~/Tools/yahoo-finance-mcp
```
</details>

## 3. Install the Claude Code CLI
Per the [official setup docs](https://code.claude.com/docs/en/setup), use any one of:
```bash
brew install --cask claude-code                      # Homebrew (upgrade with: brew upgrade claude-code)
# or the native installer (auto-updates):
curl -fsSL https://claude.ai/install.sh | bash
# or via npm (needs Node 18+):
npm install -g @anthropic-ai/claude-code
```

## 4. Set environment variables (in your shell profile)
Because the CLI inherits your shell, put these in `~/.zshrc`:
```bash
# free, instant key — needed by /analyze-industry's Census script:
export CENSUS_API_KEY="your-key"        # https://api.census.gov/data/key_signup.html
# optional: SEC EDGAR identifier (already hard-set in .mcp.json, so usually not needed):
export SEC_EDGAR_USER_AGENT="Your Name your.email@example.com"
```
Then reload: `source ~/.zshrc`.

## 5. Verify
```bash
./scripts/check-prereqs.sh    # green ✓ for every required item
claude --version
claude doctor                  # install health + auth status
```

## 6. First run
```bash
cd /path/to/claude-web-research
claude
```
- On first launch your browser opens to sign in (Claude Pro/Max/Team/Enterprise or Console). Inside a session you can re-auth with `/login`.
- You'll be prompted to **trust this project's `.mcp.json`** — approve it. Review first with `cat .mcp.json`.
- Confirm the MCP servers connected: type `/mcp` (expect `powerpoint`, `excel`, `yahoo-finance`, `sec-edgar`).
- Smoke test: `/research What are the top JavaScript frameworks in 2026?` then `/export pdf` on the result.

## Troubleshooting
- **An MCP server shows failed in `/mcp`** → ensure `uv` is on PATH (`which uv`); the `yahoo-finance` entry in `.mcp.json` must point at your clone (`~/Tools/yahoo-finance-mcp`).
- **PDF export fails** → `which pandoc weasyprint`; re-run `./scripts/setup-macos.sh`.
- **`pip` says "externally-managed-environment"** → the setup script already handles this with `--break-system-packages`; manually: `python3 -m pip install --break-system-packages python-pptx openpyxl`.
- **TLS / certificate errors from the data scripts** (corporate proxy like Zscaler) → see the TLS note in [../commands/setup-rollup-research.md](../commands/setup-rollup-research.md).
- Full diagnostics: `claude doctor`, `/status`, `/config`.

## Related
- GUI app instead: [setup-claude-code-desktop.md](setup-claude-code-desktop.md)
- Investment MCP setup: [../commands/setup-investment-research.md](../commands/setup-investment-research.md) · Roll-up data setup: [../commands/setup-rollup-research.md](../commands/setup-rollup-research.md)
- What you can do next: [general](general-research.md) · [stock](stock-research.md) · [search-fund](search-fund-research.md) research
