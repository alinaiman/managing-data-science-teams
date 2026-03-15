---
marp: true
theme: ceu-analytics
paginate: true
header: "ECBS5256 – Managing Data Science Teams"
footer: "CEU Vienna | Day 1 – Block C"
---

# Roadmaps, Bets, and Alignment

**Block C — 15:30-17:10 (100 minutes)**

**Learning Outcomes:**
- Build a 12-month roadmap tied to business outcomes
- Write a 2-page executive narrative
- Stress-test plans through structured red-team critique

<!-- Talk track: Welcome to the last block of Day 1. You have your Manager OS and your hiring plan. Now we answer the question every executive asks: where is this team going, and why should I fund it? By the end of this block you will have a roadmap, the start of an executive narrative, and you will have survived your first red-team exercise. We also have a hard stop at 17:10 for the Day 1 Checkpoint submission. -->

---

## The Roadmap Problem

Why are roadmaps in analytics **uniquely hard**?

You are not building features. You are building **capability and trust**.

- Stakeholders don't really understand what analytics teams do day to day
- Leadership asks **"What have you shipped?"** and you need a better answer than "dashboards"

<!-- Talk track: Before we get into frameworks, let's talk about why roadmaps for analytics teams are a fundamentally different beast than roadmaps for product or engineering teams. A product team ships features that users can see and click on. An engineering team ships infrastructure that other teams depend on. But an analytics team? Your best work is often invisible. When leadership asks what have you shipped, saying dashboards is the analytics equivalent of an engineer saying I wrote code. It is technically true and completely useless. -->

---

## The Roadmap Problem

Your most impactful work is often invisible — the analysis that prevented a bad decision, the data quality fix that stopped a silent failure, the model that redirected $5M in spend.

**The roadmap is your tool for making the invisible visible.**

Without one, you are at the mercy of whoever yells loudest.

<!-- Talk track: The analysis that prevented a bad product launch — nobody sees the launches that did not happen. The data quality fix that stopped a silent revenue leak — nobody thanks you for a problem they never knew existed. The roadmap is your translation layer. It takes the work your team does and makes it legible to people who do not understand what analytics teams do. Without a roadmap, you are at the mercy of whoever yells loudest. -->

---

## What Good Analytics Roadmaps Do

A good analytics roadmap is not a wish list. It is a **strategic tool**:

1. **Translate technical work into business language** — "We built a churn model" becomes "We identified $3.2M in at-risk revenue"

2. **Protect your team from drive-by requests** — Point to the roadmap and ask "Which priority should we pause?"

<!-- Talk track: A good roadmap does four things. First, it translates your technical work into language your CFO can understand. Nobody outside your team cares that you improved model AUC by twelve points. They care that you identified three million dollars in at-risk revenue. Second, it protects your team. Every analytics team gets bombarded with drive-by requests — someone from marketing who just needs a quick pull, a product manager who needs a dashboard by Friday. Without a roadmap, every request is equally urgent. With a roadmap, you have a framework for saying here is what we are working on, which of these should we pause to do your request? -->

---

## What Good Analytics Roadmaps Do

3. **Create mutual accountability** — You deliver outcomes; stakeholders provide data access, expertise, and executive air cover

4. **Force explicit trade-offs** — Instead of trying to do everything and doing nothing well, you make visible choices

<!-- Talk track: Third, accountability goes both ways. You commit to delivering outcomes, and your stakeholders commit to giving you what you need — data access, domain expertise, executive support. And fourth, it forces you to make trade-offs explicitly instead of implicitly. Implicit trade-offs mean your team burns out trying to do everything. Explicit trade-offs mean leadership understands what they are getting and what they are not. -->

---

## Block C Roadmap

**What we'll build in the next 100 minutes:**

| Component | What It Is |
|-----------|-----------|
| **North Star + Guardrails** | Metrics that define success and boundaries |
| **RICE-scored initiatives** | A prioritized backlog of analytics bets |

<!-- Talk track: Here is what we are building in this block. First, you will define a North Star metric and guardrails for your analytics team — the metrics that orient everything you do. Then you will brainstorm and RICE-score at least eight initiatives, giving you a prioritized list of bets. -->

---

## Block C Roadmap

| Component | What It Is |
|-----------|-----------|
| **Now / Next / Later roadmap** | A 12-month plan without false precision |
| **Executive narrative** | The document your VP forwards to the C-suite |
| **Red-team critique** | Stress-testing your plan before a real executive does |

<!-- Talk track: You will place those into a Now, Next, Later roadmap structure. You will write the first page of a two-page executive narrative — the kind of document that gets forwarded to the C-suite. And finally, you will pair up with someone and try to destroy each other's roadmaps in a red-team exercise. -->

---

## Block C Roadmap

You will leave with **a draft roadmap and an executive narrative** — artifacts you present in Day 2's QBR simulation.

