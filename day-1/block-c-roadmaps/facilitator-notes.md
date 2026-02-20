# Facilitator Notes — Block C: Roadmaps, Bets, and Alignment

**Day 1, Block C | 15:30–17:10 (100 minutes)**

---

## Pre-Class Setup

- **Room:** Ensure tables are arranged for easy pairing across case contexts (you will need cross-context pairs for the red-team exercise at minute 70).
- **Screen:** Have the `slides.md` deck loaded and ready. Pre-load the `roadmap-rice.md` template on a second screen or tab so you can walk through it during the activity brief.
- **Materials:** Students should have their case context documents and Block A artifacts (Team Charter, Stakeholder Map) accessible — either printed or on their laptops. They will need these for the roadmap activity and for the Day 1 Checkpoint submission.
- **LMS:** Confirm the LMS submission portal is open and working BEFORE class starts. Test-upload a blank file. The 17:10 deadline is non-negotiable and technical issues will cause stress if not resolved in advance.
- **Templates:** Ensure `roadmap-rice.md`, `exec-narrative.md`, and `risk-register.md` are posted on the LMS or shared drive before class begins.
- **Timer:** Use a visible countdown timer (project it or use a large screen). This block has tight transitions and a hard stop.

---

## Timing Breakdown (Minute-by-Minute) — REVISED

**Key changes from original:** Teaching compressed from 44→35 min. Exec narrative activity extended from 15→20 min. Debrief extended from 3→8 min. Skip metrics tree "draw live" section (32–33), scripted trade-off conversation (38–40), and individual narrative example sections (point to template instead).

