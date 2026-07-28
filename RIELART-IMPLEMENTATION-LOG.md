# RielArt Commercial Remodel - Implementation Log

**Implemented:** July 27, 2026  
**Repository:** `live-rielart`  
**Deployment status:** Source implementation complete; no production deployment, commit, payment activation, or external form submission was performed.

## Outcome

The production source now presents one clear commercial path:

1. **Brand & Website Launch — $599 USD one time**
2. **Focused Ads Management — $349 USD per month**

The advertising service visibly states the three-month initial commitment, that advertising spend is separate, and that the standard engagement covers one Google or Meta platform, one market, one language, and one primary offer. Legacy packages, AI services, audits, broad growth retainers, and obsolete public payment links are no longer presented as current offers.

## Baseline and final repository measurements

| Measure | Before remodel | After remodel |
|---|---:|---:|
| HTML files checked | 30 | 32 |
| Indexable pages | 25 | 22 |
| Sitemap URLs | 25 | 22 |
| JSON-LD blocks | 35 | 32 |
| Public forms | 2 | 1 |
| Redirect rules | 4 | 14 |
| GitHub Pages exclusions | 17 | 26 |
| Public Stripe Payment Links | 6 | 0 |
| Static-audit warnings | 0 | 0 |
| Static-audit critical failures | 0 | 0 |
| HTTP routes checked | 32 | 34 |
| Successful HTTP 200 routes | 31 | 33 |
| HTML routes in smoke crawl | 29 | 31 |
| Aggregate HTML response bytes | 435,330 | 319,743 |
| Uncompressed CSS bytes | 61,174 | 81,847 |
| Uncompressed JavaScript bytes | 14,012 | 15,038 |
| Image bytes checked | 643,390 | 643,390 |

Aggregate HTML response weight decreased by approximately 26.6 percent while the new layout and component system remained within the defined CSS, JavaScript, image, logo, and per-route HTML budgets.

## Commercial and content implementation

### Homepage

Rebuilt `index.html` around the approved ten-part narrative:

- exact headline: “Build your brand. Launch your website. Reach more customers.”
- exact supporting statement supplied in the remodel brief;
- a transparent, animated RielArt orbital mark with no card background or duplicate explanatory copy;
- the business problem and RielArt sequence;
- two and only two primary offer cards;
- a plain-language Google-versus-Meta explanation;
- four-step process;
- work samples with explicit context labels;
- practical reasons to choose RielArt;
- ten concise FAQs;
- final project-inquiry call to action.

The obsolete service ticker, pause control, hero priority tabs, excessive hero copy, and AI-style label pills were removed.

### Services and pricing

- Rebuilt `/services/` as a two-service overview.
- Added `/services/brand-website-launch/` with scope, exclusions, client responsibilities, timeline, ownership, and inquiry path.
- Added `/services/focused-ads-management/` with platform selection guidance, readiness criteria, included work, boundaries, commitment, ad-spend separation, and reporting expectations.
- Rebuilt `/pricing/` with two equal-height desktop offer cards, a direct comparison table, and a clearly labelled `$948` three-month fee example that excludes ad spend.
- Kept checkout disabled; every purchase-oriented action routes to the inquiry form.

### Process, work, about, and FAQ

- Simplified `/process/` to a consistent four-stage path rather than five dense, mismatched production cards.
- Reworked `/portfolio/` so completed work, internal projects, representative concepts, and solution models are clearly labelled.
- Rewrote `/about/` around practical service delivery and international availability without “founder-led,” invented team-size, Toronto-office, or unlimited-global-service language.
- Rebuilt `/faq/` around the two offers, account ownership, advertising platform choice, spend, commitment, tracking, website readiness, and geographic limits.

### Contact and post-submission flow

- Consolidated the site to one canonical Formspree project form.
- Added the four approved choices:
  - Brand & Website Launch
  - Focused Ads Management
  - Both services
  - Not sure yet
- Added conditional advertising fields for platform preference, target location, and intended monthly ad budget.
- Added stable query-string preselection for campaign and launch CTAs.
- Preserved client-side validation, clear error status, the Formspree endpoint, and `/thanks/`.
- Rebuilt `/thanks/` to explain review, fit confirmation, onboarding, and next steps without implying automatic acceptance.

### Legal and operational language

- Rebuilt the Privacy Policy and Terms for the approved two-offer model.
- Kept legal statements conservative about tracking, results, billing, international work, and third-party providers.
- Documented unresolved agreement, privacy, platform-access, billing, and provider decisions in `RIELART-MANUAL-REVIEW.md`.
- Included the approved Canadian mailing address without describing it as a public office or limiting service to one Canadian city.

### Insights