<!-- Talk track: Everything you build here feeds directly into the Day 2 QBR simulation in Block F, where you will present your roadmap to a mock executive panel. So treat this as a real draft, not a classroom exercise. -->

---

## Roadmaps Are Not Gantt Charts

A roadmap is a **communication tool**, not a project plan.

It answers: **"Where are we going and why?"**
It does NOT answer: "What's the exact timeline?"

> The map is not the territory. — Alfred Korzybski

A Gantt chart is a promise. A roadmap is a **bet register**.

<!-- Talk track: The single biggest mistake new analytics managers make is treating the roadmap like a project plan. A Gantt chart says we will deliver feature X on March 15th. A roadmap says we believe investing in churn modeling this quarter will reduce monthly churn by two percentage points, and here is why we believe that. If your roadmap has specific dates on it, you have built a Gantt chart and you will be held to those dates. Roadmaps communicate direction, priorities, and trade-offs. They are living documents that change as you learn. -->

---

## The Gantt Chart Trap

Your VP of Marketing asks for a churn prediction model. You put it on your Gantt chart: **deliver by March 15**.

- **February:** The data is messier than expected — key event tables are missing mobile data.
- **March 1:** You tell Marketing it will slip two weeks. They already scheduled campaigns around March 15.

<!-- Talk track: Let me tell you what happens when analytics teams make Gantt chart promises. Your VP of Marketing wants a churn model. You say March 15 because that is what the project plan says. But analytics work has inherent uncertainty — you do not know what you will find in the data until you look. The event tables are missing mobile data. Now you are two weeks late, and Marketing has already planned campaigns around your date. -->

---

## The Gantt Chart Trap

- **April 1:** The model ships. It is good work. But Marketing already hired an outside consultant because they lost confidence in your timeline.

**What went wrong?** You made a date-based commitment for work with **inherent uncertainty**.

<!-- Talk track: By the time you actually deliver in April, they have lost confidence and hired a consultant. Nobody wins. You made a date-based commitment for work with inherent uncertainty. This is the Gantt chart trap — making precise promises about work that is fundamentally unpredictable. -->

---

## The Roadmap Alternative

**Instead of the Gantt chart promise, say this:**

> "Churn modeling is our top priority this quarter. We expect to deliver within Q1. Biggest risk is data completeness."

When the timeline shifts, you are **updating an estimate**, not **breaking a promise**.

Executives can handle uncertainty. What they cannot handle is being surprised.

<!-- Talk track: Now contrast the Gantt chart approach with a roadmap-style commitment. Churn modeling is our top priority this quarter. We expect to deliver within Q1. Biggest risk is data completeness. This is honest. When the timeline shifts, you are updating an estimate, not breaking a promise. The trust dynamics are completely different. Executives can handle uncertainty. What they cannot handle is being surprised. -->

---

## The Analytics Roadmap Structure

## Now / Next / Later

| Horizon | Timeframe | Commitment |
|---------|-----------|------------|
| **Now** | This quarter | Committed — actively staffed |
| **Next** | Next quarter | Planned — scoped but flexible |
| **Later** | 6-12 months | Exploratory — directional only |

<!-- Talk track: The three-horizon model is the simplest roadmap structure that actually works. The Now column is what your team is actively building this quarter. These items are committed and staffed. The Next column is what you plan to do next quarter, scoped enough that you could start tomorrow if priorities shifted. The Later column is directional — it shows where you think the team is heading, but the details are intentionally vague. -->

---

## Horizons: Examples

| Horizon | Example |
|---------|---------|
| **Now** | Churn prediction model v1 |
| **Next** | Self-serve experimentation platform |
| **Later** | Real-time personalization engine |

Commitment decreases from Now to Later. This protects you from the Gantt chart trap.

<!-- Talk track: The key insight is that commitment level decreases as you move from Now to Later. You are making strong promises about Now, tentative plans for Next, and directional bets for Later. This is honest and it protects you from the Gantt chart trap we just discussed. -->

---

## What Each Roadmap Item Needs

**Every item on your roadmap must answer these questions:**

- **What it is** — a clear, jargon-free description
- **Why it matters to the business** (not to your team) — connect it to revenue, retention, risk, or strategic advantage

<!-- Talk track: Each item on your roadmap must answer the question a VP would ask: why does this matter to the business? If you cannot articulate that, the item does not belong on the roadmap. Notice I said why it matters to the business, not why it matters to your team. Building a feature store is exciting for your data scientists, but your VP does not care about feature stores. They care that a feature store reduces model development time from six weeks to two, which means you can respond to business needs three times faster. -->

---

## What Each Roadmap Item Needs

- **Rough size** (T-shirt: S/M/L/XL) — enough to understand trade-offs, not enough to be held to a date
- **Key dependencies** — what has to be true for this to succeed

