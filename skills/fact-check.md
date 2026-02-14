# Skill: Fact Check

Verify specific claims or data points against multiple independent sources.

## When to Use

Apply this skill when research surfaces claims that seem surprising, when sources conflict, or when accuracy is critical (statistics, dates, technical specifications).

## Instructions

1. Isolate the specific claim to verify
2. Search for the claim using multiple different queries
3. Look for primary sources (original study, official announcement, documentation)
4. Cross-reference across at least 2-3 independent sources
5. Rate the claim's reliability

## Output Format

```markdown
## Fact Check: {{TOPIC}}

### Claim
> "<exact claim being checked>"
> — Source: [Title](URL)

### Verification

| Source | Supports? | Detail |
|---|---|---|
| [Source 1](URL) | Yes / No / Partial | <what this source says> |
| [Source 2](URL) | Yes / No / Partial | <what this source says> |
| [Source 3](URL) | Yes / No / Partial | <what this source says> |

### Verdict
- **Rating**: Confirmed / Mostly True / Mixed / Unverified / Disputed / False
- **Confidence**: High / Medium / Low
- **Notes**: <context, nuance, or caveats>
```

## Placeholder

- `{{TOPIC}}` — The claim or data point to verify
