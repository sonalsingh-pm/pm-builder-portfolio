# Compass: AI Product Discovery Assistant — Product Requirements Document
**Status:** Portfolio Concept | **Version:** 1.0 | **Author:** Sonal Singh | **Last Updated:** June 2026

---

## Executive Summary

Product discovery done right is a 4 to 8 week process. A PM investigating a new market must map the user, survey the competitive landscape, size the opportunity, identify key risks, and synthesize it all into a brief that can survive executive scrutiny. Doing this well requires access to expensive research reports, weeks of calendar time, and a level of breadth that exceeds what any individual PM can realistically achieve while also managing a full delivery workload.

Compass is a multi-agent AI system that conducts structured product discovery research and delivers a stakeholder-ready discovery brief in under 90 seconds. A PM types a problem statement, and an orchestrator agent coordinates five specialized sub-agents, each responsible for one dimension of the analysis: problem framing, user segmentation, competitive landscape, opportunity sizing, and risk identification. Every section of the output is scored against a PM-written evaluation rubric, so the user knows exactly which parts of the brief are well-grounded and which need further validation.

This product was built to demonstrate end-to-end fluency with the four core concepts of modern AI product development: multi-agent orchestration, retrieval-augmented generation, evaluation frameworks, and the Model Context Protocol. It is also a genuine product that solves a problem I have lived as a principal PM for 15 years.

---

## 1. Problem Statement

### The Core Pain

Thorough product discovery is expensive in the one currency PMs never have enough of: time. A rigorous discovery brief requires synthesizing competitive intelligence, market sizing data, user research, and risk analysis into a coherent narrative. Even an experienced PM working without interruption needs 4 to 8 weeks to do this credibly. For a PM carrying a full delivery workload simultaneously, the calendar time stretches further. The result is not that PMs skip discovery. It is that they do it under constraint: incomplete competitive coverage, market data that is 12 to 18 months old, and opportunity sizing built on assumptions that were never challenged.

### The Current Workflow

A senior PM beginning discovery on a new product area today:

1. Opens 8 to 12 browser tabs searching Google, industry blogs, LinkedIn, and competitor websites for context on the problem space
2. Requests access to market research reports, often finding that the most relevant ones are paywalled at $2,000 to $5,000 or are 12 to 18 months out of date
3. Manually copies interesting data points into a Google Doc, losing track of sources along the way
4. Builds a competitive landscape spreadsheet by visiting each competitor's website, pricing page, and App Store reviews one by one
5. Attempts to size the market by stitching together 3 to 4 sources with different methodologies and different base years
6. Drafts the discovery brief across multiple working sessions, rewriting sections each time new information surfaces
7. Presents the brief to leadership knowing it is incomplete, with gaps filled by educated guesses labeled as assumptions

### Validation

Demand for AI-assisted research is validated by the rapid growth of Perplexity, which reached a reported $9 billion valuation in 2024 on the premise that professionals want synthesized answers, not lists of links to investigate manually. PMs specifically have begun using general-purpose AI tools in unstructured ways for discovery research, but without a disciplined workflow or quality framework to evaluate whether outputs are reliable. The behavior exists. The PM-specific, structured, evaluable version of it does not.

Personal validation: as a principal PM at Walmart Global Tech and across previous roles at Dell, Cornerstone OnDemand, and SAP, I have spent hundreds of hours on discovery research using the manual workflow described above. The briefing deck I produced was only as good as the time I had available, which was never enough.

### Who Feels This Most

The pain is sharpest for senior and principal PMs at technology companies who own a product area and are regularly asked to evaluate new bets, new markets, or significant feature investments. They have enough experience to know what good discovery looks like. The problem is not knowing what to do. The problem is that doing it well takes weeks they do not have, and the quality of their output depends heavily on access to expensive research resources rather than on their own ability.

---

## 2. Market Opportunity

### Total Addressable Market

Triangulated from multiple data sources:

- LinkedIn reports approximately 900,000 people globally with "Product Manager" in their job title. US share is estimated at 35 to 40%, yielding roughly 315,000 to 360,000 US PMs.
- Senior and principal PMs conducting strategic discovery represent approximately 25 to 30% of that base: roughly 80,000 to 110,000 people in the highest-pain segment.
- Adjacent roles who conduct structured discovery research (product strategists, growth leads, founders serving as their own PM) expand the addressable population to an estimated 150,000 to 200,000 professionals in the US.

At a Pro subscription price of $29 per month ($348 per year) and a 5% conversion rate across 200,000 addressable users, the US revenue opportunity is approximately $3.5M ARR at maturity. This is appropriate for an early-stage AI tools product proving product-market fit, not a claim of capturing a multi-billion dollar market.

Comparable PM tools validate willingness to pay at this price point: Reforge charges $2,000 per year, Lenny's Newsletter charges $150 per year, and Miro charges $10 to $16 per user per month. A tool that replaces weeks of manual research sits well within the range professionals have already demonstrated they will pay.

### The Gap in the Market

| Solution | What It Does | What It Misses |
|---|---|---|
| Perplexity | AI-assisted web research with sourced answers | No PM-specific workflow, no structured output, no quality scoring |
| ChatGPT / Claude (direct) | General-purpose AI for any task | No structured discovery format, no retrieval of PM methodology, no eval layer |
| Productboard AI | Synthesizes customer feedback already in Productboard | Requires existing data in Productboard, does not do discovery research |
| Dovetail | User research repository and analysis | Requires existing research data, not a discovery research tool |
| Gartner / Forrester reports | Deep market research for specific verticals | $2,000 to $5,000 per report, 12 to 18 months old, not PM-workflow integrated |
| Manual research (DIY) | Flexible and thorough if done well | 4 to 8 weeks, inconsistent quality, does not scale across teams |
| **Compass** | **Structured multi-agent discovery research with PM-written eval scoring** | **Nothing in this category exists today** |