**The test:** Can a VP read this item and understand why it matters without asking a follow-up question?

If the answer is no, rewrite it.

<!-- Talk track: The T-shirt sizing is intentional. S, M, L, XL gives enough information to understand trade-offs without creating the illusion of precision. And dependencies are critical — if your churn model depends on the data engineering team completing a pipeline migration, that needs to be on the roadmap so everyone can see it. The VP test is simple: can someone two levels above you read this item and understand why it matters without asking a follow-up question? If not, rewrite it until they can. -->

---

## RICE Prioritization

**A framework for comparing unlike things**

| Factor | Question | Scale |
|--------|----------|-------|
| **R**each | How many people/decisions affected? | # per quarter |
| **I**mpact | How much does it move the metric? | 0.25 / 0.5 / 1 / 2 / 3 |

<!-- Talk track: RICE comes from Intercom and it is the most practical prioritization framework I have found for analytics teams. Reach is how many people, decisions, or dollars are affected. Impact is how much it moves the needle — use the scale, do not make up your own. -->

---

## RICE Prioritization

| Factor | Question | Scale |
|--------|----------|-------|
| **C**onfidence | How sure are we about R, I, and E? | 100% / 80% / 50% |
| **E**ffort | How many person-months + compute costs? | Person-months (adjusted) |

$$\text{RICE Score} = \frac{R \times I \times C}{E}$$

**Note:** Effort is not just human time. GPU-intensive model training, LLM API costs, and cloud compute can dwarf labor costs at scale.

<!-- Talk track: Confidence is your honest assessment of how sure you are about the other estimates. And Effort is person-months of work. You divide the top by the bottom and get a score. The formula is simple, but the real value is in the conversation it forces. When you sit down to score Reach for an initiative and you realize you have no idea how many people it affects, that tells you something important — you need to do more discovery before you commit. One important nuance on Effort: it is not just human time anymore. If your churn model retraining costs fifteen thousand dollars a month in GPU compute, that is part of the Effort score. A GPU-intensive initiative may score very differently than a dashboard build even if both require the same person-months. Factor in compute costs, especially for ML-heavy or LLM-powered initiatives. -->

---

## RICE as a Conversation Starter

RICE is a **conversation starter**, not a calculator.

- If Project A scores higher but your gut disagrees — **explore that disagreement**
- Is your gut wrong, or is the scoring missing something?
- RICE makes hidden assumptions **explicit** and **debatable**

The score does not make the decision. **You** make the decision.

<!-- Talk track: Here is the important thing about RICE: the score is not the answer. The score is the starting point for a conversation. If the model says project A scores higher than project B but your gut says otherwise, that disagreement is the most valuable part of the exercise. Dig into it. Maybe your gut is picking up on a dependency the score does not capture. Maybe your confidence estimate is too generous. The point is not to let a formula make your decisions. The point is to make your reasoning visible so other people can challenge it. -->

---

## RICE in Practice

**Four initiatives scored head-to-head:**

| Initiative | Reach | Impact | Confidence | Effort | Score |
|-----------|-------|--------|------------|--------|-------|
| Churn Model v1 | 5,000 users/qtr | 2 (high) | 80% | 3 PM | **2,667** |
| Self-Serve Dashboard | 200 decisions/qtr | 1 (med) | 100% | 2 PM | **100** |

<!-- Talk track: Let us work through a real example. Four initiatives, scored with RICE. The Churn Model reaches five thousand users per quarter, has high impact, eighty percent confidence, and takes three person-months. Score: twenty-six sixty-seven. The Self-Serve Dashboard reaches two hundred decisions, medium impact, full confidence, two person-months. Score: one hundred. -->

---

## RICE in Practice

| Initiative | Reach | Impact | Confidence | Effort | Score |
|-----------|-------|--------|------------|--------|-------|
| Experimentation Platform | 10,000/qtr | 3 (massive) | 50% | 6 PM | **2,500** |
| Data Quality Audit | 50,000/qtr | 0.5 (low) | 100% | 1 PM | **25,000** |

**The Data Quality Audit wins?** Unsexy work scores highest — it touches everything and is cheap.

<!-- Talk track: The Experimentation Platform has massive reach and impact but only fifty percent confidence and six person-months of effort. Score: twenty-five hundred. And then the Data Quality Audit — it affects fifty thousand rows of data that feed every downstream analysis, low impact per row but full confidence and only one person-month. Score: twenty-five thousand. That is a surprising result. The unsexy data quality work scores highest because it touches everything and is cheap. This is RICE working as intended — it challenges your assumptions. -->

---

## RICE in Practice: Sensitivity

**Drop Experimentation Platform confidence to 30%:** score falls from 2,500 to **1,500**. Does that change your Q1 plan?

RICE tells you **where to argue**, not what to decide.

