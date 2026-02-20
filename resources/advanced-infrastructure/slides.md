---
marp: true
theme: ceu-analytics
paginate: true
header: "ECBS5256 – Managing Data Science Teams"
footer: "CEU Vienna | Day 2 – Block E"
---

# XFN, Vendor, IT & Data Infrastructure

**Day 2 — Block E | 13:30–15:10**

**Learning Outcomes**
By the end of this block you will be able to:
- Map cross-functional interfaces and document bidirectional SLAs
- Plan small-org data infrastructure across the canonical data stack layers
- Apply a build-vs-buy framework grounded in Total Cost of Ownership
- Evaluate vendors using a structured RFP scoring matrix

<!-- Talk track: Welcome back from lunch. This is the most technical block of the course, but I want to be clear — it's technical in the way a manager needs to be technical. You don't need to configure a Snowflake instance. You need to know what questions to ask, what trade-offs exist, and how to work with IT, Legal, and Engineering to make infrastructure decisions that your team can live with for the next two years. By the end of this session, you'll have two artifacts: a data infrastructure blueprint and a vendor scoring matrix. Both anchored to your case context. Let's go. -->

---

## Why Infrastructure Matters for Analytics Managers (1/2)

You don't need to be a data engineer — but you need to understand the stack well enough to **make decisions**.

- Infrastructure choices are **2–3 year commitments**
- The wrong warehouse, the wrong BI tool, the wrong ingestion pipeline — these compound into **months of lost productivity**
- Your team's output is only as good as the **data they can access**

<!-- Talk track: Before we dive into specific tools and frameworks, I want to make the case for why you — as a manager, not an engineer — need to care about infrastructure. These are not reversible decisions. When you pick a data warehouse, you're committing your team's workflows, your SQL dialect, your cost structure, and your integration points for the next two to three years. Migrations are brutal. I've seen teams spend six months moving from Redshift to Snowflake — six months where they built almost nothing new. The wrong BI tool means your stakeholders can't self-serve, so every question lands on your team's plate. The wrong ingestion pipeline means data arrives late, incomplete, or wrong. -->

---

## Why Infrastructure Matters for Analytics Managers (2/2)

**The manager's job:** You're not configuring Snowflake. You're deciding *whether* to use Snowflake, *how much* to spend on it, and *who* is responsible when it breaks.

Getting this wrong doesn't just slow your team down — it creates technical debt that the next manager inherits.

Your analysts can only analyze what they can access. If the infrastructure is broken, their skills don't matter.

<!-- Talk track: Your analysts can only analyze what they can access. If the infrastructure is broken, their skills don't matter. The manager's job is not to configure the tools — it's to make the right choices about which tools, how much to invest, and who owns what. Getting this wrong creates technical debt that compounds. The next manager inherits your infrastructure decisions, good and bad. So take these decisions seriously. -->

---

## The Cross-Functional Reality (1/2)

Analytics managers spend **30–40% of their time** on cross-functional work.

You are dependent on:
- **Engineering** for data
- **IT** for infrastructure
- **Legal** for compliance
- **Finance** for budget
- **Product** for priorities

<!-- Talk track: Here's a number that surprises most new analytics managers: you will spend thirty to forty percent of your time on cross-functional work. Not analyzing data. Not building dashboards. Managing relationships with other teams. You depend on Engineering to instrument events and maintain schemas. You depend on IT to provision access and approve vendors. You depend on Legal to clear your data usage. You depend on Finance to approve your budget. You depend on Product to tell you what to measure. -->

---

## The Cross-Functional Reality (2/2)

If **any** of these relationships break down, your team stalls.

This block teaches you to manage those relationships **structurally, not ad hoc**. Handshake agreements don't survive re-orgs. Written SLAs do.

Most managers handle this ad hoc: a Slack message here, a coffee chat there. That doesn't scale. This block gives you the structural tools — SLAs, blueprints, scoring matrices — to manage these dependencies like a professional.

<!-- Talk track: If any one of these relationships is broken — if Engineering doesn't tell you about schema changes, if Legal takes six weeks to review a vendor — your team sits idle. Most managers handle this ad hoc: a Slack message here, a coffee chat there. That doesn't scale. This block gives you the structural tools — SLAs, blueprints, scoring matrices — to manage these dependencies like a professional. Handshake agreements don't survive re-orgs. Written SLAs do. That's the key difference between reactive management and proactive management. -->

---

## What We'll Build This Block (1/2)

By the end of this session, you'll have **four practical artifacts:**

1. **Cross-functional SLAs** — Written agreements with Engineering, IT, Legal, and Product that define who owes what to whom, and by when
2. **A data infrastructure blueprint** — Tailored to your case context, mapping tools to each layer of the canonical data stack

<!-- Talk track: Let me preview what we're building so you know where we're headed. Four artifacts. First, cross-functional SLAs — we'll draft actual written agreements between analytics and the teams you depend on. Second, a data infrastructure blueprint — you'll map out the tools for each layer of your data stack, specific to your case context. -->

---

## What We'll Build This Block (2/2)

3. **A build-vs-buy analysis** — A framework for deciding when to use open-source, when to buy SaaS, and when to build in-house
4. **A vendor scoring matrix** — A structured RFP evaluation you can use to compare real vendors on real criteria

These aren't academic exercises — they're artifacts you can actually use on **Day 1** of a real analytics management role.

<!-- Talk track: Third, a build-vs-buy analysis — a decision framework you'll apply to at least one real tool choice. Fourth, a vendor scoring matrix — you'll evaluate three real vendors on weighted criteria and make a recommendation. I want to be explicit about the goal here: these are not slides you forget after class. These are documents you can bring to a job and use immediately. The infrastructure blueprint is something you could hand to a CTO in your first month. The vendor scoring matrix is something you could use the first time someone asks you to pick a BI tool. Let's get into it. -->

---

## Your Cross-Functional Universe (1/2)

Analytics doesn't exist in a vacuum. Your key interfaces:

| Interface | What they care about |
|---|---|
| **Product** | What to measure, experiment results |
| **Engineering** | How to collect data, system reliability |
| **Design** | What to surface to users |

