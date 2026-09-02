# Forensic Tracker — Design System

## What's here

| File | Purpose |
|---|---|
| `Design System.md` | Source of truth. Color, typography, and logo rules. Edit this first. |
| `Decisions.md` | Rationale log. Explains why a rule says what it says. Not required reading to use the system. |
| `Design System.pdf` | Rendered, human-readable version of `Design System.md`: cover, table of contents, color swatches, live type samples, logo gallery. Regenerate after editing the source (see below). |
| `build-pdf.py` | Script that renders `Design System.pdf` from HTML built out of `Design System.md`'s content. |
| `Graphics/` | Canonical logo and icon SVG files. Referenced by name from `Design System.md`. |
| `Fonts/Montserrat/` | The chosen typeface, full family, open-licensed. |

## Updating the system

Edit `Design System.md` directly. It's the only file anything else should be derived from. If a rule changes for a reason worth remembering later (a reconciled color value, a redefined clear-space rule, anything a future reviewer might question), add an entry to `Decisions.md` too.

To rebuild the PDF after an edit:

```
brew install weasyprint   # one-time, if not already installed
python3 "Design System/build-pdf.py"
weasyprint "Design System/design-system.html" "Design System/Design System.pdf"
```

`build-pdf.py` writes an intermediate HTML file next to itself, pulling live content from `Graphics/` and `Fonts/Montserrat/` as it builds. If a logo file gets renamed or removed, update `build-pdf.py` to match, or the render will fail on a missing file.

Commit and push to `main` when done. This repo is the canonical copy. Nothing else should hold a second version that needs updating separately.

## Using it from claude.ai

The GitHub connector doesn't have a single "point it here" setting. Where you pick the repo depends on how you're using it.

**One-off, inside a chat:** click the attach (+) button next to the message box, choose GitHub, select `Forensic-Tracker`, and browse to the file you need.

**Standing context, inside a Project:** open or create a claude.ai Project, and in its settings look for the option to sync a GitHub repo. Select `edubvenicev2/Forensic-Tracker`. Every conversation started in that Project then has the repo available automatically, without attaching files each time.

If the repo doesn't show up as selectable in either picker, the connector is likely turned on at the account level but hasn't been granted access to this specific repo. That's a separate, GitHub-side permission: go to GitHub's **Settings → Applications → Installed GitHub Apps → Claude → Configure**, and under repository access, add `Forensic-Tracker` (or switch to all repositories).
