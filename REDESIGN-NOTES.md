# RielArt design notes — current system: “Printed in one ink” (October 8, 2026)

Status: implemented on branch `claude/clever-allen-vt1at2` for owner review. Not deployed. No external account, DNS, Formspree, Calendly, Stripe, or provider setting was changed, and no production form was submitted.

## Audit of the previous system

What was strong: honest, well-scoped copy; two clear services with published prices; light/dark themes; accessible, dependency-free code; a thorough audit tool.

What read as generic: a small label above nearly every heading (85 instances); the same heading-left / paragraph-right split in almost every section; a navy band alternating with paper; folded corners and a gradient “path line” used as decoration; a polished but anonymous grotesk-on-blue look that could belong to any studio.

Information hierarchy problems: the prices — RielArt’s clearest differentiator — first appeared in the third section; the “sequence” section repeated the hero headline line for line; Why RielArt gave eight points equal weight behind vague one-word labels, burying the three hardest commitments (flat fee, client ownership, creative included); Pricing listed every inclusion twice.

## Why this direction

RielArt sells straight dealing to owners of real-world service businesses: two services, published prices, written boundaries, client-owned accounts, no guarantees. Those owners trust honest printed matter — a clear price card, a written quote, a well-made sign — more than technology aesthetics. So the identity borrows the discipline of a one-colour print job: economical, confident, and legible, with nothing added for effect.

## The system

1. **One ink.** The deep ultramarine of the R mark (`#1238c4`; `#1a36b8` fields and `#8fa4ff` text in dark mode), used flat: as full-width fields with paper-coloured type (homepage hero, Why RielArt, closing CTA, inner-page price boards), and as the colour of prices, links, and focus. No gradient outside the logo. No navy, no cyan.
2. **Warm paper.** `#f3efe6` paper; a deeper warm paper `#e7e1d4` for panels and alternate sections. Dark mode is a designed counterpart (night paper `#111319`) that keeps the same cobalt fields.
3. **One family.** Archivo — a grotesque descended from 19th-century American commercial type — set heavy and condensed (wdth 74–84%) for statements, titles, and prices, normal width for reading and UI. Newsreader remains for article body text only. Archivo is instanced to wdth 74–100 and wght 400–840 and subset to the site’s characters (50 KB).
4. **The price-list leader.** A dotted leader running from a service name to its price — the single signature device, used only where something has a price (homepage hero, share image).
5. **Rules, not cards.** Square corners throughout. A heavy 4px rule only on price boards, fact strips, and scope boundaries; 2px rules head lists; 1px rules divide.
6. **Labels only where they inform.** Section labels were removed except where they carry meaning: Optional setup (subordinate status), Internal project / Representative concept (honesty labels), article category, Compare the services (approved copy).

## Structural changes

- **Homepage:** prices move into the first viewport via the hero price list; the redundant sequence section was removed (it remains on About); Why RielArt leads with three large commitments over five supporting points; the work section is a compact labelled list after the process.
- **Pricing:** the cobalt price board now carries name, price, terms, and actions only; the full inclusions live once, in “What each service includes.”
- **About:** the six-card standards grid became a ruled two-column list.
- **Work:** screenshots regenerated from the redesigned homepage; facts and design decisions rewritten to describe the current system truthfully.
- **Share image:** `images/rielart-og.jpg` replaced the generic laptop photograph with a typographic card in the brand system (same path, 1200 × 630).
- Decorative → arrows were removed from buttons and links; ↗ remains only where a link opens a new tab.

## Motion

Kept deliberately small: link-underline thickening, header rule on scroll, dropdown caret, menu icon, FAQ open/close, theme glyph. No scroll-triggered effects. `prefers-reduced-motion` removes all transitions.

## Recommendations for the owner

- The Insights featured guide still uses its stock-style cover (`og-website-leads.jpg`) because the audit requires it; the other article covers share that style. Consider replacing them with typographic covers like the new share image.
- The unused portraits remain unreferenced because founder-led positioning is not approved.

## Verification

Static audit: 0 warnings, 0 critical failures. HTTP smoke crawl: 34 routes, all budgets pass (fonts 108 KB / 110 KB). Overflow sweep: 19 routes × 5 widths (320–1440) × 2 themes, no horizontal overflow. Interaction checks: dropdown, mobile menu focus, FAQ, keyboard focus on cobalt fields, form preselection, conditional advertising fields, and validation messaging. Shared cache key: `20261008ink1`.