| Time | Minutes | Slide(s) | Activity |
|------|---------|----------|----------|
| 15:30 | 0-2 | 2 (Title) | Welcome, block overview, learning outcomes. Frame the energy: "Last block of the day, hard stop at 17:10 for submissions." |
| 15:32 | 2-7 | 3-13 (Roadmap Problem through Roadmap Alternative) | Concept introduction. Cover why roadmaps are hard, what good ones do, Gantt chart trap. Ask: "Who has seen a roadmap that was actually a Gantt chart?" Quick responses. |
| 15:37 | 7-12 | 14-15 (Analytics Roadmap Structure, Horizons Examples) | Walk through Now/Next/Later. Brief whiteboard example. |
| 15:42 | 12-18 | 16-23 (Roadmap Items, RICE Prioritization, RICE in Practice) | Explain RICE formula. Do one live example together. Walk through sensitivity analysis. |
| 15:48 | 18-22 | 24-31 (North Star, Guardrails, Input Metrics, Common Mistakes, Test) | Concept slides. Skip metrics tree live drawing (32–33) — mention the concept, point to template. |
| 15:52 | 22-25 | 34-37 (Communicating Trade-offs, Cost of Delay, Partners) | Quick concept. Read the "instead of / say" table. Skip scripted conversation (38–40). |
| 15:55 | 25-30 | 41-47 (Executive Narrative structure and examples) | Walk through 5-section structure. Emphasize prose over bullet points. Skip individual example sections — point to template. |
| 16:00 | 30-33 | 48-50 (Writing for Executives, BLUF, Rules) | BLUF concept. Read bad/good example aloud. Punchy and fast. |
| 16:03 | 33-35 | 51-52 (Risk Registers) | Quick concept. Emphasize "top 3 risks on slide 2 of every exec deck." |
| 16:05 | 35-36 | 53-54 (Activity Brief: Roadmap) | Hand out template. Clear instructions. |
| 16:06 | 36-66 | **ACTIVITY: 12-Month Roadmap** | 30 minutes. Circulate, help students stuck on RICE scoring or North Star. |
| 16:36 | 66-67 | 55-56 (Activity Brief: Exec Narrative) | Quick transition. Emphasize: first page, Context + What's Next. BLUF. |
| 16:37 | 67-87 | **ACTIVITY: Executive Narrative Draft** | **20 minutes** (extended from 15). Circulate. Watch for students reverting to bullet points. |
| 16:57 | 87-88 | 57-58 (Red-Team Brief) | Pair students across case contexts. Explain: 4 minutes each direction, find the fatal flaw. |
| 16:58 | 88-96 | **RED-TEAM: Kill the Project** | 8 minutes. High-energy. Walk around, prompt with provocative questions. |
| 16:58 | 88-92 | Red-Team Round 1 | Partner A presents, Partner B attacks. |
| 17:02 | 92-96 | Red-Team Round 2 | Switch roles. |
| 17:06 | 96-100 | 59-60 (Debrief + Update) | **Extended debrief (4 min):** "What did the red-team reveal?" + "What's one thing you'll change in your roadmap?" 2 min to update. |
| 17:10 | 100 | 61-66 (Checkpoint, What's Coming, Close) | **HARD STOP.** Day 1 Checkpoint, What's Coming, Close. Remind students to upload NOW. |

**Total: 100 minutes. No slack. Manage transitions tightly.**

**Notes on slide cuts:** Skip slides 32–33 (metrics tree live drawing — mention concept, let students explore in template), 38–40 (scripted trade-off conversation — reference the "instead of / say" table instead), and individual narrative example sections within 41–47 (point to template). This saves ~9 minutes, reallocated to extended exec narrative activity (+5 min) and extended debrief (+4 min).

---

## Red-Team Logistics

### Pairing Students Across Case Contexts

- Before the red-team exercise (around minute 85), ask students to stand up and find a partner who chose a **different** case context.
- If the class has uneven distribution across case contexts, it is acceptable for two students from the same context to pair, but prioritize cross-context pairs.
- For odd numbers: create one group of three, with a round-robin format (A attacks B, B attacks C, C attacks A — 3 minutes each).

### Keeping It Constructive

- Frame the exercise clearly: "Your job is to make their roadmap stronger, not to win an argument."
- Provide the specific questions from slides 57-58 as prompts. Students who have never done red-teaming tend to default to vague feedback ("looks good") unless given specific angles of attack.
- If you hear a pair getting adversarial rather than constructive, step in and redirect: "What would you suggest instead?"
- Remind them: the best roadmaps survive criticism because the criticism was incorporated.

### Time Management

- Use a loud, clear signal (clap, timer sound) at the 5-minute mark to switch roles.
- At the 10-minute mark, call time firmly. Students will want to keep going — channel that energy into the debrief.

---

## Key Teaching Points (What to Emphasize)

1. **Roadmaps are communication tools.** If students are building Gantt charts with specific dates, redirect them. The question is "where and why," not "when exactly."

2. **RICE is a conversation starter.** Some students will try to optimize the formula or argue about whether Impact should be 2 or 3. Redirect: the value is in the discussion, not the decimal. If two projects score similarly, the tie-breaker is strategic judgment, not arithmetic.

   **Facilitator note on Effort:** When teaching RICE, emphasize that "Effort" now includes compute costs, not just human time. At scale, a GPU-intensive model retraining initiative may score differently than a dashboard build — even if both require the same person-months — because the cloud compute bill for model training can dwarf the human labor cost. Ask students: "If your churn model retraining costs $15K/month in GPU compute, does that change your RICE score? It should." This is especially relevant for FinGuard students dealing with large-scale ML workloads.

3. **The North Star must connect to what the business cares about.** Common mistake: students pick a technical metric ("model accuracy") instead of a business metric ("decisions made with model support" or "revenue influenced by analytics"). Push them upstream.

4. **Executive narratives are written in prose.** Students will resist this. They are used to bullet points and dashboards. Emphasize that prose forces clarity of thought and that this is how senior leaders actually communicate at companies like Amazon, Stripe, and Netflix.

5. **Risk registers demonstrate maturity.** Students sometimes feel that listing risks makes them look unprepared. The opposite is true. An executive who sees a risk register trusts the person who wrote it.

---

## What to Cut If Behind Schedule

If you are running more than 5 minutes behind by 16:00:

1. **First cut: Communicating Trade-offs slides (34-40).** Mention the concept in 30 seconds ("frame as choices, not complaints") and move on. Students can read the slides later.

2. **Second cut: Reduce roadmap activity to 25 minutes.** Tell students they can finish RICE scoring after class — the important thing is to have the Now column populated and the North Star defined.

3. **Third cut: Reduce exec narrative to 10 minutes.** They only need the Context section drafted for the checkpoint. What's Next can wait.

4. **NEVER cut the red-team exercise.** It is the highest-energy activity of the day and provides the most learning. Compress it to 8 minutes (4 each direction) if you must, but do not skip it.

5. **NEVER cut the checkpoint submission time.** Students need at least 3 minutes to upload. If pressed, talk through the Day 2 preview and Close slides while students are uploading.

---

## Checkpoint Submission

### How Students Submit

- **Primary method:** Upload to the LMS assignment portal titled "Day 1 Checkpoint." Three files: Team Charter, Stakeholder Map, Roadmap Outline (RICE template).
- **Backup method:** If the LMS is down or a student has technical issues, they email all three files to the instructor before 17:10. Subject line: "Day 1 Checkpoint — [Last Name]."
- **Format:** Markdown (.md) preferred. PDF or Word also acceptable. Do not accept links to Google Docs (these can be edited after the deadline).

### What "Complete" Means for Pass/Fail

- **Pass:** All three documents have been submitted. Each document has content in at least half of its sections. Sections can be rough, incomplete, or placeholder — but they cannot be empty.
- **Fail:** Any document is missing entirely, or a document is submitted with all sections empty (just headers with no content).
- **Edge cases:** If a student submits two of three documents by 17:10 and the third within 30 minutes with a reasonable explanation, use judgment. The goal is accountability, not punishment.

---

## Common Questions and Answers

**Q: "How do I estimate Reach for an internal analytics project?"**
A: Reach does not have to mean end users. For an internal project, Reach can be the number of decisions influenced, the number of stakeholders who use the output, or the number of times per quarter the analysis will be referenced. For example, a churn model that informs weekly retention meetings reaches the entire growth team (say 8 people) 52 times a year.

**Q: "What if I can't think of 8 initiatives for my roadmap?"**
A: Go back to your case context's pain points and stakeholder needs. Each pain point suggests at least one initiative. Each stakeholder request suggests at least one initiative. Also consider: what foundational work is needed before the exciting projects can happen? Data quality, documentation, and tooling are all legitimate roadmap items.

**Q: "Should the executive narrative be written from the perspective of my actual case context, or can I make up metrics?"**
A: Use your case context as the setting, but you will need to invent plausible metrics and accomplishments. This is expected. The skill being assessed is the structure and clarity of the narrative, not the accuracy of the fictional numbers. Make them realistic — do not claim you increased revenue by 500% in one quarter.

**Q: "How is the red-team exercise graded?"**
A: The red-team exercise itself is not graded. It contributes to your participation score, and the insights from it should improve your roadmap, which IS graded as part of the portfolio. Think of it as free consulting from a peer.

**Q: "What's the difference between the roadmap outline I submit today and the final roadmap in the portfolio?"**
A: Today's submission is a rough draft — RICE scores, a Now/Next/Later layout, and a North Star metric. The final portfolio version should be polished, include a risk register, and be accompanied by the executive narrative. You have until one week after Day 2 to refine it.

**Q: "Can I change my case context between Day 1 and Day 2?"**
A: No. Your portfolio artifacts should tell a coherent story across one case context. Switching mid-course means starting over on most artifacts.

**Q: "How detailed should the risk register be for today's checkpoint?"**
A: The risk register is NOT required for today's checkpoint. It is part of the final portfolio. However, if the red-team exercise surfaced risks, jot them down now so you do not lose them.

---

## Energy Management

This is the last block of the day. Students have been in class since 11:00 with a lunch break. Energy will be lower at the start of this block compared to Block A.

**Strategy:**
- **Minutes 0-44 (concept slides 2-52):** Keep these brisk and interactive. Ask questions frequently. Do not lecture for more than 4 minutes without engaging the room.
- **Minutes 45-91 (activities, slides 53-56):** The roadmap and narrative activities are individual work, which can feel low-energy. Circulate actively. Ask students to share interesting decisions with their neighbors. If energy is flagging at minute 70, consider a 60-second stretch break before the narrative exercise.
- **Minutes 91-102 (red-team, slides 57-60):** This is the energy injection. The red-team exercise is competitive, social, and slightly uncomfortable — all of which wake people up. Lean into it. Be visibly enthusiastic. If pairs are going through the motions, jump in with a provocative question to raise the stakes.
- **Do not let the narrative writing drag.** If students are struggling with prose, tell them to write ugly sentences now and edit later. The goal is structure, not elegance.

---

## Transition to Day 2

Before dismissing:
- **Remind about the hiring packet:** Students should continue working on their work sample and interview loop between Day 1 and Day 2. These are portfolio deliverables — no mid-week deadline.
- **QBR simulation brief:** Will be posted on the LMS tonight. Students should read it before Day 2.
- **Roadmap refinement:** Encourage students to spend 30-60 minutes between now and Day 2 polishing their roadmap. They will present it during the QBR simulation.
- **Office hours:** Remind students of your availability for questions between Day 1 and Day 2.
