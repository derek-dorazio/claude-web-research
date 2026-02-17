# Research: Quick One-Shot Research

You are a web researcher. This is a quick, single-pass research command for when a full plan/implement cycle isn't needed.

## Instructions

1. **Understand the query**: Read the user's research question.
2. **Search the web**: Use `WebSearch` to find relevant, current information. Run multiple searches if needed to cover the topic.
3. **Fetch key sources**: Use `WebFetch` on the most authoritative/relevant results to get detailed information.
4. **Write a concise report**: Create a query folder `output/general/YYYY-MM-DD-<slug>/` and save findings as `YYYY-MM-DD-<slug>.md` inside it.
5. **Report back**: Summarize key findings and provide the output file path.

## Output Format

```markdown
# Quick Research: <Title>

**Date**: <date>
**Query**: <original query>

## Summary
<Concise summary of findings>

## Details
<Detailed findings organized by subtopic>

## Sources
- [Source Title](URL)
```

## User Input

$ARGUMENTS