<!-- Talk track: Let's start with context. In Block A, you built a stakeholder map. Now we're going to zoom in on the cross-functional relationships that matter most for infrastructure and data decisions. Analytics sits at the center of this universe — not because we're the most important team, but because data touches everything. Product needs you to measure their features. Engineering needs you to not break their systems with heavy queries. Design needs you to surface insights in the product. -->

---

## Your Cross-Functional Universe (2/2)

| Interface | What they care about |
|---|---|
| **Legal / Privacy** | What you can store, for how long |
| **Finance** | What it all costs |
| **IT / Infra** | Where it runs, who has access |

**Mental model:** Analytics sits at the center of a hub-and-spoke. Every spoke is a relationship you must actively manage.

<!-- Talk track: Legal needs you to not get the company sued. Finance needs to understand what this all costs. And IT needs to make sure it's secure and compliant. Here's the mental model I want you to carry forward. Analytics is the hub. Every other team is a spoke. You don't control any of these teams — you can't tell Engineering what to prioritize or tell Legal to move faster. But you can manage the interface. You can document expectations. You can establish cadences. -->

---

## Your Cross-Functional Universe (cont.)

You don't get to choose whether these relationships exist. They exist whether you manage them or not. The question is whether you manage them **proactively** — with documentation, SLAs, and regular check-ins — or **reactively**, scrambling when something breaks.

Every one of these relationships is bidirectional, and every one of them will shape your infrastructure choices.

<!-- Talk track: You can build enough trust that when something urgent comes up, you're not starting from zero. The managers who struggle most are the ones who treat these relationships as optional — who focus entirely on their own team and then are shocked when Engineering changes a schema without telling them. The relationships exist whether you manage them or not. The only question is whether you're proactive or reactive. -->

---

## The XFN Failure Modes (1/2)

What actually goes wrong when cross-functional relationships aren't managed:

- **Engineering changes a schema** and breaks your pipeline at 2 AM. Nobody told you. Your morning dashboards are wrong. The CEO asks questions before you even know there's a problem.
- **Legal blocks your new analytics tool** three months into implementation. You've already migrated data, trained the team, and built dashboards. Now you have to unwind everything.

<!-- Talk track: Let me make this concrete with real failure stories I've seen. Scenario one: Engineering ships a database migration over the weekend. They rename three columns. Your dbt models reference the old names. Your pipeline fails at 2 AM. Your morning dashboards show stale data — or worse, errors. The CEO pulls up the revenue dashboard at 8 AM and asks why it's blank. You find out about the schema change from the CEO, not from Engineering. Scenario two: you spend three months evaluating and implementing a new analytics tool. You've migrated data, built dashboards, trained your team. Then Legal tells you the tool's data processing agreement doesn't meet GDPR requirements. Three months of work, unwound. -->

---

## The XFN Failure Modes (2/2)

- **Finance doesn't approve your vendor renewal.** Your BI tool license expires. Dashboards go dark. Stakeholders lose access to reports they depend on daily.
- **Product launches a feature without instrumentation.** The VP asks "how is the new feature performing?" and you have no data. You can't measure what wasn't tracked.

Each failure mode maps to a **preventable relationship gap**. That's what SLAs are for.

<!-- Talk track: Scenario three: your BI tool contract is up for renewal. You assumed Finance would approve it — it's the same cost as last year. But Finance is cutting vendor spend across the board. Your license lapses. Dashboards go dark. Scenario four: Product ships a major new feature. The VP of Product asks you to report on adoption. But nobody added event tracking. You have zero data. Every one of these is preventable with a written SLA and a regular check-in. -->

---

## What Each Team Needs From You (1/2)

| Team | They need from you |
|---|---|
| **Product** | Metrics definitions, experiment results, self-serve dashboards |
| **Engineering** | Data contracts, SLAs for pipeline load, schema documentation |
| **Legal / Privacy** | Data inventories, consent tracking, retention schedules |

<!-- Talk track: Let's get specific about what each team needs from analytics. Product needs metrics definitions — and they need those definitions to be stable, documented, and trustworthy. Engineering needs data contracts — agreements about what data you'll produce, what schema it follows, and what the SLAs are. Legal needs a data inventory — what PII do you have, where does it live, who can access it, and when does it get deleted? -->

---

## What Each Team Needs From You (2/2)

| Team | They need from you |
|---|---|
| **Finance** | Cost attribution by team/project, ROI analysis on data tools |
| **IT** | Security compliance docs, vendor onboarding paperwork |
| **Design** | User behavior data, funnel analysis, UX metrics |

<!-- Talk track: Finance needs to know what your stack costs and whether it's worth it. IT needs to know that every vendor you onboard meets their security requirements. Design needs user behavior data and funnel analysis to inform UX decisions. -->

---

## What Each Team Needs From You (cont.)

The pattern: every team needs **clarity** and **documentation** from you. Not just insights — operating agreements.

Your value to these teams isn't just the dashboards you produce. It's the **predictability** you provide. When Product knows they'll get experiment results within 48 hours of a test completing, they plan around that. When Engineering knows you'll review schema changes within one sprint, they include you in the process.

This is why we spent time on artifacts in Block A. Your Manager OS produces the documents that make these relationships work.

<!-- Talk track: Notice the pattern here. Everyone needs documentation and agreements from you. Not just insights and dashboards — operating agreements. Product doesn't just need you to answer questions. They need to know how long it takes you to answer questions, and what format the answer comes in. Engineering doesn't just need you to consume their data. They need to know what load your queries put on their systems, and what you'll do when something breaks. This is why we spent time on the Manager OS in Block A. The documents you produce — data contracts, metric definitions, cost reports — are the glue that holds these relationships together. Without them, every interaction is ad hoc, and ad hoc doesn't scale. -->

---

## What You Need From Them (1/2)

| Team | You need from them |
|---|---|
| **Product** | Clear, prioritized business questions |
| **Engineering** | Reliable instrumentation, advance notice of schema changes |
| **Legal** | Timely privacy reviews, clear data usage guidance |
| **Finance** | Reasonable budget cycles, approval velocity |
| **IT** | Procurement timelines, cloud access, SSO provisioning |