- Preserved the nine existing educational articles.
- Removed obsolete package and legacy-service calls to action.
- Brand, website, and SEO articles now lead to Brand & Website Launch.
- AI articles remain educational but lead only to the current services overview or general inquiry; AI is not presented as a current package or primary service.
- Preserved article search and metadata.

## Visual system and responsive implementation

- Preserved the RielArt logo, blue palette, typography direction, light/dark theme, and core interaction patterns.
- Added a more restrained editorial/component system for offer cards, scope sections, comparisons, FAQ rows, contact choices, and process steps.
- Normalized spacing, card structure, heading placement, action placement, and desktop card heights.
- Rebalanced hero and contact headings to avoid one- or two-word orphan lines.
- Kept the homepage hero headline to exactly three phrase lines at 320, 768, and 1440 pixel QA widths.
- Removed the background frame around the orbital hero animation.
- Preserved focus styles, the skip link, mobile navigation, Escape-to-close behavior, and focus restoration.
- Added `tabindex="-1"` to the shared main-content target so the skip link transfers focus correctly.
- Kept reduced-motion rules that stop nonessential reveal and orbital animation.

## SEO, structured data, and URL architecture

- Updated titles, descriptions, canonical URLs, Open Graph data, Twitter data, headings, and schema to the two-offer commercial model.
- Limited Service structured data to the two approved services and prices.
- Did not add unsupported `LocalBusiness`, office, review, rating, team-size, client-count, or performance claims.
- Reduced the indexable architecture from 25 to 22 URLs and synchronized `sitemap.xml`.
- Marked retired service fallbacks, packages, thank-you, 404, and old legal stubs as non-indexable where appropriate.
- Updated `_redirects` with explicit canonical migrations.

The complete route decision table is in `RIELART-URL-MIGRATION.md`.

## URL changes

| Old public route | Final route |
|---|---|
| `/services/brand-strategy-identity/` | `/services/brand-website-launch/` |
| `/services/web-design-development/` | `/services/brand-website-launch/` |
| `/services/digital-growth-management/` | `/services/focused-ads-management/` |
| `/services/ai-automation-operations/` | `/services/` |
| `/services/audits-advisory/` | `/services/` |
| `/packages/` and `/packages/*` | `/pricing/` |
| `/privacy-policy.html` | `/privacy-policy/` |
| `/terms.html` | `/terms/` |

The retired service files remain as `noindex` browser fallbacks for static-host compatibility while `_redirects` defines the production 301 behavior.

## Integrations preserved

- Client Portal links
- Formspree project-inquiry endpoint
- `/thanks/` success route
- Calendly outbound scheduling link where retained
- `hello@rielart.com`
- LinkedIn
- Cloudflare, Resend, and Stripe references where they remain relevant to privacy or client operations
- light/dark theme persistence
- mobile navigation behavior

No Google Ads tag, Meta Pixel, Conversions API, analytics platform, new cookie, or new external script was introduced.

## Payment-link configuration

The private source-of-truth location is:

`config/payment-links.json`

Current values are intentionally inactive:

```json
{
  "brandWebsiteLaunch": null,
  "focusedAdsManagement": null
}
```

No public page contains an active Stripe checkout link. Future links require owner, agreement, billing, tax, success-route, cancellation, and test-payment review before activation.

## Audit-tool changes

`tools/site_audit.py` now asserts:

- the approved homepage headline and message;
- exactly two primary commercial offer cards on the homepage, services page, and pricing page;
- exact price and cadence language;
- required advertising scope boundaries;
- exact contact choices and conditional advertising fields;
- approved schema names and prices only;
- required redirects and private payment configuration;
- absence of legacy prices, legacy public offers, public Stripe links, unsupported geography, founder/team claims, and unsupported numerical claims;
- existing canonical, asset, form, internal-link, legal, portal, sitemap, exclusion, and orphan-page requirements.

`tools/http_smoke.py` now crawls the new services and legacy fallback routes and enforces updated, explicit performance budgets.

## Files created

- `RIELART-REMODEL-STRATEGY.md`
- `RIELART-OFFER-SCOPE.md`
- `RIELART-ADS-SERVICE-SCOPE.md`
- `RIELART-URL-MIGRATION.md`
- `RIELART-COPY-MAP.md`
- `RIELART-IMPLEMENTATION-LOG.md`
- `RIELART-QA-REPORT.md`
- `RIELART-MANUAL-REVIEW.md`
- `config/payment-links.json`
- `services/brand-website-launch/index.html`
- `services/focused-ads-management/index.html`

## Release status

The source remodel and local QA are complete. Production deployment, production redirect verification, a real Formspree delivery, cross-browser testing, legal approval, and payment-link activation remain explicit owner/manual steps documented in the QA and manual-review reports.
