# CampSpark — Product Requirements Document
**Status:** Portfolio Concept | **Version:** 2.0 | **Author:** Sonal Singh | **Last Updated:** May 2026

---

## Executive Summary

Every spring, millions of working parents across the United States face the same exhausting ritual: hunting across dozens of websites, brochures, school newsletters, and Facebook groups to piece together a summer plan for their kids. The result is hours of fragmented research, chaotic coordination over text and WhatsApp, and decisions made under pressure as registration windows close.

CampSpark is a desktop-first summer camp discovery and coordination platform that transforms this process. It gives working parents a single place to discover camps that match their child's age, interests, schedule, and budget — and makes coordination with other parents effortless.

This product was born from a personal pain point. As a working parent, I spent several hours across multiple weekends each spring hunting for camp information, manually tracking options in a Google Sheet, and coordinating with other parents over text. When I shared that spreadsheet with two other parents in my network, they adopted it immediately — without being asked. That moment of organic adoption was the clearest signal that the problem was real, the need was urgent, and a better solution was overdue.

CampSpark is that better solution.

---

## 1. Problem Statement

### The Core Pain
Working parents spend several hours across multiple weekends every spring doing something that should take one focused sitting: finding the right summer camps for their kids.

The problem is not that good camps don't exist. The problem is that information about those camps is scattered across dozens of sources — individual camp websites, school newsletters, local Facebook groups, word of mouth — with no central place to search, filter, compare, or plan.

### The Current Workflow
A typical working parent planning summer camps today:

1. Starts a Google search — gets hundreds of irrelevant results
2. Visits 10-15 individual camp websites
3. Manually tracks options in a spreadsheet or notes app
4. Texts or WhatsApp messages other parents: "which camps are you doing?"
5. Discovers a great camp — but registration closed two weeks ago
6. Makes a rushed decision under time pressure

This workflow is broken. It is manual, time-consuming, emotionally draining, and produces worse outcomes than parents deserve.

### Validation
When I built a basic Google Sheet to track weeks, camps, costs, and schedules for my own family — and shared it with two other parents in my network — they adopted it immediately without any prompting. This organic adoption from a manual, imperfect solution is strong early signal that the underlying need is real and urgent.

### Who Feels This Most
The pain is sharpest for:
- **Dual-income households** where both parents work full-time and have limited bandwidth for research
- **Parents of multiple children** who need to coordinate camps across different ages and interests simultaneously
- **Socially motivated kids** who want to attend camps with friends — adding a coordination layer on top of an already complex search

---

## 2. Market Opportunity

### Total Addressable Market
- Approximately 11 million dual-income households in the US have school-age children (ages 5-15)
- Summer camp is a $3B+ industry in the US, growing ~5% annually
- The average family spends $300-$800 per child per week on summer activities
- Planning season is concentrated in February-April, creating an urgent, high-intent window

### The Gap in the Market
Existing solutions fall into two categories — neither solves the full problem:

| Solution | What It Does | What It Misses |
|---|---|---|
| Individual camp websites | Lists one camp's info | No comparison, no aggregation |
| Camp directories (Sawyer, ActivityHero) | Aggregates some listings | No planning, no coordination, incomplete data |
| Facebook groups / NextDoor | Peer recommendations | Unstructured, overwhelming, not searchable |
| Google Sheets (DIY) | Flexible tracking | Manual, no discovery, not collaborative |
| School newsletters | Curated suggestions | Infrequent, limited options, no filtering |
| **CampSpark** | **Discovery + planning + coordination** | **Nothing — this is the gap** |

### Why Now
Three macro trends are making this problem more acute:

1. **Return-to-office mandates** increase the urgency of reliable weekday childcare and structured activities during summer
2. **Rising parental expectations** — families increasingly prioritize enriching, skill-building experiences over passive childcare
3. **Information overload** — the proliferation of camps and activity providers has made discovery harder, not easier, despite more options being available

---

## 3. Target Users

### Primary Persona: The Organized Working Parent

**Who they are:**
- Ages 35-50, dual-income household, 1-3 school-age children
- Works full-time, limited bandwidth for research
- Values efficiency, organization, and confident decision-making
- Already uses tools like Google Calendar, Notion, or spreadsheets to manage family logistics

**Their needs:**
- Discover relevant camps quickly without visiting dozens of websites
- Filter by what actually matters: age, interest, location, time, budget
- Know where their children's friends are going
- Have a single source of truth for the summer plan

