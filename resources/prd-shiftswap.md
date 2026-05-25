# ShiftSwap — Product Requirements Document
**Status:** Portfolio Concept | **Version:** 1.0 | **Author:** Sonal Singh | **Last Updated:** May 2026

---

## Executive Summary

Hourly workers and shift managers at restaurants, retail stores, and healthcare facilities spend an embarrassing amount of time on a problem that should take minutes: coordinating shift swaps. Today this happens over text threads, Facebook groups, and paper sign-up sheets — leaving managers scrambling, workers stressed, and businesses understaffed at critical moments.

ShiftSwap is a mobile-first platform that makes shift coordination effortless for hourly workers and their managers. Workers post shifts they need covered, qualified colleagues claim them instantly, and managers approve with one tap. No group texts. No missed messages. No understaffed shifts.

The business model is B2B2C — ShiftSwap is sold to businesses (restaurants, retail chains, healthcare facilities) as a workforce coordination tool, and workers use it for free through their employer. This creates a clear enterprise sales motion, predictable revenue, and a product that both managers and workers genuinely want to use.

---

## 1. Problem Statement

### The Core Pain
Hourly workers need flexibility. Businesses need coverage. Today there is no reliable way to connect the two — so both suffer. Workers miss important life events because they can't find coverage. Businesses run short-staffed because coordination happens in channels nobody monitors.

### The Current Workflow
When an hourly worker needs to swap a shift today:

1. Worker texts or calls colleagues one by one looking for coverage
2. Sends a message to a group text or WhatsApp group — gets ignored or lost in noise
3. Posts to a Facebook group — manager may not see it for hours
4. Manager finds out about the problem the day of the shift when nobody shows up
5. Manager calls around frantically trying to find coverage
6. Someone comes in who isn't qualified for that role — or nobody comes in

This workflow fails workers, managers, and customers simultaneously.

### Validation
- The US has 80+ million hourly workers across food service, retail, and healthcare
- Employee scheduling is the #1 source of conflict between hourly workers and managers (SHRM, 2023)
- Staff turnover in food service averages 75% annually — scheduling inflexibility is a top-cited reason for leaving
- Existing scheduling tools (When I Work, Homebase) focus on schedule creation and time tracking, not ad-hoc coordination

### Who Feels This Most
- **Hourly workers** with unpredictable personal lives who need occasional shift flexibility but have no easy way to find coverage
- **Shift managers** at businesses with 10-50 hourly employees who spend hours per week on scheduling coordination they never signed up for

---

## 2. Market Opportunity

### Total Addressable Market
- 80M hourly workers in the US across food service (13M), retail (15M), and healthcare (20M+)
- US workforce management software market: $4.2B in 2024, growing at 9% CAGR
- Average business pays $3-8 per employee per month for scheduling software
- ShiftSwap targets the coordination layer — currently unaddressed by scheduling tools

### The Gap in the Market

| Solution | What It Does | What It Misses |
|---|---|---|
| When I Work, Homebase | Schedule creation and time tracking | No ad-hoc shift coordination between workers |
| Group text / WhatsApp | Ad-hoc coordination | Unstructured, no manager visibility, no qualification matching |
| Facebook groups | Community coordination | No integration with schedule, high noise, slow |
| Paper swap boards | Physical coordination | No mobile, no notifications, managers miss requests |
| **ShiftSwap** | **Real-time qualified shift coordination** | **Nothing — this is the gap** |

### Why Now
- Post-pandemic labor market: workers have more leverage and expect scheduling flexibility as a baseline
- Smartphone penetration among hourly workers is now 85%+ — mobile-first solutions are viable
- Businesses that offer flexibility retain workers longer — reducing the $3,500 average cost of replacing an hourly employee

---

## 3. Target Users

### Primary Persona: The Hourly Worker (Maria)