### Why Now

Three specific conditions make this the right moment:

1. **Multi-step agent reasoning is production-ready.** Claude and similar models can now execute sequential, conditional tool calls with reliable output quality. The agentic workflow Compass requires was not achievable at production quality before 2024.

2. **AI-native companies are hiring PMs who can build with AI, not just manage it.** The signal they are looking for is not familiarity with AI tools. It is hands-on design and deployment of AI systems. A PM who built a production-grade multi-agent tool is meaningfully differentiated from one who uses ChatGPT for writing assistance.

3. **The cost of AI API access has dropped to the point where a per-query model is economically viable.** Running 6 to 7 Claude API calls per discovery brief costs approximately $0.40 to $0.80. At a $29/month Pro tier with 10 briefs per month, the API cost per user is under $8, leaving a sustainable margin.

---

## 3. Target Users

### Primary Persona: Maya, Senior Product Manager

**Who she is:**
Maya is a Senior PM at a mid-to-late stage technology company. She has 7 to 10 years of PM experience and owns a product area with 3 to 4 engineers and a designer. She is regularly asked to evaluate whether her team should pursue new markets, new features, or adjacent product bets. She knows what a rigorous discovery brief looks like because she has written dozens of them. Her constraint is not expertise. It is time.

**Her tools today:**
Google, Notion for documentation, ChatGPT for writing assistance, Perplexity for ad hoc research questions, Excel for competitive tracking.

**Her needs:**
- Get to a credible first-pass discovery brief in one sitting, not across three weekends
- Know which parts of the output are evidence-grounded and which are assumptions that need validation
- Produce consistent-quality output regardless of how much time she has available that week
- Be able to explain and defend every claim in the brief in a leadership review

**Her frustration in her own words:**
"I can tell you exactly what a great discovery brief looks like. I just never have the time to write one. By the time I am done, half the competitive data is already stale and I am defending assumptions I never had time to validate."

### Secondary Persona: Priya, Head of Product

**Who she is:**
Priya manages a team of 5 to 8 PMs. She cares less about her own discovery output and more about the consistency and quality of her team's output. When five PMs investigate five different markets, she gets five briefs of wildly different depth and quality. She wants a tool that raises the quality floor across her entire team, not just for her best PM.

**Her needs:**
- Consistent discovery brief quality across her team regardless of seniority
- A structured format that makes briefs comparable across different markets
- A quality score she can use to identify which briefs need more work before going to leadership

### Out of Scope (MVP)

- Junior PMs who are still learning what good discovery looks like (Compass surfaces insights; it does not teach the discipline)
- UX researchers whose discovery work focuses on qualitative user insight, not market and competitive analysis
- Executives who need summary-level strategic input, not discovery-level depth
- Non-PM roles (engineers, designers, marketers) conducting research for purposes other than product discovery

---

## 4. Product Vision and Strategy

### Vision

Give every PM, regardless of seniority or research budget, access to the quality of discovery that previously required a full research team.

### Strategic Position

Compass is not a research assistant and not a search engine. It is a structured discovery analyst that applies a consistent PM methodology to every problem it investigates. The difference is the eval layer: Compass does not just produce output, it scores that output against PM-written quality rubrics and shows the user where the reasoning is strong and where it is not.

Competitors can replicate the retrieval. They cannot easily replicate the eval framework, because that framework represents the PM's own judgment about what good discovery looks like, encoded into the system. That is the moat: the quality bar is defined by the PM, not by the AI.

### Product Principles

1. **Show your work.** Every factual claim in a Compass brief is sourced. Every assumption is labeled as an assumption. The user should always be able to trace where a claim came from.

2. **Score the output, not just produce it.** A brief with no quality signal is a brief the user cannot trust. Every section ships with a confidence score based on PM-written rubrics. The user knows what to rely on and what to verify.

3. **Specialize, do not generalize.** Each sub-agent has one job and one system prompt optimized for that job. A Problem Framing Agent that also sizes markets produces worse output on both tasks than two specialized agents doing one thing each.

4. **Web search for current data, RAG for PM methodology.** These two retrieval mechanisms serve different jobs. Web search provides recency. The PM methodology knowledge base provides structure and disciplined frameworks. Neither replaces the other.

5. **Latency is a product problem, not just an engineering problem.** A 90-second brief generation feels fast if the user can watch the agents working. A 90-second wait at a spinner feels slow. The UI must make the wait transparent and meaningful.

6. **Honest about confidence, not maximally hedged.** Compass should flag genuine uncertainty, not hedge every sentence out of caution. A brief that says "I don't know" on every claim is not useful. A brief that scores sections honestly and flags specific gaps is.

---

## 5. MVP Scope

### Design Principle

The MVP proves one thing: a multi-agent AI system with a PM-written eval layer produces discovery briefs that are faster to generate and more consistently structured than the manual process, for any problem space a PM might investigate.

### What MVP Includes

