# 12-Month Analytics Roadmap with RICE Prioritization

**Student Name:** Alina Imanakhunova
**Date:** 16th of March
**Case Context:** Small (DataPulse) 

---

## North Star Metric

**What is your North Star metric?**
_The single number that best captures the value your analytics team delivers to the business._

| Element | Your Answer |
|---------|-------------|
| **Metric name** |Monthly Active Paying Users (MAPU)|
| **Current baseline** | ~1,600 (50,000 MAU × 3.2% conversion rate) |
| **Target (end of 12 months)** | 5,000+ MAPU|
| **Why this metric?** | This is the number that investors will need most during the Series A. It connects product engagement  directly to revenue. If MAPU grows, it means we are both acquiring users AND convincing them the product is worth paying for. It is also the metric the CEO loses sleep over. |
| **How is it measured?** | Source: PostgreSQL subscription records joined to user activity table. Calculation: count of distinct users with an active paid subscription who also triggered at least one workout event in the calendar month. Refreshed daily via warehouse ETL; reported weekly to CEO.  |

---

## Guardrail Metrics

_Guardrails are metrics that must NOT get worse while you optimize the North Star. List 3-5._

| # | Guardrail Metric | Current Baseline | Threshold (Must Not Fall Below) | Why It Matters |
|---|-----------------|-----------------|-------------------------------|----------------|
| 1 | D30 Free User Retention Rate | Unknown (currently untrusted) — estimated ~30–35% based on CEO's hedged figures | 28% | If we over-optimize conversion (e.g., aggressive paywalls) and tank free retention, the top of the funnel dries up. Free users are the pipeline for paid users. |
| 2 | Dashboard Data Freshness | N/A — no warehouse exists yet | ETL lag must stay under 24 hours once warehouse is live | Stale data destroys stakeholder trust. If Jake opens a dashboard and the numbers are 3 days old, he stops using it. |
| 3 | Production Database Incident Count | 2+ latency incidents caused by analytical queries (historical) | 0 incidents per quarter post-warehouse launch | Every production incident caused by analytics erodes Sara's trust and risks a user-facing outage. One bad incident could get analytics access revoked entirely. |

**Guidance:** Common guardrails for analytics teams include data quality SLAs (e.g., dashboard uptime > 99%), stakeholder satisfaction scores, query performance benchmarks, model fairness metrics, and data freshness guarantees. Choose guardrails that represent real risks of over-optimizing your North Star.

---

## RICE Scoring Table

_Score each initiative using the RICE framework. Then sort by RICE score to inform your Now/Next/Later placement._

**Scoring Guide:**
- **Reach:** Number of people, decisions, or dollars affected per quarter
- **Impact:** 3 = massive, 2 = high, 1 = medium, 0.5 = low, 0.25 = minimal
- **Confidence:** 100% = high certainty, 80% = reasonable, 50% = speculative
- **Effort:** Person-months of work required (include compute costs where significant)
- **RICE Score:** (Reach x Impact x Confidence) / Effort

| # | Initiative | Reach | Impact | Confidence | Effort | RICE Score | Horizon |
|---|-----------|-------|--------|------------|--------|------------|---------|
| 1 | Set up data warehouse + PostgreSQL ETL pipeline | 5 (all stakeholders unblocked by this) | 3 | 80% | 1.5 | **8.0** | Now |
| 2 | Deliver Series A investor metrics package (retention cohorts, LTV, CAC) | 5 (CEO + investors) | 3 | 80% | 1.0 | **12.0** | Now |
| 3 | Define canonical event taxonomy v1 + get mobile dev buy-in | 4 (Product, CEO, future experiments) | 2 | 80% | 0.5 | **12.8** | Now |
| 4 | Publish metrics glossary in Notion (MAU, DAU, retention, LTV, CAC) | 5 (whole company) | 2 | 100% | 0.25 | **40.0** | Now |
| 5 | Firebase events ETL into warehouse + reconcile with Amplitude | 4 (fixes mobile funnel visibility) | 2 | 50% | 1.5 | **2.7** | Next |
| 6 | Design + launch first properly instrumented A/B test framework | 3 (Product team experiments) | 2 | 80% | 1.0 | **4.8** | Next |
| 7 | Automated data quality alerting (detect broken events, schema changes, pipeline failures) | All analytics consumers | 2 | 80% | 0.7 | **457** | Next |
| 8 | Subscription conversion driver analysis (which behaviors predict free→paid upgrade?) | 1,600 paying users + all future converters | 3 | 50% | 1.0 | **450** | Next |
| 9 | Predictive churn model (ML — flag users at risk before they cancel) | 4 (retention, revenue) | 3 | 50% | 2.0 | **3.0** | Later |


