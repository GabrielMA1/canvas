# RielArt Commercial Remodel and Refinement - Implementation Log

**Implemented:** July 27-28, 2026
**Repository:** `live-rielart`
**Deployment status:** Source implementation complete; no production deployment, commit, payment activation, or external form submission was performed.

## July 28 content-consistency and Insights refinement

This narrow pass preserved the approved design, navigation, CTA hierarchy,
forms, integrations, URL architecture, and two-service commercial model.

### Public copy and editorial changes

- Replaced the two outdated AI-primary sentences on `404.html` with approved
  brand, website, and online-advertising language.
- Updated the Insights title, meta description, Open Graph metadata, Twitter
  metadata, Blog structured data, introduction, and social image around Brand,
  Websites, Advertising, and Practical Technology.
- Changed the featured guide from the automation article to the real published
  article **5 Signs Your Website Is Costing You Leads**, using its existing
  `/images/og-website-leads.jpg` image and canonical article URL.
- Reordered the editorial sequence to begin with website conversion, brand
  credibility, local customer acquisition, and practical automation.
- Consolidated index filters and article categories to **Brand**, **Websites**,
  and **Practical Technology**. No empty Advertising filter and no invented
  advertising article were added.
- Preserved all nine real articles and all original publication and
  modification dates.
- Kept the three AI/automation articles as accessible supporting editorial
  content under Practical Technology; no AI commercial package, form choice,
  navigation item, footer service, pricing offer, or Service schema was added.
- Left the homepage FAQ intact. Any future reduction remains a post-traffic
  optimization requiring visitor-behavior evidence.

### Layout and technical consistency

- Added the real featured-article image to the Insights card with intrinsic
  dimensions, descriptive alt text, and an explicit accessible link label.
- Kept article actions bottom-aligned in multi-column layouts, retained
  comparable heading regions, and reset article minimum heights at the mobile
  breakpoint so cards stack at natural content height without clipping.
- Updated the Insights sitemap `lastmod` to `2026-07-28`; canonical URLs and
  article dates were not changed.
- Advanced all 24 full-page stylesheet references from `20260728r3` to
  `20260728r4`.
- Added regression assertions for the approved 404 copy, complete Insights
  metadata, featured article, editorial sequence, filters, all nine Blog schema
  entries, article sections, image, and continued article accessibility.
- Confirmed that no RSS or feed file exists, so no feed update was required.

### Files modified by this pass

- Public content: `404.html`, `blog/index.html`, and all nine
  `blog/*/index.html` article files.
- Presentation and discovery: `assets/css/site.css`, `sitemap.xml`, and the
  shared CSS cache reference in all 24 full public HTML pages.
- Audit and documentation: `tools/site_audit.py`,
  `PRE-PUBLISH-RELEASE-REPORT.md`, `RIELART-QA-REPORT.md`,
  `RIELART-IMPLEMENTATION-LOG.md`, and `RIELART-COPY-MAP.md`.

### Validation results

- Exact `python -B tools/site_audit.py`: attempted; unavailable because
  `python` is not on this machine's `PATH`.
- Bundled Python static audit: PASS — 32 HTML files, 22 indexable/sitemap URLs,
  216 asset references, 52 images, 32 JSON-LD blocks, two approved 404
  statements, nine Insights entries, 24/24 current shared CSS references, zero
  warnings, and zero critical failures.
- Bundled Python local HTTP smoke crawl: PASS — 34 routes, 33 expected HTTP
  200 responses, the intentional missing-route 404, 317,723 aggregate HTML
  bytes, 80,143 CSS bytes, and zero failures.
- `node --check assets/js/site.js`: PASS.
- `git diff --check`: PASS; Git emitted only working-copy line-ending
  advisories.
- Browser checks: PASS at 1440 × 900, 390 × 844, and 320 × 568 for the changed
  Insights and 404 surfaces. Both themes, filters, mobile menu focus/Escape
  behavior, natural card stacking, aligned desktop card actions, broken-image
  checks, clipping, and page-level overflow passed. Browser console warnings
  and errors: 0.
- One supporting AI article was opened at its canonical route and retained one
  H1, the Practical Technology category, no broken image, and no overflow.

### Remaining manual decisions

The pre-existing owner/legal review, one authorized production Formspree
submission, real 200% browser zoom, assistive-technology checks, Safari/iOS,
Lighthouse, external-account ownership checks, and post-publication exclusion
probes remain open. No new blocker was introduced by this pass.

## July 28 focused refinement

The follow-up pass preserved the approved two-service model and completed these focused changes:

