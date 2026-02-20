# Data Infrastructure Reference Guide

This reference guide consolidates the data infrastructure, vendor management, and cross-functional collaboration content from the ECBS5256 course. It is provided as a self-study resource for students who want to deepen their understanding of analytics infrastructure decisions.

---

## The Canonical Data Stack

Every modern data stack follows this pattern:

**Sources** → **Ingestion** → **Storage** → **Transform** → **Semantic Layer** → **Visualization**

With cross-cutting concerns at every layer:

- **Governance:** Who owns what? Who can access what?
- **Observability:** Is it working? How do you know?
- **Cost management:** What does each layer cost?

### Reading an Architecture Diagram

| Layer | What it does (plain English) | Key question |
|---|---|---|
| **Sources** | Where data originates (app, APIs, files) | "Capturing everything we need?" |
| **Ingestion** | Moves data from sources to storage | "How fresh? Minutes, hours, days?" |
| **Storage** | The central repository (warehouse) | "Cost? Can it scale?" |
| **Transform** | Cleans raw data into usable tables | "How do we verify correctness?" |
| **Semantic Layer** | Defines metrics so everyone agrees | "One definition of 'revenue'?" |
| **Visualization** | Dashboards end users see | "Can stakeholders self-serve?" |

**At every layer, ask three questions:**
1. "How do we know it's working?" — observability
2. "What happens when it breaks?" — resilience
3. "What does it cost?" — cost management

---

## Stack Blueprints by Organization Size

### Small Org Stack (0 to 1)

**Goal:** Trusted numbers, fast. Don't over-engineer.

| Layer | Tool | Why |
|---|---|---|
| **Sources** | Product DB + basic events | Start with what you have |
| **Ingestion** | Fivetran or Airbyte | Managed connectors; don't build this |
| **Storage** | BigQuery or Snowflake (free tier) | Start small, scale later |
| **Transform** | dbt (Core or Cloud) | SQL-based; version-controlled; testable |
| **Viz** | Metabase or Preset | Open-source options exist; low cost |
| **Governance** | Naming conventions + a spreadsheet | Seriously. This is enough to start. |

**Monthly cost:** $500–2,000

**What to skip:** Data catalog, ML platform, feature store, semantic layer tooling. You're not there yet. Resist the urge to build for scale you don't have.

### Medium Org Stack (1 to N)

**Goal:** Self-serve metrics, experimentation, data trust at scale.

Add to the small stack:

| Layer | Addition | Why now |
|---|---|---|
| **Event platform** | Segment or RudderStack | Structured event collection; identity resolution |
| **Experimentation** | Statsig or Eppo | Rigorous A/B testing, not spreadsheet math |
| **Semantic layer** | dbt metrics or Cube | Single source of truth for metric definitions |
| **Catalog** | DataHub or Atlan | Discovery; lineage; tribal knowledge captured |
| **Observability** | Monte Carlo or Elementary | Know when data breaks before your stakeholders do |

**Governance:** Formal data owners. Published SLAs. Access controls.

**Monthly cost:** $10,000–30,000

### Large Org Stack (N to Scale)

**Goal:** Domain autonomy, ML at scale, regulatory compliance.

Add to the medium stack:

| Layer | Addition | Why now |
|---|---|---|
| **Architecture** | Data mesh / domain ownership | Decentralized ownership, centralized standards |
| **ML platform** | MLflow, SageMaker, or Vertex | Model training, versioning, deployment |
| **Feature store** | Feast or Tecton | Shared features across models |
| **Model governance** | Model cards, bias audits, monitoring | Regulatory and ethical requirements |
| **Cost management** | Kubecost, cloud billing dashboards | Because $100K+/mo demands accountability |
| **Data marketplace** | Internal data products catalog | Treat data as a product, not a byproduct |

**Governance:** Access controls, lineage, regulatory compliance, audit trails, data classification. At this scale, governance is a **team**, not a task.

**Monthly cost:** $100,000+

---

## Build vs. Buy Framework

**Four questions in order:**

1. **Is this a core differentiator?** If yes: build.
   - Your recommendation algorithm? Build. Your data warehouse? Buy.

2. **Is this commodity infrastructure?** If yes: buy.
   - Ingestion, storage, BI tooling — these are solved problems.

3. **Do you have the team to maintain it?** If no: buy.
   - "Free" open source costs your engineers' time. Forever.

4. **What's the Total Cost of Ownership?**
   - License + implementation + training + maintenance + **opportunity cost**
   - The biggest hidden cost: what your team *doesn't* build while maintaining infra.

**Default to buy** for infrastructure. Default to build for business logic.

### The Hidden Costs of "Free"

**Airflow (open-source) vs. managed alternatives:**

