# Design System — decisions log

Why the rules in `Design System.md` say what they say. Reference material, not
itself a source of rules — nothing here needs to be read to use the design system,
only to question it.

---

## Typography

**Montserrat over Proxima Nova.** The PDF names Proxima Nova as the primary
typeface and Montserrat as the substitute. Proxima Nova isn't on Google Fonts and
is normally licensed for desktop/print use separately from web-embedding —
self-hosting the copies on file would need checking that the license actually
covers that, and the copies on hand are an incomplete set (Bold/Thin/Regular only,
no Medium or SemiBold, no italics). Montserrat is already the PDF's sanctioned
substitute, is fully open-licensed (SIL OFL, free to self-host anywhere), and the
copy on hand is the complete family — 9 weights plus italics. Standardized on
Montserrat alone, for both headings and body, rather than keeping a two-font
pairing.

**Three weights, not the full family.** Montserrat ships 9 weights. Restricted the
system to 400/600/700 to keep the type system as manageable as the rest of this
document — every additional weight is one more decision available at the moment
someone's setting text, and most compositions don't need more than three.
Medium and Light are left available but not standard, for the rare case that
genuinely wants them.

**Type scale sizes carried over from the live site, not invented fresh.** The
website (built on a different font pairing, Archivo + Public Sans) had already
established a consistent set of proportions — 46–48px headlines, 32px section
heads, 16px body at 1.65 line-height, 13px uppercase eyebrow labels with 0.06em
tracking, and so on. Kept those proportions and mapped them onto Montserrat
weights instead of inventing a new scale, so switching typefaces doesn't also
quietly change the site's visual rhythm.

## Color

**Brand accent values.** The brand guideline PDF lists the two accent colors as
`#57C3BA` and `#5CC8F3`. The live website has been running `#56C3BA` and `#59C9F4`
instead — close on the teal, visibly different on the sky blue. Adopted the
website's values as canonical: they're used 148 times combined across the site,
and they're internally consistent with each other (the step-progress scale is a
mathematically correct 3-point sample between exactly these two values, which
wouldn't be true starting from the PDF's numbers). Treated the PDF as the stale
source here, not the site.

**Extended palette.** The PDF defines 4 colors total. Formalized 11 more (text,
surface, border, button, and status tokens) rather than restricting the system to
those 4, because the extra colors are already doing real jobs on the live site
that any working UI needs — page background, secondary text, link states, button
hover — and the alternative was leaving them undocumented and inconsistent.

**`border-input` as its own token.** Only one live use (a single form) at the time
this was written, but kept separate from `border-default` rather than merged into
it, since a form field reads better with a slightly cooler/darker border than a
card divider — a real distinction, not just an accident of one page's CSS.

**Status colors formalized despite one use case.** `bg-success` / `text-success`
back only a single confirmation state (a form's "you're opted in" message) as of
this writing. Documented anyway, ahead of need, because the PDF has no concept of
UI feedback states at all (only brand/marketing colors), and warning/error states
will eventually need somewhere obvious to start from.

**Step-progress scale.** Built as a clean 3-point interpolation between
`brand-teal` and `brand-sky` (`#56C3BA → #58C6D7 → #59C9F4`). On the live site,
the step indicator's circle borders already matched this exact scale — but the
step labels next to them used a different, unrelated set of colors (`#38A9C9`,
`#2E9AD6`) that don't sit on the teal-sky gradient line at all. Read as an
unintentional mismatch rather than a deliberate second scale, so the rule going
forward is that a step's label and its graphic share one token.

**Excluded `#F0F7FB` / `#E4F1F8`.** Appeared 6 times each on the live site, but
only as a diagonal-stripe pattern standing in for missing blog article images —
not brand color, just a temporary placeholder graphic. Left out of the palette.

---

## Logo usage

**Clear space redefined, twice.** The PDF specifies clear space as "4x the amount
of space around the logo" and labels the diagram `4px` — 4 pixels is meaningless
at any real logo size, and "4x" of what unit is never defined anywhere in the
document. First replacement was a single rule: clear space = 50% of the icon's
rendered height on every side, applied everywhere. That number was too large in
practice — most real brand guidelines size their clear-space unit off something
small and specific to the mark (a single letter's cap-height, one recurring icon
element), not a large fraction of the whole logo, and reserve any hard minimum for
standalone placements (marketing materials, letterhead, hero sections) rather than
embedded UI chrome like nav bars and favicons, which are never actually held to
that math in practice. Split into two rules: 10% of icon height for standalone
placements (closer to how the icon's own repeating elements, like its dots, scale
against it — a small-unit convention, just expressed as a percentage for easy
application without needing the vector file open), and no computed minimum for
embedded UI, just "don't overlap, otherwise follow normal layout spacing."

**Minimum sizes verified, not guessed.** The PDF gives print sizes (300px / 150px
/ 75px) and, for web, only "make it small while maintaining proportion until it
remains understandable" — not something actionable. Instead, rendered the icon at
16, 20, 24, 32, and 40px and the full lockup at 100–220px wide, and checked each
by eye: the icon's internal DNA-rung motif is illegible below ~24px (reads as a
plain silhouette) and clearly legible at 32px+; the full lockup floor was set at
24px tall / ~100px wide because that matches what the live site's header already
ships successfully at that size.

**Favicon carved out as its own case, not held to the icon-only floor.** The first
draft of this section applied the same 16px/32px figures to favicons as to
headers and app icons, which implied a 16px favicon was substandard. It isn't —
16×16 is the baseline favicon size by browser convention, and silhouette-only
rendering there is universal, not specific to this mark. Split it into its own
section with the actual set of sizes browsers and OSes request (16, 32, 180, 192,
512), rather than one "minimum" number.

**Placement guidance dropped.** The PDF's placement section ("avoid random
placement, ensure consistent placement") was pure boilerplate — no specific rule
was ever stated, so there was nothing to formalize or replace.

**Asset inventory and "Don't" list are net-new.** The PDF never maps logo files to
situations (when to use color vs. black vs. white, icon-only vs. full lockup) and
contains no prohibitions at all. Both were built from scratch against the actual
files in `Graphics/`.

**Gradient lockup restricted to two backgrounds.** `color-Logo-dark text.svg` and
`color-Logo-white text.svg` are limited to white/near-light backgrounds or the
brand-navy hero, because the teal-to-sky gradient loses contrast against anything
else — including brand-navy paired with certain photography. `Logo Black.svg` /
`Logo White.svg` exist as the fallback for any background where contrast is
uncertain.

**`Logo Black.svg` / `Logo White.svg` replace the "Padded" files, not because of
padding.** The original files (`Logo Black Padded.svg`, `Logo White Padded.svg`)
were suspected of having excess canvas padding based on the filename. Rasterizing
and auto-trimming them showed 0px of margin on every edge — the geometry was
already tight. The replacement files exist instead to harden the fill color
(explicit `#000000` / `#FFFFFF` rather than relying on default/inherited fill,
which breaks in some embedding contexts) and to drop the misleading "Padded" name.

**Color lockups built from existing vector pieces, not traced from the PNGs.**
`color-Logo-dark text.svg` / `color-Logo-white text.svg` were assembled from the
already-accurate `icon color.svg` icon geometry and the `Logo Black/White Padded`
text paths, with the teal-to-sky gradient reconstructed and applied to
"TRACKER." A raster trace of the source PNGs was available as a fallback but
would have produced softer, less accurate edges than reusing the real vector
source.
