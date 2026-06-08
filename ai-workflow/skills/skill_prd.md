# SKILL: Writing World Class Product Requirements Documents (PRDs)

## Purpose
This skill guides Claude in writing PRDs that reflect senior principal PM-level thinking. The output should be specific, intellectually honest, strategically grounded, and immediately usable by engineering, design, and business stakeholders. It should be the kind of PRD that makes a hiring manager at a top tech company say "this person thinks at a completely different level."

---

## Before Writing Anything — Ask These Questions

Never start writing a PRD without first gathering answers to these questions. A PRD built on assumptions is not world class — it is a document that will be wrong in important ways.

**About the problem:**
1. What is the single most painful moment in the user's current experience? Get specific — not "it's frustrating" but "I spent three weekends researching camps and still made the wrong choice."
2. What do people do today without this product? Walk through the exact manual steps.
3. What is the evidence that this problem is real? Personal experience, user interviews, organic workarounds, market data?
4. Who feels this pain most acutely — and why them specifically?

**About the solution:**
5. What is the smallest possible MVP that proves the core hypothesis?
6. What are you explicitly NOT building in the MVP — and why?
7. What is the hardest problem in this product? (Data, supply, trust, adoption, regulation?) What is your honest plan for it?

**About the business:**
8. How does this product make money? Be specific about the model and the pricing.
9. Where do you launch first — and why that specific market?
10. What is the viral or growth loop, if any?

If the person cannot answer these questions, help them think through the answers before writing. A PRD is not a writing exercise — it is a thinking exercise that happens to produce a document.

---

## Sections to Include (Always)

Every world class PRD includes all of the following sections. Do not omit any of them. Each section has a purpose.

### 1. Executive Summary
**What it is:** 3-5 sentences that capture the full picture. If a busy CPO reads only this, they should understand the product, the problem, the user, and the opportunity.

**What makes it world class:**
- Leads with a personal origin story or early validation signal if one exists — organic adoption is more compelling than any market research
- States the product's position clearly in one sentence
- Answers "why now" implicitly through context
- Never uses generic phrases like "growing market" or "unique opportunity"

