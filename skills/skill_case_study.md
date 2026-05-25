# SKILL: Writing a GitHub-Ready Case Study (README.md)

## Purpose
The case study is what a hiring manager reads when they click on your GitHub project. It is your interview answer in written form. A world class case study makes a CPO or hiring manager say "I need to talk to this person" — not "interesting, I'll keep looking."

The case study is not a summary of the PRD. It is a story about how you think — the problem you saw, the decisions you made, the tradeoffs you navigated, and what you learned.

---

## Before Writing — Answer These Questions

1. **What was the single most important insight that shaped the product?** This is your lead.
2. **What was the hardest decision you made and why?** This shows strategic thinking.
3. **What did you choose NOT to build and why?** This shows scope discipline.
4. **What did you learn from testing or research that surprised you?**
5. **What would you do differently if you started over?**
6. **What would you build next and why?**

If you cannot answer all six, the project is not ready for a case study.

---

## Structure

### Header
```markdown
# [Product Name]
### [One-line tagline — what it does and for whom]

[2-3 sentence executive summary: problem, solution, what was built]
```

### Section 1 — The Problem
**Target length:** 150-200 words

Tell the story of the problem. Not a bullet list — a narrative. Where does the pain come from? Who feels it? What do they do today that is broken?

If there is a personal origin story — lead with it. "As a working parent, I spent three weekends building a Google Sheet to track summer camps. When two other parents started using it without being asked, I knew the problem was real."

**What makes it world class:**
- Reads like a human being wrote it — not a PM template
- The pain is vivid and specific
- The reader understands who suffers and why

### Section 2 — My Approach
**Target length:** 150-200 words

How did you think about this problem? What framework or lens did you use? What questions did you ask before deciding what to build?

This section shows your product thinking process — not just the output.

**What makes it world class:**
- Shows the reasoning behind decisions, not just the decisions
- References specific tradeoffs considered
- Demonstrates customer empathy and market awareness

### Section 3 — What I Built
**Target length:** 200-300 words, plus a screenshot or prototype link

Describe what was actually built. Be specific about the core features and why each one made the cut. Include a link to the live prototype if available.

**Format:**
```markdown
**Core features:**
- [Feature] — [one sentence on why it matters]
- [Feature] — [one sentence on why it matters]
- [Feature] — [one sentence on why it matters]

**[Prototype link or screenshot]**
```

**What makes it world class:**
- Every feature has a "why" — not just what it does but why it was included
- The link to a working prototype is present and works
- Screenshots are clean and show real data — not placeholders

### Section 4 — Key Decisions and Tradeoffs
**Target length:** 200-300 words

This is the most important section. List 3-4 significant decisions with the tradeoff each one represents. This is what separates a portfolio that gets you interviews from one that doesn't.

**Format for each decision:**
```markdown
**[Decision name]**
I chose [X] over [Y] because [reason]. The tradeoff was [what was given up].
```

**Examples of strong decisions:**
- "Desktop first over mobile first — because summer planning is a research-heavy sit-down activity, not a quick mobile lookup. The tradeoff is missing parents who want to check on the go — we accept this for MVP."
- "Discovery only, no registration — to keep scope tight and avoid payment liability. The tradeoff is losing attribution when parents convert. We track click-throughs to camp sites as a proxy."
- "Self-serve camp listings over manual curation — because manual curation doesn't scale and degrades every season. The tradeoff is lower initial data quality, mitigated by a hard supply threshold before parent launch."

**What makes it world class:**
- Real tradeoffs — not "we chose the best option"
- Honest about what was given up
- Shows the reasoning was deliberate, not accidental

### Section 5 — What I Learned
**Target length:** 100-150 words

What did testing, research, or building reveal that you didn't expect? Be honest. Surprises and course corrections show intellectual humility and learning agility — both prized at the principal PM level.

**What makes it world class:**
- Specific — "I learned that parents care more about knowing where friends are going than about price filtering" not "I learned users have different needs"
- Honest — it's okay to say something didn't work
- Shows the product evolved based on evidence

### Section 6 — What I'd Do Next
**Target length:** 100-150 words

What are the 2-3 most important things to build or validate next? Connect them to what was learned.

**What makes it world class:**
- Prioritized — not a feature dump
- Tied to evidence from testing or research
- Shows you think in terms of learning goals, not just feature lists

### Section 7 — About This Project (footer)
```markdown
---
**Author:** Sonal Singh | Principal Product Manager
**Built with:** HTML, CSS, JavaScript (no frameworks)
**PRD:** [link to prd.md]
**Prototype:** [link to prototype/index.html]
**Contact:** sonalshankar06@gmail.com | [LinkedIn URL]
```

---

## Tone and Style

- **Write in first person** — "I decided," "I learned," "I chose"
- **Be specific** — numbers, names, and real examples over adjectives
- **Show the thinking, not just the output** — the reasoning matters more than the conclusion
- **Be honest about limitations** — "this is a portfolio concept, not a shipped product" is fine to say clearly
- **Write for a CPO or senior hiring manager** — assume they are smart, experienced, and skeptical

---

## Format Requirements

- Clean Markdown — renders well on GitHub
- Section headers use `##` (H2)
- Decision sub-headers use `**bold**`
- Target total length: 900-1200 words — long enough to be substantive, short enough to be read
- One prototype screenshot or GIF near the top — visual first
- All links work and point to real files in the repository

---

## Quality Checklist

Before delivering a case study, verify:
- [ ] Personal origin story or strong validation signal in Section 1
- [ ] Section 2 shows reasoning process — not just conclusions
- [ ] Prototype link works and shows real data
- [ ] At least 3 decisions with honest tradeoffs in Section 4
- [ ] At least one surprise or course correction in Section 5
- [ ] Next steps are prioritized and evidence-based
- [ ] Written in first person throughout
- [ ] No generic phrases — "unique opportunity," "seamless experience," "end-to-end solution"
- [ ] Total length 900-1200 words
- [ ] Would make a CPO want to have a conversation

---

## How This Connects to the Portfolio Website

The case study README on GitHub is linked directly from the portfolio website project card. The website says "Read Case Study" and links to the GitHub README. This means:

1. The portfolio website is the discovery surface — it gets attention
2. The case study is the depth layer — it gets you the interview
3. The prototype is the proof — it makes the case study credible

All three must exist and be linked for a project to be portfolio-ready.