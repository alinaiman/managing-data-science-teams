# Stakeholder Map Template

| Field | Your Entry |
|---|---|
| **Student Name** |Alina Imanakhunova|
| **Date** |16th of March, 2026|
| **Case Context** | Small (Seed-stage)|

---

## Power/Interest Grid

*Place each stakeholder's number (from the registry below) into the appropriate quadrant.*

```
INTEREST IN ANALYTICS
                    Low                     High
                ┌───────────────────┬───────────────────┐
                │                   │                   │
   High         │  KEEP SATISFIED   │  MANAGE CLOSELY   │
                │                   │                   │
                │  3. Backend Eng.  │  1. CEO            │
 POWER          │  8. VC Investors  │  2. Head of Product│
                │                   │                   │
                │                   │                   │
                │                   │                   │
                ├───────────────────┼───────────────────┤
                │                   │                   │
   Low          │  MONITOR          │  KEEP INFORMED    │
                │                   │                   │
                │  6. Designer      │  4. Mobile Devs   │
                │  7. Support Team  │  5. Mktg Contractor│
                │                   │                   │
                │                   │                   │
                └───────────────────┴───────────────────┘
```

---

## Stakeholder Registry

*List at least 6 stakeholders. Use roles, not names (e.g., "VP of Product" not "Sarah"). For each, assess their power over your team and their interest in your work.*

| # | Stakeholder (Role) | Power (H/L) | Interest (H/L) | Quadrant | What They Need From You | What You Need From Them | Engagement Strategy |
|---|---|---|---|---|---|---|---|
| 1 | CEO & Co-founder | H | H | Manage Closely | Investor-grade retention cohorts, LTV projections, CAC by channel — credible enough to present without hedging at Series A | Direct access to her for prioritization decisions; political air cover when requesting eng resources; fast feedback on what investors are actually asking | Weekly 1:1; shared Series A metrics tracker in Notion; async Slack for urgent investor prep questions |
| 2 | Head of Product | H | H | Manage Closely | Reliable feature-level retention data; onboarding funnel drop-off analysis; statistical validity on experiments; self-serve dashboard access | Clear hypotheses before experiments launch; buy-in on metric definitions; honest feedback when analyses are unclear | Weekly sync; embedded in sprint planning for analytics tickets; Slack channel #data-requests |
| 3 | Backend Engineer | H | L | Keep Satisfied | Zero added workload; no analytical queries hitting production DB; clean, minimal asks with lead time | Read replica or warehouse access approval; schema change notifications; PostgreSQL documentation | Async Slack only; brief monthly check-in; always document requests in writing before asking |
| 4 | Mobile Developers (×2) | L | H | Keep Informed | Clear, unambiguous event taxonomy spec they can implement without guesswork; fast review cycles on their instrumentation PRs | Implementation of new tracking in React Native; consistent naming conventions; notification when new features need tracking | Bi-weekly taxonomy review session; shared event spec doc with inline comments; tickets scoped for sprint |
| 5 | Designer | L | L | Monitor | Occasional UX research data or engagement metrics to inform design decisions | Nothing actively — passive awareness that data exists and is accessible | Monthly all-hands metrics review; ad-hoc on request |
| 6 | VC Investors (Seed Fund) | H | L | Keep Satisfied | A clean, self-consistent data room: retention curves, LTV model, engagement depth — no contradictions, no hedging | Clarity on which metrics they will scrutinize most during Series A diligence; timeline for fundraise process | No direct cadence; packaged investor data room delivered via Mira; monthly update through CEO |

**Stakeholders you might be missing:** IT/Infrastructure, Legal/Privacy, Finance/FP&A, Customer Success, Sales, HR/People Ops, External vendors, Board members or investors (for startups), Compliance/Audit (for enterprise), AI/ML platform owner or LLM/API budget controller.

---

## Key Relationships

*For your top 3 most critical stakeholders (those in "Manage Closely"), provide a deeper analysis.*

### Stakeholder 1: CEO & Co-founder, Mira Chen
 
- **Why they matter:** She is the direct manager, the budget holder, and the primary audience for the Series A metrics package. If this relationship breaks down — or if she loses confidence in the data — the analytics function loses its mandate entirely. A bad quarter of output could result in the role being deemed premature.
- **Current state of the relationship:** Needs work. She currently queries production PostgreSQL herself and hedges all retention numbers in investor conversations. She has never worked with a dedicated data person and her trust in analytics tools is low after the Amplitude/DB discrepancy incident.
- **Their goals:** She is personally measured on closing the Series A, likely at a $10–15M raise. Every conversation with investors circles back to retention, LTV, and CAC. Her goal is to walk into a pitch and answer those questions with total confidence.
- **Potential friction points:** She may push for polished investor-facing numbers before the underlying data is trustworthy. There will be tension between her urgency and the need to build a reliable foundation first. She also may continue running her own production DB queries if the warehouse is not delivered fast enough.
- **Your strategy (first 30 days):** Deliver one fast, credible win — a clean D30 retention cohort from PostgreSQL — within the first two weeks, with full methodology documented. Show her the number AND how it was calculated. Use this to begin building trust in the process, not just the output. Agree on a shared Series A metrics tracker in Notion so she has visibility into progress without needing to ask.
 