**Their frustration in their own words:**
"I spent three weekends researching camps last year. By the time I found the right one, registration was full. I ended up settling for something my kid didn't even want to do."

### Secondary Persona: The Social Coordinator Parent

**Who they are:**
- Highly networked in their school or neighborhood community
- Organizes group decisions — WhatsApp admin, school committee member
- Influences other parents' camp choices significantly

**Their needs:**
- See and share consolidated summer plans with their network
- Coordinate group signups across multiple families
- Be the person who "figured it out" for the group

**Why they matter:**
Social Coordinator Parents are CampSpark's viral growth engine. When one adopts it, they bring 3-5 other families with them.

### Out of Scope (MVP)
- Camp operators and administrators (future persona for B2B features)
- Single-income households where one parent has time for manual research
- Children under 5 (different product category — daycare, not camps)

---

## 4. Product Vision & Strategy

### Vision
Make summer planning feel like summer — effortless, exciting, and something to look forward to.

### Strategic Position
CampSpark is **not a camp directory**. Directories solve the supply problem — they list camps. CampSpark solves the **demand problem** — it helps parents find the right camp, plan around it, and coordinate with their community.

The strategic moat is the **coordination layer**. Discovery alone is replicable. But a platform where parents can see where their children's friends are going, share summer plans, and coordinate group signups creates a network effect that directories cannot replicate.

### Product Principles
1. **Reduce time, not just effort** — every feature should demonstrably save parents time
2. **Respect cognitive load** — working parents are already overwhelmed; the UI must make decisions easier, not harder
3. **Social by design** — coordination features are core, not bolted on
4. **Discovery first** — CampSpark does not own registration; it owns the decision that leads to registration
5. **Desktop first** — summer planning is a sit-down, side-by-side comparison activity, not a mobile use case

---

## 5. MVP Scope

### Design Principle: Focused Over Comprehensive
The MVP does one thing exceptionally well: help a working parent go from "I need to figure out summer camps" to "I have a plan I feel good about" in one focused sitting rather than across multiple weekends.

### What MVP Includes
| Feature | Rationale |
|---|---|
| Camp discovery with multi-parameter filtering | Core job to be done |
| Camp detail pages | Enough information to decide without leaving the platform |
| Saved camps and summer plan view | Replaces the Google Sheet |
| Shared plan links | Enables coordination without requiring both parties to sign up |
| Friend visibility (opt-in) | Key differentiator; drives social adoption |
| Camp self-registration portal | Primary supply acquisition mechanism |

### What MVP Excludes (and Why)
| Excluded | Reason |
|---|---|
| Registration and payment processing | Increases liability, operational complexity, and time to launch |
| Mobile app | Planning is a desktop use case; mobile can come later |
| AI recommendations | Requires data we don't have yet at launch |
| Camp operator analytics dashboard | Post-MVP; focus first on parent-side value |
| Calendar sync | Adds complexity without changing core behavior in MVP |
| Reviews and ratings | Requires critical mass of users before it's useful |

---

## 6. Data Strategy

### The Core Challenge
CampSpark's value to parents depends entirely on having comprehensive, accurate, and up-to-date camp listings. Without enough camps in a given geography and interest category, parents find nothing relevant and churn immediately — likely never returning. This is the single biggest risk to the product and must be treated as such.

Manual curation by an internal team is not viable. It does not scale, degrades quickly as camps update their schedules each season, and creates an ongoing operational cost that grows with every new market. The primary supply strategy must be self-sustaining.

### Primary Strategy: Camp Self-Registration

Camps have a strong, immediate incentive to list on CampSpark: parents are actively searching for exactly what they offer. A free listing on a platform with high-intent parent traffic is an obvious yes for most camp operators.

The camp-facing listing tool must be built before the parent-facing discovery product. Supply before demand is the governing rule.

**Camp onboarding flow:**
1. Camp operator finds CampSpark via outreach, search, or word of mouth
2. Claims or creates their listing using a simple self-serve form (10-15 minutes to complete)
3. Listing is reviewed and published within 24 hours
4. Camp receives a dashboard to update availability, dates, and pricing each season