**Who she is:**
- Age 24, works at a fast casual restaurant, 25-35 hours per week
- Has a second job, childcare responsibilities, or school schedule that occasionally conflicts with shifts
- Communicates primarily via text and Instagram
- Does not have a work email address
- Has been written up before for calling in sick with no coverage arranged

**Her needs:**
- Post a shift she needs covered in under 60 seconds
- Know that qualified colleagues will see it immediately
- Get confirmation that coverage is arranged without chasing people down
- Not get in trouble with her manager for last-minute changes

**Her frustration in her own words:**
"My daughter had a fever and I needed to swap my shift. I texted six people, got two responses, and neither could do it. I had to call in anyway and got a write-up. If there was just an easy way to find someone who could cover me I would have handled it myself."

### Secondary Persona: The Shift Manager (Derek)

**Who he is:**
- Age 32, manages a 20-person team at a retail store
- Spends 5-8 hours per week on scheduling coordination — responding to swap requests, calling workers to fill gaps, updating the schedule
- Uses Homebase for scheduling but relies on group text for everything that goes wrong
- Frustrated that he finds out about coverage problems too late to solve them

**His needs:**
- Know about swap requests before they become crises
- Approve or deny swaps with one tap
- Ensure the right person covers — someone with the right training and role
- Spend less time on scheduling logistics and more time on operations

**His frustration in his own words:**
"I'll get a text at 6am saying someone can't come in at 7. By then it's too late. If workers could sort this out themselves and just send me the approval request, I'd save hours every week."

### Out of Scope (MVP)
- Enterprise shift scheduling (500+ employees) — different product category
- Healthcare credentialing and licensing compliance — adds regulatory complexity beyond MVP
- Gig economy workers without fixed employer relationships

---

## 4. Product Vision & Strategy

### Vision
Make shift flexibility a standard benefit of hourly work — not a source of anxiety.

### Strategic Position
ShiftSwap is not a scheduling tool. When I Work and Homebase own scheduling. ShiftSwap owns the **coordination layer** — the space between "the schedule exists" and "the schedule is actually covered." This layer is ignored by scheduling tools and currently handled by group texts that nobody manages.

The strategic moat is **qualification matching** — ShiftSwap knows which workers are trained and authorized for which roles. This means a swap is not just "someone shows up" but "the right someone shows up." No group text can do this.

### Product Principles
1. **Workers first** — if the product doesn't work for workers, managers will never get value from it
2. **60 seconds to post a swap** — if it takes longer than this, workers will text instead
3. **Manager visibility without manager dependency** — managers should see everything without needing to do anything
4. **Qualification-aware** — never show a worker a shift they are not qualified to cover
5. **Mobile only** — hourly workers do not have laptops; this is a phone product

---

## 5. MVP Scope

### Design Principle
The MVP solves one problem end to end: a worker needs a shift covered, finds someone qualified, and gets manager approval — without a single text message.

### What MVP Includes
| Feature | Rationale |
|---|---|
| Worker shift posting | Core action — must be under 60 seconds |
| Qualification matching | Only show eligible workers for each role |
| Instant push notifications to eligible workers | Speed of response is everything |
| One-tap claim by covering worker | Friction kills adoption |
| One-tap manager approval | Managers must feel in control |
| Schedule integration (manual import CSV) | Must know the existing schedule to coordinate around it |
| Basic manager dashboard | Coverage visibility and approval queue |

### What MVP Excludes (and Why)
| Excluded | Reason |
|---|---|
| Native scheduling (building the schedule) | Out of scope — ShiftSwap coordinates, not creates |
| Payroll integration | Adds compliance complexity beyond MVP |
| In-app messaging | Group texts are fine for general chat; ShiftSwap handles coordination only |
| Shift pickup (open shifts with no owner) | Phase 2 — slightly different use case |
| API integration with When I Work / Homebase | Requires partnership agreements; CSV import works for MVP |

---

## 6. Data Strategy

### Data Requirements
ShiftSwap requires two types of data to function:

