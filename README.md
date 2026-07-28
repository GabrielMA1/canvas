# rielart.com

Static, dependency-free production website for RielArt. Deploy the repository’s public site files at the domain root.

## Public commercial model

RielArt presents exactly two primary services:

- **Brand & Website Launch — $599 USD one time**
- **Focused Ads Management — $349 USD per month**, with a three-month initial commitment

Advertising spend is separate and is paid by the client directly to Google or Meta. The general site CTA is **Get Started**, linking to `/contact/#project-inquiry`. Service-specific actions remain **Start Your Launch** and **Start Advertising**. There are no public Stripe checkout links.

Support beyond the two standard services is available only as a separately reviewed inquiry. **Ask About a Custom Scope** links to `/contact/?service=custom-scope#project-inquiry`; it does not create a third package, price, or promise of availability.

Future approved payment links have one internal configuration location: `config/payment-links.json`. Both values remain `null` until approved and tested. The `config/` directory is excluded from the GitHub Pages build.

## Site structure

- `index.html` — ten-section homepage with approved positioning, two offers, Google/Meta comparison, work, FAQ, and final inquiry CTA
- `services/` — consolidated two-service overview
- `services/brand-website-launch/` — detailed $599 launch scope
- `services/focused-ads-management/` — detailed $349 monthly advertising scope, including Google and Meta explanations
- `pricing/` — two-offer comparison, “Need both?” example, and a discreet custom-scope inquiry
- `process/` — four-step customer-facing process
- `portfolio/` — accurately labelled internal work and representative concepts
- `about/` — company approach, operating principles, ownership, and service area
- `faq/` — detailed commercial and delivery answers
- `blog/` — searchable Insights index and nine educational articles
- `contact/` — canonical inquiry with conditional advertising questions and preserved custom-scope context
- `privacy-policy/`, `terms/` — updated legal information pending the decisions recorded in `RIELART-MANUAL-REVIEW.md`
- `thanks/`, `404.html` — noindex utility pages
- `assets/css/site.css` — consolidated visual system and responsive rules
- `assets/js/site.js` — theme, navigation, FAQ, filter, reveal, conditional form, and validation behaviour
- `tools/site_audit.py` — static-site, commercial-model, integration, metadata, schema, link, and redirect audit
- `tools/http_smoke.py` — local HTTP crawler and response-budget check

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
- Test the project form choices, conditional advertising fields, error states, Formspree delivery, and thank-you redirect.
- Confirm the Client Portal, email, LinkedIn, and optional scheduling destinations.
- Confirm no public Stripe link is present; connect payment links only after approval through the documented configuration.
- Confirm no public street or mailing address, address schema, or empty `<address>` element is present; public legal questions route to `hello@rielart.com`.
- Test representative pages at 320 px, tablet, and desktop widths in both themes, with keyboard navigation, reduced motion, and 200% zoom.
- Keep representative concepts clearly labelled until permissioned client work is available.

The `RIELART-*.md` documents record the commercial strategy, offer scope, advertising limits, migration decisions, copy map, implementation details, manual decisions, and final QA.