| Feature | Rationale |
|---|---|
| Problem statement input interface | The primary entry point; must be frictionless |
| Multi-agent orchestration pipeline (orchestrator plus 5 sub-agents) | Core product capability; the reason this is agentic, not just a prompted response |
| Real-time agent status display | Makes the 60 to 90 second wait transparent; shows the system working |
| Structured 5-section discovery brief output | The deliverable; each section produced by a specialized agent |
| PM-written eval scoring per section | The quality mechanism; differentiates Compass from raw AI output |
| Source attribution per factual claim | Required for trust; PM must be able to defend every claim |
| RAG-based PM methodology retrieval | Ensures agents apply structured PM frameworks, not generic reasoning |
| Web search via MCP (Tavily integration) | Provides current market and competitive data for each brief |
| Desktop-responsive frontend | Primary use case is a sit-down research session, not mobile |

### What MVP Excludes (and Why)

| Excluded | Reason |
|---|---|
| Saved brief history | Adds database complexity; not needed to prove core value |
| PDF or Notion export | Useful but not core to proving the brief quality hypothesis |
| User accounts and authentication | Adds friction and build time; not required for portfolio demo |
| Custom eval rubrics (user-defined) | High complexity; PM-written rubrics ship as system defaults in MVP |
| MCP integrations beyond web search (Google Drive, Notion, Jira) | Each adds significant build time; web search alone is sufficient to demonstrate MCP |
| Team collaboration features | Secondary persona (Priya) is not the MVP user |
| Multi-language support | English-only is sufficient for the target beachhead market |
| Brief comparison across multiple runs | Post-MVP once usage patterns are understood |
| Mobile app or mobile-optimized layout | Discovery research is a desktop use case |

---

## 6. AI Architecture

This section documents the AI system design decisions that underpin Compass. These are product decisions, not just engineering decisions, because they directly determine output quality, latency, cost, and reliability.

### Why Multi-Agent, Not Single-Agent

A single Claude call given a problem statement and asked to produce a 5-section discovery brief will produce output that is structurally complete but qualitatively shallow. Each section competes for attention within a single context window. The agent cannot go deep on competitive analysis if it is also managing market sizing and risk identification simultaneously.

Five specialized sub-agents, each with a focused system prompt and dedicated tools, produce meaningfully better output on their specific section. The Problem Framing Agent only thinks about problem framing. The Competitive Analysis Agent only thinks about competitive analysis. Specialization improves depth.

The orchestrator exists to route, pass context between agents in the right sequence, and synthesize the final brief. It does not do analysis itself.

### Agent Inventory

| Agent | Responsibility | Primary Tool |
|---|---|---|
| Orchestrator | Creates the research plan, sequences sub-agents, synthesizes final output | None (coordination only) |
| Problem Framing Agent | Identifies the specific user, the pain, and the cost of not solving it | RAG (JTBD frameworks) |
| Market Research Agent | Finds current market size data, growth trends, industry signals | Web search via MCP |
| Competitive Analysis Agent | Maps existing solutions and their specific gaps | Web search via MCP |
| Opportunity Sizing Agent | Estimates TAM using market data from prior agents, with explicit assumptions | RAG (sizing methodologies) |
| Risk Assessment Agent | Identifies product, market, technical, and adoption risks | RAG (risk pattern library) |
| Eval Agent | Scores all 5 sections against PM-written rubrics | None (scoring only) |

### Execution Sequence and Dependencies

```
User Input
    |
Orchestrator (creates plan)
    |
Problem Framing Agent          <- runs first; output needed by all subsequent agents
    |
Market Research Agent          <- runs second; output needed by Opportunity Sizing
Competitive Analysis Agent     <- runs in parallel with Market Research (no dependency)
    |
Opportunity Sizing Agent       <- requires Market Research output
    |
Risk Assessment Agent          <- requires all prior agent outputs
    |
Eval Agent                     <- scores all 5 sections; runs last
    |
Final Brief displayed to user
```

Market Research and Competitive Analysis run in parallel because neither depends on the other's output. All other steps are sequential due to data dependencies.

### Why RAG, Not Prompt Stuffing

The PM methodology knowledge base contains 50 to 75 curated documents covering JTBD frameworks, market sizing methodologies, competitive analysis approaches, risk pattern libraries, and annotated examples of high-quality discovery briefs. This content is stable, high-quality, and specific enough to go beyond Claude's general training data.

Rather than including all 50 to 75 documents in every system prompt (expensive, slow, and beyond context window limits), agents retrieve only the 3 to 5 most relevant documents for their specific task using semantic similarity search against a Pinecone vector index. A Problem Framing Agent retrieving the 3 most relevant JTBD frameworks for a healthcare problem gets better grounding than one working from general training data alone.

Web search handles current, domain-specific information that cannot be pre-loaded because it changes continuously. RAG handles stable PM methodology that does not require currency but does require precision and quality.

### Why MCP, Not Direct API Calls

The Model Context Protocol provides a standardized interface between Claude and external tools. Rather than writing a custom integration for each data source (Tavily for web search, Pinecone for RAG, future integrations for Notion or Google Drive), MCP exposes all tools through a consistent protocol that Claude can call without per-tool custom code.

The MVP MCP server exposes two tools:

- `search_web(query: string)`: calls Tavily API and returns structured search results
- `retrieve_framework(topic: string, top_k: int)`: queries Pinecone and returns the top-k most relevant PM methodology documents

Adding a third tool (e.g., `read_notion_page(page_id)` for future MCP expansion) requires adding one tool definition to the MCP server, not rewriting the agent.

### Eval Framework

Each section of the discovery brief is evaluated by the Eval Agent using PM-written rubrics. The rubrics are defined before any code is written and represent the PM's own judgment about what good discovery output looks like.

