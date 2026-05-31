# Setup — Claude Code Desktop app (macOS, fresh machine)

Get this project running in the **Claude Code Desktop app** on a brand-new Mac. The big difference
from the CLI: when the app is launched from the Dock/Finder it does **not** inherit your shell's
`PATH` or environment variables — so we make the project's tools and keys available through the
project's `.claude/settings.local.json` instead. (Terminal user? See [setup-claude-code-cli.md](setup-claude-code-cli.md).)

← Back to [README](../README.md)

## What you'll install
Homebrew · git · Python 3 + `python-pptx`/`openpyxl` · `uv`/`uvx` (MCP runtime) · `pandoc` + `weasyprint`
(PDF) · LibreOffice (PPTX→PDF) · the Yahoo Finance MCP server · the Claude Code Desktop app.

## 1. Get the project
```bash
xcode-select --install 2>/dev/null || true   # provides git on a fresh Mac
git clone https://github.com/derek-dorazio/claude-web-research.git
cd claude-web-research
```

## 2. Install dependencies **and** configure the Desktop environment (one command)
```bash
./scripts/setup-macos.sh --configure-desktop
```
This installs Homebrew + all tools (same as the CLI), clones the Yahoo Finance MCP server, **and**
writes an `env` block into `.claude/settings.local.json` so the Desktop app can find them:

```jsonc
{
  "env": {
    "PATH": "/opt/homebrew/bin:/opt/homebrew/sbin:/Users/<you>/.local/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin",
    "CENSUS_API_KEY": ""          // ← paste your free key
  },
  ...existing permissions / enabledMcpjsonServers...
}
```
Per the Claude Code docs, this `env` block applies to **both** the Bash tool and MCP servers, so it
makes `uvx`/`uv`, `pandoc`, `weasyprint`, and `CENSUS_API_KEY` resolve in the GUI app. `.claude/settings.local.json`
is gitignored, so machine-specific paths and keys stay local.

> **Why this is needed:** GUI-launched apps don't read `~/.zshrc`, and Homebrew installs to
> `/opt/homebrew/bin` (Apple Silicon) — which isn't on the app's default `PATH`. Without this, MCP
> servers and PDF export silently fail in the Desktop app even though they work in the terminal.

## 3. Add your Census key
Open `.claude/settings.local.json` and set `CENSUS_API_KEY` to your free key from
<https://api.census.gov/data/key_signup.html>. (`SEC_EDGAR_USER_AGENT` is already set in `.mcp.json`.)

## 4. Install the Claude Code Desktop app
- Download the macOS app (universal) from the [official desktop quickstart](https://code.claude.com/docs/en/desktop-quickstart),
  open the `.dmg`, and drag **Claude** to Applications. There is **no Homebrew cask** for the Desktop app.
- It is a **separate** application from the consumer "Claude" chat app, and the **Code** tab requires a
  Claude Pro, Max, Team, or Enterprise subscription.

## 5. Open the project
1. Launch Claude → open the **Code** tab → sign in with your Anthropic account.
2. Choose **Local**, click **Select folder**, and pick the `claude-web-research` directory.
3. Approve the **`.mcp.json` trust prompt** when asked (review with the file open if you like).
4. Confirm servers connected: type `/mcp` — expect `powerpoint`, `excel`, `yahoo-finance`, `sec-edgar`.

## 6. Verify
- In a session, ask: *"Run ./scripts/check-prereqs.sh"* — every required item should be green ✓.
- Smoke test: `/research What are the top JavaScript frameworks in 2026?`, then `/export pdf` the result and open the PDF.

## Desktop gotchas (vs the CLI)
- **The `!` inline-shell prefix is CLI-only.** In Desktop, just ask in plain language (e.g. "run the NPPES script for FL home health") and Claude invokes the Bash tool.
- **Working directory** is chosen via the folder picker (defaults to home) — point it at the repo. The project already uses absolute paths in `.mcp.json` and the LibreOffice command, which is the Desktop-friendly pattern.
- **If an MCP server still won't start** after step 2, hard-code the runtime path in `.mcp.json`: change `"command": "uvx"` → `"command": "/opt/homebrew/bin/uvx"` (and `"uv"` → `"/opt/homebrew/bin/uv"`).
- **Changed `settings.local.json`?** It hot-reloads; if a server is stuck, toggle it in `/mcp` or restart the app.

## Troubleshooting
Same tool-level issues as the CLI guide — see the [Troubleshooting section there](setup-claude-code-cli.md#troubleshooting), plus the TLS/proxy note in [../commands/setup-rollup-research.md](../commands/setup-rollup-research.md).

## Related
- Terminal instead: [setup-claude-code-cli.md](setup-claude-code-cli.md)
- Investment MCP setup: [../commands/setup-investment-research.md](../commands/setup-investment-research.md) · Roll-up data setup: [../commands/setup-rollup-research.md](../commands/setup-rollup-research.md)
- What you can do next: [general](general-research.md) · [stock](stock-research.md) · [search-fund](search-fund-research.md) research