**Camp acquisition motion:**
- Pre-launch outreach to 300-500 camps in the Bay Area beachhead market
- Direct outreach to camp directors via email and phone (small operations respond well to personal outreach)
- Partner with park and recreation departments, JCC networks, and school district enrichment program directories — these organizations have existing relationships with dozens of camps each
- Offer Featured placement free for first season to early adopters — reduces friction and builds supply quality

### Secondary Strategy: Curated Seed Data

Before the parent-facing product launches, manually enter 150-200 high-quality camp listings in the Bay Area using publicly available information (camp websites, school district directories, park and recreation catalogs). This seed data ensures:
- The platform looks credible and full from Day 1
- Parents find relevant results even in interest categories where self-serve adoption lags
- The team understands data quality issues firsthand before automating

This is a one-time founder-level effort, not an ongoing operational model. Two people working full-time for four weeks can seed 200 camps.

### Tertiary Strategy: Structured Web Aggregation (Phase 2)

Post-MVP, explore automated aggregation from public sources — park and recreation department websites, school district enrichment catalogs, and camp association member directories. This requires:
- Legal review to ensure compliance with terms of service
- Data normalization pipeline to standardize inconsistent formats
- Human review layer before publishing aggregated listings

This is a Phase 2 capability, not an MVP dependency.

### Supply Threshold — Hard Launch Gate
**CampSpark will not open to parents until the following conditions are met:**

- Minimum 200 verified camp listings in the Bay Area
- Coverage across all major interest categories: sports, arts, STEM, outdoor, performing arts, and language
- At least 15 camps available for any given week in June, July, and August
- At least 10 camps per age group: ages 5-7, 8-10, 11-13, 14+

This threshold is non-negotiable. A parent who searches and finds 3 results churns and does not return. The first experience must feel comprehensive.

### Data Quality and Freshness

Camp information changes every season — dates, prices, availability, and sometimes the camp itself. Stale data is as damaging as no data.

**Mechanisms to ensure freshness:**
- Camps receive an automated "please verify your listing" email each January — before the planning season begins
- Listings that have not been updated in 12 months are flagged with a "not yet verified for this season" badge rather than removed
- Parents can report inaccurate listings via a one-click flag — flagged listings are reviewed within 48 hours
- Featured camp partners have a contractual commitment to update listings within 48 hours of any change

---

## 7. Feature Specifications

### 7.1 Camp Discovery

**Overview:**
The search and filtering experience is the heart of CampSpark. Parents should be able to go from zero to a shortlist of relevant camps in one focused session.

**Filters:**
- Child's age (or grade level)
- Interests — multi-select (sports, arts, STEM, outdoor, performing arts, language, etc.)
- Location — city, zip code, or distance radius from home or work address
- Date range — specific weeks or months
- Time window — start time, end time, full day vs. half day
- Budget — price range per week or per session
- Days of week — M-F, weekdays only, specific days

**Search behavior:**
- Filters are combinable and applied in real time
- Results update without page refresh
- Each result shows: camp name, activity type, dates, times, price, distance, and availability status
- Filters are saved per child profile for future sessions

**Edge cases:**
- No results state: suggests broadening one or two filters rather than showing an empty screen
- Sold out camps: shown with "Waitlist Available" rather than hidden — parents still want to know they exist

### 7.2 Camp Detail Pages

Each camp listing includes:
- Camp name and provider organization
- Activity type and description (2-3 sentences maximum)
- All available weeks and sessions with dates
- Daily schedule (start time, end time, days of week)
- Age range accepted
- Price per week or session
- Location with approximate driving time from user's saved home/work address
- Availability status (open, filling fast, waitlist, closed)
- External link to register on camp's own website

**Design principle:** A parent should be able to make a confident decision from this page without needing to open the camp's own website.

### 7.3 Summer Plan View

**Overview:**
A visual, calendar-like view of a child's summer — week by week — showing which camps are confirmed, saved, or still needed.

**Features:**
- Weekly grid view covering the full summer (June-August)
- Camps appear as blocks within their weeks
- Status labels: Confirmed, Saved, Researching, Gap (no camp selected yet)
- Multi-child view: toggle between children or see a combined household view
- Export to PDF or share via link

### 7.4 Social Coordination

**Overview:**
The feature that turns CampSpark from a useful tool into a platform with network effects.

**Features:**
- Parents connect with friends on CampSpark (opt-in, via email invite or link)
- When viewing a camp, parents see: "3 families in your network are considering this camp"
- Friends' summer plans are visible with permission — view only by default
- Parents can send a coordinate nudge: "We're thinking about Art Camp week of July 7 — interested?"