---

# Historical: “The Turn” refinement (September 24, 2026)

Status: implemented on branch `claude/kind-mayer-5vhoki` for owner review. Not deployed or merged. No external account, DNS, Formspree, Calendly, Stripe, or provider setting was changed, and no production form was submitted.

## Concept: The Turn, reduced to two devices

The folded R mark still drives the identity, but it is no longer repeated on every button, eyebrow, and card. It survives as two deliberate devices:

1. **The path line** — the logo's blue-to-cyan gradient, drawn as a single line that connects brand → website → customers. Used only in the hero service map, the homepage/About three-step sequence, and the process rail.
2. **The fold** — one cut corner, reserved for the pair of primary services, the contact introduction, the Work feature image, and the closing homepage CTA.

Everything else is carried by typography, rules, and spacing rather than boxes.

## Typography

- **Schibsted Grotesk** (variable, Latin, 46.8 KB, preloaded) for headings, UI, and body.
- **Newsreader** (variable, Latin, 58.1 KB) for article body text only; the browser downloads it only on Insights articles.
- Both are self-hosted under SIL OFL 1.1 (`assets/fonts/LICENSE-OFL.txt`) with a metric-adjusted local fallback. No third-party font request.
- Scale: display (hero only), page title, section title, H3, price numerals (tabular), lead, body, and small sentence-case labels. Uppercase labels and decorative 01/02/03 numbering were removed.

## Colour

Warm paper, deep ink, and RielArt blue are retained. Night bands use a deep brand navy (`#0c1b35`) rather than near-black, and re-scope the palette with CSS custom properties so every component adapts automatically. Dark mode is a designed counterpart: near-black paper with navy emphasis bands and a lighter blue. All text token pairs measure ≥ 5:1; control borders ≥ 3.4:1.

## Composition changes

- **Homepage hero:** the approved three-line headline at display scale beside a service map that ties “Build… Launch…” to Brand & Website Launch and “Reach more customers.” to Focused Ads Management. No floating cards, no prices, no trust line.
- **Homepage order:** problem + sequence → services → Google or Meta → why RielArt → work → process + Client Portal strip → FAQ → closing CTA.
- **Primary services** are one ruled two-column sheet with large tabular prices; Business Email is a lighter, rule-topped row beneath (never a third card).
- **Google or Meta** is a two-column comparison divided by an “or”.
- **Inner page heroes** set the title left and the lead right on desktop.
- **Service pages** use ruled scope ledgers and an Included / Not automatically included boundary panel.
- **Pricing** adds an arithmetic “Need both?” row ($599 once, then $349/month) that keeps the approved sentence and states it is not a third package.
- **Work** shows real screenshots of this RielArt site, a fact list, design decisions, and flagged representative concepts with structural scope sketches.
- **Insights** index is an editorial list; articles read in Newsreader with a sticky service aside on desktop.
- **Contact** keeps every field and behaviour; service choices are clearer selection tiles and the optional setup is a lighter dashed control.

## Motion

Path lines draw once (hero on load; sequence/process via CSS scroll-driven timelines where supported). Dropdowns, mobile menu, FAQ, buttons, and the theme icon use short transitions. `prefers-reduced-motion` removes all of it. No scroll-jacking or parallax.

## Technical

Static HTML, CSS, and vanilla JavaScript only. JavaScript gained one passive, rAF-throttled header scroll-state handler. Shared cache key: `20260924r1`.

---

# Historical: RielArt redesign handoff — August 26, 2026

The notes below describe the previous implementation and are kept as a record. Where they conflict with the section above, the section above is current.


Status: implemented and verified in the testing clone. Nothing was deployed, pushed, submitted, or changed in production or any external service. QA artifacts were kept outside the tracked clone.

## Design direction

The redesign is called **The Turn**. It grows from the folded-ribbon geometry of the existing RielArt mark: a business becomes recognizable through its brand, credible through its website, and easier to choose through a clear customer pathway.

