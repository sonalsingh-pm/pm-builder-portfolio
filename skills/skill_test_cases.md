# SKILL: Writing Test Cases

## Purpose
Test cases translate user stories into verifiable pass/fail scenarios. They ensure the prototype and eventual product behave as intended — including in edge cases and failure conditions that user stories often gloss over.

In a portfolio context, test cases demonstrate that you think beyond the happy path and understand quality as a product discipline, not just an engineering one.

---

## Format

Use a table for all test cases:

| Test ID | Feature | Scenario | Steps | Expected Result | Pass/Fail |
|---|---|---|---|---|---|
| TC-001 | Camp Search | Filter by age returns correct results | 1. Open search. 2. Select age 8. 3. View results. | Only camps with age range including 8 are shown. | |

---

## Test ID Convention

Use a consistent prefix per feature area:
- `TC-SRCH-001` — Search and filtering
- `TC-PLAN-001` — Planning and saving
- `TC-COORD-001` — Social coordination
- `TC-CAMP-001` — Camp operator portal
- `TC-AUTH-001` — Authentication and accounts
- `TC-EDGE-001` — Edge cases and error states

---

## Types of Test Cases to Include

### 1. Happy Path Tests
The primary flow works as expected when everything goes right.
- User searches and finds relevant results
- User saves a camp successfully
- Manager approves a swap successfully

### 2. Filter and Search Tests
Every filter combination produces the correct result set.
- Single filter applied correctly
- Multiple filters applied together correctly
- Filter that returns no results shows empty state
- Removing a filter restores previous results

### 3. Edge Case Tests
What happens at the boundaries and in unusual conditions.
- Search returns zero results
- User applies maximum number of filters
- Data fields are empty or missing
- User performs an action they are not authorized for

### 4. Error State Tests
The product behaves gracefully when something goes wrong.
- Network failure during a search
- Form submitted with missing required fields
- User tries to access a shared plan they don't have permission for

### 5. Cross-Device Tests (for mobile products)
- Primary flow works on iOS Safari
- Primary flow works on Android Chrome
- Layout is not broken at 390px width
- Touch targets are large enough to tap accurately

---

## Steps Format

Steps should be specific enough that someone who has never used the product could follow them:

**Too vague:**
- "Search for a camp"
- "Apply filters"

**Correct:**
1. Navigate to the search page
2. Enter "San Jose" in the location field
3. Select "STEM" from the interest dropdown
4. Select age "10" from the age filter
5. Click "Search" or observe real-time results

---

## Expected Result Format

Expected results must be specific and binary — either the result happened or it didn't:

**Too vague:**
- "Results are shown"
- "Page works correctly"

**Correct:**
- "Only camps tagged as STEM with age range including 10 and location within San Jose are displayed"
- "A message reading 'No camps found. Try broadening your filters.' is displayed with a button to reset all filters"

---

## Quality Checklist

Before delivering test cases, verify:
- [ ] Every user story has at least one corresponding test case
- [ ] Every filter has its own test case
- [ ] At least one empty state test case per feature
- [ ] At least one error state test case per feature
- [ ] Steps are specific enough for someone unfamiliar with the product to follow
- [ ] Expected results are specific and binary
- [ ] Test IDs follow the naming convention
- [ ] Edge cases are covered — not just happy paths
- [ ] Pass/Fail column is blank — filled in during actual testing

---

## Example Test Cases — CampSpark

| Test ID | Feature | Scenario | Steps | Expected Result |
|---|---|---|---|---|
| TC-SRCH-001 | Camp Search | Age filter returns correct results | 1. Open search. 2. Select age 10. 3. Observe results. | Only camps with age range including 10 are shown. Camps for ages 5-8 only are hidden. |
| TC-SRCH-002 | Camp Search | Multiple filters applied together | 1. Select age 10. 2. Select interest "STEM". 3. Select location "San Jose". | Only camps matching all three criteria are shown. |
| TC-SRCH-003 | Camp Search | No results state | 1. Select age 5. 2. Select interest "Coding". 3. Select budget "$0-$100". | Empty state shown with message "No camps found. Try broadening your search." and a reset button. |
| TC-PLAN-001 | Summer Plan | Save a camp | 1. View camp detail. 2. Click "Save". 3. Navigate to Summer Plan. | Camp appears in Summer Plan under the correct week with status "Saved". |
| TC-COORD-001 | Social | Share a plan via link | 1. Open Summer Plan. 2. Click "Share". 3. Copy link. 4. Open link in incognito browser. | Recipient can view the summer plan without signing in. Edit controls are not visible. |
| TC-EDGE-001 | Camp Search | Filter reset | 1. Apply 3 filters. 2. Click "Reset all filters". | All filters are cleared. Full unfiltered result set is shown. |
| TC-CAMP-001 | Camp Portal | Create a listing | 1. Go to camp portal. 2. Fill all required fields. 3. Click "Publish". | Listing appears in parent-facing search results within the correct category. |