**Privacy model:**
- All social features are opt-in
- Friends can see your plan only if you explicitly share it
- Camp-level visibility requires mutual connection

### 7.5 Camp Self-Registration Portal

**Overview:**
The supply-side tool that powers CampSpark's listing database. Camp operators create and manage their own listings.

**Features:**
- Simple listing creation form: camp name, description, activity type, age range, dates, times, price, location, registration link
- Dashboard to update listing details and availability each season
- Basic analytics: how many parents viewed this listing, how many clicked through to register
- Featured placement upgrade option

**Design principle:** A camp operator who has never used a listing platform should be able to create a complete, high-quality listing in under 15 minutes.

---

## 8. User Stories

### Discovery
- As a parent, I want to filter camps by age and interest so I only see relevant options.
- As a parent, I want to quickly scan multiple camps side-by-side to compare dates, price, and location.
- As a parent, I want to search for camps near my office, not just my home, so I can factor pickup logistics into my decision.

### Scheduling
- As a parent, I want to see available camps for specific weeks so I can fill gaps in my child's summer calendar.
- As a parent, I want to filter by time window so I only see camps that work with my work schedule.

### Coordination
- As a parent, I want to know where my child's friends are attending camps so I can factor social preferences into our decision.
- As a parent, I want to share my summer plan with other parents so we can coordinate without switching to text or WhatsApp.

### Organization
- As a parent, I want all summer plans for my children organized in one place so I have a single source of truth.
- As a parent, I want to tag camps as confirmed, saved, or researching so I know where I am in the decision process.

### Camp Operators
- As a camp director, I want to create a listing in under 15 minutes so I can reach parents who are actively searching for camps like mine.
- As a camp director, I want to update my availability in real time so parents always see accurate information.

---

## 9. Success Metrics

### North Star Metric
**Time to summer plan** — the time from a parent's first session on CampSpark to having a complete, confident summer plan. Target: one focused session of under 2 hours versus several hours across multiple weekends (current manual process).

### Engagement Metrics
| Metric | Definition | Target (Year 1) |
|---|---|---|
| Sessions per planning season | Average number of sessions per user during Feb-April | 3-5 |
| Filters applied per session | Average number of search filters used | 4+ |
| Camps saved per user | Average camps added to summer plan | 6-10 |
| Plan completion rate | % of users who fill all summer weeks for at least one child | 40% |

### Social and Coordination Metrics
| Metric | Definition | Target (Year 1) |
|---|---|---|
| Shared plans created | Number of plans shared via link | 30% of active users |
| Network connections per user | Average friends connected on platform | 3+ |
| Invite acceptance rate | % of plan share links opened by recipient | 50% |

### Supply Metrics
| Metric | Definition | Target (Launch) |
|---|---|---|
| Total verified listings | Camp listings live at parent-facing launch | 200+ (Bay Area) |
| Category coverage | Interest categories with 10+ camps | 6 of 6 |
| Listing freshness | % of listings verified for current season | 90%+ |
| Camp self-serve adoption | % of listings created by camps themselves | 60%+ |

### Business Metrics
| Metric | Definition | Target (Year 1) |
|---|---|---|
| Free to paid conversion | % of free users who upgrade to premium | 8-12% |
| Camp partner listings | Number of camps paying for promoted placement | 200+ |
| Revenue per camp partner | Average annual revenue per paying camp | $300-$1,000 |

---

## 10. Business Model

### Revenue Streams

**Stream 1: Freemium Parent Subscriptions**

| Tier | Price | Features |
|---|---|---|
| Free | $0 | Basic discovery, up to 3 saved camps, one child profile |
| Premium | $9.99/month or $29.99/season | Unlimited saved camps, multi-child view, social coordination, plan sharing, waitlist alerts |

The free tier demonstrates value. The coordination features — the most differentiated part of CampSpark — are behind the paywall, creating a clear upgrade incentive.

**Stream 2: Camp Partner Listings (Promoted Placement)**

| Tier | Price | Features |
|---|---|---|
| Basic (free) | $0 | Standard listing, external registration link, basic analytics |
| Featured | $299/season | Promoted placement in relevant searches, featured badge, detailed analytics |
| Premier | $999/season | Top placement, featured on homepage, lead capture, priority support |