<!-- Talk track: Now watch what happens when you adjust confidence on the Experimentation Platform from fifty to thirty percent. The score drops from twenty-five hundred to fifteen hundred. Does that change your Q1 plan? These are the conversations RICE is designed to provoke. RICE tells you where to argue, not what to decide. -->

---

## North Star Metric

The ONE number that captures your team's value to the business.

```
  NORTH STAR
  ┌───┼───┐
  G1  G2  G3
```

**G1, G2, G3** = Guardrails that constrain how you pursue it.

<!-- Talk track: Every analytics team needs a North Star metric — the single number that best captures the value you deliver to the business. For a growth analytics team, it might be monthly active paying users. For a risk analytics team, it might be loss rate. The North Star gives your team focus. Below the North Star sit your guardrails. These are the metrics that must not get worse while you pursue your North Star. -->

---

## Guardrails Protect the North Star

**Guardrails** are the metrics that must NOT get worse while you optimize the North Star.

Think of it like driving — the North Star is your destination, and the guardrails keep you from going off a cliff.

Optimizing one metric without constraints is dangerous.

<!-- Talk track: But optimizing one metric without constraints is dangerous. That is what guardrails are for. These are the metrics that must not get worse while you chase the North Star. If your North Star is revenue per user, your guardrails might be user satisfaction, data quality SLA adherence, and model fairness metrics. -->

---

## Guardrails Protect the North Star

**Example — Growth Analytics Team:**
- **North Star:** Monthly Active Paying Users
- **Guardrails:** User satisfaction score, data quality SLA, model fairness metrics

Guardrails prevent you from gaming your own North Star.

<!-- Talk track: You do not want to increase revenue per user by recommending exploitative products or by letting your data pipelines fall apart. Without guardrails, you optimize yourself into a corner. The guardrails are your check on unintended consequences. -->

---

## North Star, Guardrails, and Input Metrics

**North Star:** The one metric that best captures the value your team delivers.
**Guardrails:** Things that must NOT get worse while you optimize the North Star.
**Input metrics:** Things you can directly influence through your team's work.

<!-- Talk track: Let me make these concrete. Your North Star is the one number your team rallies around. Your guardrails are the constraints — the things that must not get worse while you pursue that star. Input metrics are the levers your team can actually pull. -->

---

## North Star, Guardrails, and Input Metrics

**Example — Growth Analytics Team:**
- **North Star:** Monthly Active Paying Users
- **Guardrails:** User satisfaction, data quality SLA, model fairness
- **Input Metrics:** Activation rate, 30-day retention, reactivation rate

Without input metrics, you have a North Star you cannot steer toward.

<!-- Talk track: You probably cannot directly move Monthly Active Paying Users, but you can influence activation rate and retention rate through your analyses and models. The input metrics are where your team's daily work connects to the North Star. Without guardrails you optimize yourself into a corner. Without input metrics you have a North Star you cannot steer toward. -->

---

## Choosing Your North Star: Common Mistakes

- **Vanity metric** — "Number of dashboards created" feels productive but drives no business outcome
- **Uninfluenceable metric** — "Total company revenue" is important but your 4-person team cannot move it

<!-- Talk track: Picking the right North Star is harder than it sounds. I see four common mistakes. First, vanity metrics — number of dashboards created, number of ad hoc requests completed. These feel productive but they do not drive business outcomes. Nobody got promoted because their team made a lot of dashboards. Second, picking something you cannot influence. Total company revenue is important but if you have a four-person analytics team, you are not moving that needle by yourself. -->

---

## Choosing Your North Star: Common Mistakes

- **Slow-moving metric** — "Annual customer lifetime value" takes 12 months to know if you moved it
- **Unmeasurable metric** — "Quality of analytical insights" sounds great but how do you track it?

<!-- Talk track: Third, slow-moving metrics. If it takes twelve months to know whether your work made a difference, you cannot use it to steer your team's priorities. And fourth, unmeasurable metrics. Quality of analytical insights sounds great in a mission statement but how do you actually track it quarter over quarter? -->

---

## The North Star Test

Ask three questions:

1. **Can your team directly influence it?** If not, it is someone else's North Star.
2. **Does it move when you do good work?** If not, wrong metric.
3. **Does leadership care about it?** If your VP's eyes glaze over, pick a different one.

If you answer yes to all three, you have your North Star.

<!-- Talk track: The test is simple. Three questions. Can your team directly influence it? Does it move when you do good work? Does leadership care about it? If the answer to all three is yes, you have found your North Star. If any answer is no, keep looking. Do not settle for a metric that fails even one of these tests — it will steer your team in the wrong direction for an entire quarter before you realize the problem. -->

---

## The Metrics Tree

```
Revenue Growth
      │
Active Paying Users
   ╱       ╲
Activation  Retention
```

