# SKILL: Building a Functional HTML Prototype

## Purpose
The prototype is the most powerful artifact in this portfolio. It is the difference between "I wrote a PRD about this" and "I built this." A hiring manager who can click through a working prototype remembers you. A hiring manager who reads a PRD forgets you.

The prototype is not a wireframe. It is not a mockup. It is a functional, interactive HTML experience that feels like a real product — Stripe-quality UI, real data, real interactions.

---

## Before Building — Read These First
1. The user stories for this project — they define what screens and flows to build
2. The PRD for this project — data requirements, feature details, personas
3. This skill file — technical and design standards

**Important:** Build only the flows specified in the user stories for this sprint. Do not build the entire product at once. Validate one flow, then expand.

---

## Technical Stack

### Languages
- **HTML5** — semantic markup. Use proper elements: `<nav>`, `<main>`, `<section>`, `<article>`, `<button>`, `<input>` etc.
- **CSS3** — all styles inline in a `<style>` tag. No external stylesheets.
- **Vanilla JavaScript** — all logic inline in a `<script>` tag at the bottom of body. No frameworks. No jQuery. No external libraries.

### Single File Rule
Every prototype is a single self-contained HTML file. No external dependencies except Google Fonts loaded via CSS @import. Must work by double-clicking the file — no server, no npm, no build step.

### Data Layer
Always define sample data as JavaScript arrays or objects at the top of the script tag. Never hardcode data directly into HTML — it makes filtering and dynamic rendering impossible.

```javascript
// Always at the top of <script>
const DATA = [
  { id: 1, name: "...", category: "...", price: 0, ... },
  { id: 2, name: "...", category: "...", price: 0, ... },
];

// State object — tracks current UI state
const STATE = {
  filters: { category: null, age: null, budget: null },
  saved: [],
  currentView: 'discovery',
  selectedItem: null,
};
```

### Rendering Pattern
Use a render function that reads from STATE and DATA and redraws the relevant part of the UI. Never manipulate the DOM directly for content — always re-render from state.

```javascript
function render() {
  const filtered = applyFilters(DATA, STATE.filters);
  renderResults(filtered);
  renderFilters();
  renderNav();
}

function applyFilters(data, filters) {
  return data.filter(item => {
    if (filters.category && item.category !== filters.category) return false;
    if (filters.budget && item.price > filters.budget) return false;
    return true;
  });
}
```

### Event Handling
Use event delegation on a parent container rather than attaching listeners to individual elements. This handles dynamically rendered content correctly.

```javascript
document.getElementById('results').addEventListener('click', (e) => {
  const card = e.target.closest('[data-id]');
  if (card) openDetail(card.dataset.id);

  const saveBtn = e.target.closest('[data-save]');
  if (saveBtn) saveItem(saveBtn.dataset.save);
});
```

### Navigation Between Views
Use a single-page architecture with view switching via CSS classes and JavaScript state:

```javascript
function showView(viewName) {
  document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
  document.getElementById(`view-${viewName}`).classList.add('active');
  STATE.currentView = viewName;
}
```

```css
.view { display: none; }
.view.active { display: block; }
```

---

## CSS Architecture

### CSS Variables — Define at :root
Always define the full design system as CSS variables. This ensures consistency and makes theming easy.

