# Decision Memo Template

| Field | Your Entry |
|---|---|
| **Student Name** | |
| **Date** | |
| **Case Context** | Small (Seed-stage) / Medium (Series B) / Large (Enterprise) |
| **Decision Title** | *(1-line summary, e.g., "Adopt dbt as our transformation layer")* |
| **Decision Owner (A)** | *(Who is accountable for this decision?)* |
| **Status** | Draft / Under Review / Decided / Revisiting |

---

## Context

*What situation prompted this decision? What is the business context? Why now? Keep this to 3-5 sentences. A reader who knows nothing about the situation should understand the problem after reading this section.*

> **Example:** Our Series B marketplace currently has no standardized event taxonomy. Product managers define events ad-hoc, leading to inconsistent naming, duplicate events, and unreliable funnel metrics. The Growth team recently discovered that two versions of "purchase_completed" exist with different definitions, which caused a 15% discrepancy in reported conversion rates last quarter. We need to decide whether to build a custom event taxonomy or adopt an existing standard before we scale experimentation in Q2.

**Your context:**




---

## Options Considered

*List at least 3 options. For each, provide a brief description, key pros, key cons, estimated effort, and any dependencies. Be honest about trade-offs — no option is perfect.*

### Option A: _______________

| Dimension | Assessment |
|---|---|
| **Description** | *(2-3 sentences)* |
| **Pros** | *(Bullet list)* |
| **Cons** | *(Bullet list)* |
| **Estimated Effort** | *(T-shirt size: S/M/L/XL + rough timeline)* |
| **Dependencies** | *(What/who does this require?)* |

### Option B: _______________

| Dimension | Assessment |
|---|---|
| **Description** | |
| **Pros** | |
| **Cons** | |
| **Estimated Effort** | |
| **Dependencies** | |

### Option C: _______________

| Dimension | Assessment |
|---|---|
| **Description** | |
| **Pros** | |
| **Cons** | |
| **Estimated Effort** | |
| **Dependencies** | |

> **Example options for the event taxonomy decision:**
>
> **Option A: Build a custom event taxonomy from scratch.**
> Pros: Perfectly tailored to our domain; team learns the data deeply.
> Cons: 6-8 weeks of analyst time; no external validation; maintenance burden.
> Effort: L (8 weeks). Dependencies: Buy-in from all PMs; engineering to enforce schema.
>
> **Option B: Adopt an existing standard (e.g., Segment's tracking plan spec or GA4 schema).**
> Pros: Industry-tested; faster to implement (2-3 weeks); tooling support.
> Cons: May not fit our marketplace model perfectly; vendor lock-in risk.
> Effort: M (3 weeks). Dependencies: Vendor evaluation; engineering integration.
>
> **Option C: Hybrid — adopt a standard as the base, extend with custom events for marketplace-specific concepts.**
> Pros: Fast start with industry standard; flexibility for our domain.
> Cons: Complexity of maintaining extensions; risk of "worst of both worlds" if not disciplined.
> Effort: M (4 weeks). Dependencies: Same as Option B + internal governance for extensions.

---

## Recommendation

*Which option do you recommend and why? Be specific about the reasoning. Reference the pros/cons above. Address the strongest argument against your recommendation.*

> **Example:** I recommend **Option C (Hybrid)**. It gives us 80% of the benefit of an industry standard with the flexibility to handle marketplace-specific events like "listing_created" and "offer_accepted" that no standard covers. The strongest argument against this is complexity — maintaining extensions requires discipline. I'd mitigate this by designating an "event taxonomy owner" on the analytics team who reviews all new custom events and maintains documentation. Timeline: 4 weeks to initial rollout, with a 2-week stabilization period.

**Your recommendation:**




---

## Risks & Mitigations

*What could go wrong with your recommended option? For each risk, describe the impact and your mitigation plan.*

| Risk | Likelihood (H/M/L) | Impact (H/M/L) | Mitigation |
|---|---|---|---|
| *(e.g., PMs resist adopting the new taxonomy)* | *(M)* | *(H)* | *(Involve PM leads in the design process; phase rollout by team)* |
| *(e.g., Engineering bandwidth for schema enforcement)* | *(H)* | *(M)* | *(Start with documentation + linting; defer automated enforcement to Q3)* |
| | | | |
| | | | |
| | | | |

---

## Decision Type

*Classify this decision and explain the implications for how you approach it.*

**This is a Type ___ decision.**

- **Type 1 (Irreversible / One-way door):** High-stakes, hard to undo. Requires thorough analysis, broad input, and senior approval. Examples: major vendor commitments, organizational restructuring, public-facing metric definitions.

- **Type 2 (Reversible / Two-way door):** Lower-stakes, can be undone. Default to speed, empower the team to decide, iterate. Examples: internal tool choices, process experiments, dashboard designs.

**Implications:**
- If Type 1: Who needs to approve? What additional analysis is needed? What's the decision deadline?
- If Type 2: Who is empowered to decide? When will you revisit? What would make you reverse course?

> **Example:** This is a **Type 2 decision**. While changing our event taxonomy later would be painful, it's not irreversible — we can migrate events incrementally. The cost of waiting (continued data inconsistency) is higher than the cost of choosing and iterating. I recommend the analytics manager decide with PM consultation, and we revisit in 90 days to assess adoption and identify gaps.

**Your classification and implications:**




---

## Approval & Record

| Action | Person | Date | Notes |
|---|---|---|---|
| **Drafted by** | | | |
| **Consulted** | | | |
| **Decided by** | | | |
| **Communicated to** | | | |
| **Review date** | | | *(When will this decision be revisited?)* |

---

## Evaluation Criteria

Use these dimensions to self-assess the quality of your Decision Memo:

| Criterion | Weight | What "Good" Looks Like |
|---|---|---|
| **Context clarity** | 20% | A reader unfamiliar with the situation understands the problem, its urgency, and its business impact in under 60 seconds. |
| **Option quality** | 25% | At least 3 genuine options (not straw men). Pros and cons are honest and specific. Effort estimates are realistic for the case context. |
| **Recommendation strength** | 25% | The recommendation is clear, justified by the analysis, and addresses the strongest counterargument. The reader understands not just WHAT you recommend, but WHY. |
| **Risk awareness** | 15% | Risks are realistic (not paranoid, not dismissive). Mitigations are actionable and proportionate. |
| **Decision type classification** | 15% | Correct Type 1/Type 2 classification with thoughtful implications. Demonstrates understanding of when to move fast vs. when to slow down. |

**Note:** Decision memos are optional practice exercises — they are not graded as a standalone portfolio component. However, well-crafted decision memos can strengthen other artifacts (e.g., a build-vs-buy memo supporting your roadmap). See the optional Data Infrastructure resources for advanced topics.
