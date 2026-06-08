# CampSpark — User Stories
**Product:** CampSpark | **Author:** Sonal Singh | **Last Updated:** May 2026

---

## Sprint 1 — Core Discovery Flow
*The primary flow: Landing → Filter → Results → Camp Detail → Save to Plan*

---

### Discovery & Search

**US-001**
As a working parent, I want to see a list of camps near me when I land on CampSpark so that I can immediately start evaluating options without having to search first.

*Acceptance criteria:*
- Default results show all camps sorted by distance from a default location (San Jose, CA)
- Each result shows: camp name, category, age range, price per week, distance, and available weeks
- Results count is visible: "Showing 18 camps near San Jose, CA"
- Page loads with results visible without any interaction required

---

**US-002**
As a working parent, I want to filter camps by my child's age so that I only see camps my child is eligible to attend.

*Acceptance criteria:*
- Age filter is a dropdown with ranges: 5-6, 7-8, 9-10, 11-12, 13-14
- Selecting an age immediately hides camps whose age range does not include the selected age
- Results count updates to reflect filtered results
- Selecting "Any age" removes the filter and restores all results
- Filter works without a page reload or Apply button

---

**US-003**
As a working parent, I want to filter camps by interest category so that I only see camps matching my child's interests.

*Acceptance criteria:*
- Interest filter shows these categories as selectable chips: STEM, Sports, Arts, Outdoors, Performing Arts, Language
- Selecting one category filters results to that category immediately
- Multiple categories can be selected — results show camps matching any selected category
- Active category chips are visually distinct from inactive ones
- Deselecting all chips restores all results

---

**US-004**
As a working parent, I want to filter camps by weekly budget so that I don't see camps I can't afford.

*Acceptance criteria:*
- Budget filter is a range slider from $0 to $800 per week
- Moving the slider immediately hides camps above the selected maximum price
- The selected budget is displayed numerically next to the slider: "Up to $400/week"
- Results count updates to reflect the budget filter

---

**US-005**
As a working parent, I want to filter camps by the specific week I need coverage so that I only see camps available during that week.

*Acceptance criteria:*
- Week filter is a dropdown showing all summer weeks: Jun 16, Jun 23, Jun 30, Jul 7, Jul 14, Jul 21, Jul 28, Aug 4, Aug 11, Aug 18
- Selecting a week shows only camps that have availability during that week
- Camps that are full during the selected week are hidden
- Results count updates to reflect the week filter

---

**US-005a**
As a working parent, I want to filter camps by time of day so that I only see camps that fit within my work schedule.

*Acceptance criteria:*
- Time filter is a dropdown with these options: Any time, Full day (9am-3pm), Morning only (9am-12pm), Afternoon only (1pm-4pm)
- Selecting a time option immediately hides camps that don't match that schedule
- Each camp card shows its daily schedule — start time and end time
- Default is "Any time" — all camps visible
- Results count updates to reflect the time filter
- Time filter works in combination with all other filters

---

**US-005b**
As a working parent, I want to filter camps by distance from my location so that I only see camps within a reasonable driving radius.

*Acceptance criteria:*
- Distance filter is a dropdown: Within 5 miles, Within 10 miles, Within 15 miles, Within 25 miles, Any distance
- Default location is San Jose, CA — shown as a small location indicator in the nav or filter panel
- Selecting a radius immediately hides camps beyond that distance
- Distance is shown on each camp card in miles
- Results count updates to reflect the distance filter
- Distance filter works in combination with all other filters

---

**US-006**
As a working parent, I want to see an empty state when my filters return no results so that I know what to do next rather than staring at a blank page.

*Acceptance criteria:*
- When no camps match the active filters a friendly empty state appears
- Empty state includes: an icon, heading "No camps found", and a suggestion to broaden filters
- A "Clear all filters" button resets all filters when clicked
- The empty state does not show a spinner or loading indicator

---

**US-007**
As a working parent, I want to see which of my active filters are applied at a glance so that I can quickly understand why I'm seeing these results.

*Acceptance criteria:*
- Active filters are shown as dismissible tags above the results
- Each tag shows the filter name and value: "Age: 9-10 ×", "Interest: STEM ×", "Time: Morning ×"
- Clicking the × on a tag removes that individual filter
- A "Clear all" option is visible when any filters are active

---

### Camp Detail

**US-008**
As a working parent, I want to view full details of a camp without leaving the results page so that I can evaluate it without losing my place in the results.

