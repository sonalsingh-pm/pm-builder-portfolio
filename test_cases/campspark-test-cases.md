# CampSpark – Test Cases (Portfolio Example)

Author: Sonal Singh  
Status: Conceptual test‑case outline for MVP features  

---

## 1. Camp Discovery & Filtering

| TC ID | Scenario | Steps | Expected Result |
|-------|----------|-------|-----------------|
| TC1 | Happy path search by age and interest | 1. Select age 8–10. 2. Select interest “basketball”. 3. Click “Search”. | Results show only basketball camps for 8–10 year olds. |
| TC2 | Empty results for tight filters | 1. Set strict filters (age 13–14, interest “coding”, distance 5 miles, week June 10–14). 2. Click “Search”. | System shows “No camps match your filters” and no error. |
| TC3 | Distance radius filter | 1. Set home location. 2. Set radius to 10 miles. 3. Click “Search”. | Only camps within 10 miles of home location appear. |
| TC4 | Time‑window search | 1. Set time window 9 AM–3 PM. 2. Click “Search”. | Results show only camps that operate within 9 AM–3 PM. |

---

## 2. Plan Creation & Organization

| TC ID | Scenario | Steps | Expected Result |
|-------|----------|-------|-----------------|
| TC5 | Create a plan for one child | 1. Click “New Plan”. 2. Select child name and summer year. 3. Click “Create”. | A new plan view opens with a blank grid for that child. |
| TC6 | Add a camp to a plan | 1. Search for a camp. 2. Click “Add to Plan”. 3. Select the child’s plan. | Camp appears in the plan grid for that week. |
| TC7 | Tag a camp with status | 1. Hover over a camp in the plan. 2. Click “Save”. 3. Select “wishlist”. | Camp shows a “wishlist” label in the plan view. |
| TC8 | Remove a camp from a plan | 1. Open a plan. 2. Select a camp in the grid. 3. Click “Remove”. | Camp is removed from the plan grid but still exists in search. |

---

## 3. Sharing & Coordination

| TC ID | Scenario | Steps | Expected Result |
|-------|----------|-------|-----------------|
| TC9 | Share a plan via link | 1. Open a plan. 2. Click “Share”. 3. Copy the generated link. 4. Open link in another browser/session. | Second user sees the plan in read‑only mode. |
| TC10 | Accept a shared plan invite | 1. Share a plan with a friend. 2. Friend clicks link. 3. Friend clicks “Accept Invite”. | Friend’s account gains view (or edit) access as specified. |
| TC11 | Friend‑camp overlay | 1. Subscribe to a friend’s plan. 2. Open my child’s plan. | Friend’s camps appear as overlays on the same week grid. |

---

## 4. Camp Details & Registration

| TC ID | Scenario | Steps | Expected Result |
|-------|----------|-------|-----------------|
| TC12 | Open camp details | 1. Click a camp in the list or grid. | Panel or page shows name, activity type, dates, timings, age range, price, location, and external link. |
| TC13 | External registration flow | 1. Open camp details. 2. Click “Register on Camp Website”. | New tab opens with the camp’s official site; the original CampSpark tab remains open. |
| TC14 | Missing price or location | 1. Find a camp that has no price or location listed. 2. Click “Details”. | Details view shows “Price not available” or “Location not specified” instead of being blank. |

---

## 5. Edge Cases & Robustness

| TC ID | Scenario | Steps | Expected Result |
|-------|----------|-------|-----------------|
| TC15 | GDPR / privacy‑aware sharing | 1. Share a plan with a parent who has not accepted terms. 2. Confirm consent flow. | Parent must explicitly accept consent before the plan is fully visible. |
| TC16 | Seasonality (out‑of‑season) | 1. Access CampSpark in October (off‑season). 2. Perform search. | System shows no camps by default but allows saving “wishlist” items for next year. |

This test‑case file is written as a **portfolio artifact** for Senior/Principal‑level PM roles and does not represent a shipped product.