**Common mistakes to avoid:**
- Starting with market size instead of the human problem
- Being so abstract that the reader doesn't know what the product actually does
- Underselling real validation signals (e.g., if the person built a manual workaround that others adopted — that's a lead, not a footnote)

### 2. Problem Statement
**What it is:** A rigorous description of the problem, the current broken workflow, the evidence that the problem is real, and who feels it most.

**What makes it world class:**
- The current workflow is described step by step — making the "before" vivid
- Validation is specific and honest: "two other parents adopted my Google Sheet without being asked" is more powerful than citing a Gartner report
- The "who feels this most" section names a specific segment, not all users

**Common mistakes to avoid:**
- Describing the solution in the problem section
- Generic pain descriptions ("users struggle with X") instead of specific human moments
- Overstating validation — be honest about what is confirmed vs. assumed

### 3. Market Opportunity
**What it is:** TAM analysis, competitive landscape, and the timing rationale.

**What makes it world class:**
- TAM is built from real numbers with visible math — not invented or vague
- The competitive landscape table shows specific solutions and specific gaps — not just "existing solutions are inadequate"
- "Why now" names specific macro trends, not just "the market is growing"

**Common mistakes to avoid:**
- Using TAM numbers without sources or logic
- Competitive landscape that ignores DIY workarounds — the Google Sheet, the group text, the paper form — these are your real competitors
- Claiming a market has "no competition" — every problem has a current solution, even if it's manual

### 4. Target Users
**What it is:** Specific personas with demographics, behaviors, needs, and a real-sounding quote.

**What makes it world class:**
- Primary persona is the highest-pain, highest-value user — not the broadest possible definition
- The user quote sounds like a real person said it, not a PM wrote it
- Out of scope users are explicitly listed — showing disciplined thinking

**Common mistakes to avoid:**
- Personas that could describe anyone ("busy professionals who value efficiency")
- Forgetting the economic buyer in B2B products (the person who signs the contract is often not the person who uses the product)
- Not stating explicitly who the product is NOT for

### 5. Product Vision & Strategy
**What it is:** One-sentence vision, strategic position, and 4-6 product principles.

**What makes it world class:**
- The strategic position clearly states what the product is NOT — as important as what it is
- Product principles are specific enough to be useful as a decision-making framework
- The vision is ambitious but grounded — not a platitude

**Common mistakes to avoid:**
- Vision statements that could apply to any product ("improve the user experience")
- Strategic position that doesn't differentiate from competitors
- Product principles that are too generic to guide any actual decision

### 6. MVP Scope
**What it is:** What is in the MVP, what is explicitly out, and the governing design principle.

**What makes it world class:**
- The exclusion list is as detailed as the inclusion list — every exclusion has a specific rationale
- The design principle is one sentence that would help a designer or engineer make a borderline call
- Scope is tight enough to be achievable in 3-6 months by a small team

**Common mistakes to avoid:**
- MVP that is too large — if you can't build it in 6 months with 5 people, it's not an MVP
- Exclusion list that just says "future opportunity" without explaining the rationale
- Including features the team wants to build rather than features users need

### 7. Data Strategy
**Required for:** Marketplaces, discovery platforms, content platforms, AI products, analytics tools. Skip only for pure SaaS tools where data is entirely user-generated.

**What it is:** Where the product's core data comes from, how it is acquired and maintained, and what threshold must be met before launch.

**What makes it world class:**
- The cold start problem is named explicitly and addressed with a specific plan
- Supply before demand is the governing principle for marketplace/discovery products
- A hard supply threshold gate is defined — specific numbers, not vague readiness criteria
- Data freshness and quality degradation are addressed proactively, not treated as future problems

**Common mistakes to avoid:**
- Assuming data will be available without a supply strategy
- Manual curation as a primary strategy — it doesn't scale and the PRD should acknowledge this
- Not defining a launch gate — launching with thin supply is a common marketplace killer
- Treating data quality as someone else's problem

### 8. Feature Specifications
**What it is:** For each core feature: overview, key behaviors, edge cases, and design principle.

**What makes it world class:**
- Edge cases are specific and show the author thought through failure modes
- Design principles for individual features are distinct and actionable
- The level of detail is sufficient for an engineer or designer to build without guessing at intent

**Common mistakes to avoid:**
- Features described so abstractly that implementation is still unclear
- Ignoring edge cases — a feature spec without edge cases is incomplete
- Writing engineering specs — PRDs describe intent, not implementation

### 9. User Stories
**What it is:** Structured stories in "As a [user], I want to [action] so that [outcome]" format, grouped by theme.

**What makes it world class:**
- Stories are independently testable
- Each story captures a real user need, not a feature implementation detail
- The outcome clause ("so that") is meaningful — it explains why the user wants this

**Common mistakes to avoid:**
- Stories that describe implementation ("As a user, I want a dropdown menu")
- Stories without a meaningful outcome clause
- Including stories for out-of-scope features

### 10. Success Metrics
**What it is:** North Star Metric, engagement metrics, and business metrics with specific targets.

**What makes it world class:**
- North Star Metric is a single number that best captures user value — and the baseline (current state) is specified
- Targets are specific and realistic — not aspirational vanity metrics
- A "what we will not measure yet" section shows metric sequencing discipline

**Common mistakes to avoid:**
- Multiple North Star Metrics — there can only be one
- Targets without baselines — a 40% improvement from what?
- Tracking vanity metrics (page views, registered users) instead of value metrics (tasks completed, outcomes achieved)

### 11. Business Model
**What it is:** Revenue streams with pricing, and illustrative unit economics.

**What makes it world class:**
- Pricing rationale is explained — why this price, why this model
- Unit economics are shown even if rough — LTV, CAC, payback period, or ARR target
- The incentives of all parties (users, businesses, platform) are explicitly considered

**Common mistakes to avoid:**
- Vague revenue streams ("we will monetize through partnerships")
- No unit economics — a business model without math is a hypothesis, not a strategy
- Pricing that hasn't been thought through ("we'll figure it out later")

### 12. Go-to-Market Strategy
**What it is:** Beachhead market, phased growth strategy, and the rationale for why this approach works.

**What makes it world class:**
- Beachhead is hyper-specific — not "the US market" but "working parents in Bay Area school communities"
- Growth phases are time-bounded and sequenced logically
- The viral or growth loop is named explicitly if one exists

**Common mistakes to avoid:**
- GTM that tries to reach everyone at once
- No explanation of how word spreads from early adopters to the mainstream
- Ignoring the supply-side acquisition motion for marketplace products

### 13. Launch Readiness
**What it is:** Binary conditions that must be true before launching to real users. Prevents premature launches that damage trust and cause churn.

**What makes it world class:**
- Conditions are binary — either met or not met — not subjective readiness judgments
- For marketplace products: a hard supply threshold is the first and most important gate
- A rollback plan is included — what happens if something goes wrong at launch

**Common mistakes to avoid:**
- Launch readiness that is too vague to enforce
- No supply threshold for marketplace products — this is the single most common marketplace launch mistake
- No rollback plan — optimism is not a strategy

### 14. Risks and Mitigations
**What it is:** The 4-6 biggest risks to the product's success, each with a specific mitigation.

**What makes it world class:**
- The hardest risks are named honestly — not buried or minimized
- Mitigations are specific and actionable, not "we will monitor this"
- Likelihood and impact are assessed for each risk

**Common mistakes to avoid:**
- Risks that are too generic ("the market may not adopt this")
- Mitigations that are not actually mitigating ("we will build a great product")
- Missing the most obvious risks — cold start, competitive response, data quality, regulatory exposure

### 15. Open Questions
**What it is:** Specific unresolved questions with resolution approaches.

**What makes it world class:**
- Questions are precise enough that someone could actually answer them
- Each question has a resolution approach — user research, A/B test, design partner feedback
- The list is honest — it includes things the author genuinely doesn't know yet

**Common mistakes to avoid:**
- Open questions that are actually closed ("should we build mobile?" — if you've decided desktop first, that's not open)
- No resolution approaches — open questions without plans to answer them are just worries

### 16. Future Roadmap
**What it is:** Post-MVP opportunities organized by time horizon.

**What makes it world class:**
- Near-term items are specific and directly connected to MVP learnings
- Long-term items are ambitious but grounded in a plausible path
- The roadmap shows strategic coherence — items build on each other

### 17. Appendix
**What it is:** Competitive landscape summary table and assumptions log.

**What makes it world class:**
- Assumptions log is explicit and honest — every major assumption the PRD rests on is named, with a confidence level and validation approach
- Competitive landscape table uses consistent dimensions that matter

---

## What Separates Good from World Class

**Good PRDs:**
- Cover all the sections
- Are clear and well-organized
- Describe the product accurately

**World class PRDs:**
- Name the hardest problem and show a real plan for it
- Are intellectually honest about what is known vs. assumed
- Show the author anticipated every hard question before it was asked
- Make the human problem so vivid that the solution feels inevitable
- Include specific numbers, specific users, specific markets — never vague
- Have a "Data Strategy" section that shows supply-side thinking for any marketplace or discovery product
- Have a "Launch Readiness" section with binary gates — not subjective readiness
- Show business model thinking with unit economics, not just revenue stream names

---

## Common PRD Anti-Patterns to Avoid

| Anti-Pattern | Why It's a Problem | Fix |
|---|---|---|
| "Large and growing market" | Says nothing specific | Name the market size with a source and show the math |
| "Users struggle with X" | Too vague | Describe the specific painful moment in the user's day |
| "No competition" | Not credible | Every problem has a current solution — even if it's a spreadsheet |
| MVP with 15 features | Not an MVP | Cut to the 3-5 features that prove the core hypothesis |
| Risks section that says "we will monitor" | Not a mitigation | Name a specific action that reduces the probability or impact |
| Data strategy missing for a marketplace product | The most common marketplace failure | Always include supply strategy, supply threshold, and freshness plan |
| Launch without supply threshold | Causes immediate churn that is hard to recover from | Define a hard supply gate and enforce it |
| Time targets that are too optimistic | Destroys credibility with anyone who knows the domain | Research realistic benchmarks; be honest about what improvement is achievable |
| Business model without unit economics | A hypothesis not a strategy | Show illustrative math even if rough |
| Assumptions not stated | Hides intellectual dishonesty | Include an assumptions log with confidence levels |

---

## Reference Files

The following sample PRDs demonstrate this template applied to three different product types. Read them before writing to calibrate the expected quality level.

- **CampSpark_PRD.md** — Consumer two-sided marketplace. Shows: personal origin story as validation, cold start problem treatment, supply threshold gate, social coordination moat.
- **VendorIQ_PRD.md** — B2B enterprise SaaS. Shows: enterprise sales motion, design partner strategy, framework library as data strategy, compliance and audit trail as core features.
- **ShiftSwap_PRD.md** — Consumer/SMB mobile B2B2C. Shows: worker-first design principle, qualification matching as moat, franchise expansion as GTM strategy, notification fatigue as a named risk.

---

## Quality Checklist Before Delivering

Before delivering a PRD, verify:

- [ ] Executive summary would make sense to a reader who reads nothing else
- [ ] Problem statement includes a specific current workflow (step by step)
- [ ] Validation is specific and honest — not invented or overstated
- [ ] Target users include an "out of scope" list
- [ ] MVP exclusion list is as detailed as the inclusion list
- [ ] Data Strategy section included if product is a marketplace or discovery platform
- [ ] Supply threshold defined as a hard gate (if applicable)
- [ ] North Star Metric has a baseline and a specific target
- [ ] Business model includes illustrative unit economics
- [ ] Beachhead market is hyper-specific — not a broad geography
- [ ] Launch Readiness section has binary conditions and a rollback plan
- [ ] Every risk has a specific, actionable mitigation
- [ ] Assumptions log is included and honest
- [ ] Time targets are realistic — validated against domain knowledge
- [ ] No generic phrases: "large and growing," "no competition," "unique opportunity," "users struggle with"

---

*This skill was developed based on PRD writing patterns from world class product leaders at marketplace, B2B SaaS, and consumer product companies. Apply it to produce PRDs that reflect principal PM-level strategic thinking.*