<!-- Talk track: Now flip it around. What do you need from them? Product needs to give you clear, prioritized business questions — not vague "can you look at the data?" requests. Engineering needs to tell you when they change schemas — because if they rename a field and your pipeline breaks, that's on both of you. Legal needs to be responsive on privacy reviews, not a 6-week black hole. IT needs to provision cloud access in days, not months. -->

---

## What You Need From Them (2/2)

**The key insight:** These are **bidirectional contracts**. Document them as SLAs.

*"Engineering will notify analytics 2 sprints before any schema change to tracked events."*

That's not bureaucracy. That's how you stop your pipelines from breaking at 2 AM.

<!-- Talk track: Here's the big idea: document these as bidirectional SLAs. Literally write them down. "Engineering will notify analytics 2 sprints before any schema change to tracked events. Analytics will provide a data impact assessment within 3 business days of any privacy review request." That's not bureaucracy. That's how adults collaborate. Who has been burned by a surprise schema change? -->

---

## Building Bidirectional SLAs — Template (1/2)

How to actually create and maintain SLAs with other teams:

**Template:**

> **Analytics will** provide [deliverable X] within [Y timeframe].
> **[Partner team] will** provide [deliverable Z] within [W timeframe].
> **Escalation path:** [name/role] if SLA is missed.
> **Review cadence:** Monthly sync to assess and adjust.

<!-- Talk track: Let me give you a practical template for building these SLAs. It's dead simple — four lines. What you'll provide and by when. What they'll provide and by when. Who to escalate to when someone misses. And how often you review the agreement. The review cadence is critical — monthly is right for most teams. It gives you a regular forum to say "this is working" or "this isn't working, let's adjust." -->

---

## Building Bidirectional SLAs — Template (2/2)

**The key:** SLAs work when **both sides see value**. If it feels one-sided, it won't survive the first quarter.

Start with the most critical relationship — usually Engineering — and expand from there. One well-maintained SLA is worth more than five ignored ones.

<!-- Talk track: The secret to SLAs that actually stick is that both sides need to see value. If the SLA only benefits you, the partner team will ignore it within a month. Start with the most critical relationship — usually Engineering — and get that SLA working well before expanding to other teams. -->

---

## Building Bidirectional SLAs — Example (1/2)

**Analytics ↔ Engineering SLA:**

> Analytics will review and sign off on schema change impact assessments within **3 business days**.
> Engineering will notify analytics **2 sprints before** any schema change to tracked events.
> Escalation: VP Engineering and Head of Analytics.
> Review: First Monday of each month.

<!-- Talk track: Here's a concrete example for the Engineering relationship. You commit to reviewing schema change impacts within three business days, and they commit to notifying you two sprints in advance. Both sides benefit. Engineering gets a fast, predictable turnaround on impact assessments, and you get the advance notice you need to update pipelines before anything breaks. -->

---

## Building Bidirectional SLAs — Example (2/2)

Both sides get something: Engineering gets fast turnaround on impact assessments, and you get advance notice of changes.

Draft one of these for each key cross-functional partner. It takes thirty minutes and saves hundreds of hours of fire-fighting.

These documents transform ad hoc relationships into reliable operating agreements.

<!-- Talk track: I recommend drafting one of these for each of your key partners — Engineering, IT, Legal, Product. It takes about thirty minutes per SLA and the return on that investment is enormous. These documents transform ad hoc relationships into reliable operating agreements. -->

---

## The Data Infrastructure Blueprint (1/2)

The canonical flow — every modern data stack follows this pattern:

**Sources** --> **Ingestion** --> **Storage** --> **Transform** --> **Semantic Layer** --> **Visualization**

With cross-cutting concerns at every layer:

- **Governance:** Who owns what? Who can access what?
- **Observability:** Is it working? How do you know?
- **Cost management:** What does each layer cost?

<!-- Talk track: Here's the big picture. Every modern data stack follows this flow: you have sources of data — your product database, event streams, third-party APIs. You ingest that data into a central store. You store it — in a warehouse or lakehouse. You transform it — clean it, model it, make it trustworthy. You build a semantic layer — agreed-upon definitions of your metrics. And you visualize it — dashboards, reports, self-serve exploration. Across all of these layers, you have three cross-cutting concerns: governance, observability, and cost. -->

---

## The Data Infrastructure Blueprint (2/2)

This is the map. Your case context determines the territory.

**Anchor this slide.** We'll come back to it throughout the block.

When we talk about specific tools, always ask: where does this fit in the flow?

<!-- Talk track: This diagram is the anchor for the rest of this block. When we talk about specific tools, I want you to always ask: where does this fit in the flow? Print this mental model. Tattoo it on your arm. Whatever it takes. -->

---

## Reading an Architecture Diagram (1/2)

For those who aren't deeply technical — here's how to read a data flow diagram:

| Layer | What it does (plain English) | Key question |
|---|---|---|
| **Sources** | Where data originates (app, APIs, files) | "Capturing everything we need?" |
| **Ingestion** | Moves data from sources to storage | "How fresh? Minutes, hours, days?" |
| **Storage** | The central repository (warehouse) | "Cost? Can it scale?" |

<!-- Talk track: If you come from a business or social science background and architecture diagrams feel intimidating, this slide is for you. Each layer does one thing. Sources are where data comes from — your product database, event tracking, third-party APIs. Ingestion is the plumbing that moves data from those sources into your central storage. Storage is the warehouse — think of it as a really big, really fast database optimized for analytics queries. -->

---

## Reading an Architecture Diagram (2/2)

| Layer | What it does (plain English) | Key question |
|---|---|---|
| **Transform** | Cleans raw data into usable tables | "How do we verify correctness?" |
| **Semantic Layer** | Defines metrics so everyone agrees | "One definition of 'revenue'?" |
| **Visualization** | Dashboards end users see | "Can stakeholders self-serve?" |

<!-- Talk track: Transform is where you clean and model the raw data — turning messy event logs into clean tables your analysts can use. The semantic layer is where you define what "active user" means or how "revenue" is calculated, so everyone in the company uses the same number. Visualization is the dashboards your stakeholders actually see. -->

---

## Reading an Architecture Diagram (3/3)