This model mirrors proven marketplace monetization. Camps have strong incentive to pay because CampSpark sits at the top of the parent's decision funnel.

### Unit Economics (Illustrative)
- 10,000 active parent users, 10% premium conversion at $30/season: **$30K from subscriptions**
- 200 camps on Featured or Premier at $400 average: **$80K from camp partners**
- **Year 1 total revenue target: ~$110K** — appropriate for a pre-seed stage product proving the model

---

## 11. Go-to-Market Strategy

### Beachhead Market
The Bay Area — specifically school communities in Sunnyvale, Santa Clara, San Jose, and Palo Alto. Dense population of dual-income tech households with high summer camp spending and strong peer networks.

### Growth Strategy

**Phase 1: Build supply before demand (Months 1-2)**
- Manually seed 150-200 Bay Area camp listings
- Outreach to 300+ camp operators for self-serve listings
- Do not launch to parents until supply threshold is met — this is a hard gate

**Phase 2: Seed the parent network (Months 2-4)**
- Target 3-5 school communities in the Bay Area
- Partner with PTA/PTO organizations to distribute CampSpark to parent networks
- Recruit 10-20 Social Coordinator parent advocates per school
- Measure: invite-driven signups

**Phase 3: Expand geographically (Months 6-12)**
- Replicate Bay Area playbook in Seattle, Austin, Chicago, and Boston
- Scale camp partner program in each new market

### The Viral Loop
1. One parent discovers CampSpark
2. Creates a summer plan and shares it with 2-3 other parents
3. Those parents sign up to view the plan
4. They create their own plans and share them
5. The network grows organically within school communities

---

## 12. Launch Readiness

### Hard Supply Gate
CampSpark will not open to parents until all supply threshold conditions are met (see Data Strategy section). This is non-negotiable. Premature launch with thin supply causes immediate churn and reputational damage that is very hard to recover from.

### Quality Gates
- [ ] 200 verified camp listings live in the Bay Area
- [ ] All 6 major interest categories covered with 10+ camps each
- [ ] Camp self-serve listing tool tested with 10 real camp operators
- [ ] Parent discovery flow tested with 15 real parents in target demographic
- [ ] Shared plan links tested across major browsers and email clients
- [ ] Listing freshness and staleness detection working correctly
- [ ] Mobile-responsive design validated (parents will check on phones even if primary use is desktop)

### Launch Sequence
1. **Supply build:** Seed listings and onboard camp self-serve portal (Months 1-2)
2. **Private beta:** 20-30 parents in 2-3 school communities (Month 3)
3. **PTA/PTO partnerships:** Soft launch through school networks (Month 4)
4. **General availability:** Open to Bay Area with waitlist for other markets (Month 5)

### Rollback Plan
If at launch parents report finding no relevant results in a specific category or geography — immediately flag that segment as "limited coverage" with a "more camps coming soon" message rather than showing empty results. Recruit targeted camps in the gap area within 2 weeks. Do not let empty results stand without explanation.

---

## 13. Risks and Mitigations

### Risk 1: Parent Churn from Thin Supply
**Risk:** Parents search for camps in a specific category or geography and find too few options. They leave and do not return.
**Likelihood:** High if launch threshold is not enforced
**Impact:** Very high — first impressions in consumer products are nearly impossible to recover from
**Mitigation:** Hard supply gate before parent-facing launch. Minimum 200 camps across all major categories in the Bay Area before a single parent is invited. No exceptions.

### Risk 2: Camp Self-Serve Adoption is Slow
**Risk:** Camp operators are slow to create listings — smaller independent camps have limited digital sophistication and bandwidth.
**Likelihood:** Medium
**Impact:** High — delays the supply threshold and therefore the parent launch
**Mitigation:** Personal outreach to every camp in the beachhead market. Offer to create the listing on their behalf based on information from their website — then ask them to review and approve. Reduce the work required of the camp to near zero for initial listing creation.

### Risk 3: Data Staleness Damages Trust
**Risk:** A parent plans around a camp based on CampSpark data, visits the camp's website, and discovers the information is wrong — wrong dates, wrong price, or the camp isn't running that year.
**Likelihood:** Medium (camp details change every season)
**Impact:** Very high — nothing destroys trust faster than acting on wrong information
**Mitigation:** Annual listing verification process every January. Staleness badges after 12 months without an update. Parent-flagging mechanism with 48-hour review SLA. Featured camp partners contractually committed to 48-hour update policy.

