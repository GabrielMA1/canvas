# rielart.com

Static, dependency-free production website for RielArt. Deploy the repository’s public site files at the domain root.

## Public commercial model

Approved by the owner on October 22, 2026. Headline: **The art your business deserves.** RielArt presents four primary offers:

- **Brand & Website Launch — $499 USD one time**, paid $250 at project start and $249 at launch
- **Ad Videos — $149 USD per video**, or **3 videos for $349** (motion graphics up to 30 seconds, 9:16 and 1:1, delivered in 1–3 business days)
- **Focused Ads Management — $299 USD per month**, two-month initial commitment, then month to month
- **Growth Partner — $449 USD per month**: Focused Ads Management plus two new ad videos every month, two-month initial commitment, then month to month

One approved subordinate setup is also public: **Business Email & Workspace Setup — from $149 USD one time**. It is a practical optional setup for a straightforward new Google Workspace or Microsoft 365 configuration, not a primary service.

Advertising spend is separate and is paid by the client directly to Google or Meta. Focused Ads Management includes static creative; new motion-graphics videos come from Ad Videos or Growth Partner. The general site CTA is **Get Started**, linking to `/contact/#project-inquiry`. Service-specific actions are **Start Your Launch**, **Order an Ad Video**, **Start Advertising**, and **Become a Growth Partner**. There are no public Stripe checkout links.

Support beyond these offers is available only as a separately reviewed inquiry. **Ask About a Custom Scope** links to `/contact/?service=custom-scope#project-inquiry`; it does not create another package, price, or promise of availability.

Future approved payment links have one internal configuration location: `config/payment-links.json`. Both values remain `null` until approved and tested. The `config/` directory is excluded from the GitHub Pages build.

## Site structure

- `index.html` — homepage: “The art your business deserves.” on a full-width ink field with all four offers and prices set as a price list, the problem statement, the three-offer price board with the Growth Partner band and a compact optional business-email callout, the ad-video showcase, Why RielArt, Google/Meta comparison, process with a Client Portal strip, labelled work, FAQ, and final inquiry CTA
- `services/` — overview of the four primary offers plus a subordinate business-email setup section
- `services/brand-website-launch/` — detailed $499 launch scope, two-part payment, and an optional business-email cross-reference
- `services/ad-videos/` — Ad Videos scope, formats, delivery, exclusions, usage, and the three video slots
- `services/focused-ads-management/` — detailed $299 monthly advertising scope, Google and Meta explanations, and the Growth Partner section (`#growth-partner`)
- `pricing/` — four-offer price board, “launch, then grow” example, four inclusion columns, detailed optional business-email setup, and a discreet custom-scope inquiry
- `process/` — four-step customer-facing process
- `portfolio/` — RielArt's own site as the internal project (real screenshots of this site), design decisions, and flagged representative concepts with structural scope sketches
- `about/` — company approach, operating principles, ownership, and service area
- `faq/` — detailed commercial, business-email setup, and delivery answers
- `blog/` — searchable Insights index and nine educational articles
- `contact/` — canonical inquiry with four primary choices, a non-required business-email checkbox, conditional advertising questions, and preserved query context
- `privacy-policy/`, `terms/` — legal information covering advertising and authorized business-email/workspace access, pending the decisions recorded in `RIELART-MANUAL-REVIEW.md`
- `thanks/`, `404.html` — noindex utility pages
- `assets/css/site.css` — consolidated visual system (“Printed in one ink”, October 2026) and responsive rules
- `assets/fonts/` — self-hosted Archivo and Newsreader Latin variable WOFF2 files with their SIL OFL 1.1 licence
- `assets/js/site.js` — theme, active navigation, menus, FAQ, filter, conditional form, and validation behaviour
- `assets/js/motion-insights.js` — GSAP Flip for the Insights topic filter (loaded on `/blog/` only)
- `assets/js/video-slots.js` — turns each video slot from placeholder to playable video once its file exists in `videos/` (homepage and Ad Videos page only)
- `videos/` — owner-uploaded ad videos; see `VIDEO-UPLOADS.md`
- `assets/js/form-messages.js` — inline, field-level validation messages (loaded on `/contact/` only)
- `assets/js/vendor/` — pinned GSAP 3.15.0 core and Flip, written by `tools/vendor.mjs`; there is deliberately no `package.json`
- `tools/vendor.mjs` — re-vendors pinned browser libraries with `npm pack` and prints their SHA-256
- `tools/site_audit.py` — static-site, commercial-model, integration, metadata, schema, link, and redirect audit
- `tools/http_smoke.py` — local HTTP crawler and response-budget check (HTML, CSS, JavaScript, images, logo, fonts)

Five retired service routes and the legacy package route remain as noindex compatibility pages with direct permanent mappings in `_redirects`. See `RIELART-URL-MIGRATION.md`.

## Preserved production integrations

- Client Portal: `https://portal.rielart.com`
- Formspree: `https://formspree.io/f/xojrdoel`
- Thank-you destination: `https://rielart.com/thanks/`
- Optional scheduling: `https://calendly.com/gabrielmacovei001/15min?hide_gdpr_banner=1`
- Email: `hello@rielart.com`
- LinkedIn: `https://www.linkedin.com/in/gabrielmacovei/`

## Local review

Start a static server from the repository root:

```powershell
python -m http.server 4173
```

Then run:

```powershell
python tools/site_audit.py
python tools/http_smoke.py --base-url http://127.0.0.1:4173/
```

## Pre-publish checklist

- Review `RIELART-MANUAL-REVIEW.md` and resolve all owner/legal decisions that apply to launch.
- Run the static audit and local HTTP smoke crawl.
- Test the four primary form choices, optional business-email checkbox/query state, conditional advertising fields, error states, Formspree delivery, and thank-you redirect.
- Confirm the Client Portal, email, LinkedIn, and optional scheduling destinations.
- Confirm no public Stripe link is present; connect payment links only after approval through the documented configuration.
- Confirm no public street or mailing address, address schema, or empty `<address>` element is present; public legal questions route to `hello@rielart.com`.
- Test representative pages at 320 px, tablet, and desktop widths in both themes, with keyboard navigation, reduced motion, and 200% zoom.
- Keep representative concepts clearly labelled until permissioned client work is available.

`REDESIGN-NOTES.md` describes the current design system. The `RIELART-*.md` documents record the commercial strategy, offer scope, advertising limits, migration decisions, copy map, implementation details, manual decisions, and final QA.