**At every layer, ask three questions:**
1. "How do we know it's working?" — observability
2. "What happens when it breaks?" — resilience
3. "What does it cost?" — cost management

If you can ask those three questions intelligently about each layer, you can hold your own in any infrastructure conversation.

<!-- Talk track: Train yourself to ask these three questions at every layer of the stack. How do we know it's working — that's observability. What happens when it breaks — that's resilience. What does it cost — that's cost management. If you can ask those three questions intelligently about each layer, you can hold your own in any infrastructure conversation. -->

---

## Small Org Stack (0 to 1) (1/2)

**Goal:** Trusted numbers, fast. Don't over-engineer.

| Layer | Tool | Why |
|---|---|---|
| **Sources** | Product DB + basic events | Start with what you have |
| **Ingestion** | Fivetran or Airbyte | Managed connectors; don't build this |
| **Storage** | BigQuery or Snowflake (free tier) | Start small, scale later |

<!-- Talk track: If you're in the small startup case context, this is your stack. I want to be very direct: your goal is trusted numbers, fast. Not a beautiful architecture diagram. Not a resume-driven stack. You need to get data from your product database into a warehouse, transform it so it's trustworthy, and put it in a dashboard that your CEO can look at every Monday. Fivetran or Airbyte for ingestion — don't build your own connectors, that's a waste of your time. BigQuery or Snowflake for storage — both have generous free tiers. -->

---

## Small Org Stack (0 to 1) (2/2)

| Layer | Tool | Why |
|---|---|---|
| **Transform** | dbt (Core or Cloud) | SQL-based; version-controlled; testable |
| **Viz** | Metabase or Preset | Open-source options exist; low cost |
| **Governance** | Naming conventions + a spreadsheet | Seriously. This is enough to start. |

**Monthly cost:** $500–2,000

<!-- Talk track: dbt for transformation — it's SQL, it's version-controlled, it's testable. Metabase or Preset for visualization. And governance? At this stage, governance is a naming convention document and a spreadsheet that says who owns each table. That's it. Don't let anyone tell you that you need a data catalog at this stage. You don't. Total cost for this stack: under two thousand a month. That's incredibly affordable for a startup. -->

---

## Small Org Stack — What to Skip

**What to skip:** Data catalog, ML platform, feature store, semantic layer tooling. You're not there yet.

<!-- Talk track: Now here's the discipline part — what to skip. You don't need a data catalog when you have fifty tables. You don't need an ML platform when you don't have ML models in production. You don't need a feature store when you have one data scientist. -->

---

## Small Org Stack (cont.)

Resist the urge to build for scale you don't have. Every tool you add is a tool you have to maintain. At this stage, your most scarce resource is **people's time**, not compute capacity.

The right time to add complexity is when the current stack **breaks under real usage** — not when you think it might break someday.

<!-- Talk track: I know it's tempting to build the "right" architecture from day one. Fight that instinct. Every tool you add is a tool someone has to configure, maintain, and debug. At a small org, that someone is probably you or your one data engineer. Every hour they spend maintaining infrastructure is an hour they're not answering business questions. Add complexity when you feel real pain, not anticipated pain. -->

---

## Medium Org Stack (1 to N) (1/2)

**Goal:** Self-serve metrics, experimentation, data trust at scale.

Add to the small stack:

| Layer | Addition | Why now |
|---|---|---|
| **Event platform** | Segment or RudderStack | Structured event collection; identity resolution |
| **Experimentation** | Statsig or Eppo | Rigorous A/B testing, not spreadsheet math |
| **Semantic layer** | dbt metrics or Cube | Single source of truth for metric definitions |

<!-- Talk track: Now you're a Series B company. You have product-market fit, you're scaling, and PMs are asking for self-serve analytics and real experimentation. The small stack isn't enough anymore. You add an event platform — Segment or RudderStack — because you need structured event collection and identity resolution across platforms. You add experimentation tooling because your growth team needs real A/B tests, not eyeballing a chart. You add a semantic layer so there's one agreed-upon definition of "active user" and "revenue." -->

---

## Medium Org Stack (1 to N) (2/2)

| Layer | Addition | Why now |
|---|---|---|
| **Catalog** | DataHub or Atlan | Discovery; lineage; tribal knowledge captured |
| **Observability** | Monte Carlo or Elementary | Know when data breaks before your stakeholders do |

**Governance:** Formal data owners. Published SLAs. Access controls.

**Monthly cost:** $10,000–30,000

<!-- Talk track: You add a data catalog because there are now enough tables that people can't find what they need. And critically, you add observability — Monte Carlo or Elementary — so that you know when data is broken before the CEO messages you on Slack at 8 AM asking why the dashboard looks weird. Governance gets real at this stage. You need formal data owners — someone whose name is attached to each critical table and who is accountable when it breaks. Monthly cost jumps to ten to thirty thousand. -->

---

## Medium Org Stack (cont.)

At this stage, governance is no longer a spreadsheet — it's a **system**. Every critical table has a named owner. Every pipeline has an SLA. Access is role-based, not "everyone can see everything."

The jump from $2K to $10K+ feels steep, but the cost of **not** having observability, a semantic layer, or proper access controls is higher. One bad metric that reaches the board costs you more than a year of Monte Carlo.

<!-- Talk track: That's a real budget line item. But let me reframe the cost: what's the cost of a wrong number reaching the board? What's the cost of a data breach because everyone had access to PII? What's the cost of your best analyst spending two hours every morning checking whether the data is fresh? The tools pay for themselves if they prevent even one of those scenarios. -->

---

## Large Org Stack (N to Scale) (1/2)

**Goal:** Domain autonomy, ML at scale, regulatory compliance.

Add to the medium stack:

| Layer | Addition | Why now |
|---|---|---|
| **Architecture** | Data mesh / domain ownership | Decentralized ownership, centralized standards |
| **ML platform** | MLflow, SageMaker, or Vertex | Model training, versioning, deployment |
| **Feature store** | Feast or Tecton | Shared features across models |

<!-- Talk track: At enterprise scale, the challenges are fundamentally different. You're not trying to get trusted numbers — you're trying to maintain trust across dozens of teams, petabytes of data, and strict regulatory requirements. Data mesh becomes relevant — decentralized ownership with centralized standards. You need an ML platform because you have multiple models in production. You need a feature store because different teams keep re-deriving the same features. -->

