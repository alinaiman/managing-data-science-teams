# Job Description Template

**Student Name:** Alina Imanakhunova
**Date:** 16th of March
**Case Context:** Small (Seed-Stage)
**Role Title:** Head of Data Science 
**Level:**  Senior

---

## Role Summary

*Write 2–3 sentences describing what this person does and why the role matters. Focus on impact, not activities.*

Role Summary:

> We are hiring our first and only Head of Data Science to bring order to a fast-growing fitness app that design the most suitable data ecosystem at DataPulse. You will own the full analytics stack — from fixing a broken event taxonomy in our React Native app to building the warehouse and producing the investor-grade retention and LTV metrics that will anchor our Series A fundraise. This is a high-autonomy, high-visibility role where you report directly to the CEO and your output lands in front of investors within your first 90 days.

---

## 90-Day Outcomes

*List 3–5 specific, measurable things this person will accomplish in their first 90 days. These are outcomes, not responsibilities — they describe results, not activities.*


90-Day Outcomes:

1. A clean, documented retention cohort (D1/D7/D30) is produced from PostgreSQL and presented to the CEO — with full methodology written up and agreed upon by all stakeholders as the canonical number.
2. A lightweight data warehouse is live (BigQuery or equivalent), with an ETL pipeline running from PostgreSQL and Firebase, eliminating all analytical queries against the production database.
3. A canonical event taxonomy v1 is written, reviewed with both mobile developers, and at least 80% of the top-20 critical user actions are instrumented correctly and consistently across iOS and Android.


---

## Key Responsibilities

*List 5–7 bullet points, ordered by priority (most important first). These describe ongoing responsibilities, not one-time tasks.*

Key Responsibilities:

1. Own the full data pipeline: from raw events in Firebase and PostgreSQL through to clean, trusted tables in the warehouse
2. Define and document all core metrics (MAU, DAU, retention, LTV, CAC) so every team member is working from the same definitions
3. Build and maintain dashboards for the product team and founders, making sure they are easy to use without needing to ask for help
4. Work with the mobile developers to design and implement a clean event tracking system across the app
5. Design basic A/B testing frameworks so the product team can run experiments properly, with real statistical analysis rather than gut-feel comparisons

---

## Required Qualifications

*Must-haves only. Be ruthlessly honest: if someone without an advanced degree could do this job, do not require an advanced degree. Each item should be directly tied to a 90-day outcome or key responsibility.*

Required Qualifications:

- 4+ years working in analytics, data engineering, or a similar role
- Strong SQL skills — you should be comfortable with window functions, CTEs, and working with messy real-world data
- Experience setting up or working with a data warehouse (BigQuery, Redshift, Snowflake, or similar)
- Able to explain data concepts and analysis results clearly to people who are not technical — founders, product managers, and support staff


---

## Preferred Qualifications

*Nice-to-haves that would accelerate ramp-up but are not dealbreakers. Be explicit that these are not required.*

Your Preferred Qualifications:

1. Experience with dbt or similar tools for transforming and modeling data
2. Some familiarity with A/B testing and basic statistics (you do not need to be a statistician, but you should know what statistical significance means)
3. Python or R for analysis work beyond SQL
4. Background in a B2C app or subscription business — understanding metrics like churn and LTV from experience, not just theory

---

---

## What We Offer

*Describe your compensation philosophy, growth opportunities, and team culture. Be specific rather than generic.*

**Example:**
> - Competitive salary benchmarked to [market/percentile] with equity participation
> - Direct access to founders and leadership — your analyses shape company direction
> - Budget for conferences, courses, and professional development
> - Flexible work arrangement: [remote/hybrid/in-office] with async-first communication
> - Opportunity to build the analytics function from the ground up

Your Offer:

- Competitive salary for a seed-stage startup, plus meaningful equity — you are joining early and that should be reflected in your upside
- $3,000/month budget for data tools and infrastructure — you choose what to buy
- Fully remote-friendly with async-first communication; we do not believe in meetings for the sake of meetings
- A real opportunity to build the analytics function from scratch and hire the next data person once we close the Series A
- 25 paid days off per year
- A week retreat in Thailand in the mid of November  

---

## About the Team

*Brief context about the team this person joins. Who will they work with? What is the team's current state? What is the team culture like?*

**Example:**
> You will be the first dedicated analytics hire, joining a product team of 8 engineers and 2 product managers. Today, analytics is done ad-hoc by engineers and founders using raw database queries. You will bring structure to this chaos. The culture values ownership, direct communication, and shipping — we would rather have a good-enough answer today than a perfect answer next month.

Your Team Context:

> 
You will be the one and only **Head of Data Scince** at DataPulse, a seed-stage fitness app with ~50,000 monthly active users and 15% month-over-month growth. You will report directly to the CEO and work closely with the Head of Product, one backend engineer, and two mobile developers every day.

Right now, analytics is a mess. We have Firebase events with inconsistent naming, an Amplitude setup nobody fully trusts, and
a PostgreSQL production database that the CEO queries directly for answers. Three people can ask the same question and get three different numbers. Nobody is proud of this — and that is exactly why we are hiring you.

---

## Evaluation Criteria

Use these dimensions to self-assess your job description. For official grading criteria, see `assessment/grading-rubrics.md` (Hiring Packet component, 20%).

| Criterion | What We Are Looking For |
|:---|:---|
| **Outcome Orientation** | Are the 90-day outcomes specific, measurable, and realistic? Do they drive the rest of the document? | Yes — outcomes are time-bound, tied to concrete deliverables (e.g., "D30 retention cohort with methodology documented by Day 30"), and directly reflect the Series A pressure described in the case. |
| **Honest Scoping** | Are "required" qualifications truly required? Is the level appropriate for the outcomes described? | The required list is intentionally short and grounded in what the 90-day outcomes actually demand (SQL, warehouse, stats, startup experience). The "nice to have" section is clearly separated and labeled as non-blocking. |
| **Case Context Fit** | Does the JD reflect the specific constraints and opportunities of your chosen company context? | Yes — the JD names specific tools (Firebase, Amplitude, PostgreSQL, React Native), reflects the $5K/month budget constraint implicitly (BigQuery suggestion), and acknowledges the one-person team reality throughout. |
| **Candidate Appeal** | Would a strong candidate reading this JD understand the role and be excited to apply? | The "About the Team" section is honest about the mess, which attracts builders over maintainers. The 90-day outcomes show the candidate exactly what success looks like before they accept the offer. |
| **Completeness** | Are all sections filled in with thoughtful, specific content (not generic boilerplate)? | All sections are specific to DataPulse. No generic phrases like "fast-paced environment" or "rockstar" appear. Every section connects back to the actual case constraints. |