- Warm paper and deep ink replace the previous glow-heavy presentation.
- RielArt blue leads the hierarchy; cyan is reserved for the end of the pathway and select accents.
- Selective folded corners, angled cuts, structural rules, open layouts, and whitespace echo the logo without turning the site into an industrial diagram or a ruled ledger.
- Light and dark themes are intentional counterparts, not simple inversions.
- Motion is limited to the logo-derived homepage pathway, navigation, FAQs, and the theme control. Reduced-motion preferences collapse these transitions.
- The site remains static HTML, CSS, and vanilla JavaScript with a system font stack and no new dependency.

## Commercial and technical contracts preserved

- Exactly two primary offers remain public: Brand & Website Launch at $599 USD one time, and Focused Ads Management at $349 USD per month with a three-month initial commitment and advertising spend separate.
- Business Email & Workspace Setup remains a subordinate optional setup from $149 USD one time.
- Existing URLs, canonicals, structured data, sitemap coverage, redirect rules, Client Portal links, Calendly link, Formspree endpoint, inquiry query states, accessibility landmarks, light/dark theme behavior, and legal content remain intact.
- A simple Meta short-form variation may be assembled from suitable approved or client-provided assets within the standard creative allowance; filming and full or ongoing custom video production remain separately scoped.
- The Work page uses the existing RielArt mark and CSS-native Turn geometry for one clearly labelled internal RielArt feature. Every other example remains explicitly classified as representative concept or solution model, not client work.

## Performance results

- Shared CSS: 92,044 bytes before; 58,205 bytes after.
- Shared JavaScript: 20,479 bytes before; 19,868 bytes after.
- Image library: 11,869,058 bytes before; 377,834 bytes after (96.8% reduction). Social images now match their declared 1200 × 630 dimensions.
- No external font, framework, build step, or third-party runtime was introduced.

## Verification completed

- Static audit: 32 HTML files, 22 indexable pages, 22 sitemap URLs, 217 asset references, 53 image checks, 32 JSON-LD blocks, one form, 14 redirects, zero warnings, and zero critical failures.
- The final precision pass removes only the compact homepage-hero price strip. The View Pricing action remains, and approved prices remain visible in the homepage service section, Pricing, both primary service pages, and relevant commercial content.
- The semantic Advertising Details fieldset now keeps its legend visually inside the panel, aligns differently wrapped desktop labels through shared grid rows, and returns to natural stacked labels on mobile. Hidden, Ads, Both, and switch-away states all passed.
- HTTP crawl: 34 routes requested, 33 expected HTTP 200 responses, 31 HTML routes, and every HTML/CSS/JavaScript/image/logo budget passed.
- Final browser matrix: 14 requested routes × 15 viewports × 2 themes = 420 rendered cases and 20,330 assertions, all passing. Reviewed widths were 1600, 1440, 1366, 1280, 1180, 1081, 1080, 1024, 820, 768, 430, 390, 375, 360, and 320 CSS pixels.
- Hero pixel and geometry review passed all 30 light/dark width combinations after the pricing removal, including text-range safe zones and clip hit-tests after the restrained pathway motion completed.
- Twenty-two final interaction checks passed for theme, navigation, mobile-menu, FAQ, Insights, form, reduced-motion, reflow, focus, and conditional-field behavior.
- Independent alignment review covered the full requested route matrix. Header/container/footer edges, service and pricing cards, buttons, portfolio rows, FAQ controls, form panels, mobile gutters, and content wrapping passed with no horizontal overflow, clipping, or unexplained drift.
- Desktop offer headers now reserve a responsive shared label zone only above 820 pixels, keeping price and action baselines aligned without imposing desktop whitespace on stacked mobile cards.
- At 380 pixels and below, the compact header wordmark remains available as the link's accessible name while the footer wordmark stays visible. The 320-pixel Contact required marker also stays with its label text.
- The contact success state was tested with the Formspree request intercepted locally. No real inquiry was submitted.
- All 24 public page shells use the `20260826final2` CSS and JavaScript cache key.
- JavaScript syntax and Git whitespace checks passed.

## Manual production checks still required

1. Confirm the production host implements the 14 rules in `_redirects` as real permanent redirects. A static local server cannot prove host-level 301 behavior, and GitHub Pages does not natively consume Netlify-style `_redirects` rules.
2. Confirm the Formspree project retains the intended non-JavaScript post-submit destination. The source-controlled form endpoint is correct, but dashboard behavior is external to this clone.
3. Confirm the final Meta creative wording in the signed service agreement. The repository now consistently limits the included option to a simple asset-based short-form variation and separately scopes full video production.