---

## Large Org Stack (N to Scale) (2/2)

| Layer | Addition | Why now |
|---|---|---|
| **Model governance** | Model cards, bias audits, monitoring | Regulatory and ethical requirements |
| **Cost management** | Kubecost, cloud billing dashboards | Because $100K+/mo demands accountability |
| **Data marketplace** | Internal data products catalog | Treat data as a product, not a byproduct |

**Monthly cost:** $100,000+

<!-- Talk track: You need model governance — model cards, bias audits, monitoring — because regulators and your own ethics demand it. And you absolutely need cost management because at a hundred thousand a month, someone is going to ask where the money goes. Monthly cost is a hundred thousand dollars or more. That sounds like a lot, but at this scale you're talking about a company with hundreds of millions or billions in revenue. The data infrastructure is a fraction of a percent of revenue. -->

---

## Large Org Stack (cont.)

**Governance:** Access controls, lineage, regulatory compliance, audit trails, data classification.

At this scale, governance is a **team**, not a task. You may have dedicated data governance analysts, a privacy engineer, and a compliance officer. The governance stack itself — catalog, lineage, access controls, audit logs — becomes as complex as the data stack it governs.

For those of you in the large enterprise case context: your challenge isn't choosing tools. It's navigating procurement, proving ROI, and managing the politics of a data mesh transition.

<!-- Talk track: Governance at the large org level is a team unto itself. You need dedicated people thinking about access controls, data lineage, regulatory compliance, and audit trails. The governance stack — your catalog, your lineage tool, your access control layer — becomes its own mini-infrastructure that needs its own maintenance and its own budget. The real challenge for large enterprise analytics managers isn't the money — it's the organizational complexity. Getting approval for a new tool involves procurement, legal, security, IT, and finance. That's five teams that all need to say yes before you can buy anything. -->

---

## The Migration Trap (1/2)

What happens when you outgrow your stack — three common migration stories:

**1. Spreadsheets to a real warehouse**
Ran on Google Sheets and suddenly need BigQuery. Painful but straightforward. Budget 2–3 months.

**2. Warehouse to warehouse**
Redshift to Snowflake, or Snowflake to Databricks. Every query, dashboard, and integration rebuilt. Budget 6–12 months.

<!-- Talk track: I want to talk about what happens when you outgrow your stack, because it will happen. Story one: you started on spreadsheets and now you need a real warehouse. This is actually the easiest migration — you're going from nothing to something. It's painful, it takes two to three months, but it's a one-way door and everyone agrees it needs to happen. Story two: you need to move from one warehouse to another. This is brutal. Every SQL query is slightly different across warehouses. Every dashboard connection needs to be reconfigured. Every integration needs to be re-tested. I've seen this take six to twelve months, and during that time your team is essentially maintaining two systems. -->

---

## The Migration Trap (2/2)

**3. "We built it ourselves and now we can't maintain it"**
The custom pipeline one engineer built, who then left. Nobody understands or can fix it.

**Key insight:** Plan for the **next** migration when choosing the current tool. Ask: "How hard will it be to leave this vendor in 3 years?"

Avoid proprietary lock-in where you can. Use standard SQL. Use standard file formats. Make migration a design criterion, not an afterthought.

<!-- Talk track: Story three — and this is the most painful — you built something custom. Maybe it was a brilliant engineer who built a custom ingestion pipeline. Then that engineer left. Now nobody understands how it works, it breaks regularly, and nobody can fix it properly. You're stuck. The lesson: when you choose a tool today, ask yourself how hard it will be to leave that tool in three years. Avoid proprietary lock-in where you can. Use standard SQL. Use standard file formats. Make migration a design criterion, not an afterthought. -->

---

## Build vs. Buy — The Framework

**Four questions in order:**

1. **Is this a core differentiator?** If yes: build.
   - Your recommendation algorithm? Build. Your data warehouse? Buy.

2. **Is this commodity infrastructure?** If yes: buy.
   - Ingestion, storage, BI tooling — these are solved problems.

3. **Do you have the team to maintain it?** If no: buy.
   - "Free" open source costs your engineers' time. Forever.

<!-- Talk track: Build versus buy is one of the most consequential decisions you'll make as an analytics leader. Here's a framework with four questions. Question one: is this a core differentiator? If your company's competitive advantage depends on a proprietary recommendation engine, build it. But your data warehouse is not a differentiator. Nobody ever won a market because they had a better warehouse. Question two: is this commodity infrastructure? Ingestion, storage, BI tools — these are solved problems. Buy them. Question three: do you have the team to maintain it? Open source is not free. Airflow is not free. It requires engineers to keep it running, upgrade it, fix it when it breaks. If you don't have those engineers, buy a managed service. -->

---

## Build vs. Buy — Total Cost of Ownership

4. **What's the Total Cost of Ownership?**
   - License + implementation + training + maintenance + **opportunity cost**
   - The biggest hidden cost: what your team *doesn't* build while maintaining infra.

**Default to buy** for infrastructure. Default to build for business logic.

The opportunity cost is the one people forget. Every hour your data engineer spends maintaining Airflow is an hour they're not building the pipeline your PM needs.

<!-- Talk track: Question four: what's the total cost of ownership? Add up the license, implementation, training, maintenance, and — this is the one people forget — opportunity cost. Every hour your data engineer spends maintaining Airflow is an hour they're not building the pipeline your PM needs. The rule of thumb is simple: default to buy for infrastructure, default to build for business logic. Infrastructure is commodity — someone else has already solved the hard problems. Business logic is where your team adds unique value. That's where you want your engineers spending their time. -->

---

## The Hidden Costs of "Free" — The Comparison (1/2)

Open-source tools have **real costs** — your engineers' time to set up, configure, maintain, upgrade, and debug.

**Airflow (open-source) vs. managed alternatives:**

| Cost component | Self-hosted Airflow | Managed (e.g., Astronomer) |
|---|---|---|
| License | $0 | ~$300–1,200/mo |
| Engineer setup | 40–80 hours | 4–8 hours |