**Draw yours.** Start from the business outcome and work down.

<!-- Talk track: The metrics tree is the bridge between your team's daily work and the number the CEO reports to the board. Start at the top with the business outcome your executive sponsor cares about most. Then identify your North Star. Break that into input metrics, the levers your team can actually pull. -->

---
<!-- _class: skip -->

## The Metrics Tree

```
Activation         Retention
    │                  │
Onboarding         Churn modeling,
funnel analysis    cohort analysis
```

The tree answers: **"How does my work connect to the board number?"**

<!-- Talk track: At the bottom, list the specific activities that move those input metrics. When a stakeholder asks why you are spending three weeks on churn modeling, you point to the tree. If you cannot draw this tree, your roadmap is disconnected from the business. -->

---
<!-- _class: skip -->

## Communicating Trade-offs

## Frame as choices, not complaints

| Instead of... | Say... |
|---------------|--------|
| "We don't have enough resources" | "We can do A or B this quarter — which creates more value?" |

<!-- Talk track: One of the hardest skills for a new analytics manager is communicating trade-offs without sounding like you are complaining or saying no. The key is framing. Never say we do not have enough resources. Instead, present a choice: we can do A or B this quarter, which one creates more value for the business? This reframes you from a bottleneck into a strategic partner. -->

---
<!-- _class: cut -->

## Communicating Trade-offs

| Instead of... | Say... |
|---------------|--------|
| "That's not possible" | "Here's what it would cost: 6 weeks and we'd pause the churn model" |
| "The data isn't ready" | "We need 3 weeks of instrumentation before we can answer that reliably" |

Practice these rephrases until they become automatic.

<!-- Talk track: Every time you say we cannot do that, you lose credibility. Every time you say here is what it would cost, you gain it. The data is not ready becomes we need three weeks of instrumentation before we can answer that question reliably. Notice how every reframe turns a wall into a door. Practice these rephrases until they become automatic. -->

---
<!-- _class: cut -->

## The Cost of Delay

> "Every week we delay the experimentation platform costs us approximately $40K in unoptimized conversion — here's the math."

Quantify the cost of waiting. When you can put a dollar figure on delay, executives will prioritize for you.

<!-- Talk track: The cost of delay is your most powerful tool for communicating trade-offs. If you can quantify what it costs the business to wait another week on a project, executives will prioritize for you. You do not need exact numbers. A reasonable estimate is infinitely better than no estimate. Every week we delay the experimentation platform costs us approximately forty thousand dollars in unoptimized conversion — here is the math. That sentence will get more executive attention than any status update you have ever written. -->

---
<!-- _class: cut -->

## Partners, Not Opponents

Product and Eng are your **partners**, not your opponents.

Approach every trade-off conversation as a **joint problem-solving exercise**, not a negotiation.

You are all trying to move the same business metrics.

<!-- Talk track: And remember: Product and Engineering are your partners. I cannot stress this enough. The moment you start thinking of trade-off conversations as us versus them, you have already lost. You are all trying to move the same business metrics. Approach every conversation as a joint problem-solving exercise. Here is what we are facing. Here are the options. What should we do together? -->

---
<!-- _class: cut -->

## The Trade-off Conversation: Setup

**Scenario:** Your team is building a churn model (top Q1 priority). The VP of Product walks in: "We need a dashboard for the new feature launch this week."

**The wrong way:**
> "We don't have bandwidth right now."

*Why this fails:* The VP hears "no" and goes around you.

<!-- Talk track: Let me script out how this actually sounds in practice. Your VP of Product shows up wanting a dashboard for a feature launch. This happens every week in every analytics team. The wrong way is to say we do not have bandwidth. That is a wall. The VP hears no, gets frustrated, and either goes around you or escalates to your boss. Either way, you lose. -->

---
<!-- _class: skip -->

## The Trade-off Conversation: The Right Way

> "Absolutely — let me show you what that would involve. Right now my team is committed to the churn model, which Sarah in Marketing is counting on for Q2. We have three options:
> 1. **Pause churn model for 1 week** — dashboard this week, churn model slips to mid-April.
> 2. **Quick version now, full version later** — I can set up a basic Looker view today. It covers 80% of what you need.

<!-- Talk track: The right way starts with absolutely, which is a yes. Then you lay out the current commitment, name the stakeholder who is depending on it, and present concrete options with real costs. The first option is full pause — dashboard this week but churn model slips. The second option is a quick-and-dirty version that covers eighty percent of the need. -->

---
<!-- _class: skip -->

## The Trade-off Conversation: The Right Way

> 3. **Next sprint** — We finish churn model on schedule and start the dashboard March 24.
>
> Which of these works best for your launch timeline?"

*Why this works:* You said yes, presented costs, and made it their choice.

