# Forensic Tracker — Design System

Source of truth for color, type, and logo usage across the website and any other
creative output (decks, one-pagers, social).

---

## Color

### Brand primitives

| Token | Hex | RGB | Role |
|---|---|---|---|
| `brand-navy` | `#07223C` | 7, 34, 60 | Primary brand color. Headings, icon fill, primary text. |
| `brand-teal` | `#56C3BA` | 86, 195, 186 | Accent, gradient start. |
| `brand-sky` | `#59C9F4` | 89, 201, 244 | Accent, gradient end. |
| `brand-white` | `#FFFFFF` | 255, 255, 255 | — |

### Text

| Token | Hex | Role |
|---|---|---|
| `text-heading` | `#07223C` | Headings, nav active state |
| `text-body` | `#1C3550` | Default body copy |
| `text-secondary` | `#3E5871` | Muted/secondary copy, inactive nav |
| `text-inverse` | `#FFFFFF` | Text on dark surfaces |
| `text-inverse-muted` | `#CDE9F4` | Secondary text on dark surfaces |
| `text-link` | `#07417A` | Default link color |
| `text-link-hover` | `#07223C` | Link hover state |

### Surfaces

| Token | Hex | Role |
|---|---|---|
| `surface-page` | `#F4F5FA` | Default page background |
| `surface-card` | `#FFFFFF` | Cards, header, content panels |
| `surface-hero` | `#082848` | Dark hero/feature section background |

### Borders & dividers

| Token | Hex | Role |
|---|---|---|
| `border-default` | `#DDE4F6` | Card borders, section dividers |
| `border-input` | `#C7D2E6` | Form field borders |

### Interactive (buttons)

| Token | Hex | Role |
|---|---|---|
| `cta-bg` | `#84C7EC` | Primary button background |
| `cta-bg-hover` | `#6BB8E5` | Primary button hover |
| `cta-text` | `#07223C` | Text on primary button |

### Status

| Token | Hex | Role |
|---|---|---|
| `bg-success` | `#DCF3E8` | Success state background |
| `text-success` | `#1D8A57` | Success state icon/text |

### Step-progress scale

A 3-stop scale for sequential step indicators (e.g. step 1 of 3 in a process).

| Token | Hex | Position |
|---|---|---|
| `step-1` | `#56C3BA` | 0% (= `brand-teal`) |
| `step-2` | `#58C6D7` | 50% |
| `step-3` | `#59C9F4` | 100% (= `brand-sky`) |

When a step indicator uses this scale on a graphic element (icon, circle, bar), any
label text for that same step must use the matching `step-N` token — never a
different color for the label than for its graphic.

---

## Typography

### Typeface

Montserrat, all weights. Source files: `Design System/Fonts/Montserrat/`.

Fallback stack, for the moment before Montserrat loads:
`'Montserrat', -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif`.

### Weights

Three weights cover the system. Don't reach outside this set without a specific
reason.

| Weight | Name | Role |
|---|---|---|
| 400 | Regular | Body copy, paragraphs |
| 600 | SemiBold | Subheads, nav, buttons, UI labels |
| 700 | Bold | Headings, eyebrow/label text |

Medium (500) and Light (300) are available in `Fonts/Montserrat/` if a specific
composition needs them, but aren't part of the standard set.

### Type scale

| Role | Size | Weight | Line height | Letter spacing | Case |
|---|---|---|---|---|---|
| H1 | 48px | 700 | 1.15 | normal | Sentence case |
| H2 | 32px | 700 | 1.2 | normal | Sentence case |
| H3 | 22px | 600 | 1.3 | normal | Sentence case |
| H4 | 18px | 600 | 1.3 | normal | Sentence case |
| Eyebrow / label | 13px | 700 | 1.2 | 0.06em | UPPERCASE |
| Body large | 18px | 400 | 1.6 | normal | Sentence case |
| Body | 16px | 400 | 1.65 | normal | Sentence case |
| Small / caption | 13px | 400 | 1.4 | normal | Sentence case |
| Nav link | 14px | 600 | 1.2 | normal | Sentence case |
| Button | 15px | 600 | 1.2 | normal | Sentence case |