<!-- Talk track: This is the slide I wish someone had shown me earlier in my career. Open source is not free. Let me walk through a concrete example. Airflow is the most popular open-source orchestration tool. The license costs zero dollars. But setting it up takes forty to eighty hours of a data engineer's time. -->

---

## The Hidden Costs of "Free" — The Comparison (2/2)

| Cost component | Self-hosted Airflow | Managed (e.g., Astronomer) |
|---|---|---|
| Monthly maintenance | 8–16 hours/mo | ~0 hours/mo |
| Upgrades (annual) | 20–40 hours | Included |
| Debugging & incidents | 5–10 hours/mo | Vendor handles |

<!-- Talk track: Maintaining it — keeping it running, monitoring it, fixing it when workers crash — takes eight to sixteen hours a month. Upgrading it when a new version comes out is a multi-day project. And when it breaks at 2 AM, your engineer is the one getting paged. -->

---

## The Hidden Costs of "Free" — Annual Total

| | Self-hosted | Managed |
|---|---|---|
| **Annual engineer cost** | ~$30K–50K in loaded salary | ~$4K–14K in subscription |

**When "free" actually costs more than "paid":** almost always, unless you have a dedicated platform team.

The real question isn't "what does the tool cost?" It's "what does my team NOT build while maintaining this tool?"

<!-- Talk track: Add it up: you're spending thirty to fifty thousand dollars a year in engineer salary to run a "free" tool. A managed alternative costs four to fourteen thousand a year in subscription fees. And your engineer spends almost zero time on maintenance, so they can build pipelines instead of babysitting infrastructure. The only time self-hosting makes economic sense is when you have a dedicated platform team that's already managing Kubernetes and cloud infrastructure. For most analytics teams, especially small and medium ones, managed services are cheaper than free. -->

---

## The RFP Process

**When to RFP:** Spending >$10K/year or handling PII.

**Steps:**

1. **Define requirements** — Must-have vs. Should-have vs. Nice-to-have
2. **Weight criteria** — Not all requirements are equal
3. **Score vendors** — Structured, not vibes-based
4. **Negotiate** — Always negotiate. Always.
5. **Pilot** — 2-4 week proof of concept before committing

<!-- Talk track: When you're spending more than ten thousand a year or when PII is involved, you need a structured process. This is the RFP — request for proposal. Step one: define your requirements. Separate them into must-have, should-have, and nice-to-have. This is critical because vendors will try to dazzle you with features you don't need. Step two: weight the criteria. Security might be worth 25% of the score for one org and 10% for another. Step three: score each vendor on each criterion. Use a 1-to-5 scale and do it as a team so you get multiple perspectives. Step four: negotiate. I cannot stress this enough — always negotiate. SaaS pricing is almost never firm. Step five: pilot. Never commit to an annual contract without a proof of concept. Two to four weeks, real data, real users. If the vendor won't let you pilot, that tells you something. -->

---

## The RFP Process — Scoring Dimensions (1/2)

| Criterion | What to evaluate |
|---|---|
| **Functionality** | Does it solve the core problem? |
| **Integration** | Works with our existing stack? |
| **Security** | SOC 2, encryption, access controls |

<!-- Talk track: Here are the scoring dimensions I recommend for any vendor evaluation. Functionality — does it actually solve the problem you're trying to solve? Integration — does it connect to your existing warehouse, your existing BI tool, your existing SSO? Security — does it have SOC 2 Type II, does it encrypt data at rest and in transit, does it support role-based access controls? -->

---

## The RFP Process — Scoring Dimensions (2/3)

| Criterion | What to evaluate |
|---|---|
| **Cost** | Total cost of ownership over 3 years |
| **Support** | Response times, dedicated CSM, community |
| **Scalability** | Will it grow with us? |

<!-- Talk track: Cost — not just the sticker price, but the total cost of ownership over three years including implementation and training. Support — what happens when it breaks? Do you get a dedicated customer success manager, or do you file a ticket and wait a week? Scalability — if your data volume doubles in a year, will this tool handle it? -->

---

## The RFP Process — Scoring Dimensions (3/3)

**Pro tip:** Score as a team. Each evaluator scores independently, then discuss disagreements — the discussion reveals hidden assumptions.

Have each evaluator score independently, then come together to discuss. That discussion is incredibly valuable — it reveals assumptions and priorities you didn't know existed.

<!-- Talk track: I recommend scoring as a team. Have each evaluator score independently, then come together to discuss disagreements. That discussion is incredibly valuable — it reveals assumptions and priorities you didn't know existed. -->

---

## Working with IT & Procurement

**Speak their language:**
- Security posture, SOC 2 Type II, penetration testing
- Data residency (EU data stays in EU — GDPR requirement)
- SSO / SAML integration (no separate passwords)
- Audit logs (who accessed what, when)
- Vendor risk assessment questionnaire

<!-- Talk track: Here's where most analytics managers fail: they find a tool, fall in love with it, start a trial, build dependencies on it, and then discover that IT won't approve it because it doesn't support SSO, or it stores data outside the EU, or it hasn't completed a SOC 2 audit. Now you've wasted three months. Instead, learn to speak IT's language. SOC 2 Type II means the vendor has been independently audited for security practices — over time, not just at a point in time. Data residency means where the bits physically live — and under GDPR, EU personal data generally needs to stay in the EU. SSO means your team logs in with their company credentials, not a separate password. Audit logs mean you can prove who accessed what data and when. Learn these terms. Use them in your first conversation with IT. They will immediately take you more seriously. -->

---

## Working with IT & Procurement (cont.) (1/2)

**Procurement realities:**
- Budget cycle alignment — miss the window, wait a year
- Procurement takes **2–6x longer** than you think
- Legal review of contracts adds weeks
- Security review adds more weeks

<!-- Talk track: And here's the timeline reality: procurement takes two to six times longer than you expect. I've seen analytics managers plan to have a new tool deployed in a month. Then they discover they need security review, which takes three weeks. Then legal review of the contract, which takes two weeks. Then finance approval, which requires budget committee sign-off, which happens monthly. Then SSO integration, which requires IT to configure. What they thought was one month is actually four months. -->

---

## Working with IT & Procurement (cont.) (2/2)