```css
:root {
  /* Colors — Primary */
  --color-primary: #4F46E5;        /* indigo — adjust per project */
  --color-primary-dark: #4338CA;
  --color-primary-light: #EEF2FF;
  --color-primary-border: #C7D2FE;

  /* Colors — Neutrals */
  --color-bg: #FFFFFF;
  --color-bg-soft: #F8FAFC;
  --color-bg-muted: #F1F5F9;
  --color-text: #0F172A;
  --color-text-mid: #334155;
  --color-text-muted: #64748B;
  --color-border: #E2E8F0;
  --color-border-strong: #CBD5E1;

  /* Colors — Status */
  --color-success: #10B981;
  --color-success-light: #D1FAE5;
  --color-warning: #F59E0B;
  --color-warning-light: #FEF3C7;
  --color-danger: #EF4444;
  --color-danger-light: #FEE2E2;

  /* Typography */
  --font-display: 'Fraunces', Georgia, serif;
  --font-body: 'Inter', system-ui, -apple-system, sans-serif;

  /* Type Scale */
  --text-xs: 0.75rem;       /* 12px — labels, badges */
  --text-sm: 0.875rem;      /* 14px — secondary text, captions */
  --text-base: 1rem;        /* 16px — body text */
  --text-lg: 1.125rem;      /* 18px — large body, card titles */
  --text-xl: 1.25rem;       /* 20px — section subheadings */
  --text-2xl: 1.5rem;       /* 24px — section headings */
  --text-3xl: 1.875rem;     /* 30px — page headings */
  --text-4xl: 2.25rem;      /* 36px — hero headings */
  --text-5xl: 3rem;         /* 48px — display headings */

  /* Font Weights */
  --weight-light: 300;
  --weight-regular: 400;
  --weight-medium: 500;
  --weight-semibold: 600;
  --weight-bold: 700;

  /* Spacing — 4px base unit */
  --space-1: 0.25rem;   /* 4px */
  --space-2: 0.5rem;    /* 8px */
  --space-3: 0.75rem;   /* 12px */
  --space-4: 1rem;      /* 16px */
  --space-5: 1.25rem;   /* 20px */
  --space-6: 1.5rem;    /* 24px */
  --space-8: 2rem;      /* 32px */
  --space-10: 2.5rem;   /* 40px */
  --space-12: 3rem;     /* 48px */
  --space-16: 4rem;     /* 64px */

  /* Border Radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-xl: 16px;
  --radius-full: 9999px;

  /* Shadows */
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
  --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.07), 0 2px 4px -1px rgba(0,0,0,0.05);
  --shadow-lg: 0 10px 15px -3px rgba(0,0,0,0.08), 0 4px 6px -2px rgba(0,0,0,0.04);
  --shadow-xl: 0 20px 25px -5px rgba(0,0,0,0.08), 0 10px 10px -5px rgba(0,0,0,0.03);

  /* Transitions */
  --transition-fast: 150ms ease;
  --transition-base: 200ms ease;
  --transition-slow: 300ms ease;

  /* Layout */
  --max-width: 1200px;
  --nav-height: 64px;
}
```

### Typography Classes
```css
/* Always import these fonts */
@import url('https://fonts.googleapis.com/css2?family=Fraunces:wght@300;400;600;700;900&family=Inter:wght@300;400;500;600;700&display=swap');

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
  font-family: var(--font-body);
  font-size: var(--text-base);
  color: var(--color-text);
  background: var(--color-bg);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

h1, h2, h3 { font-family: var(--font-display); letter-spacing: -0.03em; line-height: 1.1; }
h1 { font-size: var(--text-4xl); font-weight: var(--weight-bold); }
h2 { font-size: var(--text-3xl); font-weight: var(--weight-bold); }
h3 { font-size: var(--text-xl); font-weight: var(--weight-semibold); }
```

### Navigation
```css
nav {
  position: fixed; top: 0; left: 0; right: 0;
  height: var(--nav-height); z-index: 100;
  background: rgba(255,255,255,0.92);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--color-border);
  display: flex; align-items: center;
  padding: 0 var(--space-8);
  gap: var(--space-8);
}
```

### Buttons — Four Variants
```css
.btn {
  display: inline-flex; align-items: center; gap: var(--space-2);
  padding: var(--space-3) var(--space-6);
  border-radius: var(--radius-md);
  font-family: var(--font-body);
  font-size: var(--text-sm); font-weight: var(--weight-medium);
  cursor: pointer; border: none;
  transition: all var(--transition-base);
  text-decoration: none; white-space: nowrap;
}
.btn-primary { background: var(--color-primary); color: white; }
.btn-primary:hover { background: var(--color-primary-dark); transform: translateY(-1px); box-shadow: var(--shadow-md); }

.btn-secondary { background: white; color: var(--color-primary); border: 1px solid var(--color-primary-border); }
.btn-secondary:hover { background: var(--color-primary-light); transform: translateY(-1px); }

.btn-ghost { background: transparent; color: var(--color-text-mid); }
.btn-ghost:hover { background: var(--color-bg-soft); color: var(--color-text); }

.btn-sm { padding: var(--space-2) var(--space-4); font-size: var(--text-xs); }
.btn-lg { padding: var(--space-4) var(--space-8); font-size: var(--text-base); }
.btn:disabled { opacity: 0.5; cursor: not-allowed; transform: none; }
```

### Cards
```css
.card {
  background: white;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-xl);
  padding: var(--space-6);
  box-shadow: var(--shadow-sm);
  transition: all var(--transition-base);
}
.card:hover {
  box-shadow: var(--shadow-lg);
  border-color: var(--color-primary-border);
  transform: translateY(-2px);
}
```