- removed the former public street/mailing location from shared footers, About, legal copy, and homepage Organization JSON-LD without inventing a replacement address;
- changed the general site CTA from the former project-start label to **Get Started** while preserving **Start Your Launch**, **Start Advertising**, **See full scope**, **View Pricing**, **Contact**, and **Client Portal**;
- removed the homepage hero trust line and its unused styling;
- aligned equivalent offer and platform-card regions with shared header, note, flexible-content, footer, and action behavior rather than per-card spacing patches;
- replaced the row-by-row pricing comparison with two independent service-inclusion columns so neither service is described through what the other contains;
- added one separately reviewed custom-scope inquiry after the inclusion section without adding a package, price, Service schema, or primary offer;
- mapped `service=custom-scope` to the existing **I am not sure yet** choice while submitting `Custom scope inquiry` in a hidden context field;
- rebuilt the contact introduction as a contained dark card beside the existing form, with compact review/recommendation/next-step content and no split-background slab or sticky artifact;
- updated contact metadata and ContactPage schema to **Contact RielArt**;
- replaced the narrow horizontal-scroll comparison with semantic service articles and lists that stack naturally on smaller screens;
- removed obsolete address, contact-panel, and retired ticker CSS;
- retained JavaScript at `20260728r1` and bumped shared CSS references to `20260728r2` for the independent-inclusion layout.

### Focused-refinement baseline and final measurements

| Measure | July 28 baseline | Final |
|---|---:|---:|
| HTML files checked | 32 | 32 |
| Indexable pages | 22 | 22 |
| Sitemap URLs | 22 | 22 |
| GitHub Pages exclusions | 26 | 27 |
| Internal artifacts excluded | 19 | 20 |
| Global Get Started links checked | N/A | 60 |
| Custom-scope inquiry links checked | 0 | 1 |
| Public PostalAddress schemas | 1 | 0 |
| Organization address properties | 1 | 0 |
| Static-audit warnings | 0 | 0 |
| Static-audit critical failures | 0 | 0 |
| HTTP routes checked | 34 | 34 |
| Successful HTTP 200 routes | 33 | 33 |
| Aggregate HTML response bytes | 319,743 | 317,224 |
| Uncompressed CSS bytes | 81,847 | 79,273 |
| Uncompressed JavaScript bytes | 15,038 | 15,551 |
| HTTP-smoke failures | 0 | 0 |

### Focused-refinement file log

| File | Refinement |
|---|---|
| `404.html` | Updated the general CTA, removed the footer location, and bumped shared asset versions. |
| `about/index.html` | Removed the visible location block, updated the general CTA vocabulary, and bumped assets. |
| `assets/css/site.css` | Added robust offer/platform/contact alignment, rebuilt the contact composition, styled custom scope, improved touch sizing, and removed retired address/contact/ticker CSS. |
| `assets/js/site.js` | Added safe `custom-scope` mapping and hidden inquiry context while preserving existing service and advertising-field logic. |
| `blog/index.html` | Updated shared general CTAs/footer and asset versions. |
| `blog/ai-chatbot-small-business/index.html` | Updated shared general CTAs/footer and asset versions. |
| `blog/ai-chatbot-vs-live-chat/index.html` | Updated shared general CTAs/footer and asset versions. |
| `blog/brand-identity-mistakes/index.html` | Updated shared general CTAs/footer and asset versions. |
| `blog/core-web-vitals-small-business/index.html` | Updated shared general CTAs/footer and asset versions. |
| `blog/local-seo-checklist-toronto/index.html` | Updated shared general CTAs/footer and asset versions. |
| `blog/small-business-automation-ideas/index.html` | Updated shared general CTAs/footer and asset versions. |
| `blog/website-builder-vs-wordpress/index.html` | Updated shared general CTAs/footer and asset versions. |
| `blog/website-costing-you-leads/index.html` | Updated shared general CTAs/footer and asset versions. |
| `blog/website-maintenance-checklist/index.html` | Updated shared general CTAs/footer and asset versions. |
| `contact/index.html` | Updated metadata/schema, rebuilt the left card, preserved four choices/Formspree fields, added custom context, removed the footer location, and bumped assets. |
| `faq/index.html` | Updated shared general CTAs/footer and asset versions. |
| `index.html` | Removed address schema and hero trust line, aligned offer cards, updated general CTAs/footer, and bumped assets. |
| `portfolio/index.html` | Updated shared general CTAs/footer and asset versions. |
| `pricing/index.html` | Added aligned offer regions, two independent service-inclusion columns, a combined-scope clarification, separate custom-scope inquiry, warmer fit language, updated footer/CTA, and bumped assets. |
| `privacy-policy/index.html` | Replaced postal-contact language with email-only contact, updated shared CTA/footer, and bumped assets. |
| `process/index.html` | Updated the general CTA vocabulary/footer and bumped assets. |
| `services/index.html` | Added aligned offer regions, updated general CTAs/footer, and bumped assets. |
| `services/brand-website-launch/index.html` | Preserved the service CTA and scope while updating shared general CTAs/footer and asset versions. |
| `services/focused-ads-management/index.html` | Preserved the service CTA and scope while updating shared general CTAs/footer and asset versions. |
| `terms/index.html` | Replaced postal-contact language with email-only contact, updated shared CTA/footer, and bumped assets. |
| `thanks/index.html` | Replaced cold approval wording, updated shared CTA/footer, and bumped assets. |
| `README.md` | Documented the current CTA hierarchy, custom-scope path, and no-public-address rule. |
| `RIELART-COPY-MAP.md` | Updated approved CTA, pricing, contact, hero, and custom-scope copy. |
| `RIELART-REMODEL-STRATEGY.md` | Updated the current conversion path and public-location position. |
| `RIELART-OFFER-SCOPE.md` | Recorded custom scope as a separate inquiry rather than a third offer. |
| `RIELART-MANUAL-REVIEW.md` | Updated owner/legal checks for email-only public contact and the separate custom-scope path. |
| `AUDIT-MANUAL-REVIEW.md` | Marked the legacy review historical and removed the retired street-location literal. |
| `RIELART-REFINEMENT-PLAN.md` | Added the pre-implementation scope, baseline, non-goals, and validation plan. |
| `RIELART-QA-REPORT.md` | Recorded final automated, responsive, theme, menu, form-state, and manual-review results. |
| `RIELART-IMPLEMENTATION-LOG.md` | Added this complete refinement record and final measurements. |
| `_config.yml` | Excluded the refinement plan from the public Pages build. |
| `tools/site_audit.py` | Added regression rules for address/schema removal, CTA hierarchy, neutral pricing, custom scope, contact metadata, and two-offer integrity. |

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
- Rebuilt `/pricing/` with two equal-height desktop offer cards, independent two-column inclusion lists, and a clearly labelled `$948` three-month fee example that excludes ad spend.
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
- The earlier remodel briefly included a public postal contact; the July 28 refinement removed it from the public site and retained email-only legal contact.