*Acceptance criteria:*
- Clicking a camp card opens a slide-in detail panel from the right
- The results list remains visible behind the panel
- The panel shows: camp name, provider, full description, age range, price, location, daily schedule, all available weeks with status, and a registration link
- The panel can be closed by clicking the X button or clicking outside the panel
- Closing the panel returns focus to the results list

---

**US-009**
As a working parent, I want to see which weeks are available, filling fast, or full for a camp so that I can make a timely decision about registering.

*Acceptance criteria:*
- Each week is shown as a selectable button in the camp detail panel
- Available weeks: green button, labeled "Open"
- Filling fast weeks: amber button, labeled "Filling fast"
- Full weeks: red button, labeled "Full — Join waitlist"
- Full weeks are visible but not selectable for saving to plan
- Clicking a week button selects it and enables the "Save to My Plan" button

---

### Social Coordination

**US-010**
As a working parent, I want to see a social signal on camps my friends' families are considering so that I can factor my child's social preferences into my decision.

*Acceptance criteria:*
- On camps where friends are considering, a signal appears: "3 families in your network are considering this"
- The signal appears on the camp card in results and in the detail panel
- On camps with no network activity, a teaser appears: "See where your friends are sending their kids — Invite friends"
- The teaser includes a small "Invite friends" link
- The social signal does not dominate the card — it is secondary information

---

**US-010a**
As a working parent, I want to see which specific families in my network are considering a camp so that I can reach out to coordinate directly.

*Acceptance criteria:*
- Clicking the social signal ("3 families in your network considering this") expands to show family names
- Expanded state shows: avatar initials, family name, and "considering" or "registered" status
- Example: "Emma's family · considering", "Priya's family · registered", "+1 more"
- Clicking anywhere outside the expanded state collapses it
- This works on both the camp card and the detail panel

---

**US-010b**
As a working parent, I want to invite friends to CampSpark so that I can see where they are sending their kids and coordinate together.

*Acceptance criteria:*
- Clicking "Invite friends" opens a modal
- Modal title: "Invite friends to coordinate"
- Modal shows a shareable link: "campspark.com/invite/[username]" with a "Copy link" button
- Clicking "Copy link" changes the button to "Copied ✓" for 2 seconds
- Modal also shows an email input: "Or invite by email" with a "Send invite" button
- Clicking "Send invite" shows a confirmation: "Invite sent to [email]"
- Modal can be closed with an X button or clicking outside
- A brief explanation is shown: "When friends join, you'll see which camps they're considering"

---

### Save to Plan

**US-011**
As a working parent, I want to save a camp and week to my summer plan so that I can track what I'm considering without having to remember it.

*Acceptance criteria:*
- After selecting a week in the camp detail panel, clicking "Save to My Plan" saves the camp
- A toast notification appears: "Bay Area Coding Camp saved to Maya's plan"
- The save button changes state to "Saved ✓" after clicking
- The camp card in the results list shows a filled save icon indicating it is saved
- Saved camps persist within the session

---

**US-012**
As a working parent, I want to save a camp directly from the results list without opening the detail panel so that I can quickly shortlist camps during an initial scan.

*Acceptance criteria:*
- Each camp card has a save icon (heart) visible on hover
- Clicking the save icon saves the camp without opening the detail panel
- When saved via the card, the system uses the first available week by default
- A toast notification confirms: "Saved — tap to choose a specific week"
- The save icon changes to a filled state immediately on click

---

**US-013**
As a working parent, I want to see how many camps I have saved so that I know how far along my planning is.

*Acceptance criteria:*
- The navigation bar shows a saved count: "My Plan (3)" updating in real time as camps are saved
- The count is visible on all screens without navigating away
- Clicking "My Plan" in the nav shows a summary of saved camps

---

## Sprint 2 — Summer Plan View
*Build after Sprint 1 flow is validated.*

- US-014: View saved camps in a weekly calendar grid
- US-015: See gaps in the summer where no camp is selected
- US-016: Toggle between multiple children's plans
- US-017: Remove a camp from the plan
- US-018: See total budget across all saved camps

## Sprint 3 — Social Coordination (Full)
*Build after Sprint 2 is validated.*

- US-019: Share summer plan via a link
- US-020: View a shared plan without signing in
- US-021: See friend's plan and compare camp selections

## Sprint 4 — Camp Operator Portal
*Build after parent-side flows are validated.*

- US-022: Camp operator creates a listing
- US-023: Camp operator updates availability
- US-024: Camp operator views listing analytics

---

*User stories authored by Sonal Singh | Principal Product Manager*
*sonalshankar06@gmail.com | linkedin.com/in/sonalsingh444*