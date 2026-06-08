# PM Builder Portfolio — CLAUDE.md

## Purpose
This is where I build my PM portfolio as a builder — not just a writer of PRDs.
The goal is to identify real problems, write PRDs, build functional prototypes,
test them, and publish them to GitHub. This demonstrates that I am an end-to-end
product builder, not just someone who hands specs to engineers.

Every project here should be something I'd be proud to show in a principal PM interview
at LinkedIn, Yelp, Shopify, or a late-stage startup.

---

## Folder Structure
PM-BUILDER-PORTFOLIO/
├── CLAUDE.md                            ← you are here
├── README.md
├── _redirects                           ← Netlify routing: / → portfolio/index.html
├── portfolio/
│   └── index.html                       ← portfolio website, deployed to Netlify, do not move
├── projects/                            ← one folder per project, everything inside
│   ├── campspark/
│   │   ├── prd.md
│   │   ├── user-stories.md
│   │   ├── test-cases.md
│   │   ├── data.json
│   │   ├── prototype/
│   │   │   └── index.html
│   │   └── case-study.html
│   ├── lumen/
│   │   ├── prototype/
│   │   │   └── index.html
│   │   └── case-study.html
│   ├── sparky/
│   │   └── teardown.html
│   └── dropbox/
│       └── prototype/
│           └── index.html
├── ai-workflow/                             ← Claude tooling, not portfolio content
│   ├── skills/
│   │   ├── skill_brief.md
│   │   ├── skill_prd.md
│   │   ├── skill_prototype.md
│   │   ├── skill_discovery.md
│   │   ├── skill_user_stories.md
│   │   ├── skill_test_cases.md
│   │   ├── skill_research_sync.md
│   │   ├── skill_case_study.md
│   │   └── skill_job_search.md
│   └── templates/
│       └── prd-template.md
├── memory/                              ← self-improving loop memory
│   ├── rules.md
│   ├── hypotheses.md
│   └── rejected.md
└── resources/                           ← reference PRDs (not active projects)
    ├── prd-vendoriq.md
    └── prd-shiftswap.md

---

## Commands and Their Skills

When a command is called, automatically read the files listed — no additional instructions needed in the prompt.

| Command | Read These Files Automatically | Output |
|---|---|---|
| `/brief [name]` | `ai-workflow/skills/skill_brief.md` | `projects/[name]/brief.md` |
| `/discovery [name]` | `ai-workflow/skills/skill_discovery.md` → `projects/[name]/brief.md` | `projects/[name]/discovery.md` |
| `/prd [name]` | `ai-workflow/skills/skill_prd.md` → `ai-workflow/templates/prd-template.md` → `projects/campspark/prd.md` | `projects/[name]/prd.md` |
| `/prototype [name] Sprint [N]` | `ai-workflow/skills/skill_prototype.md` → `projects/[name]/user-stories.md` → `projects/[name]/prd.md` — build only the sprint specified | `projects/[name]/prototype/index.html` |
| `/user-stories [name]` | `ai-workflow/skills/skill_user_stories.md` → `projects/[name]/prd.md` | `projects/[name]/user-stories.md` |
| `/test-cases [name]` | `ai-workflow/skills/skill_test_cases.md` → `projects/[name]/user-stories.md` | `projects/[name]/test-cases.md` |
| `/research-sync [name]` | `ai-workflow/skills/skill_research_sync.md` → `projects/[name]/prd.md` | `projects/[name]/research.md` |
| `/case-study [name]` | `ai-workflow/skills/skill_case_study.md` → `projects/[name]/prd.md` → `projects/[name]/user-stories.md` → `projects/[name]/research.md` | `projects/[name]/case-study.html` |

---

## Self-Improving Loop

Before starting any task:
1. Read `memory/rules.md` and apply all confirmed rules automatically
2. Check `memory/hypotheses.md` for relevant hypotheses to this domain
3. Do not ask permission to apply rules — just apply them

After completing any task where feedback is given:
1. Identify the pattern in the feedback
2. If confirmed pattern: add to `memory/rules.md`
3. If new observation: add to `memory/hypotheses.md`
4. If hypothesis disproven: move to `memory/rejected.md`

