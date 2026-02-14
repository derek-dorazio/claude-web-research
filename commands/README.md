# Commands

Slash commands for Claude Code. The executable command files live in `.claude/commands/` (required by Claude Code), and are documented here for easy reference.

## Available Commands

| Command | File | Description |
|---|---|---|
| `/plan` | [plan.md](../\.claude/commands/plan.md) | Create a structured research plan |
| `/implement` | [implement.md](../\.claude/commands/implement.md) | Execute a research plan into a full report |
| `/research` | [research.md](../\.claude/commands/research.md) | Quick one-shot web research |
| `/summarize` | [summarize.md](../\.claude/commands/summarize.md) | Condense any output into a 1-page summary |

## How Commands Work

Commands are markdown prompt files stored in `.claude/commands/`. When you type `/plan <topic>` in Claude Code, the contents of `plan.md` are loaded as instructions and `$ARGUMENTS` is replaced with whatever you typed after `/plan`.

## Adding a New Command

1. Create a new `.md` file in `.claude/commands/`
2. Include `$ARGUMENTS` where you want the user's input inserted
3. Define the output path (should go into `output/<command-name>/`)
4. Add a new output subdirectory if needed: `mkdir output/<command-name>`
5. Document the command in this README

## Command Workflow

```
/plan <topic>          -->  output/plan/<date>-<slug>.md
       |
       v (review & edit)
/implement <plan-path> -->  output/implement/<date>-<slug>-report.md
       |
       v (optional)
/summarize <file-path> -->  <original>-summary.md
```