**Problem Framing rubric (scored 0 to 10 per criterion):**
- Specificity of user identified (0: "users," 10: named segment with demographic and behavioral context)
- Evidence vs. assumption ratio (0: all assertions, no sources, 10: every claim sourced or labeled as assumption)
- Cost of the problem (0: vague "it's frustrating," 10: specific time, money, or outcome cost stated)

**Market Research rubric:**
- Recency of data (0: no dates cited, 10: all data from within 18 months)
- Quantification (0: qualitative only, 10: market size with visible math)
- Source diversity (0: single source, 10: three or more independent sources)

**Competitive Analysis rubric:**
- Coverage of alternatives (0: only named competitors, 10: includes DIY workarounds and manual approaches)
- Specificity of gaps (0: "existing solutions are inadequate," 10: named gap for each solution)
- Positioning clarity (0: unclear why Compass would be different, 10: clear differentiation stated)

**Opportunity Sizing rubric:**
- Math visibility (0: number with no derivation, 10: full TAM logic visible with each assumption labeled)
- Assumption honesty (0: presented as fact, 10: every assumption labeled with confidence level)
- Scenario range (0: single point estimate, 10: low/base/high range with drivers named)

**Risk Assessment rubric:**
- Naming the hardest risks (0: generic risks only, 10: hardest specific risks for this product named)
- Mitigation specificity (0: "we will monitor," 10: specific action that reduces likelihood or impact)
- Risk completeness (0: one or two risks, 10: four or more distinct risk categories covered)

The Eval Agent receives each completed section alongside the relevant rubric and scores each criterion. The section score is the average of its criteria scores, converted to a 0 to 100 scale. The overall brief score is the average of all section scores.

---

## 7. Data Strategy

### Knowledge Base: PM Methodology Library

**What it contains:** 50 to 75 curated documents organized into five categories:

