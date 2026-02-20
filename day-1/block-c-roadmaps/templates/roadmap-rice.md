# 12-Month Analytics Roadmap with RICE Prioritization

**Student Name:** _______________
**Date:** _______________
**Case Context:** [ ] Small (DataPulse) | [ ] Medium (MarketBridge) | [ ] Large (FinGuard)

---

## North Star Metric

**What is your North Star metric?**
_The single number that best captures the value your analytics team delivers to the business._

| Element | Your Answer |
|---------|-------------|
| **Metric name** | |
| **Current baseline** | _(Use a plausible estimate based on your case context)_ |
| **Target (end of 12 months)** | |
| **Why this metric?** | _(How does it connect to the business outcome your executive sponsor cares about most?)_ |
| **How is it measured?** | _(Data source, calculation method, refresh frequency)_ |

**Example (DataPulse):** North Star = Monthly Active Paying Users (MAPU). Current baseline: ~1,600 (50K MAU x 3.2% conversion). 12-month target: 5,000+. This is the metric investors care about most and directly drives revenue.

---

## Guardrail Metrics

_Guardrails are metrics that must NOT get worse while you optimize the North Star. List 3-5._

| # | Guardrail Metric | Current Baseline | Threshold (Must Not Fall Below) | Why It Matters |
|---|-----------------|-----------------|-------------------------------|----------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

**Guidance:** Common guardrails for analytics teams include data quality SLAs (e.g., dashboard uptime > 99%), stakeholder satisfaction scores, query performance benchmarks, model fairness metrics, and data freshness guarantees. Choose guardrails that represent real risks of over-optimizing your North Star.

---

## RICE Scoring Table

_Score each initiative using the RICE framework. Then sort by RICE score to inform your Now/Next/Later placement._

**Scoring Guide:**
- **Reach:** Number of people, decisions, or dollars affected per quarter
- **Impact:** 3 = massive, 2 = high, 1 = medium, 0.5 = low, 0.25 = minimal
- **Confidence:** 100% = high certainty, 80% = reasonable, 50% = speculative
- **Effort:** Person-months of work required
- **RICE Score:** (Reach x Impact x Confidence) / Effort

| # | Initiative | Reach | Impact | Confidence | Effort | RICE Score | Horizon |
|---|-----------|-------|--------|------------|--------|------------|---------|
| 1 | | | | | | | Now / Next / Later |
| 2 | | | | | | | Now / Next / Later |
| 3 | | | | | | | Now / Next / Later |
| 4 | | | | | | | Now / Next / Later |
| 5 | | | | | | | Now / Next / Later |
| 6 | | | | | | | Now / Next / Later |
| 7 | | | | | | | Now / Next / Later |
| 8 | | | | | | | Now / Next / Later |

_Add more rows as needed. You need at least 8 initiatives._

**Note:** The RICE score informs but does not dictate the Horizon. A high-scoring initiative with a critical dependency might be placed in Next rather than Now. A lower-scoring initiative might be in Now because it unblocks higher-value work. Document your reasoning when the placement deviates from the score ranking.

---

## Roadmap Visualization

_Place your initiatives in the appropriate horizon. Include the RICE rank for reference._

### Now (This Quarter — Committed)
_These are actively staffed and in progress. You are accountable for delivering these._

| Initiative | Size (S/M/L/XL) | Key Dependency | Expected Outcome |
|-----------|-----------------|----------------|-----------------|
| | | | |
| | | | |
| | | | |

### Next (Next Quarter — Planned)
_These are scoped and ready to start. They move into Now when the current quarter's work is complete._

| Initiative | Size (S/M/L/XL) | Key Dependency | Expected Outcome |
|-----------|-----------------|----------------|-----------------|
| | | | |
| | | | |
| | | | |

### Later (6-12 Months — Exploratory)
_These are directional. Details are intentionally vague. They represent where the team is heading._

| Initiative | Size (S/M/L/XL) | Key Dependency | Expected Outcome |
|-----------|-----------------|----------------|-----------------|
| | | | |
| | | | |

---

## Dependencies and Sequencing

_What depends on what? Identify the critical path through your roadmap._

### Key Dependencies

| Initiative | Depends On | Type | Risk if Delayed |
|-----------|-----------|------|----------------|
| | | Technical / Data / People / Stakeholder | |
| | | Technical / Data / People / Stakeholder | |
| | | Technical / Data / People / Stakeholder | |

### Sequencing Notes

_Describe the critical path: which initiatives must be completed before others can start? Are there any initiatives that can run in parallel?_

---

## Metrics Tree

_Draw the connection from business outcome to team activities._

```
Business Outcome:  [What the CEO/board cares about]
                        │
North Star:        [Your North Star metric]
                   ╱              ╲
Input Metrics: [Metric A]      [Metric B]
                   │                │
Team Activities: [Activity 1]   [Activity 3]
                 [Activity 2]   [Activity 4]
```

_Replace the placeholders above with your actual metrics tree._

---

## Evaluation Criteria

This artifact will be assessed as part of the Roadmap + Exec Narrative portfolio component (20% of course grade). For the Day 1 Checkpoint (10%, pass/fail), only completeness is assessed — all sections must have content.

**For the final portfolio submission, this roadmap will be evaluated on:**

| Criterion | Excellent | Good | Needs Work |
|-----------|-----------|------|------------|
| **North Star & Guardrails** | Clear metric with baseline and target; guardrails protect against obvious over-optimization risks | Metric identified but baseline or target is vague; guardrails present but not well-justified | Missing baseline/target; guardrails absent or unrelated to North Star |
| **RICE Scoring** | 8+ initiatives scored with plausible estimates; scoring drives meaningful prioritization discussion | 8 initiatives scored but estimates feel arbitrary; limited connection between scores and placement | Fewer than 8 initiatives or RICE applied mechanically without judgment |
| **Now/Next/Later Placement** | Placement is defensible; deviations from RICE ranking are explained; realistic given team size | Placement follows RICE scores but lacks nuance about dependencies or team capacity | Placement feels random or disconnected from scores |
| **Dependencies** | Critical path is clear; external dependencies identified; realistic about what blocks what | Some dependencies noted but not systematically mapped | Dependencies not addressed |
| **Business Alignment** | Every initiative connects clearly to business outcomes; a VP could read this and understand why | Most initiatives have business rationale; some feel like internal projects | Roadmap reads like a technical task list, not a business strategy |
