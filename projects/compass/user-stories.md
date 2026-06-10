# User Stories — Compass: AI Product Discovery Assistant

**PRD Reference:** `projects/compass/prd.md`
**MVP Scope Only**
**Author:** Sonal Singh | June 2026

---

## Theme 1: Problem Statement Input

- As a senior PM, I want to type a problem statement in plain language so that I can start a discovery research session without learning a specific query format.

- As a senior PM, I want to see example problem statements in the input field so that I understand the right level of specificity before I submit my first query.

- As a senior PM, I want to see a character count and a minimum length requirement so that I know when my input has enough detail to produce a quality brief.

- As a senior PM, when my input is fewer than 50 characters, I want to see an inline message explaining why more detail is needed so that I do not submit a vague query and get a low-quality brief.

**Acceptance criteria for input submission:**
- Input field accepts plain text, minimum 50 characters, maximum 500 characters
- Character count visible as user types
- Submit button is disabled until minimum length is met
- Submitting triggers the agent status panel immediately with no delay visible to the user
- Three example problem statements are shown as placeholder text or as clickable examples below the input field

---

## Theme 2: Agent Orchestration and Status Display

- As a senior PM, I want to see a live status panel showing which agents are running and which have completed so that the wait time feels purposeful rather than opaque.

- As a senior PM, I want to see a brief description of what each running agent is doing so that I understand what research is being conducted on my behalf.

- As a senior PM, I want to see each brief section appear as its agent completes so that I can begin reading before the full brief is finished.

- As a senior PM, when a single agent step takes longer than 30 seconds, I want to see a "still working" indicator so that I know the system has not stalled.

- As a senior PM, when an agent fails and cannot complete its section, I want to see a clear explanation of what happened and receive the rest of the brief so that a single failure does not block the entire output.

**Acceptance criteria for agent status panel:**
- Panel shows all 7 agents: orchestrator, 5 sub-agents, eval agent
- Each agent shows one of three states: queued (grey), running (animated), complete (green checkmark)
- Running agent shows a one-line description of its current task
- Completed agent shows the time it took (e.g., "14s")
- Sections appear in the output panel as each sub-agent finishes, not all at once at the end

---

## Theme 3: Discovery Brief Output

- As a senior PM, I want a structured 5-section discovery brief so that I have a consistent, defensible starting point for any executive presentation.

- As a senior PM, I want each section to display its content in plain, structured prose so that I can read and share it without reformatting.

- As a senior PM, I want every factual claim in the brief to show a source citation so that I can verify or defend each claim without doing additional research.

- As a senior PM, I want unverified assumptions in the brief to be explicitly labeled as assumptions so that I know which claims require further validation before I present them.

- As a senior PM, I want an executive summary at the top of the brief synthesizing all 5 sections so that I can share a one-paragraph overview with stakeholders before they read the full brief.

- As a senior PM, I want a "suggested next steps" section at the end of the brief so that I know what to validate or investigate before moving forward.

**Acceptance criteria for brief output:**
- Brief contains exactly 5 sections: Problem Framing, User Segmentation, Competitive Landscape, Opportunity Sizing, Risks and Open Questions
- Each section is 200 to 350 words
- Executive summary appears above all 5 sections
- Suggested next steps appear below all 5 sections
- Factual claims with a web search source show a numbered citation linking to the source URL
- Claims without a verifiable source are marked "[Assumption]" inline

---

## Theme 4: Eval Scoring Display

- As a senior PM, I want each section of the brief to display a quality score from 0 to 100 so that I know at a glance how much to trust each section before presenting it.

- As a senior PM, I want to see a color-coded score indicator per section (green, yellow, red) so that I can identify weak sections without reading the rubric detail.

- As a senior PM, I want to expand any section score to see the individual rubric criteria and their scores so that I understand specifically why a section scored the way it did.

- As a senior PM, I want to see an overall brief quality score at the top of the output so that I can quickly assess whether the brief is ready to share with stakeholders.

- As a senior PM, when a section scores below 50, I want to see a specific suggested action so that I know exactly what to do to address the quality gap.

**Acceptance criteria for eval scoring:**
- Each section shows a score bar (0 to 100) with color: green 75 to 100, yellow 50 to 74, red 0 to 49
- Clicking or tapping the score bar expands a rubric breakdown showing each criterion name, its score out of 10, and a one-sentence explanation
- Overall brief score shown prominently at the top of the brief, calculated as the average of all 5 section scores
- Sections scoring below 50 show a callout: "Low confidence: [specific suggested action]"
- Eval scores appear after all 5 sections are displayed, not before

---

## Theme 5: RAG Retrieval (Internal Behavior, PM-Verifiable)

- As a senior PM, I want the Problem Framing Agent to apply a structured JTBD framework to my input so that the user and pain point are identified using a recognized PM methodology, not generic reasoning.

- As a senior PM, I want the Opportunity Sizing Agent to show its TAM calculation with visible math and labeled assumptions so that I can evaluate the estimate's credibility independently.

- As a senior PM, I want the Risk Assessment Agent to surface product-specific risks (not generic ones) so that the risks named are actually relevant to the problem I submitted.

---

## Theme 6: Web Search via MCP (Internal Behavior, PM-Verifiable)

- As a senior PM, I want the Market Research Agent to cite sources with dates so that I can confirm the market data is current and not outdated.

- As a senior PM, I want the Competitive Analysis Agent to name specific competitors with specific gaps so that the competitive landscape is grounded in real products, not generalities.

- As a senior PM, when web search returns no relevant results for a specific query, I want the affected section to flag this explicitly so that I know the section is based on Claude's training data rather than current web data.

**Acceptance criteria for web search citation:**
- Every web-sourced fact in the brief includes a citation with URL and publication date where available
- If a search query returns no results, the section notes: "Current web data unavailable for this query. Output based on model training data."

---

## Edge Cases

- As a senior PM, when I submit a problem statement that describes a solution rather than a problem (e.g., "build a mobile app for logistics tracking"), I want the Problem Framing Agent to reframe it as a problem and explain the reframe so that the brief addresses the underlying need rather than justifying a predetermined solution.

- As a senior PM, when I submit a problem statement about a niche or highly regulated domain (e.g., FDA drug approval processes), I want to see a notice that Compass is optimized for tech product discovery and that web search coverage may be limited so that I calibrate my expectations for this type of input.

- As a senior PM, when total brief generation exceeds 120 seconds, I want to see the sections that have completed and a clear message about what is still generating so that I can begin reading rather than waiting for a complete output.

- As a senior PM, when a source URL in the brief returns a 404 error, I want to see "source no longer available" rather than a broken link so that the brief remains readable even if sources go offline.

---

*User stories authored by Sonal Singh | June 2026*
*Stories cover MVP scope only as defined in `projects/compass/prd.md`*