### Risk 4: Cold Start on Social Features
**Risk:** Social coordination features are useless if none of a parent's friends are on the platform.
**Likelihood:** High in early months
**Impact:** Medium (affects premium conversion; does not affect core discovery value)
**Mitigation:** Allow plan sharing via link — recipient does not need a CampSpark account to view. Show "invite friends" prompts at high-intent moments. Target Social Coordinator parents first — they bring their networks with them.

### Risk 5: Seasonality Creates Unsustainable Business
**Risk:** 80% of usage is concentrated in February-April. The business is not viable if it requires a full team year-round for 3 months of revenue.
**Likelihood:** High (seasonality is real)
**Impact:** Medium (operational, not product validity)
**Mitigation:** Design the team and cost structure around seasonality from day one. Annual subscription pricing captures revenue before and after the peak season. Explore off-season hooks: fall activity planning, winter break camps, early access to next summer's listings.

---

## 14. Open Questions

| Question | Why It Matters | How to Resolve |
|---|---|---|
| What is the right free vs. paid feature split? | Too generous = no conversion; too restrictive = no adoption | A/B test paywall placement after 500 active users |
| Should plan sharing require the recipient to sign up? | Affects viral growth vs. product adoption tradeoff | Test both in beta |
| How do we handle camp data for markets outside the Bay Area? | Affects geographic expansion strategy significantly | Validate Bay Area model fully before expanding |
| What is the right pricing for camp partners in Year 1? | Mispricing kills B2B revenue stream | Pilot $99, $299, and $999 tiers with 20 Bay Area camps |
| Should CampSpark eventually own registration? | Fundamentally changes product scope and business model | Revisit after 10,000 active parents and strong supply partnerships |

---

## 15. Future Roadmap (Post-MVP)

### Near Term (6-12 months post-launch)
- **AI-powered recommendations** — "Based on your child's age, past camps, and your network's choices, here are 5 camps we think you'll love"
- **Waitlist alerts** — "A spot opened at Coding Camp — register now before it fills again"
- **Camp operator analytics dashboard** — views, click-throughs, and conversion data for paying camp partners
- **Automated listing aggregation** — structured scraping from park and recreation department and school district directories

### Medium Term (Year 2)
- **Mobile app** — for quick checks and coordination on the go
- **Calendar integration** — sync confirmed camps to Google Calendar or Outlook
- **Group signup coordination** — "Create a group of 5 families for Art Camp week of July 7"
- **Parent reviews and ratings** — social proof once the user base is large enough to be meaningful

### Longer Term (Year 3+)
- **Direct registration and payment** — own the full transaction once trust and scale are established
- **National expansion** — beyond major metros into suburban markets
- **B2B SaaS for camp operators** — full CRM, registration management, and parent communication tools

---

## 16. Appendix

### Competitive Landscape Summary

| Platform | Discovery | Planning | Coordination | Supply Model | Business Model |
|---|---|---|---|---|---|
| Sawyer | Partial | None | None | Camp self-serve | Transaction fee |
| ActivityHero | Partial | None | None | Camp self-serve | Transaction fee |
| Facebook Groups | Unstructured | None | Informal | User-generated | Ads |
| Google Sheets (DIY) | None | Manual | Manual | N/A | Free |
| **CampSpark** | **Full** | **Full** | **Full** | **Self-serve + seeded** | **Freemium + B2B** |

### Assumptions Log
| Assumption | Confidence | Validation Needed |
|---|---|---|
| Parents spend 3+ hours on camp planning per season | High — personal experience + peer validation | Survey 50 parents |
| Social coordination drives adoption | High — organic Google Sheet sharing validates this | Test with seed users |
| Camps will create free listings if outreach is personal | Medium | Test with 30 Bay Area camps pre-launch |
| Camps will pay for promoted placement | Medium — analogous models work in other verticals | Pilot with 10 camps |
| Desktop is the right primary surface | High — planning behavior is research-heavy | Validate with session analytics |
| 200 camps is sufficient for a credible Bay Area launch | Medium | Validate through parent search testing before launch |

---

*CampSpark is a portfolio project created to demonstrate product thinking, marketplace strategy, and end-to-end PRD ownership. It does not represent a shipped product.*

*Author: Sonal Singh | Principal Product Manager | sonalshankar06@gmail.com*