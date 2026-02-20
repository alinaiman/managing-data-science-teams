# Data Infrastructure Blueprint — 6-Month Plan

| Field | Value |
|---|---|
| **Student Name** | |
| **Date** | |
| **Case Context** | Small (0-1) / Medium (1-N) / Large (N-Scale) |

---

## Current State Assessment

Describe the data infrastructure that exists today in your case context. Be specific about tools, gaps, and pain points.

**Existing Tools & Systems:**

| Layer | Current Tool/System | Status | Key Pain Point |
|---|---|---|---|
| Sources | | | |
| Ingestion | | | |
| Storage | | | |
| Transformation | | | |
| Semantic Layer | | | |
| Visualization | | | |
| Governance | | | |
| Observability | | | |

**Top 3 Pain Points (ranked):**

1. _
2. _
3. _

**Data Trust Level:** (How much do stakeholders trust the numbers today? High / Medium / Low / None)

---

## Target Architecture

Describe the data stack you are building toward over the next 6 months. Map each layer to the canonical blueprint: Sources -> Ingestion -> Storage -> Transform -> Semantic Layer -> Visualization, with Governance and Observability as cross-cutting concerns.

**Target Stack Diagram (describe or sketch):**

```
[Sources] --> [Ingestion] --> [Storage] --> [Transform] --> [Semantic Layer] --> [Visualization]
                                    |                              |
                              [Governance] <-- cross-cutting --> [Observability]
```

**For each layer, describe:**
- What tool or approach you'll use
- Why you chose it over alternatives
- What it replaces or adds vs. current state

---

## 6-Month Implementation Plan

Break the 6 months into three phases. For each phase, list what gets built or bought, who is responsible, and what the dependencies are.

### Phase 1: Month 1-2 (Foundation)

| Action Item | Owner | Dependency | Done When |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

**Phase 1 goal:** _

### Phase 2: Month 3-4 (Build-Out)

| Action Item | Owner | Dependency | Done When |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

**Phase 2 goal:** _

### Phase 3: Month 5-6 (Maturity & Governance)

| Action Item | Owner | Dependency | Done When |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

**Phase 3 goal:** _

---

## Tool Selection Summary

For each tool you are selecting, document what you chose, what you considered, and why.

| Category | Selected Tool | Alternative Considered | Rationale for Selection |
|---|---|---|---|
| Ingestion | | | |
| Storage / Warehouse | | | |
| Transformation | | | |
| Semantic Layer | | | |
| Visualization / BI | | | |
| Governance | | | |
| Observability | | | |
| Other: _________ | | | |

**Build vs. Buy Decisions:**

| Component | Build or Buy? | Reasoning (reference the 4-question framework) |
|---|---|---|
| | | |
| | | |

---

## Budget Estimate

Estimate costs for your target stack. Use real vendor pricing where possible; order-of-magnitude estimates are acceptable.

| Tool / Service | Monthly Cost | Annual Cost | One-Time Implementation Cost |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| **Total** | | | |

**Cost context:** How does this compare to the team's total budget? What percentage of headcount cost does infrastructure represent?

**Cost optimization opportunities:** Where could you save money if budget is cut by 30%?

---

## Risks & Dependencies

| Risk | Likelihood (H/M/L) | Impact (H/M/L) | Mitigation Strategy |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

**Key Dependencies:**
- Engineering team: _
- IT / Procurement: _
- Legal / Privacy: _
- Budget approval: _

---

## Governance Plan

How will you ensure data quality, access control, and compliance in the target architecture?

**Data Ownership:**

| Data Domain | Owner (Role) | Responsibilities |
|---|---|---|
| | | |
| | | |

**Access Controls:**
- Who can read production data?
- Who can write to production tables?
- How are permissions managed? (Role-based, individual, etc.)

**Quality Standards:**
- How will you test data quality? (dbt tests, Great Expectations, manual checks)
- What SLAs exist for data freshness?
- How are data incidents handled?

**Compliance:**
- Data classification applied? (Public / Internal / Confidential / Restricted)
- Retention policies defined?
- GDPR / privacy requirements addressed?

---

## Evaluation Criteria

This deliverable will be assessed on:

| Criterion | Weight | What "good" looks like |
|---|---|---|
| **Completeness** | 20% | All sections filled with specific, concrete content — no placeholders left blank |
| **Case Context Fit** | 25% | The plan is appropriately scoped for your case context (small orgs don't propose enterprise tooling; large orgs address governance and procurement) |
| **Technical Soundness** | 20% | Tool selections make sense together as a stack; no obvious integration gaps or contradictions |
| **Build-vs-Buy Reasoning** | 15% | Decisions reference the 4-question framework; trade-offs are explicit, not assumed |
| **Budget Realism** | 10% | Cost estimates are in the right order of magnitude; hidden costs (implementation, training, maintenance) are acknowledged |
| **Risk Awareness** | 10% | Key risks are identified with concrete mitigation strategies, not generic statements |
