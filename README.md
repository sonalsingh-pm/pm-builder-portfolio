# PM Builder Portfolio

A system for building world class PM portfolio projects — from problem brief through working prototype and GitHub case study.

Built by **Sonal Singh** | Principal Product Manager
[LinkedIn](https://linkedin.com/in/sonalsingh444) · [sonalsingh.email@gmail.com](mailto:sonalsingh.email@gmail.com)

---

## What This Is

Most PM portfolios are just documents. This one is different — every project here includes a working prototype you can click through, a world class PRD, and a case study that tells the full product story.

The system uses Claude Code with a set of skills and commands that produce consistently high quality output across every project.

---

## Folder Structure

```
pm-builder-portfolio/
├── CLAUDE.md                        ← Claude Code instructions and command definitions
├── README.md                        ← you are here
│
├── PRDs/                            ← problem briefs, PRDs, and case studies
│   ├── [name]-brief.md
│   ├── [name]-prd.md
│   └── [name]-case-study.md
│
├── prototypes/                      ← functional HTML prototypes
│   └── [name]/
│       └── index.html               ← single self-contained file, open by double-clicking
│
├── user_stories/                    ← user stories per project, organized by sprint
│   └── [name]-user-stories.md
│
├── test_cases/                      ← test cases per project
│   └── [name]-test-cases.md
│
├── research/                        ← user research notes and synthesis
│   └── [name]-research.md
│
├── skills/                          ← how Claude Code does things
│   ├── skill_brief.md               ← how to write a problem brief
│   ├── skill_discovery.md           ← how to run customer discovery
│   ├── skill_prd.md                 ← how to write a world class PRD
│   ├── skill_prototype.md           ← how to build a functional HTML prototype
│   ├── skill_user_stories.md        ← how to write user stories
│   ├── skill_test_cases.md          ← how to write test cases
│   ├── skill_research_sync.md       ← how to synthesize user research
│   └── skill_case_study.md          ← how to write a GitHub case study
│
├── memory/
│   ├── rules.md
│   ├── hypotheses.md
│   └── rejected.md
│
└── resources/                       ← reference material for Claude Code
    ├── prd-template.md              ← reusable PRD skeleton
    ├── prd-vendoriq.md              ← sample PRD: B2B enterprise SaaS
    └── prd-shiftswap.md             ← sample PRD: consumer/SMB mobile
```

---

## File Naming Convention

Every project follows a consistent naming convention so Claude Code can derive file paths dynamically from the project name alone:

| File | Convention |
|---|---|
| Problem brief | `PRDs/[name]-brief.md` |
| Full PRD | `PRDs/[name]-prd.md` |
| Case study | `[name]-case-study.html (root, deployed to Netlify)` |
| User stories | `user_stories/[name]-user-stories.md` |
| Test cases | `test_cases/[name]-test-cases.md` |
| Research notes | `research/[name]-research.md` |
| Prototype | `prototypes/[name]/index.html` |

**Example for CampSpark:**
```
PRDs/campspark-brief.md
PRDs/campspark-prd.md
PRDs/campspark-case-study.md
user_stories/campspark-user-stories.md
test_cases/campspark-test-cases.md
research/campspark-research.md
prototypes/campspark/index.html
```

---

## Commands

All commands are run in Claude Code. Claude Code reads the relevant skill files automatically — no extra instructions needed in the prompt.

| Command | What It Does |
|---|---|
| `/brief [name]` | Write a one-page problem brief |
| `/discovery [name]` | Run customer discovery, JTBD mapping, opportunity sizing |
| `/prd [name]` | Write a full world class PRD |
| `/user-stories [name]` | Write user stories organized by sprint |
| `/prototype [name] Sprint [N]` | Build a functional HTML prototype for the specified sprint |
| `/test-cases [name]` | Write test cases from the user stories |
| `/research-sync [name]` | Synthesize user research notes into structured insights |
| `/case-study [name]` | Write a GitHub-ready README case study |

**Example workflow for a new project:**
```
/brief campspark
/discovery campspark
/prd campspark
/user-stories campspark
/prototype campspark Sprint 1
/test-cases campspark
/research-sync campspark
/case-study campspark
```

---

## How to Add a New Project

1. Think of a real problem worth solving
2. Run `/brief [name]` in Claude Code
3. Review the brief — does the problem feel real and urgent?
4. Run `/prd [name]`
5. Run `/user-stories [name]`
6. Run `/prototype [name] Sprint 1`
7. Open `prototypes/[name]/index.html` and click through the flow
8. Talk to 2-3 real users
9. Run `/research-sync [name]` with your notes
10. Update the PRD and prototype based on what you learned
11. Run `/case-study [name]`
12. Publish to GitHub

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

| Project | Status | PRD | Prototype | Case Study |
|---|---|---|---|---|
| CampSpark | Live | ✅ Complete | ✅ Live | ✅ Live |

---

## How the Skills System Works

Each skill file teaches Claude Code how to produce world class output for a specific artifact type. Skills are generic — they apply to any project, not just CampSpark.

When you run a command, Claude Code:
1. Reads the relevant skill file — learns the standards and quality bar
2. Reads the project's existing files — gets the context
3. Produces output that meets the skill's quality checklist

Skills are in the `skills/` folder. Resources (templates and sample PRDs) are in `resources/`. Never mix them — skills teach Claude how to think, resources give Claude material to reference.

---

## Tech Stack for Prototypes

Every prototype is:
- A single self-contained HTML file
- Vanilla HTML, CSS, and JavaScript — no frameworks
- Opens by double-clicking — no server or build step needed
- Mobile-responsive
- Stripe-quality visual design

See `skills/skill_prototype.md` for the full technical specification including CSS architecture, component patterns, and UX standards.

---

*This portfolio is a work in progress. Projects are added as they are completed.*