| Cost component | Self-hosted Airflow | Managed (e.g., Astronomer) |
|---|---|---|
| License | $0 | ~$300–1,200/mo |
| Engineer setup | 40–80 hours | 4–8 hours |
| Monthly maintenance | 8–16 hours/mo | ~0 hours/mo |
| Upgrades (annual) | 20–40 hours | Included |
| Debugging & incidents | 5–10 hours/mo | Vendor handles |

| | Self-hosted | Managed |
|---|---|---|
| **Annual engineer cost** | ~$30K–50K in loaded salary | ~$4K–14K in subscription |

**When "free" actually costs more than "paid":** almost always, unless you have a dedicated platform team.

---

## The RFP Process

**When to RFP:** Spending >$10K/year or handling PII.

**Steps:**

1. **Define requirements** — Must-have vs. Should-have vs. Nice-to-have
2. **Weight criteria** — Not all requirements are equal
3. **Score vendors** — Structured, not vibes-based
4. **Negotiate** — Always negotiate. Always.
5. **Pilot** — 2-4 week proof of concept before committing

### Scoring Dimensions

| Criterion | What to evaluate |
|---|---|
| **Functionality** | Does it solve the core problem? |
| **Integration** | Works with our existing stack? |
| **Security** | SOC 2, encryption, access controls |
| **Cost** | Total cost of ownership over 3 years |
| **Support** | Response times, dedicated CSM, community |
| **Scalability** | Will it grow with us? |

**Pro tip:** Score as a team. Each evaluator scores independently, then discuss disagreements — the discussion reveals hidden assumptions.

---

## Working with IT & Procurement

**Speak their language:**
- Security posture, SOC 2 Type II, penetration testing
- Data residency (EU data stays in EU — GDPR requirement)
- SSO / SAML integration (no separate passwords)
- Audit logs (who accessed what, when)
- Vendor risk assessment questionnaire

**Procurement timeline reality (3–6 months):**

| Month | Step | Who's involved |
|---|---|---|
| **Month 1** | Identify need, get IT alignment, vendor research | Analytics + IT |
| **Month 1–2** | Vendor demos, shortlist to 2–3 options | Analytics + IT + stakeholders |
| **Month 2–3** | Pilot / proof of concept with real data | Analytics + Engineering |
| **Month 3** | Security questionnaire + vendor risk assessment | IT Security |
| **Month 3–4** | Legal review of contract + data processing agreement | Legal |
| **Month 4** | Budget approval (align to budget cycle!) | Finance |
| **Month 4–5** | SSO integration + access provisioning | IT |
| **Month 5–6** | Full deployment + team training | Analytics |

**The golden rule:** Involve IT early. Not as a blocker — as a partner.

---

## Privacy & Governance Basics

### GDPR Essentials for Analytics Managers

| Concept | What it means for you |
|---|---|
| **Lawful basis** | You need a legal reason to process personal data (consent, legitimate interest, etc.) |
| **Data minimization** | Collect only what you need. "We might need it someday" is not a reason. |
| **Right to erasure** | Users can ask you to delete their data. Your pipeline must support this. |
| **Consent management** | Track what users consented to. Don't use data beyond that scope. |

### Data Classification

- **Public** — Can share openly (blog metrics, public benchmarks)
- **Internal** — Company-wide access (aggregate dashboards)
- **Confidential** — Need-to-know (user-level data, financial details)
- **Restricted** — Highest sensitivity (PII, health data, payment data)

### Retention

Don't keep what you don't need. Set policies. Enforce them. Every table in your warehouse should have a retention policy. "Keep forever" is not a policy — it's a liability.

---

## Cross-Functional Interfaces

Analytics managers spend **30–40% of their time** on cross-functional work. Key interfaces:

| Interface | What they care about | What you need from them |
|---|---|---|
| **Product** | Metrics definitions, experiment results | Clear, prioritized business questions |
| **Engineering** | Data contracts, SLAs for pipeline load | Reliable instrumentation, advance notice of schema changes |
| **Legal / Privacy** | Data inventories, consent tracking | Timely privacy reviews, clear data usage guidance |
| **Finance** | Cost attribution, ROI analysis | Reasonable budget cycles, approval velocity |
| **IT** | Security compliance, vendor paperwork | Procurement timelines, cloud access, SSO provisioning |
| **Design** | User behavior data, funnel analysis | UX research collaboration |

### Bidirectional SLA Template

> **Analytics will** provide [deliverable X] within [Y timeframe].
> **[Partner team] will** provide [deliverable Z] within [W timeframe].
> **Escalation path:** [name/role] if SLA is missed.
> **Review cadence:** Monthly sync to assess and adjust.

### Example: Analytics ↔ Engineering SLA

> Analytics will review and sign off on schema change impact assessments within **3 business days**.
> Engineering will notify analytics **2 sprints before** any schema change to tracked events.
> Escalation: VP Engineering and Head of Analytics.
> Review: First Monday of each month.

---

*This reference guide is provided as supplementary material for ECBS5256 Managing Data Science Teams — Central European University, Vienna.*
