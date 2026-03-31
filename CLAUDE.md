# Ariane Hair Braiding — Project Brief for Claude Code

## What This Project Is
A luxury hair braiding salon website for **Ariane Hair Braiding** — a high-end African American braiding studio.
The brand aesthetic is: **Elegant · Premium · Sophisticated · Warm · Culturally Rich · Timeless**.
Think high-end beauty studio in Atlanta, DC, or NYC. Editorial. Not trendy. Not flashy.

---

## File Structure
```
ariane-hair-braiding/
├── index.html              # Homepage (fully built)
├── ariane-logo-dark.svg    # Logo — cream/gold on dark backgrounds
├── ariane-logo-light.svg   # Logo — charcoal/gold on light backgrounds
├── ariane-design-system.html  # Brand reference (do not edit)
├── CLAUDE.md               # This file
└── images/                 # Drop real photos here when ready
```

---

## Design System — Color Tokens

Always use these exact values. Never substitute with generic colors.

```css
/* Primary */
--ink:       #0d0b09;   /* Deepest text */
--cream:     #f5f0e8;   /* Page background */
--gold:      #b8954a;   /* Primary accent */
--gold-lt:   #d4af6e;   /* Light gold — italic headings, hover */
--gold-dk:   #8a6c2f;   /* Dark gold — pressed states */

/* Dark backgrounds */
--warm:      #2a1f14;   /* Hero, about, booking sections */
--mid:       #5c4a35;   /* Mid-dark overlays */
--dust:      #e8dfd0;   /* Muted light text on dark */

/* Nav */
Nav default:  rgba(13, 11, 9, 0.72) with blur(8px)
Nav scrolled: rgba(13, 11, 9, 0.92) with blur(18px)
```

---

## Typography

```
Display / Headlines : Cormorant Garamond — font-weight 300, often italic for emphasis
Body copy           : Jost — font-weight 300
Section labels      : Jost — 0.65rem, letter-spacing 0.35em, ALL CAPS, color: var(--gold)
Prices / Stats      : Cormorant Garamond — font-weight 300, large size, color: var(--gold)
```

Google Fonts import (already in index.html — reuse on all new pages):
```html
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Jost:wght@200;300;400;500&display=swap" rel="stylesheet">
```

---

## Logo Usage

The logo is an inline SVG (crown arc motif + ARIANE wordmark + HAIR BRAIDING subtitle).
- **On dark backgrounds** → use `ariane-logo-dark.svg` or the dark inline SVG variant
- **On light backgrounds** → use `ariane-logo-light.svg`
- **In the nav** → always the dark variant (nav has dark frosted background)
- **Never** replace the logo with plain text

---

## Component Patterns

### Section Label (use before every H2)
```html
<p class="section-label">Label Text</p>
```
```css
.section-label {
  font-size: 0.65rem;
  letter-spacing: 0.35em;
  text-transform: uppercase;
  color: var(--gold);
  display: flex; align-items: center; gap: 14px;
}
.section-label::before {
  content: ''; width: 30px; height: 1px;
  background: var(--gold); display: inline-block;
}
```

### Primary Button
```html
<a href="#booking" class="btn-primary">Book Your Session</a>
```
Background: `var(--gold)` → hover: `var(--gold-lt)`, color: `var(--ink)`

### Ghost Button (on dark backgrounds)
```html
<a href="#" class="btn-ghost">View Services</a>
```
Color: `var(--dust)`, with `→` arrow that shifts right on hover.

### Divider Ornament
```html
<div class="ornament-divider">✦</div>
```

---

## Page Layout Rules

- **Max content width**: 1200px, centered with `margin: 0 auto`
- **Section padding**: `120px 60px` desktop, `80px 24px` mobile
- **Grid gap**: `2px` for card grids (creates a luxury editorial feel)
- **No rounded corners** anywhere — this brand uses sharp edges only
- **No box shadows** that look "material design" — subtle or none
- **Negative space is intentional** — don't fill empty space

---

## Sections Already Built (index.html)

1. ✅ Nav — fixed, dark frosted glass, SVG logo
2. ✅ Hero — split grid, dark left panel, photo right
3. ✅ Marquee strip — gold background, scrolling service names
4. ✅ About — dark section, stats (7+ years, 500+ clients, 15+ styles)
5. ✅ Services — 6-card grid with hover reveals
6. ✅ Gallery — editorial masonry grid
7. ✅ Testimonials — 3 client reviews
8. ✅ Booking form — appointment request
9. ✅ Footer — links, hours, contact info, social links

---

## Pages Still To Build

- [ ] `services.html` — full services page with pricing table
- [ ] `gallery.html` — full gallery with filter by style
- [ ] `about.html` — Ariane's story, team, studio photos
- [ ] `booking.html` — standalone booking page (or Calendly embed)
- [ ] `contact.html` — map, hours, contact form

---

## Brand Voice (for any copy)

- Speak to the client like **royalty** — "Your crown", "Your session"
- Warm but elevated — never casual, never corporate
- Short sentences. Confident. No filler words.
- Use em dashes (—) not hyphens for pauses
- Reference African heritage with **pride and specificity**, not generically

**Good**: *"Rooted in African tradition, refined for the modern woman."*
**Bad**: *"We offer a variety of braiding services for all hair types."*

---

## Code Standards

- **No frameworks** — plain HTML, CSS, JS only (no React, no Tailwind)
- **CSS variables** for all colors — never hardcode hex values inline
- **Mobile-first** responsive — breakpoint at 900px
- **Animations** — slow and deliberate (0.3s–0.8s), `cubic-bezier(0.16, 1, 0.3, 1)`
- **Images** — use Unsplash placeholders until real photos arrive:
  - Hair/braiding: `https://images.unsplash.com/photo-1605497788044-5a32c7078486`
  - Salon interior: `https://images.unsplash.com/photo-1522337360788-8b13dee7a37e`
  - Stylist portrait: `https://images.unsplash.com/photo-1580618672591-eb180b1a973f`
- **Accessibility** — all images need `alt` text, buttons need labels
- **No `!important`** — fix specificity properly

---

## What NOT To Do

- ❌ Don't use purple, teal, or cool-toned colors anywhere
- ❌ Don't use Inter, Roboto, or system fonts
- ❌ Don't add rounded corners (`border-radius`) to cards or buttons
- ❌ Don't make animations fast or bouncy
- ❌ Don't add gradients that look "web 2.0" or "app-like"
- ❌ Don't add emoji to the UI
- ❌ Don't replace the SVG logo with plain text
- ❌ Don't use flexbox gap shortcuts that break Safari < 14

---

## Real Content Placeholders

Fill these in when the client provides real info:

| Field | Placeholder | Replace With |
|---|---|---|
| Phone | (555) 123-4567 | Real number |
| Email | hello@arianehairbraiding.com | Real email |
| Address | TBD | Real address |
| Instagram | # | Real handle |
| Est. year | Est. 2018 | Real year |
| Pricing | Starting from $X | Real prices |

---

*Last updated: February 2026 · Built by Claudio*