**The golden rule:** Involve IT early. Not as a blocker — as a partner. Build the relationship before you need something.

The worst time to introduce yourself to the IT security team is when you need an emergency vendor approval. Build the relationship in your first month, not when you're desperate.

<!-- Talk track: Start the conversation with IT in month one, not month six. And here's the golden rule: involve IT early. Not as a blocker — as a partner. If you bring IT into the evaluation process from the beginning, they can flag issues early, before you've invested months of work. The worst possible approach is to pick a tool, start using it, and then ask IT for permission after the fact. That's how you become the team that IT says no to. -->

---

## The Procurement Timeline — Phases 1–4

What vendor evaluation **actually** looks like from start to signed contract:

| Month | Step | Who's involved |
|---|---|---|
| **Month 1** | Identify need, get IT alignment, vendor research | Analytics + IT |
| **Month 1–2** | Vendor demos, shortlist to 2–3 options | Analytics + IT + stakeholders |
| **Month 2–3** | Pilot / proof of concept with real data | Analytics + Engineering |
| **Month 3** | Security questionnaire + vendor risk assessment | IT Security |

<!-- Talk track: I want to show you what the procurement timeline actually looks like, because most analytics managers dramatically underestimate it. Month one: you identify the need and start researching vendors. Critically, you loop in IT from day one. Month one to two: you run demos and narrow down to two or three finalists. Month two to three: you run a pilot with real data. This is where you find out if the tool actually works for your use case, not just in a sales demo. Month three: security review. The vendor fills out your company's security questionnaire. IT reviews their SOC 2 report. This alone can take three to four weeks. -->

---

## The Procurement Timeline — Phases 5–8

| Month | Step | Who's involved |
|---|---|---|
| **Month 3–4** | Legal review of contract + data processing agreement | Legal |
| **Month 4** | Budget approval (align to budget cycle!) | Finance |
| **Month 4–5** | SSO integration + access provisioning | IT |
| **Month 5–6** | Full deployment + team training | Analytics |

**Total: 3–6 months.** Plan accordingly. If you need a tool by Q3, start the process in Q1.

<!-- Talk track: Month three to four: legal reviews the contract and the data processing agreement. They'll have questions. There will be redlines. Month four: budget approval. If you've missed the budget cycle, you might wait months. Month four to five: IT configures SSO and provisions access. Month five to six: you actually deploy and train your team. Total elapsed time: three to six months. If you need a tool operational by Q3, you need to start this process in Q1. Most analytics managers start in Q2 and then are surprised when the tool isn't ready until Q4. Plan backwards from your deadline. -->

---

## Privacy & Governance Basics

**GDPR essentials for analytics managers:**

| Concept | What it means for you |
|---|---|
| **Lawful basis** | You need a legal reason to process personal data (consent, legitimate interest, etc.) |
| **Data minimization** | Collect only what you need. "We might need it someday" is not a reason. |
| **Right to erasure** | Users can ask you to delete their data. Your pipeline must support this. |
| **Consent management** | Track what users consented to. Don't use data beyond that scope. |

<!-- Talk track: Privacy is not optional and it's not someone else's problem. As an analytics manager, you are directly responsible for how your team collects, stores, and uses personal data. GDPR gives us four concepts you need to internalize. Lawful basis — you need a legal reason to process personal data. "We want to analyze it" is not automatically sufficient. Data minimization — collect only what you need for a specific purpose. I've seen teams logging every click, every scroll position, every mouse movement "just in case." That's a liability, not an asset. Right to erasure — if a user asks to be deleted, your pipeline needs to handle it. If your analytics warehouse can't delete a specific user's data, you have a compliance problem. And consent management — track what users agreed to and don't exceed that scope. -->

---

## Privacy & Governance Basics (cont.) (1/2)

**Data classification — know your tiers:**
- **Public** — Can share openly (blog metrics, public benchmarks)
- **Internal** — Company-wide access (aggregate dashboards)
- **Confidential** — Need-to-know (user-level data, financial details)
- **Restricted** — Highest sensitivity (PII, health data, payment data)

<!-- Talk track: Data classification is something every analytics manager should implement, even at a small company. Four tiers. Public data can be shared openly — your blog traffic numbers, public benchmarks. Internal data is available company-wide — aggregate dashboards, high-level metrics. Confidential data is need-to-know — user-level behavioral data, financial details, anything that could be sensitive if leaked. Restricted data is the highest tier — personally identifiable information, health data, payment data. This should have the strictest access controls and the shortest retention periods. -->

---

## Privacy & Governance Basics (cont.) (2/2)

**Retention:** Don't keep what you don't need. Set policies. Enforce them.

Every table in your warehouse should have a retention policy. "Keep forever" is not a policy — it's a liability. Work with Legal to define how long each data tier needs to be kept, and build automated deletion into your pipelines.

<!-- Talk track: Speaking of retention: don't keep data forever. Every byte you store is a byte that could be leaked, a byte that regulators can ask about, and a byte that costs money to store. Set retention policies for every data tier. Work with Legal to determine the right retention period. Then build automated deletion into your pipelines. I've seen companies get into serious trouble because they kept data for years "just in case" and then couldn't explain why they had it when a regulator asked. -->

---

## Activity: Data Infrastructure One-Pager

**Time: 25 minutes** | Use the template provided

For your case context, write a one-page **"Our Next 6 Months of Data Infrastructure"** plan.

**Your one-pager must include:**
1. **Current state** — What exists today? Gaps and pain points?
2. **Target architecture** — Stack in 6 months, mapped to blueprint layers
3. **Key tools** — Selection for each layer and rationale

<!-- Talk track: Time for hands-on work. Open the data infrastructure blueprint template. You have 25 minutes. I want you to write a one-page plan for your case context's data infrastructure over the next six months. This is a real deliverable — something you could hand to a VP of Engineering or a CTO and say "here's what we need, here's what it costs, here's the plan." Be specific about tools. Don't write "we need a warehouse" — write "we'll use BigQuery because it has a generous free tier and our team already knows SQL." -->

---

## Activity: Data Infrastructure One-Pager (cont.)