1. **Schedule data** — which shifts exist, who is assigned to them, what role each shift requires
2. **Worker qualification data** — which workers are trained and authorized for which roles

Both are business-owned data that ShiftSwap must ingest, not generate.

### Supply Strategy
**MVP approach — manual import:**
- Managers upload their existing schedule via CSV export from their current scheduling tool
- Managers enter worker qualifications manually or via CSV during onboarding
- This is a one-time setup task per business — not ongoing operational overhead

**Phase 2 — native integrations:**
- Direct API integrations with When I Work, Homebase, and Deputy
- Automatic schedule sync eliminates manual uploads
- This is the path to frictionless onboarding at scale

### Supply Threshold
ShiftSwap is not a marketplace in the traditional sense — supply is bounded by each business's workforce. The launch gate is:

- Minimum 8 workers per business location to ensure enough coverage candidates for any swap
- Businesses with fewer than 8 workers per shift are not viable customers for MVP

### Data Quality and Freshness
- Schedule data must be current — a swap posted against a stale schedule creates real operational problems
- Prompt managers to re-upload the schedule when a new schedule period begins
- Long-term: detect schedule staleness (no updates in 7+ days) and send a refresh reminder

---

## 7. Feature Specifications

### 7.1 Shift Posting

**Overview:**
The core worker action. Must be fast, simple, and require no decisions beyond "which shift do I need covered."

**Key behaviors:**
- Worker opens the app and sees their upcoming shifts from the current schedule
- Taps the shift they need covered — no search, no manual entry
- Optionally adds a note ("need coverage — daughter is sick")
- Posts with one tap — notification immediately sent to all eligible workers for that role
- Worker sees a live list of who has been notified and whether anyone has claimed

**Edge cases:**
- Worker tries to post a shift less than 2 hours away: allowed with a warning that response time may be short
- Worker posts a shift and then finds coverage outside the app: can cancel the post
- No eligible workers exist for a shift: manager is notified immediately with context

**Design principle:** Posting a swap should feel like sending a text — not filling out a form.

### 7.2 Qualification Matching

**Overview:**
The feature that makes ShiftSwap more than a group text. Only workers who are trained and authorized for a specific role see swap requests for that role.

**Key behaviors:**
- Each shift has a role requirement (e.g., "Barista," "Cashier," "Shift Lead")
- Each worker has a qualification profile set by the manager
- Only workers with the matching qualification receive swap notifications
- Workers cannot claim a shift they are not qualified for — even if they see it through a notification

**Edge cases:**
- Manager has not entered qualifications for a worker: that worker is excluded from all swaps until qualifications are set
- All qualified workers are already scheduled during the swap shift: system flags this and notifies the manager with no candidates available

**Design principle:** A qualified swap, not just any swap. Coverage that doesn't work is worse than no coverage.

### 7.3 Manager Approval Flow

**Overview:**
Managers stay in control without being in the critical path. They approve or deny swaps — but the coordination happens without them.

**Key behaviors:**
- When a worker claims a shift, manager receives a push notification: "[Worker A] wants to cover [Worker B]'s shift on [date]. Approve?"
- Manager taps Approve or Deny — one action, no navigation required
- If manager does not respond within a configurable window (default: 2 hours), they receive a reminder
- Approved swaps are automatically reflected in the schedule view
- Denied swaps re-open for other workers to claim

**Edge cases:**
- Manager approves a swap that creates an overtime situation for the covering worker: warning displayed before approval but manager can override
- Manager is unavailable and a backup manager is not set: escalation path must be configured during onboarding

**Design principle:** Managers should feel like they are approving decisions, not making them.

---

## 8. User Stories

### Worker Stories
- As a worker, I want to post a shift I need covered in under 60 seconds so I can handle it quickly without stress.
- As a worker, I want to know immediately when someone claims my shift so I'm not left wondering if I'm covered.
- As a worker, I want to claim open shifts from colleagues so I can pick up extra hours when I want them.
- As a worker, I want to receive notifications only for shifts I'm qualified to cover so I'm not overwhelmed with irrelevant requests.