### Badges and Chips
```css
.badge {
  display: inline-flex; align-items: center; gap: var(--space-1);
  padding: var(--space-1) var(--space-3);
  border-radius: var(--radius-full);
  font-size: var(--text-xs); font-weight: var(--weight-medium);
  white-space: nowrap;
}
.badge-success { background: var(--color-success-light); color: #065F46; }
.badge-warning { background: var(--color-warning-light); color: #92400E; }
.badge-danger  { background: var(--color-danger-light);  color: #991B1B; }
.badge-primary { background: var(--color-primary-light); color: var(--color-primary); }
.badge-neutral { background: var(--color-bg-muted); color: var(--color-text-muted); }
```

### Form Elements
```css
.input {
  width: 100%; padding: var(--space-3) var(--space-4);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  font-family: var(--font-body); font-size: var(--text-sm);
  color: var(--color-text); background: white;
  transition: border-color var(--transition-fast);
  outline: none;
}
.input:focus { border-color: var(--color-primary); box-shadow: 0 0 0 3px var(--color-primary-light); }

.select {
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24' fill='none' stroke='%2364748B' stroke-width='2'%3E%3Cpolyline points='6 9 12 15 18 9'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right var(--space-3) center;
  padding-right: var(--space-8);
}
```

### Filter Chips — for multi-select filters
```css
.filter-chip {
  padding: var(--space-2) var(--space-4);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-full);
  font-size: var(--text-sm); font-weight: var(--weight-medium);
  color: var(--color-text-muted); background: white;
  cursor: pointer; transition: all var(--transition-fast);
  user-select: none;
}
.filter-chip:hover { border-color: var(--color-primary); color: var(--color-primary); }
.filter-chip.active {
  background: var(--color-primary); color: white;
  border-color: var(--color-primary);
}
```

### Empty State
```css
.empty-state {
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  padding: var(--space-16) var(--space-8);
  text-align: center; gap: var(--space-4);
}
.empty-state-icon { font-size: 3rem; opacity: 0.3; }
.empty-state-title { font-size: var(--text-xl); font-weight: var(--weight-semibold); color: var(--color-text); }
.empty-state-desc { font-size: var(--text-sm); color: var(--color-text-muted); max-width: 320px; }
```

### Modal
```css
.modal-overlay {
  position: fixed; inset: 0; z-index: 200;
  background: rgba(0,0,0,0.4);
  display: flex; align-items: center; justify-content: center;
  padding: var(--space-6);
  opacity: 0; pointer-events: none;
  transition: opacity var(--transition-base);
}
.modal-overlay.active { opacity: 1; pointer-events: all; }
.modal {
  background: white; border-radius: var(--radius-xl);
  padding: var(--space-8); width: 100%; max-width: 480px;
  box-shadow: var(--shadow-xl);
  transform: translateY(16px);
  transition: transform var(--transition-base);
}
.modal-overlay.active .modal { transform: translateY(0); }
```

### Slide-in Panel (for detail views)
```css
.panel {
  position: fixed; top: 0; right: 0; bottom: 0;
  width: 480px; max-width: 100%;
  background: white; z-index: 150;
  box-shadow: var(--shadow-xl);
  overflow-y: auto;
  transform: translateX(100%);
  transition: transform var(--transition-slow);
}
.panel.active { transform: translateX(0); }
.panel-overlay {
  position: fixed; inset: 0; z-index: 140;
  background: rgba(0,0,0,0.3);
  opacity: 0; pointer-events: none;
  transition: opacity var(--transition-base);
}
.panel-overlay.active { opacity: 1; pointer-events: all; }
```

### Responsive Layout
```css
/* Mobile first */
.container { width: 100%; max-width: var(--max-width); margin: 0 auto; padding: 0 var(--space-6); }

/* Grid */
.grid-2 { display: grid; grid-template-columns: 1fr; gap: var(--space-4); }
.grid-3 { display: grid; grid-template-columns: 1fr; gap: var(--space-4); }

@media (min-width: 768px) {
  .grid-2 { grid-template-columns: repeat(2, 1fr); }
  .grid-3 { grid-template-columns: repeat(2, 1fr); }
}
@media (min-width: 1024px) {
  .grid-3 { grid-template-columns: repeat(3, 1fr); }
}

/* Main content padding for fixed nav */
main { padding-top: var(--nav-height); }
```

---

## UX Patterns