---
 
### Stakeholder 2: Head of Product, Jake Oduya,
 
- **Why they matter:** He is the highest-frequency internal customer. If he cannot self-serve or trust the data, analytics becomes a bottleneck rather than an enabler — and he will revert to gut-instinct decisions, undermining the entire purpose of the function. His buy-in on metric definitions is also critical: if Product and Data use different definitions of "active user," every analysis will be contested.
- **Current state of the relationship:** Neutral but frustrated. He tried to use Amplitude independently, discovered the data was unreliable, and lost confidence in both the tool and the underlying tracking. He has strong opinions about which metrics matter and will push back if analyses do not match his mental model.
- **Their goals:** He is measured on product engagement and retention improvements. He wants to move from opinion-driven to data-driven product development — specifically, he wants to know which features drive retention and whether the social accountability features are working.
- **Potential friction points:** He may request analyses before the data is clean enough to support them. He also has strong pre-existing opinions on metrics (e.g., his own definition of "active user") that may conflict with the canonical definitions needed for investor reporting. There is a risk he deprioritizes event instrumentation tickets in favor of feature work.
- **Your strategy (first 30 days):** Schedule a dedicated 60-minute session in Week 1 to map out his top five analytical questions. Use these to prioritize early warehouse work and ensure visible wins are directly tied to his needs. Co-author the "active user" definition with him so he owns it, rather than having it imposed on him.
 
---
 
### Stakeholder 3: Backend Engineer, Sara Kim
 
- **Why they matter:** She is the sole guardian of the production PostgreSQL database — the only current source of truth. Without her cooperation, there is no path to a read replica or warehouse integration. If the relationship sours, she could (reasonably) block data access requests, creating a critical bottleneck. She also holds institutional knowledge of the schema that no documentation currently captures.
- **Current state of the relationship:** Unknown / cautious. She has raised legitimate concerns about production DB queries causing user-facing latency and has not had time to address them. She is likely relieved that a data person has been hired but protective of her time and infrastructure.
- **Their goals:** She is measured on API reliability, system uptime, and shipping backend features. Her primary goal is that nothing the analytics function does degrades production performance or adds to her on-call burden.
- **Potential friction points:** Any request that requires her time — setting up a read replica, granting warehouse access, explaining schema — competes directly with her existing workload. If early data requests feel like they are adding to her plate, she will disengage.
- **Your strategy (first 30 days):** Open the relationship with a single, specific, low-effort ask: a 30-minute schema walkthrough, pre-scheduled with a written agenda so she can prepare efficiently. Frame all subsequent requests around reducing her burden (e.g., "once the warehouse is set up, no one will ever need to touch production for analytics again"). Never send an unplanned Slack asking for database help.
 
---

---

## Communication Plan

*How often and through what channels will you communicate with each quadrant?*

| Quadrant | Frequency | Channel | Content | Owner |
|---|---|---|---|---|
| **Manage Closely** (CEO, Head of Product) | Weekly | 1:1 meeting (30 min) + Slack DM for async | Progress vs. 90-day plan; active analyses; decisions needed; blockers; Series A metric status | Head of Data |
| **Keep Satisfied** (Backend Engineer, VC Investors) | Monthly (Engineer); per fundraise milestone (Investors) | Async Slack for Engineer; packaged data room via CEO for Investors | For Engineer: upcoming data requests with lead time, confirmation of zero production impact. For Investors: clean metrics package, no raw data or methodology details | Head of Data |
| **Keep Informed** (Mobile Devs, Marketing Contractor) | Bi-weekly | Shared spec doc + Slack channel #data-taxonomy; bi-weekly review session | New or updated event specs; tracking requirements for upcoming features; UTM/attribution tagging reminders for Marketing | Head of Data |
| **Monitor** (Designer, Support Team) | Monthly | All-hands metrics review (45 min) | Single source-of-truth dashboard walkthrough; top product insights; open Q&A | Head of Data |
 

---

## Evaluation Criteria

Use these dimensions to self-assess the quality of your Stakeholder Map. For official grading criteria, see `assessment/grading-rubrics.md` (Manager OS component, 15%).

| Criterion | Weight | What "Good" Looks Like |
|---|---|---|
| **Completeness** | 25% | At least 6 stakeholders identified, covering multiple functions (not just Product). Includes non-obvious stakeholders (IT, Legal, Finance, etc.). |
| **Accuracy of power/interest assessment** | 20% | Power and interest levels are realistic for the case context. A startup CEO is high power; a junior PM is not. Assessments are justified. |
| **Quality of needs analysis** | 20% | "What they need from you" and "What you need from them" are specific and actionable, not vague. |
| **Engagement strategy specificity** | 20% | Strategies include concrete actions (frequency, channel, content), not just "build relationship." |
| **Key relationship depth** | 15% | Top 3 stakeholder analyses show genuine strategic thinking — friction points, personal goals, specific 30-day actions. |

**Note:** This is a draft artifact. You will refine it throughout the course and submit a polished version in your Manager Portfolio. The draft is assessed on completeness and thoughtfulness, not perfection.
