# rielart.com

Static, dependency-free production website for RielArt. Deploy the repository’s public site files at the domain root.

## Public commercial model

Approved by the owner on October 22, 2026 and simplified the same month. Headline: **The art your business deserves.** RielArt sells three single services and one bundle:

- **Brand & Website Launch — $349 USD one time**, paid $175 at project start and $174 when the site goes live
- **Ad Videos — $99 USD per video** (animation up to 30 seconds, vertical and square, ready in 1–3 business days)
- **Ads Management — $249 USD per month**, month to month with no minimum (formerly “Focused Ads Management”; the URL `/services/focused-ads-management/` is unchanged)
- **Growth Partner — $399 USD per month**, 3-month minimum then month to month: Brand & Website Launch, Ads Management, two new ad videos a month, business email setup, and Google Business Profile setup. Against buying the same things separately it saves $701 in the first three months ($1,898 vs $1,197) and $48 a month after that ($447 vs $399).

Extras: **Business Email & Workspace Setup — from $129 USD one time**, **Google Business Profile Setup — $79**, and **extra website pages — $79 each**. Business email and Google Business Profile setup are included with Growth Partner.

Advertising spend is separate and is paid by the client directly to Google or Meta (shown to visitors as “Facebook & Instagram”). The general site CTA is **Get Started**, linking to `/contact/#project-inquiry`. Service-specific actions are **Start Your Launch**, **Order an Ad Video**, **Start Advertising**, and **Become a Growth Partner**. There are no public Stripe checkout links.

### New client offer (active)

Every page has a thin banner, “Open to new clients: 10% off your first month*”, whose asterisk links to a small-print note at the foot of the page (`#offer-terms-note`): 10% off the first month of Ads Management or Growth Partner with a 3-month commitment; ad budget not included. The same terms appear under the Pricing plans (`#plans-footnote`), in the FAQ, and in Terms (`#new-client-offer`). To end the offer, remove the `offer-banner` aside and the `offer-terms` footer paragraph from every page, the asterisks and footnote on Pricing, the FAQ entries (homepage and FAQ page, including JSON-LD), and the Terms paragraph, then run the audit.

Support beyond these offers is available only as a separately reviewed inquiry. **Ask About a Custom Scope** links to `/contact/?service=custom-scope#project-inquiry`; it does not create another package, price, or promise of availability.

Future approved payment links have one internal configuration location: `config/payment-links.json`. Both values remain `null` until approved and tested. The `config/` directory is excluded from the GitHub Pages build.

## Search and visibility (October 2026)

- Page titles and descriptions use the words customers search for (“small business website design”, “video ads”, “Google Ads & Facebook Ads management”) with the price where it helps.
- The homepage H1 opens with a plain keyword line (“Websites, video ads & online advertising for small businesses”) above the brand line, and a “Made for small businesses like yours” section names the kinds of businesses served.
- Organization schema carries a slogan and `knowsAbout`; every service page has Service schema with current prices; FAQ pages have FAQPage schema; the sitemap lists all 27 public pages with current dates.
- Service pages link to the matching guides, and the guides link back to the services.

Owner-only steps that matter most for Google: verify rielart.com in Google Search Console and Bing Webmaster Tools and submit `https://rielart.com/sitemap.xml`; create and verify a Google Business Profile (service-area business, no public address needed); ask the first clients for Google reviews; upload the three ad videos; and add a real client project to Work as soon as one is approved.

## Site structure

- `index.html` — homepage: new-client banner, “The art your business deserves.” beside a CSS motion-graphics reel of the four services ending on a social ad that brings in a customer message (pausable; still frame under reduced motion), the problem statement, the three-offer price board with the Growth Partner band, an Extras row, the ad-video showcase, Why RielArt, Google/Meta comparison, process with a Client Portal strip, labelled work, FAQ, and final inquiry CTA
- `services/` — overview of the four offers, the Extras row, and a plain-language guide to where to start
- `services/brand-website-launch/` — detailed $399 launch scope, two-part payment, and an optional business-email cross-reference
- `services/ad-videos/` — Ad Videos scope, formats, delivery, exclusions, usage, and the three video slots
- `services/focused-ads-management/` — plain-language Ads Management scope ($249/month), a four-step explainer, Google and Facebook & Instagram explanations, and the Growth Partner section (`#growth-partner`)
- `pricing/` — plan cards in the style of software pricing pages: a Services | Extras switch (`assets/js/pricing-plans.js`; both groups show without JavaScript), four plan cards with Growth Partner printed in solid ink as “Best value”, three extras cards (business email, Google Business Profile, extra page), small-print offer terms, a custom-scope line, the “Why Growth Partner costs less” receipt, and what each price covers
- `process/` — four-step customer-facing process
- `portfolio/` — RielArt's own site as the internal project (real screenshots of this site), design decisions, and flagged representative concepts with structural scope sketches
- `about/` — company approach, operating principles, ownership, and service area
- `faq/` — detailed commercial, business-email setup, and delivery answers
- `blog/` — searchable Insights index and eleven educational articles, including “How Much Does a Small Business Website Cost in 2026?” and “Google Ads vs Facebook Ads” (Advertising category)
- `contact/` — canonical inquiry with four primary choices plus “not sure”, optional Extras checkboxes (business email, Google Business Profile, extra pages), conditional advertising questions, and preserved query context
- `privacy-policy/`, `terms/` — legal information covering advertising and authorized business-email/workspace access, pending the decisions recorded in `RIELART-MANUAL-REVIEW.md`
- `thanks/`, `404.html` — noindex utility pages
- `assets/css/site.css` — consolidated visual system (“Printed in one ink”, October 2026) and responsive rules
- `assets/fonts/` — self-hosted Archivo and Newsreader Latin variable WOFF2 files with their SIL OFL 1.1 licence
- `assets/js/site.js` — theme, active navigation, menus, FAQ, filter, conditional form, and validation behaviour
- `assets/js/motion-insights.js` — GSAP Flip for the Insights topic filter (loaded on `/blog/` only)
- `assets/js/hero-reel.js` — pause control and off-screen pausing for the homepage reel
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