<!-- Talk track: The third option is next sprint — on schedule for both but the dashboard waits. Notice what you did. You never said no. You made the trade-off visible. You made it their decision, not yours. Nine times out of ten, the VP picks option two or three. And now you are a strategic partner, not a bottleneck. Practice this pattern until it is muscle memory. -->

---
<!-- _class: skip -->

## The 2-Page Executive Narrative

## Structure

1. **Context** — Where we are (team, state, environment)
2. **What We Did** — Key wins and metrics moved
3. **What We Learned** — Insights and surprises

<!-- Talk track: The two-page executive narrative is the single most important document an analytics manager writes. It is not a status update. It is not a dashboard. It is a story about where your team is, what you have accomplished, what you have learned, and where you are going. -->

---

## The 2-Page Executive Narrative

4. **What's Next** — Priorities and bets for next quarter
5. **What We Need** — Asks and blockers

**Written in prose, not bullet points.**

> Executives read narratives; teams read dashboards.

This is the document that gets forwarded to the CEO's CEO.

<!-- Talk track: It is written in prose because prose forces clarity of thought. Bullet points let you hide behind vague statements. When you write in complete sentences, you have to actually think about what you are saying. This is the document that your VP forwards to the C-suite. It is the document that gets read in the board meeting prep. Every word matters. -->

---

## Executive Narrative: Context

**A condensed example for a fictional analytics team at MarketBridge:**

**Context:** "The Analytics team (5 ICs, 1 manager) supports MarketBridge's two-sided marketplace connecting homeowners with service professionals across 12 metro areas. This quarter we operated at full capacity following the successful onboarding of two analysts hired in Q3."

*What makes this work: concrete numbers, no jargon, establishes scope in three sentences.*

<!-- Talk track: Let me show you what each section looks like when it is done well. This is a condensed example for a fictional analytics team at MarketBridge, the two-sided marketplace. Look at the Context section — three sentences, and you know the team size, what they support, and where they stand. No jargon. -->

---

## Executive Narrative: Results

**What We Did:** "We reduced 60-day logo churn from 8.2% to 6.1% by deploying a propensity model that flags at-risk accounts 30 days before renewal. Customer Success now reviews the top 50 at-risk accounts weekly — 34 of 41 flagged accounts renewed."

*What makes this work: one clear outcome, quantified before and after, shows who uses it and how.*

<!-- Talk track: The What We Did section has one clear outcome with before and after numbers, and it shows who actually uses the work. Customer Success reviews the top fifty at-risk accounts weekly — that shows your work is integrated into a real business process, not sitting on a shelf. -->

---

## Executive Narrative: Insights

**What We Learned:** "Our biggest surprise was that product usage intensity is a weaker churn predictor than support ticket sentiment. Accounts that file frustrated tickets — even if they use the product daily — churn at 3x the rate."

*What makes this work: a genuine insight that changes how leadership thinks about the business.*

<!-- Talk track: The What We Learned section is where most narratives fall flat. People write platitudes. This example shares a genuine surprise — product usage intensity is a weaker churn predictor than support ticket sentiment. That is the kind of insight that makes a VP lean forward. -->

---

## Executive Narrative: Plans

**What's Next:** "In Q2, we are investing in self-serve reporting for the Sales team. Currently, 40% of our ad hoc requests come from Sales asking the same five questions. Automating this frees ~1.5 analyst-months per quarter."

*What makes this work: clear priority, quantified opportunity cost, explains the why.*

<!-- Talk track: The What is Next section explains the priority, quantifies the opportunity cost in analyst-months, and explains why this is the highest-leverage investment. Every section earns the reader's attention by being specific, quantified, and connected to business outcomes. -->

---

## Executive Narrative: Asks

**What We Need:** "We need Engineering to prioritize the event schema migration by April 15. Without it, our experimentation platform — the top Q3 initiative — cannot reliably track treatment assignment."

*What makes this work: specific ask, specific date, explains the consequence of not getting it.*

<!-- Talk track: And What We Need is a specific, dated ask with a clear consequence. Not we need more resources, but we need the event schema migration by April fifteenth or our Q3 initiative is blocked. Notice the pattern: specific, quantified, and connected to business outcomes. -->

---

## Writing for Executives: BLUF

## Bottom Line Up Front

**Lead with the answer. Then provide the evidence.**

> **Bad:** "Our team conducted extensive analysis of user behavior patterns across multiple segments..."

> **Good:** "We reduced 30-day churn by 18%, saving $2.1M. Here's how."

<!-- Talk track: BLUF — Bottom Line Up Front — is a military communication concept that every analytics manager should internalize. Executives do not have time to read through your methodology to find the conclusion buried on page two. The bad example buries the lead under a pile of process description. The good example takes six seconds to read and communicates the most important information immediately. That is respect for your reader's time. -->

---

## Rules for Executive Writing

### Four rules that will make your writing 10x more effective:

