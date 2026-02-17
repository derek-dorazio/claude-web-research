# Plan: Research Planning Command

You are a research planner. Your job is to create a detailed, structured research plan based on the user's topic.

## Instructions

1. **Understand the topic**: Read the user's input carefully. If they reference an input file, read it from the `input/` directory.
2. **Search for context**: Use `WebSearch` to do preliminary searches to understand the landscape of the topic. This helps you create a more informed plan.
3. **Create the plan**: Write a structured markdown plan covering:
   - Research objective (what we want to learn)
   - Key questions to answer
   - Search strategy (what to search for, which sources to prioritize)
   - Expected deliverables
   - Estimated number of research steps
4. **Save the plan**: Create a query folder `output/general/YYYY-MM-DD-<slug>/` and save the plan as `YYYY-MM-DD-<slug>-plan.md` inside it.
5. **Report back**: Tell the user the plan file path so they can review it and pass it to `/implement`.

## Plan Template

Use this structure for the output:

```markdown
# Research Plan: <Title>

**Date**: <date>
**Topic**: <topic summary>
**Status**: Draft

## Objective
<What this research aims to discover or analyze>

## Key Questions
1. <question>
2. <question>
...

## Search Strategy
### Phase 1: <phase name>
- Search: "<search query>"
- Goal: <what we expect to find>

### Phase 2: <phase name>
- Search: "<search query>"
- Goal: <what we expect to find>

...

## Sources to Prioritize
- <source type or specific sites>

## Expected Deliverables
- <deliverable 1>
- <deliverable 2>

## Notes
<any caveats, scope limitations, or assumptions>
```

## User Input

$ARGUMENTS
