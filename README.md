# PM Builder Portfolio

A system for building end-to-end PM portfolio projects — from problem brief through working prototype and published case study.

Built by **Sonal Singh** | Principal Product Manager
[LinkedIn](https://linkedin.com/in/sonalsingh444) · [sonalsingh.email@gmail.com](mailto:sonalsingh.email@gmail.com) · [Live Portfolio](https://sonalsingh-pm.netlify.app)

---

## What This Is

Most PM portfolios are documents. This one is different — every project includes a working prototype you can click through, a full PRD, and a case study that tells the complete product story.

The system uses Claude Code with a set of AI workflow skills that produce consistently high-quality output across every project. The goal is to demonstrate end-to-end PM capability: problem framing, customer discovery, product decisions, and shipped artifacts.

---

## Live Projects

| Project | Type | Status | Links |
|---|---|---|---|
| [Lumen](projects/lumen/) | AI Decisioning, Lifecycle Growth | Case study + Prototype live | [Case Study](projects/lumen/case-study.html) · [Prototype](projects/lumen/prototype/index.html) |
| [Sparky Teardown](projects/sparky/) | Product Evaluation, AI Shopping | Teardown live | [Teardown](projects/sparky/teardown.html) |
| [Dropbox Teams](projects/dropbox/) | B2B Platform, Enterprise Growth | Case study + Prototype live | [Case Study](projects/dropbox/prototype/index.html) |
| [CampSpark](projects/campspark/) | Consumer, Zero-to-One | Case study + Prototype live | [Case Study](projects/campspark/case-study.html) · [Prototype](projects/campspark/prototype/index.html) |

---

## Folder Structure

```
pm-builder-portfolio/
├── portfolio/
│   └── index.html               ← deployed portfolio website (do not move)
│
├── projects/                    ← one folder per project, everything inside
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
│
├── ai-workflow/                 ← Claude AI skill files and templates
│   ├── skills/                  ← how Claude produces each artifact type
│   │   ├── skill_brief.md
│   │   ├── skill_discovery.md
│   │   ├── skill_prd.md
│   │   ├── skill_prototype.md
│   │   ├── skill_user_stories.md
│   │   ├── skill_test_cases.md
│   │   ├── skill_research_sync.md
│   │   └── skill_case_study.md
│   └── templates/
│       └── prd-template.md      ← reusable PRD skeleton
│
└── resources/                   ← reference PRDs (sample projects, not active)
    ├── prd-shiftswap.md         ← sample: consumer/SMB mobile workforce tool
    └── prd-vendoriq.md          ← sample: B2B enterprise vendor evaluation SaaS
```

---

## Commands

All commands run in Claude Code. Claude reads the relevant skill files automatically — no extra instructions needed.

| Command | What It Does |
|---|---|
| `/brief [name]` | Write a one-page problem brief |
| `/discovery [name]` | Customer discovery guide, JTBD mapping, opportunity sizing |
| `/prd [name]` | Write a full PRD |
| `/user-stories [name]` | Write user stories organized by sprint |
| `/prototype [name] Sprint [N]` | Build a functional HTML prototype for the specified sprint |
| `/test-cases [name]` | Write test cases from user stories |
| `/research-sync [name]` | Synthesize user research notes into structured insights |
| `/case-study [name]` | Write a published case study |

**Workflow for a new project:**
```
/brief [name]
/discovery [name]
/prd [name]
/user-stories [name]
/prototype [name] Sprint 1
/test-cases [name]
/research-sync [name]      ← after talking to real users
/case-study [name]
```

---

## Quality Bar

Every project must answer these four questions before it is portfolio-ready:

1. What problem does this solve and for whom?
2. Why does this problem matter — what is the cost of not solving it?
3. What did I build and what were the key decisions?
4. What would I do differently or next?

---

## How the AI Workflow Works

Each skill file in `ai-workflow/skills/` defines the standards and quality bar for one artifact type. Skills are generic — they apply to any project.

When you run a command, Claude:
1. Reads the relevant skill file to learn the quality standard
2. Reads the project's existing files for context
3. Produces output that meets the skill's checklist

Reference PRDs in `resources/` give Claude calibration examples for specific product domains (consumer mobile, B2B enterprise SaaS) without being tied to any active project.

---

## Tech Stack for Prototypes

Every prototype is:
- A single self-contained HTML file — open by double-clicking, no build step
- Vanilla HTML, CSS, and JavaScript
- Mobile-responsive
- Designed to feel like a real product, not a wireframe

---

*This portfolio is a work in progress. Projects are added as they are completed.*