### Don't

- Don't use a weight outside 400/600/700 without a specific reason.
- Don't set body text below 13px.
- Don't set headings or body copy in uppercase — reserve uppercase for eyebrow/label
  text and buttons only.
- Don't artificially stretch, condense, skew (fake italic), or bold (text-shadow
  stacking) the typeface — use the weight and style Montserrat actually ships.
- Don't substitute another typeface, even temporarily — use the fallback stack
  above if Montserrat isn't available yet.

## Logo usage

### Asset inventory

All canonical files live in `Design System/Graphics/`. Never redraw, retrace, or
reconstruct the logo from an image — always place one of these files as-is.

| File | Contents | Use when |
|---|---|---|
| `color-Logo-dark text.svg` | Full lockup, navy "FORENSIC," gradient "TRACKER," color icon | Default lockup, on white/light backgrounds |
| `color-Logo-white text.svg` | Full lockup, white "FORENSIC," gradient "TRACKER," color icon | On the brand-navy hero background or an equally dark photo/color |
| `Logo Black.svg` | Full lockup, solid black, outline icon | Single-color contexts on light backgrounds: print, watermarks, faxes, anywhere color/gradients aren't supported |
| `Logo White.svg` | Full lockup, solid white, outline icon | Single-color contexts on dark backgrounds |
| `icon color.svg` | Icon only, full color, gradient | Square/small contexts with enough room for full color: app icon, social avatar, large favicon |
| `icon black.svg` | Icon only, solid black, outline | Icon-only on light backgrounds, single color |
| `icon white.svg` | Icon only, solid white, outline | Icon-only on dark backgrounds, single color |

Never use the full lockup's gradient version (`color-Logo-*`) on a background other
than white/near-white or the brand-navy hero — the teal-to-sky gradient loses
contrast against anything else, including brand-navy on its own paired with certain
photography. Use `Logo Black.svg` / `Logo White.svg` for any background where
contrast is uncertain.

### Clear space

**Standalone placements** (title slides, letterhead, printed materials, an app-icon
tile, a hero section where the logo is the graphic) — minimum clear space on every
side is **10% of the icon mark's rendered height**, measured from the icon's
outermost stems. No text, edge, or other graphic may enter that margin.

**Embedded UI placements** (nav bar, table header, favicon, card header, anywhere
the logo sits inside existing layout chrome) — no computed minimum. Follow the
surrounding layout's normal spacing; the only hard rule is that no other element
may overlap or directly touch the logo.

### Minimum size

| Asset | Absolute floor | Recommended minimum |
|---|---|---|
| Icon only (header, app icon, social avatar, anywhere legibility matters) | 24px (motif barely reads) | 32px (motif reads clearly) |
| Full lockup | 24px tall / ~100px wide | 32–40px tall |

Below the absolute floor, don't place the logo at all — it stops being recognizable
as the mark rather than just getting smaller.

### Favicon

Favicons are exempt from the icon-only minimum above — silhouette-only rendering
at small sizes is expected and normal there, not a legibility failure. Export from
`icon color.svg` at each of these sizes rather than picking one:

| Size | Surface |
|---|---|
| 16×16 | Browser tab, bookmarks bar (baseline, universal support) |
| 32×32 | HiDPI tabs, Windows taskbar |
| 180×180 | iOS home-screen icon (apple-touch-icon) |
| 192×192, 512×512 | Android / PWA icons |

### Don't

- Don't recolor the logo outside the four files above — no custom tints, no
  matching it to a page's accent color.
- Don't stretch, skew, or scale the icon and wordmark by different factors — scale
  the whole lockup uniformly.
- Don't rotate the logo.
- Don't add drop shadows, glows, outlines, or other effects — the files are final
  as designed.
- Don't place the gradient color version on a background that isn't white/near-white
  or the brand-navy hero (see Asset inventory above).
- Don't crop the lockup — if space is tight, switch to the icon-only mark instead
  of cutting the wordmark off.
