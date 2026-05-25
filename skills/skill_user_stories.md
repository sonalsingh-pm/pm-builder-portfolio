# SKILL: Writing User Stories

## Purpose
User stories translate PRD features into specific, testable, independently deliverable units of work. World class user stories are precise enough for an engineer to estimate and implement without guessing at intent — and specific enough for a QA engineer to write a test case against.

---

## Format

Every user story follows this format:
```
As a [specific user type], I want to [specific action] so that [meaningful outcome].
```

All three parts are required. A story without a "so that" is incomplete — it describes what without explaining why.

---

## Before Writing — Answer These Questions

1. Which PRD features are in MVP scope? Write stories only for these.
2. Who are the distinct user types? Each type gets their own stories.
3. What is the primary job to be done for each feature? Start there.
4. What are the edge cases for each story? Each edge case may need its own story.

---

## What Makes a World Class User Story

**Specific user type — not generic**
- Weak: "As a user..."
- Strong: "As a working parent planning summer camps..."

**Specific action — not vague**
- Weak: "I want to find camps..."
- Strong: "I want to filter camps by age, interest, and weekly time window..."

**Meaningful outcome — answers "so what"**
- Weak: "...so that I can use the product."
- Strong: "...so that I only see options that fit my child's schedule and my work constraints."

**Independently testable**
Each story should be testable on its own. If you cannot write a single test case for a story, it is too broad — split it.

**Appropriately scoped**
Stories should be completable in 1-3 engineering days. If a story would take a sprint to build, it is an epic — break it into smaller stories.

---

## Structure

Group stories by theme matching the PRD feature sections. Within each theme, order stories by: primary happy path first, then secondary flows, then edge cases.

```markdown
# User Stories — [Product Name]

## [Theme 1 — matches PRD feature]
- As a [user], I want to [action] so that [outcome].
- As a [user], I want to [action] so that [outcome].

## [Theme 2]
- As a [user], I want to [action] so that [outcome].

## Edge Cases
- As a [user], when [condition], I want to [action] so that [outcome].
```

---

## Acceptance Criteria

For complex or high-risk stories, include acceptance criteria:

```markdown
**Story:** As a parent, I want to filter camps by age so that I only see camps my child is eligible for.

**Acceptance criteria:**
- Selecting age 8 shows only camps with age range that includes 8
- Selecting age 8 hides camps with age range of 10-14
- Age filter updates results without page reload
- Selecting "any age" removes the age filter and shows all camps
- If no camps match the selected age, an empty state is shown with a suggestion to broaden filters
```

Include acceptance criteria for:
- Any story involving filtering, search, or data display
- Any story involving permissions or privacy
- Any story with multiple edge cases
- Any story the engineer would likely have questions about

---

## User Types to Consider

For each product, identify all distinct user types from the PRD personas. Common types:

**Consumer marketplace (CampSpark):**
- Working parent (primary)
- Social coordinator parent (secondary)
- Camp operator (supply side)

**B2B SaaS (VendorIQ):**
- Procurement manager (primary user)
- Evaluator / stakeholder (scorer)
- CPO / economic buyer (approver)

**B2B2C mobile (ShiftSwap):**
- Hourly worker (primary)
- Shift manager (approver)
- Business owner (buyer)

---

## Anti-Patterns to Avoid

| Anti-Pattern | Problem | Fix |
|---|---|---|
| "As a user, I want a dropdown menu" | Describes implementation, not need | "As a parent, I want to select multiple interests so that I can find camps covering more than one activity" |
| No "so that" clause | Incomplete — no outcome stated | Always include the outcome |
| Story too large | Cannot be estimated or tested | Split into 2-3 smaller stories |
| Duplicate stories | Confusion and double work | Review for overlap before delivering |
| Stories for out-of-scope features | Scope creep | Only write stories for MVP features |
| Generic user type | Not actionable | Name the specific persona |

---

## Quality Checklist

Before delivering user stories, verify:
- [ ] All three parts present: user type, action, outcome
- [ ] User types are specific — match PRD personas
- [ ] Actions are specific — unambiguous to an engineer
- [ ] Outcomes are meaningful — answer "so what"
- [ ] Stories cover only MVP-scope features
- [ ] Edge cases have their own stories
- [ ] Complex stories have acceptance criteria
- [ ] No story would take more than 3 engineering days
- [ ] Stories are grouped by theme matching PRD features
- [ ] Each story is independently testable