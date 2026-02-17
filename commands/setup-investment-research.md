# Setup: Investment Research Capabilities

How to configure the Yahoo Finance and SEC EDGAR MCP servers for investment research.

## Prerequisites

- `uv` installed: `brew install uv`
- Git (for cloning Yahoo Finance MCP)

## Yahoo Finance MCP

Provides: stock prices, financial statements, metrics, news, options, analyst ratings.

### Setup

1. **Clone the repository** (already done if following the plan):
   ```bash
   git clone https://github.com/Alex2Yang97/yahoo-finance-mcp.git ~/Tools/yahoo-finance-mcp
   ```

2. **Update `.mcp.json`**: Ensure the path matches your clone location:
   ```json
   "yahoo-finance": {
     "command": "uv",
     "args": [
       "--directory",
       "/Users/YourName/Tools/yahoo-finance-mcp",
       "run",
       "server.py"
     ],
     "env": {}
   }
   ```

3. **Test**: Restart Claude Code, then try asking for stock info on any ticker.

### Available Tools

| Tool | Description |
|---|---|
| `get_stock_info` | Comprehensive stock data (price, metrics, fundamentals) |
| `get_historical_stock_prices` | OHLCV data with customizable periods |
| `get_financial_statement` | Income statement, balance sheet, cash flow |
| `get_yahoo_finance_news` | Latest news articles |
| `get_stock_actions` | Dividends and stock splits |
| `get_holder_info` | Institutional, insider, and major holders |
| `get_recommendations` | Analyst ratings and history |
| `get_option_expiration_dates` | Available option expiration dates |
| `get_option_chain` | Calls/puts for a specific expiration |

## SEC EDGAR MCP

Provides: official SEC filings (10-K, 10-Q, 8-K), XBRL-parsed financials, insider trading data.

### Setup

1. **Set user agent** (required by SEC): Add to your `~/.zshrc`:
   ```bash
   export SEC_EDGAR_USER_AGENT="YourName your.email@example.com"
   ```
   Then: `source ~/.zshrc`

2. **Update `.mcp.json`**: Already configured to use `uvx` (auto-installs):
   ```json
   "sec-edgar": {
     "command": "uvx",
     "args": ["sec-edgar-mcp"],
     "env": {
       "SEC_EDGAR_USER_AGENT": "YourName your.email@example.com"
     }
   }
   ```

3. **Test**: Restart Claude Code, then try looking up a company filing.

### Available Tools

| Tool | Description |
|---|---|
| Company lookup | Search by name or CIK number |
| Filings access | 10-K (annual), 10-Q (quarterly), 8-K (events) |
| XBRL financials | Balance sheet, income statement, cash flow with exact numbers |
| Insider trading | Form 3/4/5 transaction data |

## Troubleshooting

**Yahoo Finance not connecting**:
- Verify path in `.mcp.json` points to cloned repo
- Check `uv` is installed: `which uv`
- Test manually: `uv --directory /path/to/yahoo-finance-mcp run server.py`

**SEC EDGAR not connecting**:
- Check env var is set: `echo $SEC_EDGAR_USER_AGENT`
- Format must be: `"Name email@domain.com"`
- Check `uvx` is available: `which uvx`

**General MCP issues**:
- Restart Claude Code after changing `.mcp.json`
- Validate JSON syntax (no trailing commas)
