import re

BASE = "/Users/edubmba/Documents/Forensic-Tracker/Design System"
GFX = f"{BASE}/Graphics"
FONTS = f"{BASE}/Fonts/Montserrat"

def svg(name, prefix):
    with open(f"{GFX}/{name}") as f:
        s = f.read()
    s = re.sub(r'<\?xml[^>]*\?>\s*', '', s)
    ids = set(re.findall(r'\bid="([^"]+)"', s))
    for old in ids:
        new = f"{prefix}-{old}"
        s = re.sub(rf'\bid="{re.escape(old)}"', f'id="{new}"', s)
        s = re.sub(rf'url\(#{re.escape(old)}\)', f'url(#{new})', s)
        s = re.sub(rf'(xlink:href|href)="#{re.escape(old)}"', rf'\1="#{new}"', s)
    return s

icon_color = svg("icon color.svg", "ic")
icon_black = svg("icon black.svg", "ib")
icon_white = svg("icon white.svg", "iw")
logo_color_dark = svg("color-Logo-dark text.svg", "lcd")
logo_color_white = svg("color-Logo-white text.svg", "lcw")
logo_black = svg("Logo Black.svg", "lb")
logo_white = svg("Logo White.svg", "lw")
logo_color_white_cover = svg("color-Logo-white text.svg", "cov")

def color_row(token, hexval, extra, role):
    return f'''<div class="crow">
      <div class="swatch" style="background:{hexval}"></div>
      <div class="cmeta">
        <div class="ctoken"><code>{token}</code></div>
        <div class="chex">{hexval}{extra}</div>
        <div class="crole">{role}</div>
      </div>
    </div>'''

def hx_to_rgb(h):
    h = h.lstrip('#')
    r,g,b = int(h[0:2],16), int(h[2:4],16), int(h[4:6],16)
    return f" &nbsp;·&nbsp; rgb({r}, {g}, {b})"

