# Team Charter Template

| Field | Your Entry |
|---|---|
| **Student Name** |Alina Imanakhunova|
| **Date** | 16th of March |
| **Case Context** | Small (Seed-stage)|

---

## Team Purpose & Mission

*Why does this analytics team exist? What value does it create for the organization? Write 2-3 sentences that a non-technical executive would understand.*

**Purpose & Mission:**
The DataPulse analytics team exists because right now nobody in the company fully trusts any number they see. Our job is to fix that — build one reliable source of truth and make sure every important decision, especially the Series A pitch, is backed by data people can actually stand behind. In short: we turn messy, scattered data into clear answers the CEO can take into an investor meeting without hedging.



---

## Scope & Boundaries

*What is this team responsible for? Equally important: what is explicitly NOT your responsibility?*

| In Scope | Out of Scope |
|---|---|
| Define and own core business metrics: DAU, MAU, retention, LTV, CAC | Anything touching the production database infrastructure — that is Sara's territory |
| Set up a data warehouse and build ETL pipelines from PostgreSQL and Firebase | Deploying ML models or doing feature engineering — too early for this stage |
| Design a clean event taxonomy and work with mobile devs to implement it properly | Customer support tooling and CRM systems |
| Deliver the full Series A metrics package: retention cohorts, LTV model, CAC by channel | Running real-time engineering dashboards (uptime, API health) — owned by Engineering |
| Build self-serve dashboards so the product team can answer routine questions themselves | Ad-hoc queries directly against the production database — everything goes through the warehouse |
| Create an A/B testing framework with real statistics, not just "did the number go up?" | Marketing attribution modeling until event tracking is actually clean |
| | |
| | |

> **Tip:** Being explicit about what's OUT of scope is often more valuable than defining what's in scope. It prevents scope creep and sets clear expectations with stakeholders.

---

## Team Principles

*List 3-5 operating principles that guide how your team works. Good principles are specific, actionable, and occasionally uncomfortable. Avoid generic platitudes.*

**Team Principles:**

1. **Trust is built in public.** Every metric has a written definition before it goes into any report or dashboard. If I cannot explain exactly how a number is calculated, I do not share it — not with Jake, not with Mira, definitely not with investors.
 
2. **Fast work and solid work are not opposites.** Every quick-win deliverable should also move the infrastructure forward, even a little. I will not ship a one-off analysis that nobody can reproduce next month.
 
3. **Teach, do not just deliver.** The team has never worked with a data person before. If I just hand people dashboards without explaining them, the trust problem does not get solved — it just moves. I will run short walkthroughs, write plain-language docs, and celebrate when Jake answers his own question without asking me.


---

## Key Interfaces

*Who does your team interact with regularly? For each interface, describe the nature of the relationship and the primary mechanism for interaction.*

| Team / Role | Relationship | Interaction Mechanism | Frequency |
|---|---|---|---|
| **Mira Chen, CEO** | Direct manager and the main reason this role exists — she needs the Series A numbers | Weekly 1:1; shared Notion tracker for investor metrics | Weekly |
| **Jake Oduya, Head of Product** | My most frequent internal customer — he wants to stop making decisions based on gut feel | Weekly sync; Slack channel #data-requests; sprint planning | Weekly |
| **Sara Kim, Backend Engineer** | The person who controls database access — I need her cooperation but cannot add to her workload | Async Slack only; written requests with lead time; max one ask per week | Ad-hoc, low-touch |
| **Luis Herrera & Priya Nair, Mobile Devs** | They have to implement the event taxonomy I design — their buy-in is critical | Bi-weekly review session; shared event spec doc; sprint tickets | Bi-weekly |
| **VC Investors** | External audience for the Series A — they will stress-test every number Mira presents | No direct contact; I package the data room and Mira delivers it | Monthly update via CEO |
| | | | |
| | | | |

---

## Success Metrics

*How will you know if your team is succeeding? Define 3-5 KPIs or OKRs for your team's first year. Mix leading indicators (process metrics) with lagging indicators (outcome metrics).*

> **Example (Acme Analytics):**
> - **Stakeholder NPS > 8** — Quarterly survey of primary stakeholders on analytics team effectiveness
> - **Time-to-insight < 2 days** for standard queries (current baseline: 5 days)
> - **80% of A/B tests** have a pre-registered analysis plan before launch
> - **Zero critical metric errors** in executive reporting (measured by corrections issued)

| # | Metric | Target | Current Baseline | Measurement Method |
|---|---|---|---|---|
| 1 | Core KPIs agreed and trusted by all stakeholders | 100% sign-off on written definitions by Day 60 | Three people ask the same question and get three different answers | Everyone signs off on the Notion metrics glossary |
| 2 | Analytical queries hitting the production database | Zero incidents after warehouse goes live | At least 2 user-facing latency incidents caused by analytical queries | Engineering incident log, confirmed by Sara |
| 3 | Series A metrics package delivered and credible | Done by Day 75; Mira presents with no hedging | "We think retention is around 30–35%" — no confident number exists | Mira's confidence in investor meetings; VC feedback |
| 4 | Event tracking coverage for top 20 user actions | 95% tracked correctly, consistent naming, under 2% data discrepancy | Mixed camelCase and snake_case; onboarding survey not tracked at all | Weekly automated validation script vs. taxonomy doc |
---

## Cadences & Rituals

*What recurring meetings and practices will your team follow? Adapt to your case context — a 3-person startup team needs different cadences than a 15-person enterprise team.*

| Cadence | Ritual | Duration | Purpose | Attendees |
|---|---|---|---|---|
| **Daily** | Async Slack update in #data-pulse | 5 min | Let Mira see progress and blockers without needing a meeting | Just me |
| **Weekly** | 1:1 with Mira | 30 min | Check progress on 90-day plan; unblock Series A metric work | Me + CEO |
| **Weekly** | Sync with Jake | 30 min | Review open requests; share what I found; agree on next priority | Me + Head of Product |
| **Bi-weekly** | Taxonomy review with mobile devs | 45 min | Make sure new features get tracked correctly before they ship, not after | Me + Luis + Priya |
| **Monthly** | All-hands metrics review | 45 min | Show the whole team one honest dashboard; build data literacy slowly | All 12 staff |
| **Quarterly** | Roadmap planning session | 2 hours | Decide what the next quarter's data work should actually be | Me + CEO + Head of Product |

---

## Evaluation Criteria

Use these dimensions to self-assess the quality of your Team Charter. For official grading criteria, see `assessment/grading-rubrics.md` (Manager OS component, 15%).

| Criterion | Weight | What "Good" Looks Like |
|---|---|---|
| **Specificity to case context** | 25% | The charter clearly reflects the constraints and opportunities of your chosen context (Small/Medium/Large). A reader could identify which context you chose without being told. |
| **Actionability of principles** | 20% | Principles are specific enough that a team member could use them to make a daily decision. No generic platitudes. |
| **Completeness of scope** | 20% | Both in-scope and out-of-scope are clearly defined. Key boundaries are drawn. |
| **Quality of success metrics** | 20% | Metrics are specific, measurable, and tied to business outcomes. Mix of leading and lagging indicators. |
| **Clarity of interfaces** | 15% | Key interfaces are identified with interaction mechanisms and frequency. No major stakeholders missing. |

**Note:** This is a draft artifact. You will refine it throughout the course and submit a polished version in your Manager Portfolio. The draft is assessed on completeness and thoughtfulness, not perfection.