### Filtering
- Filters update results in real time — no "Apply" button
- Active filters are visually distinct — filled chip, not just outlined
- Filter count shown in results: "Showing 12 camps"
- Clear all filters option always visible when filters are active
- Empty state appears immediately when no results match — do not show a spinner

### Detail Views
- Use a slide-in panel from the right for detail views — keeps context of results visible
- Panel has a close button (X) top right and clicking the overlay closes it
- Panel scrolls independently of the main content

### Save / Shortlist Actions
- Save button gives immediate visual feedback — icon fills, color changes
- Saved state persists within the session via STATE object
- A saved count or indicator is visible in the navigation

### Toasts / Confirmations
- Use a toast notification for confirmations — bottom center, auto-dismisses after 2.5 seconds
- Never use alert() or confirm() — always use inline UI

```javascript
function showToast(message) {
  const toast = document.getElementById('toast');
  toast.textContent = message;
  toast.classList.add('visible');
  setTimeout(() => toast.classList.remove('visible'), 2500);
}
```

```css
#toast {
  position: fixed; bottom: var(--space-8); left: 50%;
  transform: translateX(-50%) translateY(100px);
  background: var(--color-text); color: white;
  padding: var(--space-3) var(--space-6);
  border-radius: var(--radius-full);
  font-size: var(--text-sm); font-weight: var(--weight-medium);
  transition: transform var(--transition-base);
  z-index: 300; pointer-events: none;
}
#toast.visible { transform: translateX(-50%) translateY(0); }
```

---

## Visual Design Principles

### Aesthetic Reference
The target aesthetic is Stripe meets Linear — white background, clean typography, strong use of color as accent not wallpaper, generous white space, subtle shadows. Not dark mode. Not Bootstrap gray. Not material design.

### Color Usage Rules
- Primary color on interactive elements only — buttons, links, active states, focus rings
- Neutral grays for text hierarchy — not black
- Status colors (green, amber, red) only for actual status — not decoration
- Background colors used sparingly to create section separation

### White Space
- More white space than feels comfortable — tight layouts look amateur
- Card padding minimum var(--space-6) — never less
- Section padding minimum var(--space-12) top and bottom
- Gap between cards minimum var(--space-4)

### Typography Hierarchy
- One display font (serif) for headings — creates personality and distinction
- One body font (sans-serif) for everything else — creates readability
- Never more than 3 font sizes on one screen
- Body text maximum 65 characters per line — use max-width on text containers

### Icons
- Use inline SVG for all icons — no icon fonts, no external icon libraries
- Keep icons simple — 24x24px viewBox, 1.5-2px stroke width
- Use stroke icons not fill icons for UI — they feel lighter and more modern

---

## Sample Data Guidelines

- Minimum 15 items for any discovery or marketplace product
- Data must be specific — real names, real locations, real prices
- Vary data across all filter dimensions so every filter combination returns results
- Include status variety — available, filling fast, sold out
- Include price variety — budget, mid-range, premium
- Test every filter combination before delivering

---

## What to Build First

**Always build the primary flow first — one screen at a time:**
1. The landing/discovery screen with real data rendered
2. The filter interaction working on that screen
3. The detail view for one item
4. The primary action (save, select, approve) working

**Do not build navigation, secondary flows, or polish until the primary flow works end to end.**

Confirm with the user after the primary flow is working before building additional screens.

---

## Quality Checklist

Before delivering any prototype verify:
- [ ] Opens by double-clicking — no server required
- [ ] No broken layout at 390px mobile or 1280px desktop
- [ ] No placeholder text — all content is real and specific
- [ ] Primary user flow from user stories works end to end
- [ ] All filters update results in real time
- [ ] Empty state appears when no results match
- [ ] Save or primary action gives immediate visual feedback
- [ ] Detail view opens and closes correctly
- [ ] All buttons either work or are visibly disabled
- [ ] Toast notifications used — no alert()
- [ ] CSS variables used consistently throughout
- [ ] Looks like a Stripe-quality product — not a wireframe

---

## What to Avoid

- Bootstrap, Tailwind, or any CSS framework CDN — write real CSS using the patterns above
- jQuery or any JS library — vanilla JS only
- External image URLs — use CSS gradients or inline SVG
- alert() or confirm() — use toast notifications
- Hardcoding data in HTML — always use JS data arrays
- Incomplete flows — every button either works or is disabled
- Tight layouts — always more white space than feels necessary
- Black text — use var(--color-text) #0F172A not pure #000000
- Generic placeholder data — real names, real prices, real places always