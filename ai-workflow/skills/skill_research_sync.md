# SKILL: Research Synthesis (research-sync)

## Purpose
Research synthesis turns raw notes from user interviews, prototype testing, or observation sessions into structured, actionable insights. It is the bridge between talking to users and making better product decisions.

World class research synthesis does not just summarize what users said. It finds the patterns underneath, names the insights that were not obvious before the research, and connects them directly to PRD assumptions and product decisions.

---

## When to Run research-sync

Run this command after:
- Completing user interviews (even informal ones — a conversation with 2 parents counts)
- Testing a prototype with real users
- Observing users in their natural environment
- Receiving feedback on a shared prototype or PRD
- Collecting survey responses

Do not wait until you have "enough" research. Two conversations produce insights. Run synthesis after every round of learning.

---

## Input Format

Provide raw notes in any format:
- Bullet points from interviews
- Direct quotes
- Observations during prototype testing
- Survey responses
- Informal feedback received

The messier the input, the more value synthesis adds.

---

## Output Structure

### 1. Research Summary (3-5 sentences)
Who was researched, how many people, what method, when. Be honest about the sample size and its limitations.

**Example:**
"Spoke with 4 working parents in the Bay Area, all dual-income households with at least one school-age child. Conducted 20-minute semi-structured interviews focused on their summer camp planning process. Sample is small and skewed toward tech industry parents — findings should be validated with a broader sample before major product decisions."

### 2. Key Themes (3-5 themes)
Group findings into themes. Each theme should have a name, a one-sentence description, and supporting evidence from the raw notes.

**Format:**
```markdown
**Theme: [Name]**
[One sentence describing the pattern]

Supporting evidence:
- "[Direct quote or observation]" — [User descriptor, e.g. "Parent of 2, San Jose"]
- "[Direct quote or observation]"
- [Observation from prototype testing]
```

### 3. Surprising Findings
What did you learn that you did not expect? These are the most valuable insights — they reveal where your assumptions were wrong.

List 2-3 specific surprises with evidence.

### 4. Assumption Validation
Go through the Assumptions Log in the PRD. For each assumption, state whether this round of research validated, invalidated, or left it unresolved.

**Format:**
```markdown
| Assumption | Status | Evidence |
|---|---|---|
| Parents spend 3+ hours on camp planning | Validated | All 4 participants confirmed multiple hours across multiple sessions |
| Social coordination drives adoption | Partially validated | 3 of 4 mentioned friends' choices matter; 1 said they decide independently |
| Desktop is the right primary surface | Unresolved | Not tested in this round |
```

### 5. Product Implications
What should change in the PRD or prototype based on this research? Be specific — name the section or feature and the proposed change.

**Format:**
```markdown
**Finding:** Parents care more about knowing where friends are going than about price filtering.
**Implication:** Move social coordination features from Premium tier to Free tier. Reconsider whether price filter is a top-priority filter or secondary.
**Recommended action:** Update PRD Section 10 (Business Model) to move friend visibility to free tier. Reprioritize filter order in prototype.
```

### 6. Open Questions
What questions did this research raise that need further investigation?

List 2-4 specific questions with a proposed method for answering each.

---

## Quality Standards

**What makes world class synthesis:**
- Specific — "3 of 4 parents said" not "most parents said"
- Honest about sample limitations
- Connects findings directly to PRD assumptions
- Names specific product implications with recommended actions
- Includes direct quotes — they are more compelling than paraphrases
- Acknowledges what was NOT learned as clearly as what was learned

**Common mistakes to avoid:**
- Confirming what you already believed and ignoring contradictory signals
- Synthesis that is just a summary of what people said — not insight
- No connection to PRD assumptions or product decisions
- Overstating confidence from a small sample
- Burying the most important finding in the middle

---

## Quality Checklist

Before delivering a research synthesis, verify:
- [ ] Sample is described honestly including limitations
- [ ] Themes are named and have supporting evidence with quotes
- [ ] At least one surprising finding is included
- [ ] Every major PRD assumption has a validation status
- [ ] Product implications are specific — name the section and the proposed change
- [ ] Recommended actions are concrete and assigned
- [ ] Open questions are listed with proposed resolution methods
- [ ] Direct quotes are used — not just paraphrases