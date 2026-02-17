# Skills

Reusable research skill prompts that can be referenced by commands or used standalone. Each skill is a focused technique or methodology that Claude can apply during research.

## Available Skills

### General Research

| Skill | File | Purpose |
|---|---|---|
| Source Evaluation | [evaluate-sources.md](evaluate-sources.md) | Assess credibility and reliability of sources |
| Compare & Contrast | [compare.md](compare.md) | Structured comparison of multiple options/tools/approaches |
| Fact Check | [fact-check.md](fact-check.md) | Verify claims against multiple sources |
| Deep Dive | [deep-dive.md](deep-dive.md) | Thorough single-topic investigation from a URL or source |

### Investment Research

| Skill | File | Purpose |
|---|---|---|
| Financial Statements | [financial-statements.md](financial-statements.md) | Pull and analyze income statement, balance sheet, cash flow |
| Stock Metrics | [stock-metrics.md](stock-metrics.md) | Retrieve valuation and performance metrics for stocks |
| Competitor Analysis | [competitor-analysis.md](competitor-analysis.md) | Compare company against sector peers on financial metrics |
| Valuation | [valuation.md](valuation.md) | Estimate intrinsic value using DCF, comps, or other methods |

## How Skills Work

Skills are reusable prompt templates. They can be:

1. **Referenced by commands** — A command's prompt can instruct Claude to apply a skill during execution
2. **Used directly** — Copy-paste a skill prompt into a conversation for ad-hoc use
3. **Chained together** — Apply multiple skills in sequence (e.g., deep-dive then fact-check)

## Adding a New Skill

1. Create a new `.md` file in this folder
2. Include a clear heading, purpose, instructions, and output format
3. Use `{{TOPIC}}`, `{{URL}}`, or `{{INPUT}}` as placeholders for dynamic content
4. Document the skill in this README