### Manager Stories
- As a manager, I want to approve or deny shift swaps with one tap so I stay in control without spending time on coordination.
- As a manager, I want to see all pending and upcoming swaps in one dashboard so I always know my coverage status.
- As a manager, I want to be notified immediately if a shift has no coverage candidates so I can intervene before it becomes a crisis.
- As a manager, I want to set which workers are qualified for which roles so swaps always go to the right people.

### Business Owner Stories
- As a business owner, I want to reduce last-minute no-shows so my business runs smoothly even when workers have personal conflicts.
- As a business owner, I want workers to handle coordination themselves so my managers can focus on operations.

---

## 9. Success Metrics

### North Star Metric
**Shift coverage rate** — the percentage of posted swap requests that result in a confirmed, manager-approved coverage arrangement before the shift starts.
- **Target:** 85%+ of posted swaps result in confirmed coverage
- **Baseline:** estimated 50-60% resolution rate via current text-based coordination (many requests go unresolved)

### Engagement Metrics
| Metric | Definition | Target |
|---|---|---|
| Time to post a swap | Seconds from app open to swap posted | Under 60 seconds |
| Time to first claim | Minutes from swap posted to first worker claiming | Under 30 minutes |
| Manager response time | Minutes from claim notification to manager approval | Under 2 hours |
| Worker DAU/MAU | Active workers as % of enrolled workers per month | 40%+ |

### Business Metrics
| Metric | Definition | Target |
|---|---|---|
| Locations per customer | Average number of locations per paying business | 3+ (indicates expansion) |
| Net Revenue Retention | Revenue from existing customers YoY | 110%+ |
| Manager satisfaction | CSAT score from shift managers at 90 days | 4.2/5+ |
| Worker satisfaction | CSAT score from workers at 30 days | 4.0/5+ |

### What We Will Not Measure Yet
- Payroll accuracy impact — no payroll integration in MVP
- Turnover reduction — requires 12+ months of data to measure meaningfully
- Labor cost optimization — out of scope for coordination-focused MVP

---

## 10. Business Model

### Revenue Streams

**Stream 1: B2B SaaS Subscription (Primary)**

ShiftSwap is sold to businesses, not workers. Workers use it free through their employer.

| Tier | Price | Features |
|---|---|---|
| Starter | $49/month per location | Up to 20 workers, basic swap coordination, manager approval |
| Growth | $99/month per location | Up to 50 workers, analytics dashboard, multi-manager support |
| Enterprise | Custom | Unlimited workers, API integration, dedicated support, custom reporting |

**Pricing rationale:**
At $49/month, ShiftSwap pays for itself if it prevents just one understaffed shift per month — the average cost of being understaffed for one shift (lost sales, overtime premium, customer experience) far exceeds $49.

**Stream 2: Shift Pickup Marketplace (Future)**
Workers who want extra hours can browse and claim open shifts across businesses that use ShiftSwap. ShiftSwap takes a small fee per successful placement. This is a post-MVP feature that requires sufficient network density.

### Unit Economics (Illustrative)
- 500 business locations at average $75/month = $450K ARR
- CAC: estimated $800 per location through inside sales
- Payback period: ~11 months
- LTV at 24-month average retention: $1,800 per location
- **LTV:CAC ratio: 2.25x** — healthy for an SMB SaaS product

---

## 11. Go-to-Market Strategy

### Beachhead Market
Independent and small-chain restaurants in the Bay Area — specifically fast casual and casual dining with 10-40 hourly employees per location. These businesses have high scheduling volatility, low IT sophistication, and urgent pain with staffing coordination.

### Growth Strategy

**Phase 1: Direct outbound to restaurant owners (Months 1-3)**
- Target 50 Bay Area restaurants with direct outreach to owners and general managers
- Offer 60-day free trial with hands-on onboarding support
- Goal: 10-15 paying locations by end of Month 3

