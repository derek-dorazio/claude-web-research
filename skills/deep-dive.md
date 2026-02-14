# Skill: Deep Dive

Perform a thorough investigation of a single source, topic, or URL to extract maximum value.

## When to Use

Apply this skill when a particular source or subtopic deserves more than a surface-level read — long articles, technical documentation, research papers, or densely packed pages.

## Instructions

1. Fetch and read the full content of the source
2. Extract the key arguments, data points, and conclusions
3. Identify what's novel or noteworthy vs. what's common knowledge
4. Note any claims that should be fact-checked
5. Summarize in structured format

## Output Format

```markdown
## Deep Dive: {{TOPIC}}

**Source**: [Title]({{URL}})
**Date Read**: <date>
**Content Type**: Article / Documentation / Paper / Report / Other

### Key Points
1. <main point>
2. <main point>
3. <main point>

### Notable Data
- <statistic, figure, or specific finding>
- <statistic, figure, or specific finding>

### Quotes Worth Noting
> "<relevant quote>"

### Claims to Verify
- <claim that needs cross-referencing>

### Connections
- Relates to: <other research topics or findings>
- Contradicts: <any conflicting information found elsewhere>

### Assessment
<Brief assessment of this source's value to the overall research>
```

## Placeholder

- `{{URL}}` — The URL to investigate
- `{{TOPIC}}` — The research context