1. Problem framing frameworks (JTBD theory, pain mapping, user segmentation approaches): 12 to 15 documents
2. Market sizing methodologies (TAM/SAM/SOM approaches, analogous market sizing, bottom-up vs. top-down): 8 to 10 documents
3. Competitive analysis frameworks (Porter's Five Forces adapted for tech, positioning maps, gap analysis): 8 to 10 documents
4. Risk identification patterns (common product failure modes, cold start risks, adoption risks, competitive response patterns): 10 to 12 documents
5. Annotated examples of high-quality discovery briefs with inline commentary: 12 to 15 documents

**Sources:** Publicly available PM writing from First Round Review, Lenny's Newsletter, SVPG, Reforge (public posts), and Sonal Singh's own portfolio case studies. No proprietary or paywalled content.

**Embedding and indexing:** Each document is chunked into 400 to 500 token segments with 50 to 100 token overlap. Chunks are embedded using OpenAI's text-embedding-3-small model (1,536 dimensions) and stored in a Pinecone serverless index. Total index size at MVP: approximately 800 to 1,200 vectors, well within Pinecone's free tier limits.

**Maintenance:** The knowledge base is a curated, stable asset that does not require real-time updates. A quarterly review process identifies outdated frameworks and adds new ones as PM practice evolves. This is a manual process requiring approximately 4 to 6 hours per quarter.

### Web Search: Current Market Data

Web search via the Tavily API provides real-time market information that the knowledge base cannot supply: current market size estimates, recent competitor news, funding announcements, and industry trends. Each sub-agent that requires current data (Market Research Agent, Competitive Analysis Agent) makes 2 to 3 targeted search queries through the MCP server.

Tavily API pricing: $0.001 per search. At 5 searches per brief, web search cost is under $0.01 per brief and is not a meaningful cost driver.

### Eval Rubrics: Authorship and Versioning

The eval rubrics are the PM's primary artifact in this system. They represent explicit, encoded judgment about what good discovery output looks like. They are written before the system is built and are versioned as the product evolves.

MVP rubrics cover all 5 sections (as documented in the AI Architecture section above). Rubrics are stored as structured JSON and loaded into the Eval Agent's system prompt at runtime. Version control is handled via the code repository. Changes to rubrics are treated as product decisions, not engineering changes, and require review before deployment.

### Pinecone Launch Gate

Compass will not be made publicly accessible until the following knowledge base conditions are met:
- Minimum 50 documents indexed across all 5 framework categories
- Minimum 8 documents per category (no category can be sparse)
- Semantic search tested with 20 diverse PM problem statements and retrieval quality validated manually

---

## 8. Feature Specifications

### 8.1 Problem Statement Input Interface

**Overview:**
The entry point for every Compass session. The PM types a problem statement and clicks Analyze. The interface must make it easy to write a good problem statement and set clear expectations for what the tool will produce.

**Key behaviors:**
- Single text area, minimum 50 characters, maximum 500 characters
- Placeholder text provides 3 example problem statements to guide first-time users
- A "writing tips" tooltip explains what makes a good problem statement: specific user named, specific pain described, not a solution
- Submit triggers immediate loading state with agent status panel

**Edge cases:**
- Input under 50 characters: inline validation message "Add more context for better results" before submission is allowed
- Input that describes a solution rather than a problem: the Problem Framing Agent's system prompt is designed to identify and reframe solution-framed inputs. The UI does not attempt to validate this before submission.
- Non-English input: supported by Claude's multilingual capability but not optimized for MVP. If non-English input produces poor results, the user sees the standard output with a potentially lower eval score.

**Design principle:** The input interface should feel like briefing a smart research analyst, not configuring a software tool.

### 8.2 Agent Orchestration Pipeline

**Overview:**
The backend system that coordinates the multi-agent workflow. The orchestrator receives the problem statement, creates a research plan, dispatches sub-agents in the correct sequence (with parallelism where dependencies allow), and compiles the final brief.

**Key behaviors:**
- Orchestrator produces a research plan (internal, not shown to user) that sequences the sub-agents based on the problem statement
- Problem Framing Agent runs first; its output is passed as context to all subsequent agents
- Market Research and Competitive Analysis agents run in parallel
- Opportunity Sizing Agent waits for Market Research output before starting
- Risk Assessment Agent receives all prior outputs as context
- Eval Agent runs after all 5 sections are complete

**Agent-to-agent context passing:**
Each agent receives: (1) the original problem statement, (2) the relevant framework documents retrieved from RAG, (3) outputs from all agents that ran before it. Context is managed to stay within each agent's token budget (approximately 8,000 tokens per agent call).

**Edge cases:**
- Web search returns no relevant results for a specific query: the agent proceeds with RAG-only context and the affected section receives a lower confidence score reflecting the absence of current data
- An agent call fails (API timeout, rate limit): the orchestrator retries once, then marks the section as "unavailable" and continues. The brief is delivered with a partial section and an explanation.
- Generation exceeds 120 seconds total: a timeout message is shown with the partial brief displayed

**Design principle:** The pipeline should be observable. Every agent transition is visible to the user in real time.

### 8.3 Real-Time Agent Status Display

**Overview:**
A live panel showing which agent is currently running, which have completed, and which are queued. This turns the 60 to 90 second generation time from an opaque wait into a transparent process.

**Key behaviors:**
- Panel shows all 7 agents (orchestrator, 5 sub-agents, eval agent) with status indicators: queued, running, complete
- Running agent shows a brief description of what it is doing ("Researching current market data...")
- Completed agent shows a checkmark and the time it took
- Section content appears in the output panel as each agent completes (streaming display, not all at once at the end)
- Eval scores appear as the final step after all sections are scored

**Edge cases:**
- User closes the browser tab during generation: generation continues on the backend. If user returns within 10 minutes, the completed brief is displayed. After 10 minutes, the session expires.
- An agent takes longer than 30 seconds on a single step: a "still working" indicator appears so the user knows the system has not stalled.

**Design principle:** The user should always know what the system is doing and why it is taking the time it is taking.

### 8.4 Discovery Brief Output

**Overview:**
The structured 5-section output of the Compass pipeline. Each section is produced by a dedicated sub-agent and displayed with its source citations and eval score.

**Section structure (per section):**
- Section title and brief description of what this section covers
- Agent-produced content (2 to 4 paragraphs or structured bullets, depending on section)
- Source citations: each factual claim links to its web search source or indicates it comes from the PM methodology library
- Eval score: numeric score (0 to 100) with a one-line explanation of the highest-impact scoring factor
- "Assumptions flagged" count: number of claims in this section labeled as unverified assumptions

**Overall brief:**
- A brief-level quality score (average of all 5 section scores) displayed prominently at the top
- A one-paragraph executive summary generated by the orchestrator synthesizing all 5 sections
- A "suggested next steps" section generated by the Risk Assessment Agent based on the open questions identified

**Edge cases:**
- A section scores below 50: a callout box appears: "This section has low confidence. Suggested action: [specific validation step]."
- A source URL returns a 404 error when clicked: the citation shows as "source no longer available" rather than a broken link.
- The problem statement is extremely broad (e.g., "help people be happier"): the Problem Framing Agent narrows the scope and explains its framing decision in the section output.

**Design principle:** Every section should answer the question "how much should I trust this?" before the reader finishes reading it.

### 8.5 Eval Scoring Display

**Overview:**
The mechanism by which Compass shows the PM the quality of each section, grounded in PM-written rubrics.

**Key behaviors:**
- Each section displays a score bar (0 to 100) with a color indicator: green (75 to 100), yellow (50 to 74), red (0 to 49)
- Clicking the score bar expands a rubric breakdown showing the score for each individual criterion and a one-sentence explanation
- The overall brief score aggregates all section scores and is shown at the top of the brief
- A "what to do about this" prompt appears for any criterion scoring below 5 out of 10

**Edge cases:**
- All sections score above 85: a "high confidence brief" badge appears at the top with the message "This brief is well-grounded. Most sections have strong evidence. Review assumptions flagged before presenting to leadership."
- A section score is disputed by the user: a "flag this score" button allows the user to note disagreement. This data is collected for rubric improvement (post-MVP feature).

**Design principle:** The eval display should feel like a trusted colleague giving specific, honest feedback, not an AI self-congratulating on its own output.

---

## 9. User Stories

### Problem Input
- As a senior PM, I want to describe a problem in plain language so that I do not need to learn a specific query format to get useful output.
- As a senior PM, I want to see example problem statements so that I understand what level of specificity produces the best results.

### Discovery Process
- As a senior PM, I want to see which agents are running and what they are doing so that the wait time feels purposeful rather than opaque.
- As a senior PM, I want to see each brief section appear as it is completed so that I can begin reading before the full brief is finished.

### Discovery Output
- As a senior PM, I want a structured 5-section discovery brief so that I have a consistent starting point for any executive presentation.
- As a senior PM, I want every factual claim in the brief to be sourced so that I can defend it in a leadership review without doing additional research.
- As a senior PM, I want unverified assumptions explicitly labeled so that I know which claims need further validation before I present them.

### Eval Scoring
- As a senior PM, I want each section of the brief scored against a quality rubric so that I know where to focus my time on further research.
- As a senior PM, I want to understand why a section scored low so that I can take a specific action to address the gap.
- As a senior PM, I want the scoring criteria explained in PM language so that I can trust the rubric reflects real quality standards.

### Overall Brief
- As a senior PM, I want a brief-level confidence score so that I can quickly assess whether the output is ready to share with stakeholders.
- As a senior PM, I want suggested next steps from the tool so that I know what to validate before moving forward.

---

## 10. Success Metrics

### North Star Metric

**Metric:** Brief Quality Score

**Definition:** The average eval score (0 to 100) across all sections of all briefs generated in a given week. This is the single best proxy for whether Compass is doing its job: producing high-quality, well-grounded discovery output.

**Target:** Average weekly brief quality score of 72 or higher within 60 days of launch.

**Baseline:** 0 (product does not yet exist). A manually written discovery brief from a senior PM, graded against the same rubric, consistently scores 65 to 80. Compass should match or exceed average human performance.

### Engagement Metrics

| Metric | Definition | Target (60 days post-launch) |
|---|---|---|
| Briefs completed per user | Number of full briefs generated per unique user | 3+ |
| Completion rate | Percentage of submissions that result in a completed brief (not abandoned) | 85% |
| Time to brief | Median time from submission to full brief displayed | Under 90 seconds |
| Section re-run rate | Percentage of users who re-run a specific section | Under 20% (high re-run = low satisfaction) |

### Quality Metrics

| Metric | Definition | Target |
|---|---|---|
| Average section score | Mean eval score per section across all briefs | 70+ |
| Low-confidence section rate | Percentage of sections scoring below 50 | Under 15% |
| Source citation rate | Percentage of factual claims with a source link | 80%+ |
| Assumption flag accuracy | Percentage of flagged assumptions confirmed as unverified by users who review | [PLACEHOLDER - requires user feedback mechanism] |

### Business Metrics (Portfolio Project Context)

| Metric | Definition | Target (90 days) |
|---|---|---|
| Unique visitors | Unique visitors to the Compass portfolio page | 500+ |
| Brief generation rate | Total briefs generated by visitors | 200+ |
| Return visitor rate | Percentage of users who return for a second session | 30%+ |

### What We Will Not Measure (Yet)

- Revenue: Compass is a portfolio project, not a commercial product, so revenue metrics are not applicable to the MVP
- NPS or user satisfaction surveys: requires a critical mass of users to be statistically meaningful
- Cost per brief: tracked internally for architecture decisions but not a user-facing metric in MVP

---

## 11. Business Model

### Context

Compass is a portfolio project designed to demonstrate AI PM capability, not a commercial product in the MVP phase. The business model below is documented to show the PM's thinking about commercial viability, not as a deployment plan.

### Revenue Streams

**Stream 1: Pro Subscription (Individual PM)**

| Tier | Price | Included |
|---|---|---|
| Free | $0 | 3 briefs per month, watermarked output, standard model |
| Pro | $29 per month | Unlimited briefs, no watermark, priority model access, brief history |

Pricing rationale: $29 per month ($348 per year) is below the $2,000 per year threshold of tools like Reforge and well within the willingness to pay established by Lenny's Newsletter ($150 per year) and Miro ($10 to 16 per user per month). A tool that replaces weeks of research justifies this price point.

**Stream 2: Team Tier**

| Tier | Price | Included |
|---|---|---|
| Team | $99 per month | Up to 5 seats, team-level quality dashboard, consistent rubric enforcement |
| Enterprise | [PLACEHOLDER: custom pricing] | Unlimited seats, custom eval rubrics, API access, SSO |

### Unit Economics (Illustrative)

Assumptions:
- Average Pro user generates 10 briefs per month
- API cost per brief: $0.40 to $0.80 (6 to 7 Claude API calls at Claude Sonnet 4.6 pricing, plus Tavily search at $0.005 per brief)
- Infrastructure cost per user per month: $0.50 (Railway backend, Pinecone free tier at MVP scale)

At $29 per month Pro revenue:
- API and infrastructure cost: $4.50 to $8.50 per user per month
- Gross margin per Pro user: $20.50 to $24.50 (71% to 84%)
- Payback period at $0 CAC (organic discovery via portfolio): immediate

At 1,000 Pro users:
- Monthly revenue: $29,000
- Monthly costs (API plus infrastructure): $4,500 to $8,500
- Monthly gross profit: $20,500 to $24,500
- Annual run rate: $246,000 to $294,000

This math is illustrative, not a financial projection. It demonstrates the business can work at scale, not that it will.

---

## 12. Go-to-Market Strategy

### Beachhead Market

PMs at AI-native and AI-forward technology companies in the San Francisco Bay Area. Specifically: PMs who are already using Claude or ChatGPT for research tasks and are frustrated by the lack of structure and quality scoring in the output.

This segment is chosen for three reasons:
1. They already believe AI can help with PM work. The activation hurdle is lower.
2. They are concentrated on LinkedIn and in PM communities (Reforge, Lenny's Newsletter) where Sonal already has a professional presence.
3. They are the most likely to share Compass with colleagues and write about it on LinkedIn, which is the primary organic growth motion.

### Growth Strategy

**Phase 1: Portfolio launch and PM community seeding (Months 1 to 2)**

- Compass goes live on the portfolio site at sonalsingh-pm.netlify.app
- Sonal posts a LinkedIn case study: "I built a multi-agent AI discovery tool. Here is how it works and a real brief it produced for a problem I investigated."
- The post includes a live link to Compass and one complete example brief
- Target: 200 unique visitors, 50 briefs generated

**Phase 2: Community distribution (Months 2 to 4)**

- Share Compass in Reforge Slack community, Lenny's Newsletter subscriber community, and PM Slack groups
- Write a technical breakdown post: "How I used RAG, agents, and evals to build a PM research tool" targeted at AI-curious PMs
- Target: 500 unique visitors, 200 briefs generated, 30% return rate

**Phase 3: Refinement based on usage (Months 4 to 6)**

- Review the 200+ briefs generated for quality patterns
- Identify which problem statement types produce the best and worst results
- Update eval rubrics and agent prompts based on observed failure modes
- This is the research-sync step that informs the case study

### Why This Works

The viral motion is the brief itself. A PM who generates a compelling discovery brief using Compass is likely to share it in a Slack channel or team meeting. "How did you produce this so fast?" is the organic question that drives word of mouth. The product demonstrates its own value in the output, not in the description.

---

## 13. Launch Readiness

### Quality Gates (All must be true before public access)

- [ ] RAG knowledge base contains a minimum of 50 documents, minimum 8 per category, retrieval quality validated across 20 diverse test prompts
- [ ] All 5 sub-agents and the orchestrator have been tested with a minimum of 15 problem statements each across different industries and problem types
- [ ] Eval rubrics have been validated by grading 10 manually written discovery briefs and confirming scores align with PM judgment
- [ ] End-to-end brief generation time is under 90 seconds for 80% of test runs
- [ ] Source citations are present and correct for 90%+ of factual claims in test briefs
- [ ] Frontend displays correctly in Chrome, Safari, and Firefox on desktop
- [ ] API error handling tested: a failed agent call produces a graceful degraded output, not a crash
- [ ] Claude API key and Tavily API key are stored as environment variables on Railway and are not exposed to the client

### Launch Sequence

1. Knowledge base built and indexed in Pinecone (Week 1)
2. Backend agents built and tested individually (Weeks 2 to 3)
3. Agent pipeline integrated and tested end-to-end with 15+ problem statements (Week 3)
4. Frontend built and connected to backend (Week 4)
5. Eval rubrics finalized and Eval Agent tested (Week 4)
6. End-to-end QA across browsers (Week 5)
7. Portfolio card added and LinkedIn post drafted (Week 5)
8. Public launch (Week 6)

### Rollback Plan

If Compass produces low-quality briefs at launch (brief quality score average below 55 across the first 20 visitor-generated briefs), the portfolio card is updated to "coming soon" and the Netlify deployment is restricted to password protection while the agent prompts and rubrics are revised. The product is not taken down entirely: a password-protected version remains accessible for interview demos.

---

## 14. Risks and Mitigations

### Risk 1: AI Hallucination Producing Confident but Wrong Market Data

**Risk:** The Market Research Agent produces a market size figure that sounds authoritative but is fabricated or from a misread source. A PM presents this to leadership and is embarrassed when it cannot be verified.

**Likelihood:** Medium. Claude is strong at web search synthesis but will occasionally confabulate numbers when sources are ambiguous.

**Impact:** High. Trust is the core product. One high-profile hallucination damages credibility for every brief produced.

**Mitigation:** Every numeric claim must include a source citation or be labeled as an assumption. The eval rubric penalizes unsourced quantitative claims. Ongoing: a red-team exercise after every rubric update, specifically testing whether the system produces unsourced numbers.

### Risk 2: Generation Latency Exceeds User Tolerance

**Risk:** The 6 to 7 sequential (and partially parallel) API calls take 120 seconds or more, and users abandon before the brief is complete.

**Likelihood:** Medium. API call latency is variable and can spike.

**Impact:** Medium. Affects user experience and completion rate; does not affect brief quality.

**Mitigation:** Streaming display means users see content appearing within 15 to 20 seconds of submission, not at the end. The agent status panel makes the wait transparent. Target maximum generation time of 120 seconds; if exceeded, a partial brief is shown with a "still generating" indicator. On the backend: parallelism is maximized where dependencies allow (Market Research and Competitive Analysis run simultaneously).

### Risk 3: API Cost Exceeds Budget at Scale

**Risk:** Unexpected traffic drives Claude API costs above what the free-tier Railway deployment and personal API budget can absorb.

**Likelihood:** Low for a portfolio project but non-zero if a post goes viral.

**Impact:** Low to medium. Cost is manageable at portfolio scale; a viral post could create a $100 to $500 unplanned expense.

**Mitigation:** Rate limiting on the backend: maximum 3 briefs per IP address per day. A cost monitoring alert is set at $50 and $100 on the Anthropic dashboard. The rollback plan (restrict to password protection) is available if costs spike unexpectedly.

### Risk 4: Output Quality Variance Across Problem Spaces

**Risk:** Compass produces excellent briefs for tech product problems and mediocre briefs for niche or specialized domains (healthcare regulatory, defense, deep B2B enterprise) where web search returns low-quality results.

**Likelihood:** High. Web search quality is highly correlated with how much public information exists about a domain.

**Impact:** Medium. Affects some users significantly; does not affect the core portfolio demonstration.

**Mitigation:** The eval scoring system naturally surfaces this: low-confidence sections score lower and trigger "suggested actions." The case study will document this limitation explicitly and describe it as an intended product decision (Compass is optimized for tech product discovery, not all domains). Post-MVP: domain-specific knowledge bases for healthcare, fintech, etc.

### Risk 5: The Portfolio Demo Feels Too Technical for Non-Technical Interviewers

**Risk:** An interviewer who is not familiar with agents, RAG, or MCP sees a "fancy AI chatbot" rather than a sophisticated AI system and misses the depth of the product decisions.

**Likelihood:** Medium. Not all hiring managers at PM roles have deep AI literacy.

**Impact:** Low. Interviewers with AI literacy will be impressed. Interviewers without it still see a working product that solves a real problem.

**Mitigation:** The case study is written to be legible at two levels: a non-technical PM can follow the product story, and a technical interviewer or AI-native hiring manager can engage with the architecture decisions. The PRD and case study are linked from the portfolio card so the full depth of thinking is accessible to anyone who wants it.

---

## 15. Open Questions

| Question | Why It Matters | How to Resolve |
|---|---|---|
| What confidence threshold should trigger a "low confidence" section alert? | Too low a threshold (e.g., below 70) creates alert fatigue; too high a threshold (below 40) misses real quality gaps | Start at 50 and adjust based on the first 50 briefs generated |
| Should the eval rubric be visible to users by default or on-demand? | Visible rubric increases transparency but may overwhelm first-time users | Show rubric on-demand via an expandable "why this score?" UI element |
| Does the parallel execution of Market Research and Competitive Analysis cause context bleed in the Opportunity Sizing Agent? | If both agents write to a shared context, the Opportunity Sizing Agent may receive contradictory signals | Test with 10 problem statements; if observed, add an orchestrator synthesis step before Opportunity Sizing |
| How should Compass handle problem statements about markets where public web search returns mostly paywalled content? | Affects output quality for enterprise, healthcare, and finance domains significantly | Document as a known limitation in the UI; add a tooltip on the input form: "Compass works best for consumer tech, B2B SaaS, and e-commerce problems" |
| What is the right level of section length? | Sections that are too long add reading time without adding precision; too short feels superficial | Set a 200 to 350 word target per section in each agent's system prompt; adjust based on user feedback |

---

## 16. Future Roadmap

### Near Term (Months 3 to 6 post-launch)

- **User-defined eval rubrics:** Allow PMs to modify the default rubrics to reflect their organization's quality standards
- **Brief history and versioning:** Save briefs so users can compare two analyses of the same problem over time
- **MCP expansion to Notion and Google Drive:** Connect Compass to the PM's existing research documents so the agents have access to proprietary context, not just public web data
- **Domain-specific knowledge bases:** Add specialized PM methodology libraries for healthcare, fintech, and enterprise B2B, with domain-appropriate eval rubrics

### Medium Term (Months 6 to 12)

- **Team features:** Shared rubrics, team-level quality dashboard, brief comparison across team members
- **Structured input templates:** Instead of free-form problem statements, guided input for specific scenarios (new market entry, feature investment, competitive response)
- **Brief export to Notion and Confluence:** One-click export with formatted output that drops directly into the PM's existing documentation workflow
- **Longitudinal brief tracking:** Monitor how competitive landscapes change over time by re-running a brief quarterly and surfacing what changed

### Longer Term (Year 2)

- **Agent personalization:** Compass learns which eval criteria a specific PM consistently overrides and adjusts rubrics to match their individual standards over time
- **Integration with product roadmap tools:** Connect brief insights to Productboard, Linear, or Jira so discovery outputs flow directly into backlog prioritization
- **Multi-language support:** Extend Compass to discovery research in Spanish, French, German, and Japanese markets

---

## 17. Appendix

### Competitive Landscape Summary

| Tool | Structured PM Workflow | Multi-Agent | Eval Scoring | RAG | MCP | PM-Specific |
|---|---|---|---|---|---|---|
| Perplexity | No | No | No | Partial | No | No |
| ChatGPT / Claude (direct) | No | No | No | No | No | No |
| Productboard AI | Partial | No | No | No | No | Yes (feedback only) |
| Dovetail | Partial | No | No | No | No | Yes (research repo) |
| Gartner reports | Yes | N/A | No | N/A | N/A | Partial |
| **Compass** | **Yes** | **Yes** | **Yes** | **Yes** | **Yes** | **Yes** |

### Assumptions Log

| Assumption | Confidence | Validation Needed |
|---|---|---|
| Senior PMs will pay $29/month for structured AI discovery briefs | Medium | Test with 10 senior PMs in Reforge community |
| A 50-to-75 document PM methodology library is sufficient to ground agent outputs meaningfully | Medium | Test with 20 diverse problem statements and compare outputs against briefs written without RAG |
| Average brief generation time will be under 90 seconds in production | Medium | Benchmark with 20 test runs after pipeline is complete |
| Eval scores from Claude-as-judge align with PM judgment on what "good" looks like | Medium | Grade 10 manually written briefs, compare Claude scores to human scores |
| Web search provides sufficient current data for most tech product discovery use cases | High | Test with 15 diverse tech product problem statements |
| The parallel execution of Market Research and Competitive Analysis is safe (no context conflicts) | Low | Explicitly test and validate before launch |
| LinkedIn post will drive meaningful portfolio traffic | Low | Cannot be validated before launch; success depends on post reach and community resonance |
| 50 documents per category is sufficient to demonstrate RAG value to a technical interviewer | Medium | Ask 3 AI-literate PMs to review the architecture section and assess whether the RAG usage is credible |

---

*Compass is a portfolio project created to demonstrate end-to-end AI product design, multi-agent system thinking, and hands-on implementation capability. It does not represent a commercially deployed product.*

*Author: Sonal Singh | Principal Product Manager | sonalshankar06@gmail.com*