**Phase 2: Franchise expansion (Months 3-9)**
- One franchise group adoption = instant access to 20-100 locations
- Target regional franchise operators of national chains (not the corporate entity — the franchisee)
- A single franchise owner saying yes is worth 10 individual restaurant wins

**Phase 3: Vertical expansion (Months 6-12)**
- Retail: similar scheduling volatility, same coordination problem
- Healthcare: higher complexity but significantly higher willingness to pay for compliance
- Enter retail first (lower complexity), healthcare second

### Why This Works
Restaurant owners make fast decisions when the pain is immediate. A 60-day trial with a personal demo and onboarding support dramatically reduces the perceived risk of trying something new. One successful franchise operator case study unlocks dozens of peer referrals — restaurant owners talk to each other constantly.

---

## 12. Launch Readiness

### Supply Threshold
ShiftSwap is not a two-sided marketplace — there is no supply-side acquisition problem. The launch gate is operational readiness:

- [ ] End-to-end swap flow tested with a real restaurant team (not internal)
- [ ] Manager approval notifications tested on iOS and Android
- [ ] CSV schedule import tested with exports from When I Work, Homebase, and Google Sheets
- [ ] Push notification delivery rate confirmed above 95% in testing
- [ ] At least 3 beta businesses have completed at least 5 real swaps each

### Quality Gates
- [ ] Swap posting flow completes in under 60 seconds on a mid-range Android device
- [ ] Qualification matching confirmed accurate in 100% of test scenarios
- [ ] Manager approval flow works correctly in airplane mode (queues and sends when connected)
- [ ] Data privacy review completed — worker personal data handling compliant with CCPA
- [ ] Onboarding flow tested with a non-technical restaurant manager without assistance

### Launch Sequence
1. **Private beta:** 3-5 Bay Area restaurants, founders handle onboarding personally
2. **Expanded beta:** 15-20 locations, light customer success support
3. **Limited GA:** Self-serve signup with a 14-day free trial, inside sales for businesses over 3 locations
4. **Full GA:** Open to all markets with self-serve and sales motion running in parallel

### Rollback Plan
If a critical bug causes swap notifications to fail silently — workers post swaps that nobody sees — immediately disable swap posting and notify all affected managers directly. Manual coordination is the fallback; managers must know immediately so they can revert to their previous process. Fix SLA: 4 hours from detection to resolution.

---

## 13. Risks and Mitigations

### Risk 1: Worker Adoption is the Bottleneck
**Risk:** Managers buy the product but workers don't use it. If workers still text each other, the product has no value.
**Likelihood:** High
**Impact:** High
**Mitigation:** Worker onboarding must be sub-5-minutes and require zero training. The app must be as simple as texting. Seed adoption by having managers post the first 2-3 swap opportunities themselves to show workers it works before asking them to use it independently.

### Risk 2: Managers Bypass the App
**Risk:** Managers approve verbal swaps outside the app, creating schedule inconsistencies and making ShiftSwap redundant.
**Likelihood:** Medium
**Impact:** High
**Mitigation:** Make manager approval so fast that going through the app is the path of least resistance. If approval takes one tap and 10 seconds, managers have no reason to handle it any other way.

### Risk 3: High Churn if Business Closes or Changes
**Risk:** Restaurant industry has high business failure rates. A customer disappears when a location closes.
**Likelihood:** High (for individual locations)
**Impact:** Low (if portfolio of locations is diversified)
**Mitigation:** Target franchise operators and multi-location businesses from the start. Losing one location in a 10-location franchise account is acceptable; losing the account entirely is the risk to avoid.

### Risk 4: When I Work or Homebase Adds Coordination Features
**Risk:** An incumbent scheduling tool adds a shift swap feature, commoditizing ShiftSwap's core value proposition.
**Likelihood:** Medium
**Impact:** High
**Mitigation:** Qualification matching and the worker-first UX are significantly harder to build than incumbents acknowledge. Speed to 1,000+ locations creates switching cost and brand recognition. Build the coordination intelligence layer deep enough that a checkbox feature from an incumbent cannot match it.