**Note:** Initiative #1 (warehouse + ETL) scores lower than #2 and #3 because it has higher effort, but it is placed in **Now** anyway because it is a hard dependency for almost everything else on this list. Without the warehouse, there is no reliable source of truth, no self-serve dashboard, and no safe path away from production DB queries. It is the critical path item that unblocks the entire roadmap. Similarly, #5 (event taxonomy implementation) scores lower than some Next items but cannot be delayed — every future experiment and funnel analysis depends on clean event data.

---

## Roadmap Visualization

_Place your initiatives in the appropriate horizon. Include the RICE rank for reference._

### Now (This Quarter — Committed)
_These are actively staffed and in progress. You are accountable for delivering these._

| Initiative | Size (S/M/L/XL) | Key Dependency | Expected Outcome |
|-----------|-----------------|----------------|-----------------|
| Data warehouse + PostgreSQL ETL pipeline | L | Sara Kim's approval for DB access; read replica or connection string | Zero analytical queries hitting production DB; all future work runs on clean warehouse data |
| Series A investor metrics package | M | Warehouse live; at minimum a direct PostgreSQL connection | CEO walks into investor meetings with confident, documented retention/LTV/CAC numbers — no hedging |
| Canonical event taxonomy v1 + mobile dev implementation | M | Luis and Priya sprint capacity; taxonomy doc reviewed and approved | Consistent event naming across iOS and Android; critical actions (onboarding survey, workout completion) tracked reliably |
| Metrics glossary (shared definitions) | S | CEO + Head of Product 60-min alignment session | One agreed definition of MAU, DAU, D1/D7/D30 retention, LTV, CAC across the whole company |

### Next (Next Quarter — Planned)
_These are scoped and ready to start. They move into Now when the current quarter's work is complete._

| Initiative | Size (S/M/L/XL) | Key Dependency | Expected Outcome |
|-----------|-----------------|----------------|-----------------|
| Firebase ETL + Amplitude reconciliation | M | Warehouse live; event taxonomy v1 implemented | Single pipeline for all event data; the Amplitude vs. PostgreSQL discrepancy is finally resolved |
| A/B test framework (design + templates) | M | Metrics glossary; warehouse; Head of Product buy-in | First properly instrumented experiment launched with pre-registration, sample size calc, and clean analysis |
| Automated data quality alerting | S | Warehouse + ETL pipelines running | Team is notified within 1 hour of broken events or pipeline failures; no more silent bad data |
| Subscription conversion driver analysis | M | At least 3 months of clean warehouse data | Data-backed answer to "what do free users do in the app before they upgrade?" — informs product and marketing |

### Later (6-12 Months — Exploratory)
_These are directional. Details are intentionally vague. They represent where the team is heading._

| Initiative | Size (S/M/L/XL) | Key Dependency | Expected Outcome |
|-----------|-----------------|----------------|-----------------|
| Predictive churn model | XL | 6+ months of clean subscriber behavior data; Python environment | Proactive retention campaigns targeting at-risk subscribers before they cancel |

---

## Dependencies and Sequencing

_What depends on what? Identify the critical path through your roadmap._

### Key Dependencies

| Initiative | Depends On | Type | Risk if Delayed |
|-----------|-----------|------|----------------|
| Series A investor metrics package | Data warehouse OR direct PostgreSQL read access | Technical | CEO continues hedging retention numbers in investor meetings; Series A delayed or undervalued |
| Firebase ETL + Amplitude reconciliation | Event taxonomy v1 implemented in app | Data | Fixing the pipeline on top of inconsistent events solves nothing; Amplitude discrepancy persists |
| A/B test framework | Metrics glossary signed off; warehouse live | Stakeholder + Technical | Experiments lack agreed success metrics; results are contested just like current "tests" |
| Predictive churn model | 6+ months of clean warehouse data | Data | Model trained on incomplete or dirty data is unreliable; could trigger harmful retention interventions |

### Sequencing Notes

_Describe the critical path: which initiatives must be completed before others can start? Are there any initiatives that can run in parallel?_

If Sara Kim cannot prioritize database access setup in Month 1 (due to her existing workload), the entire roadmap shifts right. This is the single most important dependency to resolve in Week 1.
---

## Metrics Tree

_Draw the connection from business outcome to team activities._

```
Business Outcome:  Raise Series A at strong valuation
                              │
North Star:        Monthly Active Paying Users (MAPU)
                   ~1,600 today → 5,000+ in 12 months
                   ╱                          ╲
Input Metric A:                        Input Metric B:
Monthly Active Users (MAU)             Free → Paid Conversion Rate
~50,000 today                          3.2% today
          │                                      │
          ├── D1 Retention                        ├── Onboarding completion rate
          ├── D7 Retention                        ├── Workouts completed in first 7 days
                   │                                        │
Team Activities:                        Team Activities:
- Build retention cohort dashboards     - Onboarding funnel drop-off analysis
- Fix event taxonomy for session        - Conversion driver analysis
  tracking                              - A/B test framework for onboarding
- Automated churn alerting              
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