1. **No jargon.** "We improved model AUC by 0.12" means nothing to a CFO. Say: "Our model now correctly identifies 85% of at-risk accounts, up from 73%."

2. **Quantify everything.** Dollars, percentages, users affected. "Significant improvement" is not a number.

<!-- Talk track: Four rules. No jargon means no jargon. If you write AUC or p-value in an executive narrative, you have failed. Translate everything into business language: dollars, users, time, risk. Quantify everything — significant improvement is not a number, and executives know it. They will assume you are hiding behind vague language because the real numbers are not impressive. -->

---

## Rules for Executive Writing

3. **One page = one main idea.** If you need more space, you need fewer ideas per page.

4. **Write for the person who has 3 minutes and 47 unread emails.** Every sentence must earn its place.

<!-- Talk track: One page, one main idea. If you are cramming three ideas onto one page, split them up or cut the weakest one. And remember who your reader is — someone with three minutes between meetings and forty-seven unread emails. Every sentence must earn its place on the page. Read each sentence and ask: does this change what my reader thinks or does? If not, delete it. -->

---

## Risk Registers

Every roadmap has risks. **Acknowledging them is not weakness — it is honest planning.**

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Key data engineer leaves | Medium | High | Cross-train, document pipelines |
| Privacy regulation change | Low | High | Monthly legal sync, flexible architecture |

<!-- Talk track: Every roadmap has risks, and the worst thing you can do is pretend they do not exist. A risk register is a simple table that forces you to name what could go wrong, assess how likely it is and how bad it would be, and document what you are doing about it. -->

---

## Risk Registers

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Stakeholder priority shift | High | Medium | Quarterly roadmap reviews with VP |

Your top 3 risks should be on slide 2 of every executive presentation.

Executives trust leaders who name risks before they become surprises.

<!-- Talk track: Your top three risks should appear on the second slide of every executive presentation — right after the summary, before the details. Why? Because executives trust leaders who name risks early. It shows you have thought about what could go wrong and you have a plan. Risks are not weaknesses. They are signs that you are planning honestly. An executive who is surprised by a risk will lose trust in you. An executive who was warned about a risk three months ago will respect your judgment. -->

---

## Activity: 12-Month Roadmap
## 30 minutes

**Build a 12-month roadmap for your case context.**

1. Define your **North Star metric** and **3 guardrail metrics**
2. Brainstorm at least **8 initiatives**
3. **RICE score** each initiative

<!-- Talk track: This is the big activity for this block. You have 30 minutes to build a 12-month roadmap for your case context. Start by defining your North Star metric — what is the one number that best captures the value your team delivers? Then identify three guardrails. Next, brainstorm at least eight initiatives. Do not self-censor — get them all on paper first. Then RICE score each one. -->

---

## Activity: 12-Month Roadmap

4. Place initiatives in **Now / Next / Later** based on scores and dependencies
5. Identify **top 3 dependencies** that could block your plan

**Use the `roadmap-rice.md` template.** Work individually, but talk to case-context peers if stuck.

<!-- Talk track: Finally, place them into Now, Next, and Later columns. Use the template I have provided. Work individually, but if you are stuck on what initiatives make sense for your case context, talk to the people at your table who chose the same context. I will be circulating to help. -->

---

## Activity: Executive Narrative Draft
## 20 minutes

**Write the first page of your 2-page executive narrative.**

Focus on two sections:
1. **Context** — Team size, capabilities, business environment, key constraints.
2. **What's Next** — Top 3 priorities for next quarter and why they matter.

<!-- Talk track: Now take 20 minutes to write the first page of your executive narrative. Focus on Context and What is Next. Write in complete sentences — I know bullet points are tempting, but resist. Imagine your reader is two levels above you. -->

---

## Activity: Executive Narrative Draft

**Use the `exec-narrative.md` template.**

Write in **complete sentences**. No bullet points.
Imagine your reader is your VP's VP.

Do not try to make it perfect — get the structure and the key messages right.

<!-- Talk track: They do not know the details of your team's daily work. They need to understand where you are and where you are going in about 90 seconds of reading. This draft will become part of your portfolio, and you will refine it further before the Day 2 QBR simulation. Do not try to make it perfect. Polish comes later. -->

---

## Red-Team: Kill the Project
## 8 minutes

**Pair up with someone from a DIFFERENT case context.**

Your job: **find the fatal flaw** in their roadmap.

<!-- Talk track: This is my favorite exercise of the day. Pair up with someone who chose a different case context than yours. You have 8 minutes total — 4 minutes each direction. Your job is to find the fatal flaw in their roadmap. -->

---

## Red-Team: Kill the Project

Ask these questions:
- "What assumption, if wrong, kills this plan?"
- "What is the biggest risk you haven't identified?"
- "Which initiative has the lowest confidence — why is it there?"
- "If you lose one headcount, what falls apart?"

