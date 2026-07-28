# RielArt Focused Refinement Plan

**Prepared:** July 28, 2026  
**Repository baseline:** `aafba2c`  
**Scope:** Focused refinement of the current two-service static website. This is not a redesign or offer-architecture change.
**Status:** Implemented and locally verified; see `RIELART-IMPLEMENTATION-LOG.md` and `RIELART-QA-REPORT.md`.

## Protected foundations

The refinement will preserve:

- Brand & Website Launch at **$599 USD one time**.
- Focused Ads Management at **$349 USD per month**.
- The three-month advertising commitment and separate advertising spend.
- The Google-versus-Meta recommendation model.
- Existing public URL architecture, redirects, canonical URLs, sitemap, and two-service schema except where contact metadata or address removal requires an update.
- Static HTML, CSS, and JavaScript architecture.
- Light and dark themes, theme toggle, mobile navigation, skip link, focus styles, reduced-motion handling, and responsive behavior.
- Client Portal, Formspree endpoint, `/thanks/`, Calendly, email, LinkedIn, and current contact-form qualification logic.
- Service-specific calls to action: **Start Your Launch** and **Start Advertising**.

## Baseline validation

### Static audit

- HTML files: 32
- Indexable pages and sitemap URLs: 22
- Forms: 1
- Orphan indexable pages: 0
- Public Stripe links: 0
- Warnings: 0
- Critical failures: 0

### Local HTTP crawl

- Routes checked: 34
- Successful HTTP 200 routes: 33
- Intentional 404 route: 1
- Aggregate HTML response bytes: 319,743
- Failures: 0
- Existing HTML, CSS, JavaScript, image, and logo budgets: PASS

## Planned production changes

### 1. Public address removal

Remove the Canadian mailing address and “Canadian mailing address” label from:

- shared public footers;
- homepage Organization JSON-LD;
- About-page address block;
- Privacy Policy contact language;
- Terms contact language;
- any public metadata, hidden text, or reusable markup found during the final repository scan.

The footer will retain copyright, Privacy, and Terms without an empty `<address>` element. Legal contact language will use `hello@rielart.com` only. No replacement office or address will be invented.

### 2. Global CTA vocabulary

Replace every public, general-purpose **Start Your Project** action with **Get Started**, preserving its current `/contact/#project-inquiry` destination or equivalent query-string context.

Keep unchanged:

- Start Your Launch
- Start Advertising
- See full scope
- View Pricing
- Client Portal
- Contact navigation labels

Update contact-page metadata and ContactPage schema to use **Contact RielArt** rather than **Start Your Project**.

### 3. Homepage hero

Remove the complete trust-line element:

> Clear scope. Straightforward pricing. Client-owned accounts.

Rebalance the hero action spacing without replacing the line or leaving an empty wrapper.

### 4. Card alignment

Use shared, resilient card layout rules:

- stretch comparable sibling cards through their parent grid;
- structure offer cards as grid rows for header, price, optional note, features, and actions;
- reserve an inaccessible, presentation-only structural note row through CSS rather than hidden filler text;
- anchor offer and platform action regions at the bottom;
- align comparable selection-card text blocks;
- preserve natural stacked height on tablet/mobile;
- avoid fixed-height clipping and per-card margin patches.

Primary targets:

- homepage and services/pricing offer cards;
- homepage Google and Meta platform panels;
- pricing comparison and custom-scope panel;
- contact service-selection cards;
- comparable work and process card groups.

### 5. Pricing comparison

Use the approved neutral introduction:

- **Eyebrow:** Compare the services
- **Headline:** What each service includes.
- **Supporting copy:** Choose the service that matches what your business needs now. Brand & Website Launch creates or refreshes your online foundation, while Focused Ads Management manages one active Google or Meta campaign.

Rewrite each comparison cell as a factual scope statement without suggesting that either service is incomplete or automatically dependent on the other.

### 6. Custom-support inquiry

Add one discreet section after the comparison table:

- **Headline:** Need something beyond these scopes?
- **Body:** RielArt can review ongoing website support, content updates, blog publishing, additional landing pages, or broader campaign requirements separately.
- **CTA:** Ask About a Custom Scope
- **Destination:** `/contact/?service=custom-scope#project-inquiry`

Do not add a package, price, schema service, comparison column, or primary offer card.

Map `custom-scope` to the existing **I am not sure yet** form choice and preserve the custom request context in a hidden form field. The form will continue to expose exactly four primary choices.

### 7. Contact composition

Rebuild the contact introduction as a contained dark card beside the existing form:

- desktop ratio approximately 38/62;
- aligned top edges and coordinated radii;
- no background slab, overlap, or excessive dark empty height;
- non-sticky by default unless a bounded desktop implementation proves useful;
- compact “What happens next” sequence;
- compact Email, Existing client, and Optional call links;
- stacked natural-height layout below desktop;
- one-column service choices at narrow widths;
- existing Formspree behavior and qualification fields preserved.

Approved contact copy:

- **Eyebrow:** Contact RielArt
- **Headline:** Let’s talk about your business.
- concise review, recommendation, and next-step language using “When the request is a fit.”

### 8. Documentation and audit updates

Update:

- `RIELART-COPY-MAP.md`
- `RIELART-REMODEL-STRATEGY.md`
- `RIELART-OFFER-SCOPE.md`
- `RIELART-IMPLEMENTATION-LOG.md`
- `RIELART-QA-REPORT.md`
- `RIELART-MANUAL-REVIEW.md` where the old address is treated as current
- `README.md`
- `_config.yml`
- `tools/site_audit.py`
- `tools/http_smoke.py` only if final response-weight changes require a justified budget adjustment

New audit assertions will cover the removed address, empty `<address>` elements, approved CTA hierarchy, removed hero trust line, neutral comparison copy, custom-scope inquiry behavior, unchanged service-specific CTAs/prices/integrations, and the absence of a third primary offer.

## Validation plan

### Automated

- `tools/site_audit.py`
- `tools/http_smoke.py`
- JavaScript syntax check
- `git diff --check`
- targeted repository searches for retired address, CTA, trust-line, comparison, and approval wording

### Browser and responsive

Use the local static preview for actual checks at:

- 320 × 568
- 360 × 800
- 390 × 844
- 430 × 932
- 768 × 1024
- 1024 × 768
- 1280 × 720
- 1440 × 900
- 1920 × 1080

Check:

- homepage, pricing, contact, services, work, process, and representative supporting pages;
- light and dark themes;
- mobile navigation and Escape/focus restoration;
- card alignment on side-by-side layouts;
- no card clipping or page-level overflow when stacked;
- query-string service preselection, including `custom-scope`;
- conditional advertising fields and empty-form validation;
- visible focus and logical DOM order;
- console errors.

Where the available browser cannot genuinely emulate 200 percent zoom or reduced motion, report static implementation verification and leave the runtime test open rather than claiming it passed.

## Non-goals

- No new public package or price.
- No payment link or checkout.
- No replacement office or address.
- No offer, navigation, route, sitemap, or platform-model redesign.
- No dependency, framework, CMS, or build-chain addition.
- No production deployment or external-account mutation without separate authorization.
