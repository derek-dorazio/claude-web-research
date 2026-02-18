# Commands

Slash commands for Claude Code. The executable command files live in `.claude/commands/` (required by Claude Code), and are documented here for easy reference.

## Available Commands

### Research
| Command | File | Description |
|---|---|---|
| `/plan` | [plan.md](../.claude/commands/plan.md) | Create a structured research plan |
| `/implement` | [implement.md](../.claude/commands/implement.md) | Execute a research plan into a full report |
| `/research` | [research.md](../.claude/commands/research.md) | Quick one-shot web research |
| `/summarize` | [summarize.md](../.claude/commands/summarize.md) | Condense any output into a 1-page summary |
| `/analyze-stock` | [analyze-stock.md](../.claude/commands/analyze-stock.md) | Comprehensive investment research on a public company |

### Export
| Command | File | Description |
|---|---|---|
| `/slides` | [slides.md](../.claude/commands/slides.md) | Create a PowerPoint deck from research or a topic |
| `/excel` | [excel.md](../.claude/commands/excel.md) | Create or read Excel workbooks |
| `/pdf-report` | [pdf-report.md](../.claude/commands/pdf-report.md) | Convert markdown report to PDF |
| `/pdf-slides` | [pdf-slides.md](../.claude/commands/pdf-slides.md) | Convert PowerPoint to PDF |
| `/export` | [export.md](../.claude/commands/export.md) | Convert report to multiple formats at once |

## How Commands Work

Commands are markdown prompt files stored in `.claude/commands/`. When you type `/plan <topic>` in Claude Code, the contents of `plan.md` are loaded as instructions and `$ARGUMENTS` is replaced with whatever you typed after `/plan`.

## Adding a New Command

1. Create a new `.md` file in `.claude/commands/`
2. Include `$ARGUMENTS` where you want the user's input inserted
3. Define the output path (save into the appropriate query folder under `output/<type>/`)
4. Follow the convention: all artifacts for one query go in `output/<type>/YYYY-MM-DD-<slug>/`
5. Document the command in this README

## Command Workflow

```
/plan <topic>          -->  output/general/<date>-<slug>/<date>-<slug>-plan.md
       |
       v (review & edit)
/implement <plan-path> -->  output/general/<date>-<slug>/<date>-<slug>.md
       |
       v (optional)
/summarize <file-path> -->  <same-folder>/<original>-summary.md
       |
       v (optional)
/slides <file-path>   -->  <same-folder>/<date>-<slug>.pptx
/excel <file-or-desc> -->  <same-folder>/<date>-<slug>.xlsx
/export <file> all    -->  <same-folder>/<date>-<slug>.zip (if 2+ files)
```