### Insights

- Preserved the nine existing educational articles.
- Removed obsolete package and legacy-service calls to action.
- Brand, website, and SEO articles now lead to Brand & Website Launch.
- AI articles remain educational but lead only to the current services overview or general inquiry; AI is not presented as a current package or primary service.
- Preserved article search and metadata.

## Visual system and responsive implementation

- Preserved the RielArt logo, blue palette, typography direction, light/dark theme, and core interaction patterns.
- Added a more restrained editorial/component system for offer cards, scope sections, service-inclusion lists, FAQ rows, contact choices, and process steps.
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

## July 29, 2026 — inline Contact-form success state

### Root cause

The Contact form already had a submit listener, but that listener only applied
the busy state and disabled the button. It did not prevent the form's native
navigation or submit with `fetch()`. JavaScript-enabled visitors therefore
followed Formspree's normal POST response to its generic thank-you page.

### Production implementation

- Kept the approved action `https://formspree.io/f/xojrdoel` and
  `method="post"` unchanged.
- Wrapped the existing guidance and form in one initial-state container.
- Added one initially hidden, focusable, polite live-region success card as
  its sibling inside the existing `.contact-form-panel`.
- Replaced only the Contact submit listener with `fetch(form.action)` using
  `FormData` and `Accept: application/json`.
- Preserved native validation, invalid-field handling, the sending
  announcement, `aria-busy`, the disabled button, and the duplicate-request
  guard.
- Reveals the success card only after `response.ok`; empty or malformed JSON
  on a successful HTTP response is handled safely.
- Resets the form only after success, restores its busy state, moves focus to
  the success card, and scrolls its beginning below the sticky header only
  when needed.
- On Formspree or network failure, preserves every entry, restores the
  original button, removes the busy state, focuses the existing accessible
  status region, and allows retry.
- Removed the source-controlled `_next` field. The existing `/thanks/` page
  was not modified.
- Advanced the Contact page's CSS and JavaScript cache keys only.

Public production files changed:

- `contact/index.html`
- `assets/js/site.js`
- `assets/css/site.css`

Testing and documentation files changed:

- `tools/site_audit.py`
- `RIELART-IMPLEMENTATION-LOG.md`
- `RIELART-QA-REPORT.md`
- `PRE-PUBLISH-RELEASE-REPORT.md`

No framework, package, dependency manifest, backend, analytics storage, or
unrelated public-page change was introduced.

### Progressive fallback owner action

Owner action required in Formspree: Set the form's Thank You redirect to
`https://rielart.com/thanks/` so non-JavaScript submissions also remain within
the RielArt website. Codex cannot configure the external Formspree dashboard.