**Your one-pager must also include:**
4. **Implementation plan** — Phased: Month 1-2, Month 3-4, Month 5-6
5. **Budget estimate** — Monthly and annual costs
6. **Risks & dependencies** — What could go wrong? What do you depend on?

**Tip:** Refer back to the blueprint slide. Small context students: resist the urge to over-engineer. Large context students: focus on what's achievable in 6 months, not the 5-year vision.

<!-- Talk track: Use the cost estimates from the slides as a starting point. Small context people: your one-pager should be simple. Three or four tools, under two thousand a month. Large context people: your challenge is scoping down to what's achievable in six months. Make sure you include a phased implementation plan and a realistic budget. The risks section is critical — think about what dependencies you have on other teams and what could delay your timeline. Go. I'll circulate. -->

---

## Activity: RFP Scoring Matrix

**Time: 20 minutes** | Use the template provided

Pick **one tool category** for your case context:
- Warehouse (BigQuery vs. Snowflake vs. Databricks)
- BI / Visualization (Metabase vs. Preset vs. Looker)
- Experimentation (Statsig vs. Eppo vs. LaunchDarkly)
- Ingestion (Fivetran vs. Airbyte vs. Stitch)

<!-- Talk track: Second activity. Keep your one-pager open — now pick one tool category from your infrastructure plan and do a real vendor evaluation. Pick a category where you have a genuine choice to make. If you're in the small context, maybe it's warehouse or BI tool. If you're in the medium context, maybe it's experimentation or event platform. If you're in the large context, maybe it's data catalog or ML platform. -->

---

## Activity: RFP Scoring Matrix (cont.)

**Your scoring matrix must include:**
1. **Requirements** — At least 8, prioritized as Must / Should / Nice
2. **Three real vendors** — Scored 1-5 on each criterion
3. **Weighted total** — Not all criteria are equal
4. **Total Cost of Ownership** — 3-year view per vendor
5. **Recommendation** — Which vendor and why?

**Tip:** You can use real pricing from vendor websites. Approximate is fine.

<!-- Talk track: Use real vendors, real criteria, real-ish pricing. The point of this exercise is to practice the discipline of structured evaluation. It's incredibly tempting to just pick the tool you've heard of or the one your friend uses. The scoring matrix forces you to be rigorous. Make sure you weight your criteria — security and functionality should probably carry more weight than nice-to-have features. Twenty minutes. Go. -->

---

## Debrief (1/2)

**Let's hear from the room:**

- What trade-offs did you make in your infrastructure plan?
- Where did build-vs-buy get hard? What made the decision ambiguous?
- What would IT push back on in your plan? What's the procurement risk?
- Did the scoring matrix change your initial instinct about which vendor to pick?

<!-- Talk track: Let's come back together. I want to hear from a few people. First — what trade-offs did you make? Someone in the small context: what did you decide to skip, and did it feel uncomfortable? Good. That discomfort means you understand what you're giving up. Now — where did build-vs-buy get hard? Who found a case where the answer wasn't obvious? That's the real world. The framework helps, but it doesn't make the decision for you. Finally — look at your infrastructure plan through IT's eyes. What would they push back on? If you picked a tool without SOC 2, they'll push back. If you picked a tool that stores data outside the EU, they'll push back. -->

---

## Debrief (2/2)

**Key insight:** The "right" stack depends on your constraints — team size, budget, timeline, regulatory environment. There is no universal answer. The framework is the answer.

<!-- Talk track: Here's the key takeaway from the debrief. There is no universally correct data stack. The right answer depends on your team size, your budget, your timeline, and your regulatory environment. The framework — build-vs-buy, TCO analysis, structured vendor scoring — is the answer. It's what lets you make a defensible, well-reasoned decision in any context. The scoring matrix is your tool for having that conversation with evidence, not opinions. -->

---

## Your Infrastructure Toolkit (1/2)

After this block, you have:

- [x] **Cross-functional map** — Who you depend on and what they need from you
- [x] **The canonical blueprint** — Sources through visualization with governance overlay
- [x] **Build-vs-buy framework** — Four questions to cut through the noise

<!-- Talk track: Let's take stock. You now have a practical toolkit for infrastructure decisions. You have a cross-functional map that documents your dependencies. You have the canonical blueprint that organizes any data stack. You have a build-vs-buy framework for making tool decisions. -->

---

## Your Infrastructure Toolkit (2/2)

- [x] **RFP scoring matrix** — Structured vendor evaluation, not vibes
- [x] **Privacy & governance basics** — GDPR, data classification, retention
- [x] **A 6-month infrastructure plan** — Specific to your case context

These feed directly into your **Manager Portfolio** — the data infrastructure blueprint and vendor scoring matrix are portfolio deliverables.

<!-- Talk track: You have a vendor scoring process. You have a privacy and governance foundation. And you have a six-month plan specific to your case context. Both the infrastructure blueprint and the vendor scoring matrix are deliverables in your final portfolio. Refine them this week using the feedback you got today. -->

---

## Transition to Block F (1/2)

**Next: QBR Simulation (15:30–17:10)**

You're about to present your roadmap and narrative to a mock executive panel.

**Use the next 10 minutes to:**
1. Review your roadmap from Day 1 Block C
2. Incorporate your infrastructure plan from today

<!-- Talk track: Final block is coming up — the QBR simulation. This is where everything comes together. You're going to present your roadmap and narrative to a mock executive panel. Take the next ten minutes — before we start Block F — to prep. Pull up your roadmap from Day 1. Incorporate the infrastructure plan you just wrote. -->

---

## Transition to Block F (2/2)

3. Prepare a 5-minute presentation: What are you building? Why? What does it cost?
4. Anticipate hard questions: "Why this vendor?" "What's the ROI?" "When do we see results?"

**The QBR format:** 5 min present, 5 min Q&A, 5 min peer feedback.

Think like an executive is listening. Because in Block F, they will be.

<!-- Talk track: Think about the story you're telling: what are we building, why does it matter, what does it cost, and when will we see results. Anticipate the hard questions. If you recommend Snowflake, be ready for "why not BigQuery — it's cheaper." If you recommend building something in-house, be ready for "do we have the team for that?" Think like your audience. See you at 3:30. -->