### Risk 5: Notification Fatigue
**Risk:** Workers receive too many swap notifications and start ignoring them, reducing coverage rates.
**Likelihood:** Medium
**Impact:** Medium
**Mitigation:** Smart notification controls — workers set availability preferences (days, times, roles they'll cover) so they only receive relevant, timely notifications. Fewer but more relevant notifications produce better response rates.

---

## 14. Open Questions

| Question | Why It Matters | How to Resolve |
|---|---|---|
| Should workers be able to initiate direct swap requests to a specific colleague? | Changes coordination dynamic significantly | Test both models in beta — broadcast vs. direct |
| What is the right manager approval window before a swap auto-approves? | Balances manager control with coordination speed | Survey 10 managers on preference |
| Should ShiftSwap handle shift pickup (open shifts without an owner)? | Expands scope but addresses adjacent pain | Validate demand in beta before building |
| How do we handle workers at multiple locations of the same business? | Multi-location workers exist in retail and healthcare | Design for this from the start even if rare in MVP |
| What is the right price point for franchise operators vs. independent restaurants? | Pricing strategy differs significantly by segment | Test both segments in parallel in first 6 months |

---

## 15. Future Roadmap (Post-MVP)

### Near Term (6-12 months)
- **Shift pickup marketplace** — workers claim open shifts across all locations they are qualified for
- **Native integrations** — direct API sync with When I Work, Homebase, Deputy
- **Recurring availability preferences** — workers set standing availability so they get the right notifications automatically
- **Manager analytics** — who are your most flexible workers? Which shifts get covered fastest?

### Medium Term (Year 2)
- **Cross-business coordination** — workers pick up shifts at partner businesses (requires credential matching)
- **Predictive understaffing alerts** — "Based on historical patterns, your Saturday closing shift is at high risk of a swap request. Consider scheduling a backup now."
- **Healthcare vertical** — compliance-aware coordination with license and certification tracking
- **Payroll integration** — automatic timesheet updates when swaps are confirmed

### Longer Term (Year 3+)
- **Demand forecasting** — "You'll need 15% more staff next Saturday based on local event data"
- **AI-powered scheduling suggestions** — proactive recommendations to reduce swap frequency
- **Worker reputation scores** — reliability ratings visible to managers to improve swap matching quality

---

## 16. Appendix

### Competitive Landscape Summary

| Platform | Ad-hoc Coordination | Qualification Matching | Manager Approval Flow | Worker Mobile UX | Business Model |
|---|---|---|---|---|---|
| When I Work | None | None | N/A | Good | SaaS per employee |
| Homebase | Basic group message | None | None | Good | Freemium SaaS |
| Group Text / WhatsApp | Yes | None | None | Native | Free |
| Paper swap board | Yes | Manual | Manual | None | Free |
| **ShiftSwap** | **Structured** | **Automated** | **One-tap** | **First-class** | **B2B SaaS** |

### Assumptions Log

| Assumption | Confidence | Validation Needed |
|---|---|---|
| Workers will download and use a dedicated app for shift swaps | Medium | Beta with 3 restaurants before building further |
| 85% coverage rate is achievable | Medium | Measure in beta; adjust target based on data |
| Restaurant owners will pay $49-99/month for scheduling coordination | Medium | Confirmed by 3 early conversations; validate at scale |
| Qualification matching is a meaningful differentiator vs. group text | High | Confirmed in manager interviews |
| Franchise expansion is a viable growth motion | Medium | Test with 2 franchise operators in Year 1 |

---

*ShiftSwap is a portfolio project created to demonstrate consumer/SMB product thinking, B2B2C go-to-market strategy, and mobile-first product design. It does not represent a shipped product.*

*Author: Sonal Singh | Principal Product Manager | sonalshankar06@gmail.com*