<!-- Talk track: Ask the hard questions: what assumption, if wrong, kills this plan? What is the biggest risk they have not identified? If they lose one headcount, what breaks? Be constructive but do not pull your punches. The best feedback is specific and actionable. Do not just say the roadmap is unrealistic — say which initiative is unrealistic and why. This exercise simulates what will happen when you present your roadmap to your VP. Better to find the flaws now than in that meeting. -->

---

## Red-Team Debrief

**What survived? What didn't?**

- Which assumptions were most vulnerable?
- What risks did your partner identify that you missed?
- How did a different perspective change your thinking?

> "The best roadmaps get stronger through criticism."

<!-- Talk track: Let us debrief. Raise your hand if your partner found a flaw you had not considered. Good — that is the point. The best roadmaps are not the ones that survive criticism unchanged. They are the ones that get stronger through criticism. -->

---

## Red-Team Debrief

**Note what the red-team revealed** — update your roadmap and risk register after class.

Jot down at least one new risk or one initiative to modify before you forget.

<!-- Talk track: Before we move on, take thirty seconds to jot down the key insight from your red-team partner. What risk did they surface? What initiative needs rethinking? Write it down now so you don't lose it. You'll update your roadmap and risk register after class — this is exactly what happens in real quarterly planning. You present your plan, smart people poke holes in it, and you make it better. -->

---

## Day 1 Checkpoint

## Due by 17:10 — HARD DEADLINE

**Submit three artifacts (drafts — completeness, not polish):**

1. **Team Charter** (Block A)
2. **Stakeholder Map** (Block A)
3. **Roadmap Outline** with RICE scoring (Block C)

<!-- Talk track: Here is your hard deadline for today. By 17:10 — that is when this block ends — you need to submit three artifacts to the LMS. Your Team Charter from Block A, your Stakeholder Map from Block A, and your Roadmap Outline with RICE scoring from this block. These are all drafts. I am grading on completeness, not polish. -->

---

## Day 1 Checkpoint

**This is 10% of your grade — pass/fail on completeness.**

Upload to the LMS before you leave.
Missing sections are okay. Empty templates are not.

<!-- Talk track: If a section is rough, that is fine. If a section is empty, that is not fine. This checkpoint is worth 10 percent of your grade and it is pass-fail. Upload all three documents before you leave the room. If you are having technical issues with the LMS, email them to me directly before 17:10. -->

---

## What's Coming on Day 2

**Monday, March 23**

| Block | Topic | Activity |
|-------|-------|----------|
| **D** (11:00) | Growth & Performance | PGP + calibration |
| **E** (13:30) | Portfolio Workshop & Peer Review | Revise artifacts + peer feedback |
| **F** (15:30) | QBR Simulation | Present roadmap |

<!-- Talk track: Here is what is coming on Day 2 next Monday. Block D covers growth and performance — you will draft a personal growth plan and a calibration-ready performance summary. Block E is a portfolio workshop — you will revise your weakest artifact, give and receive structured peer feedback, and prepare for the QBR simulation. And Block F is the big one — the QBR simulation. You will present your roadmap and executive narrative to a mock executive panel, and they will ask you hard questions. -->

---

## What's Coming on Day 2

### Before Day 2:
- **Continue your hiring packet** — work sample design and interview loop (portfolio deliverables)
- **Read the QBR simulation brief** (posted on LMS tonight)
- Review your roadmap — Day 2 Block F uses it

<!-- Talk track: Before Day 2, you have homework. Continue building out your hiring packet — the work sample and interview loop build on the JD and rubric you drafted today. These are portfolio deliverables, so take your time and do them well. Also read the QBR simulation brief, which I will post on the LMS tonight. And review your roadmap — you will be presenting it. -->

---

## Close Day 1

**You now have the core of your Manager OS.**

- You have a **charter** that defines how your team operates
- You know your **stakeholders** and how to work with them
- You have a **hiring plan** to build the team you need
- You have a **roadmap** that connects your work to business outcomes

<!-- Talk track: That is Day 1. Take a moment to appreciate what you have built today. You walked in this morning with a case context and an empty folder. You now have a team charter, a stakeholder map, the beginning of a hiring plan, a twelve-month roadmap with RICE scoring, and the first page of an executive narrative. That is the core of a Manager Operating System. -->

---

## Close Day 1

Day 2 is about **people, refinement, and presenting it all.**

> "Management is not about having all the answers. It's about building the system that finds them."

Thank you. See you on March 23.

<!-- Talk track: On Day 2, we will add the people dimension — growth plans, performance management, difficult conversations. Then you will refine your portfolio artifacts with structured peer feedback. And in the final block, you will present everything in a QBR simulation. Submit your checkpoint artifacts now, and I will see you on March 23. Have a good week. -->