This happens automatically. No need to ask for it.

---

## Git and Deployment Rules

- Commit changes locally as needed, but do NOT push to GitHub automatically.
- Only push to GitHub when explicitly told: "push to GitHub" or "deploy."

---

## Hard Rules — Apply to Every Output

### PRDs
- Always read `skills/skill_prd.md` before writing any PRD
- Always use `resources/prd-template.md` as the structure
- Always use `PRDs/campspark-prd.md` as the quality calibration example
- Always include a Data Strategy section for any marketplace or discovery product
- Always include a Launch Readiness section with binary gates
- Always include an Assumptions Log with confidence levels
- Never use: "large and growing market," "no competition," "unique opportunity," "seamless experience"
- Business model must include illustrative unit economics — not just revenue stream names
- Time targets must be realistic — not aspirational

### Prototypes
- Always read `skills/skill_prototype.md` before building any prototype
- Single self-contained HTML file — no external dependencies except Google Fonts
- No placeholder text — all content must be real and relevant
- Primary user flow must work end to end
- Must feel like a real product — not a wireframe

### Case Studies
- Always read `skills/skill_case_study.md` before writing any case study
- Written in first person throughout
- At least 3 decisions with honest tradeoffs
- At least one surprising finding or course correction
- 900-1200 words

### Writing Style (All Outputs)
- Write at a principal PM level: strategic, specific, intellectually honest
- Numbers and specificity over adjectives
- Show tradeoffs: what you chose and what you gave up
- Assume the reader is a sophisticated hiring manager or CPO
- Clean Markdown unless another format is explicitly requested
- Never use em dashes (—) in any copy, descriptions, or content. Use commas, colons, or rephrase instead.

---

## How to Work on a New Problem

1. `/brief` → define the problem clearly
2. `/discovery` → customer interview guide, JTBD mapping, opportunity sizing
3. `/prd` → write the full PRD
4. `/user-stories` → write user stories
5. `/prototype` → build the HTML prototype
6. `/test-cases` → write test cases
7. Talk to real users, test the prototype
8. `/research-sync` → synthesize what you learned
9. Update PRD and prototype based on learnings
10. `/case-study` → write the case study markdown

---

## Quality Bar

Every project must answer these four questions before it is portfolio-ready:
1. What problem does this solve and for whom?
2. Why does this problem matter — what is the cost of not solving it?
3. What did I build and what were the key decisions?
4. What would I do differently or next?

If it cannot answer all four it is not ready for GitHub.

---

## Active Projects

### CampSpark — Summer Camp Discovery and Coordination
**Status:** PRD complete | Prototype live | Case study live
**PRD:** `projects/campspark/prd.md`
**User stories:** `projects/campspark/user-stories.md`
**Test cases:** `projects/campspark/test-cases.md`
**Prototype:** `projects/campspark/prototype/index.html`
**Case study:** `projects/campspark/case-study.html`
**Live URL:** https://sonalsingh-pm.netlify.app/projects/campspark/prototype/index.html

**What it is:** A desktop-first platform helping working parents discover summer camps, plan their child's summer, and coordinate with other parents — replacing the fragmented process of visiting dozens of websites and coordinating over group texts.

**Primary user:** Dual-income working parent, ages 35-50, 1-3 school-age children.

**Strategic differentiator:** The social coordination layer — parents can see where their children's friends are going and share summer plans with their network.

**Key constraints:**
- Desktop first — planning is a research-heavy sit-down activity
- Discovery only in MVP — does not own registration or payment
- Supply before demand — do not launch to parents until 200+ verified Bay Area listings exist

---

## Portfolio Website

The portfolio website lives at `portfolio/index.html`.
It is deployed to Netlify and linked from Sonal's LinkedIn profile and resume.
Do not move this file — it will break the live URL.
Every completed project gets a card in the Projects section.
All prototype links must always work before any commit.

---

## Author
Sonal Singh | Principal Product Manager
sonalsingh.email@gmail.com | linkedin.com/in/sonalsingh444