html = f'''<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>Forensic Tracker Design System</title>
<style>

@font-face {{ font-family:'Montserrat'; src:url('{FONTS}/Montserrat-Regular.otf'); font-weight:400; }}
@font-face {{ font-family:'Montserrat'; src:url('{FONTS}/Montserrat-Medium.otf'); font-weight:500; }}
@font-face {{ font-family:'Montserrat'; src:url('{FONTS}/Montserrat-SemiBold.otf'); font-weight:600; }}
@font-face {{ font-family:'Montserrat'; src:url('{FONTS}/Montserrat-Bold.otf'); font-weight:700; }}

@page {{
  size: Letter;
  margin: 20mm 20mm 18mm;
  @bottom-center {{ content: counter(page); font-family:'Montserrat'; font-size:9pt; color:#8A97A8; }}
}}
@page cover {{ margin:0; @bottom-center{{content:none}} }}
@page toc {{ @bottom-center{{content:none}} }}

* {{ box-sizing:border-box; }}
body {{ margin:0; font-family:'Montserrat',sans-serif; color:#1C3550; font-size:10.5pt; line-height:1.5; }}
h1,h2,h3,h4 {{ font-weight:700; color:#07223C; margin:0 0 4mm; }}
h2 {{ font-size:20pt; border-bottom:1.5pt solid #DDE4F6; padding-bottom:3mm; margin-top:0; }}
h3 {{ font-size:13pt; margin-top:8mm; }}
p {{ margin:0 0 3mm; }}
table {{ width:100%; border-collapse:collapse; margin:3mm 0 6mm; font-size:9pt; }}
th {{ text-align:left; font-size:8pt; text-transform:uppercase; letter-spacing:0.05em; color:#3E5871; border-bottom:1pt solid #DDE4F6; padding:2mm 3mm; }}
td {{ padding:2mm 3mm; border-bottom:0.5pt solid #EDF0F8; vertical-align:top; }}
code {{ font-family:'Courier New',monospace; font-size:9pt; background:#F4F5FA; padding:1px 4px; border-radius:2px; }}
.section {{ page: content; break-before: page; }}
.section:first-of-type {{ counter-reset: page 1; }}
.dont {{ background:#FAECE7; border-left:3pt solid #D85A30; padding:3mm 5mm; margin-top:4mm; break-inside:avoid; }}
.dont li {{ margin-bottom:1.5mm; }}
.note {{ background:#F4F5FA; border-left:3pt solid #84C7EC; padding:3mm 5mm; margin:3mm 0; font-size:9.5pt; }}

/* cover */
.cover {{ page:cover; background:#07223C; color:#fff; height:297mm; width:216mm;
  display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; }}
.cover .mark {{ width:60mm; margin-bottom:14mm; }}
.cover h1 {{ color:#fff; font-size:34pt; margin:0; letter-spacing:0.01em; }}
.cover .sub {{ color:#59C9F4; font-size:12pt; text-transform:uppercase; letter-spacing:0.12em; font-weight:700; margin-top:5mm; }}

/* toc */
.toc {{ page:toc; break-before:page; }}
.toc ul {{ list-style:none; margin:0; padding:0; }}
.toc li {{ display:flex; align-items:baseline; font-size:11pt; padding:2.5mm 0; border-bottom:0.5pt dotted #C7D2E6; }}
.toc li.sub {{ font-size:9.5pt; color:#3E5871; padding-left:6mm; border-bottom:none; }}
.toc a {{ color:inherit; text-decoration:none; display:flex; width:100%; align-items:baseline; }}
.toc .label {{ flex-shrink:0; }}
.toc .fill {{ flex:1; }}
.toc a::after {{ content: target-counter(attr(href url), page); font-weight:600; }}

/* color swatches */
.crow {{ display:flex; align-items:center; gap:4mm; margin-bottom:3mm; break-inside:avoid; }}
.swatch {{ width:16mm; height:16mm; border-radius:2mm; border:0.5pt solid rgba(0,0,0,0.08); flex-shrink:0; }}
.ctoken code {{ font-size:9.5pt; }}
.chex {{ font-size:9pt; color:#3E5871; margin-top:0.5mm; }}
.crole {{ font-size:9pt; color:#5C6B80; margin-top:0.5mm; }}
.cgrid {{ columns:2; column-gap:8mm; }}
.steprow {{ display:flex; gap:4mm; margin:3mm 0 5mm; }}
.stepchip {{ flex:1; height:14mm; border-radius:2mm; display:flex; align-items:center; justify-content:center; color:#fff; font-size:9pt; font-weight:600; }}

/* type samples */
.tsample {{ border-bottom:0.5pt solid #EDF0F8; padding:3mm 0; break-inside:avoid; }}
.tsample .meta {{ font-size:8pt; color:#8A97A8; text-transform:uppercase; letter-spacing:0.05em; margin-bottom:1mm; }}
.wsample {{ display:flex; align-items:baseline; gap:6mm; padding:2.5mm 0; border-bottom:0.5pt solid #EDF0F8; }}
.wsample .big {{ font-size:22pt; width:60mm; flex-shrink:0; }}
.wsample .meta {{ font-size:9pt; color:#3E5871; }}

/* logo gallery */
.lgrid {{ display:flex; flex-wrap:wrap; gap:5mm; margin:4mm 0 6mm; }}
.lcard {{ width:44mm; border:0.5pt solid #DDE4F6; border-radius:2mm; overflow:hidden; break-inside:avoid; }}
.lcard .stage {{ height:26mm; display:flex; align-items:center; justify-content:center; padding:3mm; }}
.lcard .stage.on-white {{ background:#fff; }}
.lcard .stage.on-navy {{ background:#07223C; }}
.lcard .stage svg {{ max-width:100%; max-height:100%; }}
.lcard .cap {{ padding:2mm 3mm; font-size:7.5pt; }}
.lcard .cap .fname {{ font-family:'Courier New',monospace; font-size:7.5pt; display:block; margin-bottom:0.5mm; color:#07223C; }}
.lcard .cap .desc {{ color:#5C6B80; }}

</style></head><body>

<div class="cover">
  <div class="mark">{logo_color_white_cover}</div>
  <h1>Design System</h1>
  <div class="sub">Forensic Tracker</div>
</div>

<div class="toc">
  <h2 style="margin-top:14mm">Contents</h2>
  <ul>
    <li><a href="#sec-color"><span class="label">Color</span><span class="fill"></span><span class="num"></span></a></li>
    <li class="sub"><a href="#sub-primitives"><span class="label">Brand primitives</span><span class="fill"></span><span class="num"></span></a></li>
    <li class="sub"><a href="#sub-text"><span class="label">Text</span><span class="fill"></span><span class="num"></span></a></li>
    <li class="sub"><a href="#sub-surfaces"><span class="label">Surfaces</span><span class="fill"></span><span class="num"></span></a></li>
    <li class="sub"><a href="#sub-borders"><span class="label">Borders &amp; dividers</span><span class="fill"></span><span class="num"></span></a></li>
    <li class="sub"><a href="#sub-interactive"><span class="label">Interactive</span><span class="fill"></span><span class="num"></span></a></li>
    <li class="sub"><a href="#sub-status"><span class="label">Status</span><span class="fill"></span><span class="num"></span></a></li>
    <li class="sub"><a href="#sub-step"><span class="label">Step-progress scale</span><span class="fill"></span><span class="num"></span></a></li>
    <li><a href="#sec-type"><span class="label">Typography</span><span class="fill"></span><span class="num"></span></a></li>
    <li class="sub"><a href="#sub-typeface"><span class="label">Typeface &amp; weights</span><span class="fill"></span><span class="num"></span></a></li>
    <li class="sub"><a href="#sub-scale"><span class="label">Type scale</span><span class="fill"></span><span class="num"></span></a></li>
    <li><a href="#sec-logo"><span class="label">Logo usage</span><span class="fill"></span><span class="num"></span></a></li>
    <li class="sub"><a href="#sub-assets"><span class="label">Asset inventory</span><span class="fill"></span><span class="num"></span></a></li>
    <li class="sub"><a href="#sub-clearspace"><span class="label">Clear space &amp; minimum size</span><span class="fill"></span><span class="num"></span></a></li>
  </ul>
</div>

<div class="section" id="sec-color">
<h2>Color</h2>

<h3 id="sub-primitives">Brand primitives</h3>
<div class="cgrid">
{color_row('brand-navy','#07223C', hx_to_rgb('#07223C'), 'Primary brand color. Headings, icon fill, primary text.')}
{color_row('brand-teal','#56C3BA', hx_to_rgb('#56C3BA'), 'Accent, gradient start.')}
{color_row('brand-sky','#59C9F4', hx_to_rgb('#59C9F4'), 'Accent, gradient end.')}
{color_row('brand-white','#FFFFFF', hx_to_rgb('#FFFFFF'), '&nbsp;')}
</div>

<h3 id="sub-text">Text</h3>
<div class="cgrid">
{color_row('text-heading','#07223C', hx_to_rgb('#07223C'), 'Headings, nav active state')}
{color_row('text-body','#1C3550', hx_to_rgb('#1C3550'), 'Default body copy')}
{color_row('text-secondary','#3E5871', hx_to_rgb('#3E5871'), 'Muted/secondary copy, inactive nav')}
{color_row('text-inverse','#FFFFFF', hx_to_rgb('#FFFFFF'), 'Text on dark surfaces')}
{color_row('text-inverse-muted','#CDE9F4', hx_to_rgb('#CDE9F4'), 'Secondary text on dark surfaces')}
{color_row('text-link','#07417A', hx_to_rgb('#07417A'), 'Default link color')}
{color_row('text-link-hover','#07223C', hx_to_rgb('#07223C'), 'Link hover state')}
</div>

<h3 id="sub-surfaces">Surfaces</h3>
<div class="cgrid">
{color_row('surface-page','#F4F5FA', hx_to_rgb('#F4F5FA'), 'Default page background')}
{color_row('surface-card','#FFFFFF', hx_to_rgb('#FFFFFF'), 'Cards, header, content panels')}
{color_row('surface-hero','#082848', hx_to_rgb('#082848'), 'Dark hero/feature section background')}
</div>

<h3 id="sub-borders">Borders &amp; dividers</h3>
<div class="cgrid">
{color_row('border-default','#DDE4F6', hx_to_rgb('#DDE4F6'), 'Card borders, section dividers')}
{color_row('border-input','#C7D2E6', hx_to_rgb('#C7D2E6'), 'Form field borders')}
</div>

<h3 id="sub-interactive">Interactive (buttons)</h3>
<div class="cgrid">
{color_row('cta-bg','#84C7EC', hx_to_rgb('#84C7EC'), 'Primary button background')}
{color_row('cta-bg-hover','#6BB8E5', hx_to_rgb('#6BB8E5'), 'Primary button hover')}
{color_row('cta-text','#07223C', hx_to_rgb('#07223C'), 'Text on primary button')}
</div>

<h3 id="sub-status">Status</h3>
<div class="cgrid">
{color_row('bg-success','#DCF3E8', hx_to_rgb('#DCF3E8'), 'Success state background')}
{color_row('text-success','#1D8A57', hx_to_rgb('#1D8A57'), 'Success state icon/text')}
</div>

<h3 id="sub-step">Step-progress scale</h3>
<p>A 3-stop scale for sequential step indicators (e.g. step 1 of 3 in a process).</p>
<div class="steprow">
  <div class="stepchip" style="background:#56C3BA">step-1 &nbsp;#56C3BA</div>
  <div class="stepchip" style="background:#58C6D7">step-2 &nbsp;#58C6D7</div>
  <div class="stepchip" style="background:#59C9F4">step-3 &nbsp;#59C9F4</div>
</div>
<p>When a step indicator uses this scale on a graphic element (icon, circle, bar), any label text for that same step must use the matching <code>step-N</code> token &mdash; never a different color for the label than for its graphic.</p>
</div>

<div class="section" id="sec-type">
<h2>Typography</h2>

<h3 id="sub-typeface">Typeface</h3>
<p>Montserrat, all weights. Fallback stack, for the moment before Montserrat loads:<br>
<code>'Montserrat', -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif</code></p>

<h4>Weights</h4>
<p>Three weights cover the system. Don't reach outside this set without a specific reason.</p>
<div class="wsample"><div class="big" style="font-weight:400">Aa Bb Cc</div><div class="meta"><strong>400 &middot; Regular</strong> &mdash; Body copy, paragraphs</div></div>
<div class="wsample"><div class="big" style="font-weight:600">Aa Bb Cc</div><div class="meta"><strong>600 &middot; SemiBold</strong> &mdash; Subheads, nav, buttons, UI labels</div></div>
<div class="wsample"><div class="big" style="font-weight:700">Aa Bb Cc</div><div class="meta"><strong>700 &middot; Bold</strong> &mdash; Headings, eyebrow/label text</div></div>
<p style="margin-top:3mm">Medium (500) and Light (300) are available if a specific composition needs them, but aren't part of the standard set.</p>

<h3 id="sub-scale">Type scale</h3>
<div class="tsample"><div class="meta">H1 &middot; 48px &middot; 700 &middot; line-height 1.15</div><div style="font-size:34pt;font-weight:700">Evidence Notification System</div></div>
<div class="tsample"><div class="meta">H2 &middot; 32px &middot; 700 &middot; line-height 1.2</div><div style="font-size:23pt;font-weight:700">From forensic hit to investigative action</div></div>
<div class="tsample"><div class="meta">H3 &middot; 22px &middot; 600 &middot; line-height 1.3</div><div style="font-size:16pt;font-weight:600">Notify. Update. Escalate.</div></div>
<div class="tsample"><div class="meta">H4 &middot; 18px &middot; 600 &middot; line-height 1.3</div><div style="font-size:13pt;font-weight:600">Investigation accelerator</div></div>
<div class="tsample"><div class="meta">Eyebrow / label &middot; 13px &middot; 700 &middot; 0.06em tracking &middot; uppercase</div><div style="font-size:9.5pt;font-weight:700;letter-spacing:0.06em;text-transform:uppercase">Notify. Update. Escalate.</div></div>
<div class="tsample"><div class="meta">Body large &middot; 18px &middot; 400 &middot; line-height 1.6</div><div style="font-size:13pt;font-weight:400">Forensic Tracker notifies investigators the moment a forensic hit lands.</div></div>
<div class="tsample"><div class="meta">Body &middot; 16px &middot; 400 &middot; line-height 1.65</div><div style="font-size:11.5pt;font-weight:400">Every update is logged in the case console, from lab bench to documented response.</div></div>
<div class="tsample"><div class="meta">Small / caption &middot; 13px &middot; 400 &middot; line-height 1.4</div><div style="font-size:9.5pt;font-weight:400">Article image caption or metadata text.</div></div>
<div class="tsample"><div class="meta">Nav link &middot; 14px &middot; 600</div><div style="font-size:10pt;font-weight:600">Product</div></div>
<div class="tsample"><div class="meta">Button &middot; 15px &middot; 600</div><div style="font-size:10.5pt;font-weight:600">Get a demo</div></div>

<div class="dont">
<strong>Don't</strong>
<ul>
<li>Don't use a weight outside 400/600/700 without a specific reason.</li>
<li>Don't set body text below 13px.</li>
<li>Don't set headings or body copy in uppercase &mdash; reserve uppercase for eyebrow/label text and buttons only.</li>
<li>Don't artificially stretch, condense, skew (fake italic), or bold (text-shadow stacking) the typeface.</li>
<li>Don't substitute another typeface, even temporarily.</li>
</ul>
</div>
</div>

<div class="section" id="sec-logo">
<h2>Logo usage</h2>

<h3 id="sub-assets">Asset inventory</h3>
<p>Never redraw, retrace, or reconstruct the logo from an image &mdash; always place one of these files as-is.</p>

<div class="lgrid">
  <div class="lcard"><div class="stage on-white">{logo_color_dark}</div><div class="cap"><span class="fname">color-Logo-dark text.svg</span><span class="desc">Default lockup, on white/light backgrounds</span></div></div>
  <div class="lcard"><div class="stage on-navy">{logo_color_white}</div><div class="cap"><span class="fname">color-Logo-white text.svg</span><span class="desc">On the brand-navy hero or an equally dark background</span></div></div>
  <div class="lcard"><div class="stage on-white">{logo_black}</div><div class="cap"><span class="fname">Logo Black.svg</span><span class="desc">Single-color, light backgrounds: print, watermarks, faxes</span></div></div>
  <div class="lcard"><div class="stage on-navy">{logo_white}</div><div class="cap"><span class="fname">Logo White.svg</span><span class="desc">Single-color, dark backgrounds</span></div></div>
  <div class="lcard"><div class="stage on-white" style="padding:6mm 10mm">{icon_color}</div><div class="cap"><span class="fname">icon color.svg</span><span class="desc">Icon only, full color: app icon, social avatar, large favicon</span></div></div>
  <div class="lcard"><div class="stage on-white" style="padding:6mm 10mm">{icon_black}</div><div class="cap"><span class="fname">icon black.svg</span><span class="desc">Icon only, light backgrounds, single color</span></div></div>
  <div class="lcard"><div class="stage on-navy" style="padding:6mm 10mm">{icon_white}</div><div class="cap"><span class="fname">icon white.svg</span><span class="desc">Icon only, dark backgrounds, single color</span></div></div>
</div>

<p>Never use the full lockup's gradient version (<code>color-Logo-*</code>) on a background other than white/near-white or the brand-navy hero &mdash; the teal-to-sky gradient loses contrast against anything else. Use <code>Logo Black.svg</code> / <code>Logo White.svg</code> for any background where contrast is uncertain.</p>

<h3 id="sub-clearspace">Clear space</h3>
<p><strong>Standalone placements</strong> (title slides, letterhead, printed materials, an app-icon tile, a hero section where the logo is the graphic) &mdash; minimum clear space on every side is <strong>10% of the icon mark's rendered height</strong>, measured from the icon's outermost stems. No text, edge, or other graphic may enter that margin.</p>
<p><strong>Embedded UI placements</strong> (nav bar, table header, favicon, card header) &mdash; no computed minimum. Follow the surrounding layout's normal spacing; the only hard rule is that no other element may overlap or directly touch the logo.</p>

<h4>Minimum size</h4>
<table>
<tr><th>Asset</th><th>Absolute floor</th><th>Recommended minimum</th></tr>
<tr><td>Icon only (header, app icon, avatar, anywhere legibility matters)</td><td>24px &mdash; motif barely reads</td><td>32px &mdash; motif reads clearly</td></tr>
<tr><td>Full lockup</td><td>24px tall / ~100px wide</td><td>32&ndash;40px tall</td></tr>
</table>
<p>Below the absolute floor, don't place the logo at all &mdash; it stops being recognizable as the mark rather than just getting smaller.</p>

<h4>Favicon</h4>
<p>Favicons are exempt from the icon-only minimum above &mdash; silhouette-only rendering at small sizes is expected and normal there. Export from <code>icon color.svg</code> at each size rather than picking one:</p>
<table>
<tr><th>Size</th><th>Surface</th></tr>
<tr><td>16&times;16</td><td>Browser tab, bookmarks bar (baseline, universal support)</td></tr>
<tr><td>32&times;32</td><td>HiDPI tabs, Windows taskbar</td></tr>
<tr><td>180&times;180</td><td>iOS home-screen icon (apple-touch-icon)</td></tr>
<tr><td>192&times;192, 512&times;512</td><td>Android / PWA icons</td></tr>
</table>

<div class="dont">
<strong>Don't</strong>
<ul>
<li>Don't recolor the logo outside the files above &mdash; no custom tints, no matching it to a page's accent color.</li>
<li>Don't stretch, skew, or scale the icon and wordmark by different factors &mdash; scale the whole lockup uniformly.</li>
<li>Don't rotate the logo.</li>
<li>Don't add drop shadows, glows, outlines, or other effects.</li>
<li>Don't place the gradient color version on a background that isn't white/near-white or the brand-navy hero.</li>
<li>Don't crop the lockup &mdash; if space is tight, switch to the icon-only mark instead.</li>
</ul>
</div>
</div>

</body></html>'''

with open("/private/tmp/claude-501/-Users-edubmba-Documents-Forensic-Tracker/e894654e-7e45-4242-9678-240f62453fc9/scratchpad/design-system.html","w") as f:
    f.write(html)
print("wrote html", len(html), "bytes")
