# RielArt Pre-Publish Release-Gate Report

**Audit date:** July 28, 2026  
**Target:** `https://rielart.com/` on GitHub Pages  
**Base commit audited:** `2cbd4cc7000ca9bf6a2790a534fe54247b07c66f`  
**Final disposition:** **CONDITIONAL PASS — READY AFTER LISTED CHECKS**

## 1. Final release disposition

The source candidate has no remaining automated P0 or P1 release defect after
the two narrow fixes documented in section 16 and the approved content-
consistency pass documented in section 18. Commercial integrity, local routes,
metadata, structured data, assets, form behavior, responsive layout, browser
console behavior, deployment exclusions, and exposed-file checks pass.

Publication remains conditional because legal/owner approvals, one authorized
production Formspree submission, real assistive-technology/200% zoom checks,
and Lighthouse metrics cannot be completed safely or fully from this
repository-only environment.

No speculative redesign, pricing change, offer change, navigation change, CTA
change, analytics addition, dependency addition, or integration change was
performed. The only public messaging changes are the explicitly approved 404
and Insights refinements documented in section 18.

## 2. Commands executed

### Required commands

1. `python -B tools/site_audit.py`
   - Attempted exactly as requested.
   - Result: did not run because `python` is not available on this machine's
     `PATH`.
2. `C:\Users\Gabriel\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe -B tools/site_audit.py`
   - Equivalent bundled Python execution.
   - Result before release fixes: pass.
   - Result after release fixes and artifact creation: pass.
3. `C:\Users\Gabriel\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe -m http.server 4173 --bind 127.0.0.1`
   - Local static server started successfully at
     `http://127.0.0.1:4173/`.
4. `C:\Users\Gabriel\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe -B tools/http_smoke.py --base-url http://127.0.0.1:4173/`
   - Result before release fixes: pass.
   - Result after release fixes: pass.
5. `node --check assets/js/site.js`
   - Result: pass; no output and exit code 0.
6. `git diff --check`
   - Result before release fixes: pass; no output and exit code 0.
   - Final result: pass; no whitespace errors. Git emitted only the
     repository's existing LF-to-CRLF working-copy advisories.

### Additional release checks

- `git ls-remote origin HEAD refs/heads/main`
- SHA-256 comparisons between live and local homepage, pricing, contact, CSS,
  and JavaScript files before the release-gate fixes.
- Live HTTP header and exposure probes with `curl.exe -sS -I`.
- Repository scans with `git ls-files`, `rg`, `Get-ChildItem`, and
  `Get-FileHash`.
- In-app browser tests for all 32 HTML routes, 36 responsive cases, contact
  behavior, themes, mobile navigation, focus restoration, validation
  announcements, broken images, clipped content, card alignment, touch
  controls, and console errors.

No real Formspree submission, payment, message, account change, or deployment
was performed.

## 3. Automated results

### Static audit

The pre-fix static audit completed with:

- HTML files checked: 32
- Indexable pages checked: 22
- Sitemap URLs checked: 22
- Sitemap `lastmod` values checked: 22
- Local and remote asset references checked: 216
- Images checked for alt text and dimensions: 52
- JSON-LD blocks checked: 32
- Forms checked: 1
- Orphan indexable pages: 0
- Approved visible price markers: 2/2
- Redirect rules checked: 14
- GitHub Pages exclusions checked: 27
- Internal artifact paths safely excluded: 20
- Public Stripe Payment Links: 0
- Global `Get Started` links checked: 60
- Custom-scope links checked: 1
- Approved 404 positioning statements checked: 2
- Insights editorial entries checked: 9
- Current shared CSS cache references checked: 24/24
- PostalAddress schemas: 0
- Organization address properties: 0
- Unsupported numerical claims: 0
- Warnings: 0
- Critical failures: 0

The final audit was rerun after all three release artifacts existed. It
reported 30 GitHub Pages exclusions, 23 safely excluded internal artifact
paths, zero warnings, zero critical failures, and a final **PASS**. The new
exclusion rules were therefore tested rather than assumed.

### Local HTTP smoke crawl

The final crawl completed with:

- Routes checked: 34
- Expected HTTP 200 routes: 33
- HTML routes: 31
- Expected missing-route HTTP 404: pass
- Aggregate HTML response bytes: 317,723
- HTML budget: no route above 61,440 bytes
- CSS: 80,143 / 83,968 bytes
- JavaScript: 15,551 / 20,480 bytes
- Image library: 643,390 / 665,600 bytes
- Logo: 8,587 / 10,240 bytes
- Failures: 0

Additional final checks:

- `node --check assets/js/site.js`: pass.
- `git diff --check`: pass with line-ending advisories only.
- `PRE-PUBLISH-BLOCKERS.json`: valid JSON.
- CSS cache references: 24 at `20260728r4`, 0 at `20260728r3`.
- Manifest public include lines: 48.

### Browser matrix

- 36 responsive cases:
  - four representative routes;
  - nine required viewports per route.
- Page-level horizontal overflow failures: 0
- Clipped-text failures: 0
- Broken-image failures: 0
- H1 failures: 0
- Controls below the 24-pixel minimum spot-check threshold: 0
- Side-by-side offer-card height/action alignment failures: 0
- Stacked-card natural-height failures: 0
- Browser console warning/error failures across all 32 HTML routes: 0

### Tool availability

- Lighthouse: unavailable; no Lighthouse scores were invented.
- axe-core: unavailable; no axe result was claimed.
- Browser performance timing APIs: not exposed by the controlled browser
  environment; no LCP, CLS, TBT, transfer-size, or request-count values were
  invented.
- Real 200% browser zoom, NVDA, VoiceOver, and Safari/iOS: unavailable.

## 4. Route results

### Canonical and sitemap routes

Every route below returned local HTTP 200, has one H1, one title, a meta
description, one canonical, valid robots behavior, valid JSON-LD where
applicable, working local assets, no broken internal link, no console error,
and correct sitemap parity:

- `/`
- `/about/`
- `/services/`
- `/services/brand-website-launch/`
- `/services/focused-ads-management/`
- `/pricing/`
- `/portfolio/`
- `/process/`
- `/contact/`
- `/faq/`
- `/blog/`
- `/blog/website-builder-vs-wordpress/`
- `/blog/ai-chatbot-small-business/`
- `/blog/brand-identity-mistakes/`
- `/blog/website-costing-you-leads/`
- `/blog/small-business-automation-ideas/`
- `/blog/local-seo-checklist-toronto/`
- `/blog/core-web-vitals-small-business/`
- `/blog/ai-chatbot-vs-live-chat/`
- `/blog/website-maintenance-checklist/`
- `/privacy-policy/`
- `/terms/`

### Utility routes

- `/thanks/`: HTTP 200, noindex as intended.
- `/404.html`: HTTP 200 when requested directly; the live host returns the
  same custom body with HTTP 404 for an unknown path.
- A generated missing route returned HTTP 404.

### Legacy compatibility routes

All compatibility files returned local HTTP 200 and then navigated once to the
intended current destination without a loop:

- `/privacy-policy.html` → `/privacy-policy/`
- `/terms.html` → `/terms/`
- `/packages/` → `/pricing/`
- `/services/brand-strategy-identity/` →
  `/services/brand-website-launch/`
- `/services/web-design-development/` →
  `/services/brand-website-launch/`
- `/services/digital-growth-management/` →
  `/services/focused-ads-management/`
- `/services/ai-automation-operations/` → `/services/`
- `/services/audits-advisory/` → `/services/`

GitHub Pages does not consume the repository's Netlify-style `_redirects`
file. The public compatibility HTML files are therefore the effective
GitHub Pages behavior. They are noindex, use direct canonical targets, and do
not chain back to a retired URL.

## 5. Deployment manifest result

`DEPLOYMENT-FILE-MANIFEST.txt` identifies exactly 48 public production files.
It separately lists every tracked internal report, audit JSON, tool,
configuration file, repository-control file, strategy document, QA file,
implementation log, and required release artifact that must not appear in the
generated site.

Host/build determination:

- `CNAME` contains `rielart.com`.
- The live `Server` header is `GitHub.com`.
- No `.nojekyll` file is present.
- GitHub Pages/Jekyll exclusion behavior is therefore applicable.
- The live host returned HTTP 404 for `.git`, `.env`, `README.md`, internal
  reports, `config`, `tools`, source maps, backup names, `_config.yml`,
  `_redirects`, and an image-directory request.
- The official Jekyll rules exclude dot-prefixed, underscore-prefixed,
  tilde-suffixed, and configured `exclude` paths.

The release-gate artifacts were added to `_config.yml` and to the static
audit's internal-artifact list. Their post-publication HTTP 404 checks remain
a manual deployment gate.

## 6. Commercial integrity result

**Pass.**

- Brand & Website Launch: `$599 USD one time`.
- Focused Ads Management: `$349 USD per month`.
- Three-month initial commitment: visible.
- Advertising spend separate: visible.
- Exactly two primary public services: confirmed.
- Custom support: separately reviewed inquiry, not a third package.
- AI automation: educational content only, not a primary service.
- Retired prices `$497`, `$247`, `$149`, `$249`, `$399`, and `$699`: absent
  from public source.
- Public Stripe checkout/subscription links: 0.
- `config/payment-links.json`: both values are `null` and the directory is
  excluded.
- Global CTA: `Get Started`.
- `Start Your Project`: absent.
- Service CTAs: `Start Your Launch` and `Start Advertising`.
- Founder-led or “RielArt is new” language: absent.
- Public street/mailing address: absent.
- PostalAddress or LocalBusiness schema: absent.
- Fake testimonials, client results, awards, partnerships, statistics, and
  guarantees: not found.
- Portfolio concepts are explicitly labelled as internal or representative,
  without unverified outcomes.

## 7. Contact-form result

**Local behavior passes; one authorized production submission remains open.**

- Exactly four main choices:
  - Brand & Website Launch
  - Focused Ads Management
  - Both services
  - I am not sure yet
- Query preselection passed for:
  - `brand-website-launch`
  - `focused-ads-management`
  - `both-services`
  - `not-sure`
  - `custom-scope`
- `custom-scope` selects “I am not sure yet” and preserves
  `Custom scope inquiry` in the dedicated hidden context field.
- Advertising fields appear only for Focused Ads Management and Both
  services.
- Advertising controls are disabled when hidden, preventing misleading hidden
  values from being submitted.
- Required-field validation prevented navigation, applied `aria-invalid` to
  10 empty required controls, and announced:
  `Please review the highlighted required fields.`
- Formspree endpoint remains
  `https://formspree.io/f/xojrdoel`.
- Thank-you destination remains
  `https://rielart.com/thanks/`.
- Privacy consent is required.
- The Formspree disclosure is visible.
- The `pageshow` handler restores the submit label, enabled state, busy state,
  and status after browser navigation; the production submission/back
  sequence remains part of the authorized production test.
- No real inquiry was sent.

### Exact owner instructions for one controlled production submission

1. Publish the reviewed release to the intended GitHub Pages source.
2. Open
   `https://rielart.com/contact/?service=focused-ads-management#project-inquiry`
   in a private browser window.
3. Confirm Focused Ads Management is selected and the three advertising
   fields are visible.
4. Use an owner-controlled email and obvious test values such as
   `RELEASE TEST — DELETE` in the business name and message. Do not enter real
   prospect or client data.
5. Complete every required field, select a harmless test advertising choice,
   accept the privacy consent, and submit exactly once.
6. Confirm navigation to `https://rielart.com/thanks/`.
7. Confirm the intended mailbox receives exactly one Formspree message with:
   the selected service, all visible advertising fields, consent value, and no
   stale disabled values.
8. Verify reply-to, spam handling, Formspree account owner, retention,
   deletion, rate-limit, and notification settings.
9. Use Back once and confirm the submission button is enabled and reads
   `Send My Inquiry`.
10. Delete or clearly archive the controlled test in Formspree and the mailbox.
11. Separately open the custom-scope URL without submitting and confirm its
   visible preselection/context remains correct.

## 8. Responsive result

The following viewports were tested on the homepage, Focused Ads Management,
pricing, and contact routes:

- 320 × 568
- 360 × 800
- 390 × 844
- 430 × 932
- 768 × 1024
- 1024 × 768
- 1280 × 720
- 1440 × 900
- 1920 × 1080

Verified:

- Homepage offer and platform cards
- Google and Meta cards
- Pricing cards
- Independent two-column service-inclusion lists
- Custom-scope section
- Contact introduction panel
- Four contact choice cards
- Conditional advertising fields
- Form controls and footer
- Mobile navigation
- Light and dark themes
- Side-by-side action alignment
- Natural card height after stacking
- No page-level horizontal overflow
- No clipped text
- No broken local image
- No undersized primary control in the automated spot check
- No filler content made accessible
- No empty Contact overlay or blank dark region

The former pricing comparison table was intentionally replaced by two semantic
article/list columns. There is no remaining horizontal table or table keyboard
interaction to test. At narrow widths the two inclusion columns stack without
horizontal scrolling.

## 9. Accessibility result

Automated and browser-supported checks passed for:

- one H1 per full page;
- heading-order warnings: 0;
- main, header, navigation, and footer landmarks;
- skip link presence;
- visible global `:focus-visible` outline;
- form labels, fieldsets, radio semantics, required states, and live status;
- image alternatives and explicit image dimensions;
- descriptive internal link purpose;
- mobile-menu Escape close, focus containment, and focus restoration;
- reduced-motion CSS for global animation/transition reduction and both orbit
  animation implementations;
- both colour themes;
- responsive reflow down to 320 pixels.

Confirmed P1 fixes:

- Light accent token changed from `#2468ee` to `#2162df` so small accent text
  meets 4.5:1 on the light soft surfaces where it is used.
- `.optional` now uses `var(--muted)`, producing
  `rgb(83, 103, 130)` on white in light mode and
  `rgb(170, 187, 208)` on the dark form surface.

Not available and therefore required manually:

- axe scan;
- true 200% browser zoom;
- NVDA;
- VoiceOver;
- Safari/iOS;
- a real touch device;
- full gradient-aware contrast verification with a production accessibility
  scanner.

## 10. Performance result

Lighthouse was not installed and adding a dependency was prohibited.
Controlled browser performance timing APIs were not exposed. Therefore:

- Performance score: unavailable
- Accessibility score: unavailable
- Best Practices score: unavailable
- SEO score: unavailable
- LCP: unavailable
- CLS: unavailable
- TBT/responsiveness proxy: unavailable
- Per-route transfer size: unavailable
- Per-route request count: unavailable

No values were invented.

Available static performance evidence:

- HTML: every route under the 61,440-byte budget.
- CSS: under the 83,968-byte budget.
- JavaScript: 15,551 bytes, under the 20,480-byte budget.
- Image library: 643,390 bytes, under the 665,600-byte budget.
- Logo: 8,587 bytes, under the 10,240-byte budget.
- Largest individual image: `images/og-website-leads.jpg`, 94,267 bytes.
- Every local image has explicit dimensions.
- One local stylesheet is render-blocking by design.
- One small inline theme initializer prevents theme flash.
- Main site JavaScript is local and deferred.
- Third-party script tags: 0.
- Source maps: 0.
- Mixed-content asset references: 0.
- CSS cache key advanced to `20260728r4`.
- JavaScript cache key remains `20260728r1` because JavaScript did not change.

Run Lighthouse mobile and desktop on the homepage, pricing, contact, Focused
Ads Management, and the largest article
`/blog/small-business-automation-ideas/` before marketing publication.

## 11. Security and hosting result

Live checks:

- HTTP → HTTPS: 301 pass.
- HTTPS: pass.
- HSTS: `max-age=31556952` pass.
- Mixed content in public source: none.
- Directory listing probe: HTTP 404.
- `.git` exposure: HTTP 404.
- `.env` exposure: HTTP 404.
- Internal Markdown/JSON exposure probes: HTTP 404.
- `config/payment-links.json`: HTTP 404.
- `tools/site_audit.py`: HTTP 404.
- Source-map probe: HTTP 404.
- Backup-file probe: HTTP 404.
- Custom missing-path response: HTTP 404 with the custom 404 body.
- Live homepage, pricing, contact, CSS, and JavaScript matched the local base
  commit by SHA-256 before this release-gate patch.
- Git remote `HEAD` and `main` both matched the audited base commit.

Headers not present on the GitHub Pages marketing host:

- Content-Security-Policy
- X-Content-Type-Options
- Referrer-Policy
- Permissions-Policy
- explicit frame protection

GitHub Pages exposes `Server: GitHub.com` and standard GitHub/Fastly cache
headers. These are hosting-platform characteristics. They are recorded as
non-blocking hosting follow-ups for this static site. No restrictive meta CSP
or other HTML workaround was added because it could break Formspree, Calendly,
the Client Portal, theme behavior, or future approved payment flows.

## 12. External integration checklist

| Integration | Source check | Read-only live check | Release status |
|---|---|---|---|
| Client Portal | Exact URL preserved | HTTP 200 | Owner/account verification required |
| Formspree | Exact endpoint preserved | HEAD returned expected non-POST HTTP 400; no submission sent | Controlled POST required |
| Thank-you page | Exact `_next` preserved | HTTP 200 | Verify after controlled submission |
| Calendly | Exact URL preserved | HTTP 200 | Owner/privacy/configuration review required |
| LinkedIn | Exact URL preserved | Automated probe received LinkedIn anti-bot HTTP 999 | Owner browser check required |
| Email | `mailto:hello@rielart.com` preserved | Not an HTTP endpoint | Owner mailbox check required |
| Stripe | No public link; internal values null | Not applicable | Configure only after approval |

## 13. Manual tasks required before publication

1. Owner and qualified counsel approve:
   - contracting identity;
   - required business disclosures;
   - Privacy Policy and Terms;
   - governing-law and target-market obligations;
   - the decision not to publish a street or mailing address.
2. Owner verifies Gabriel Macovei's name, photograph, biography, article
   attribution, LinkedIn destination, and every internal/representative-work
   label.
3. Complete the controlled production Formspree test in section 7.
4. Verify Calendly account ownership, disclosure, cookie behavior, and whether
   `hide_gdpr_banner=1` remains approved.
5. Verify Client Portal, mailbox, LinkedIn, Cloudflare, Resend, and recovery
   ownership.
6. Run real 200% zoom, keyboard-only, Safari/iOS, NVDA or VoiceOver, and touch
   checks.
7. Run Lighthouse mobile and desktop on the five routes listed in section 10.
8. After publication, verify CSS `20260728r4`, the custom 404 status, and HTTP
   404 for all three release-gate artifacts.

## 14. Manual tasks required before accepting payment or starting client work

1. Approve the Brand & Website Launch agreement:
   payment timing, tax, refund, cancellation, schedule triggers, page count,
   content, feedback, revisions, handoff, ownership, licensing, third-party
   costs, and change control.
2. Approve Focused Ads Management terms:
   first charge, three-month commitment, renewal, cancellation, pauses,
   failed payments, refunds, disputes, early termination, access removal,
   support, and out-of-scope approval.
3. Document Google and Meta client-owned account access, advertiser
   verification, billing, funding, recovery, and offboarding procedures.
4. Define the one-hour monthly website-edit allowance, measurement, reset,
   no-rollover rule, prioritization, backup, rollback, and additional-work
   approval.
5. Approve privacy roles, data-processing terms, retention, deletion, security,
   incident response, tracking consent, reporting, attribution, and advanced
   conversion restrictions.
6. Approve advertising claims, asset licences, client approvals, platform
   policies, sensitive/regulated industries, and international market review.
7. Configure a future Stripe flow only after agreements and payment,
   cancellation, refund, tax, receipt, success, and ownership decisions are
   approved.

## 15. Post-launch tasks

- Configure Google Search Console.
- Configure Bing Webmaster Tools.
- Add analytics only after explicit approval and required consent/policy work.
- Collect field Core Web Vitals.
- Measure real conversion quality.
- Add only verified case studies.
- Add testimonials only with permission.
- Review non-critical hosting headers when the hosting architecture permits.
- Replace compatibility-page redirects with server-level 301 responses if the
  deployment architecture later supports them.

## 16. Exact findings and changes

### P1-A11Y-CONTRAST-001 — fixed

- **Finding:** The light accent token was 4.38:1 on a soft light surface, and
  optional form text was 4.44:1 in light mode and 3.69:1 in dark mode.
- **Severity:** P1.
- **Evidence:** Browser-computed colours plus WCAG relative-luminance
  calculation.
- **File:** `assets/css/site.css`.
- **Modification:** `--blue` changed from `#2468ee` to `#2162df`;
  `.optional` changed from `#687991` to `var(--muted)`.
- **Related modification:** 24 full public HTML pages now reference
  `site.css?v=20260728r4`; the later content-consistency pass advanced the
  cache key after the Insights card styles changed.
- **Validation:** Computed colours confirmed in both themes; targeted 390-pixel
  homepage/contact checks retained no overflow.
- **Remaining risk:** Real device, gradient-aware scanner, and assistive
  technology checks remain manual.

### P1-DEPLOY-EXCLUSION-001 — fixed

- **Finding:** The three newly requested release-gate artifacts were not
  present in the existing Jekyll exclusions because they did not yet exist.
- **Severity:** P1.
- **Evidence:** Pre-change `_config.yml` and audit artifact-name list.
- **Files:** `_config.yml`, `tools/site_audit.py`.
- **Modification:** Added exact exclusions and audit recognition for:
  `PRE-PUBLISH-RELEASE-REPORT.md`, `PRE-PUBLISH-BLOCKERS.json`, and
  `DEPLOYMENT-FILE-MANIFEST.txt`.
- **Validation:** Final static audit runs with all artifacts present.
- **Remaining risk:** Confirm their live URLs return HTTP 404 after publication.

### Remaining automated blockers

None.

### Remaining manual gates

The exact manual publication gates are listed in section 13 and in
`PRE-PUBLISH-BLOCKERS.json`.

## 17. Scope confirmation

No speculative redesign was performed. Approved prices, service scopes,
navigation, CTA hierarchy, page structure, Formspree, Calendly, Client Portal,
privacy text, and commercial terms were not changed. The two confirmed P1
release defects were fixed, followed by the explicitly approved 404 and
Insights content-consistency refinements in section 18.

## 18. Content-consistency and Insights refinement

### Public outdated phrases changed

Only two outdated public commercial phrases were found:

1. `404.html`
   - Removed: “Review how brand, web, and AI work can be structured around
     practical business needs.”
   - Added: “Review how brand, website, and online advertising can be
     structured around practical business needs.”
2. `404.html`
   - Removed: “Learn more about services, process, pricing, ownership, support,
     AI, and the Client Portal.”
   - Added: “Learn more about services, process, pricing, ownership,
     advertising, and the Client Portal.”

The full public-source search classified the remaining AI/automation
occurrences as useful educational article content. No AI package, price,
navigation service, homepage pillar, contact choice, footer service, or
commercial Service schema remains.

### Insights decision and metadata

- Final title, Open Graph title, and Twitter title:
  `RielArt Insights | Brand, Websites, Advertising & Practical Technology`.
- Final meta, Open Graph, Twitter, and Blog schema description:
  `Practical insights from RielArt about business branding, websites, Google
  and Meta advertising, digital credibility, automation, and useful
  technology.`
- Social and Blog schema image:
  `https://rielart.com/images/og-website-leads.jpg`.
- Featured guide: **5 Signs Your Website Is Costing You Leads**.
- Featured URL: `/blog/website-costing-you-leads/`.
- Featured category: **Websites**.
- Featured image includes intrinsic dimensions, descriptive alt text, and an
  explicit accessible link label.
- No article publication or modification date changed.

The final editorial order is:

1. Website conversion — featured website-leads article
2. Brand credibility — brand-identity mistakes
3. Customer acquisition — local SEO checklist
4. Practical automation — automation ideas
5. Website platform choice
6. Website performance
7. Website maintenance
8. Practical AI chatbots
9. Practical AI versus live chat

Index filters are All, Brand, Websites, and Practical Technology. No empty
Advertising filter and no fabricated advertising article were added.

### Files modified

- `404.html`
- `blog/index.html`
- all nine existing `blog/*/index.html` article files
- `assets/css/site.css`
- `sitemap.xml`
- all 24 full public HTML pages for CSS cache key `20260728r4`
- `tools/site_audit.py`
- `PRE-PUBLISH-RELEASE-REPORT.md`
- `RIELART-QA-REPORT.md`
- `RIELART-IMPLEMENTATION-LOG.md`
- `RIELART-COPY-MAP.md`

No RSS or feed file exists, so no feed update was required.

### Validation

- Exact `python -B tools/site_audit.py`: attempted; `python` is unavailable on
  `PATH`.
- Bundled Python `tools/site_audit.py`: PASS with 32 HTML files, 22 indexable
  and sitemap URLs, 216 asset references, 52 images, 32 JSON-LD blocks, two
  approved 404 statements, nine Insights entries, zero warnings, and zero
  critical failures; all 24 shared CSS cache references were current.
- Local server and bundled Python HTTP smoke: PASS with 34 routes, 33 expected
  HTTP 200 responses, the intentional 404, 317,723 aggregate HTML bytes,
  80,143 CSS bytes, and zero failures.
- `node --check assets/js/site.js`: PASS.
- `git diff --check`: PASS with line-ending advisories only.
- Focused browser checks at 1440 × 900, 390 × 844, and 320 × 568: PASS for
  light/dark themes, featured image, filters, desktop card/action alignment,
  natural mobile stacking, mobile-menu focus and Escape close, broken images,
  clipping, and page-level overflow.
- Supporting AI article canonical route: PASS.
- Browser console warnings/errors: 0.

### Remaining manual decisions

The homepage FAQ was not shortened; future reduction is a post-traffic
optimization. The pre-existing owner/legal approvals, one authorized
production Formspree test, real 200% zoom, assistive technology, Safari/iOS,
Lighthouse, external-account verification, and post-publication artifact
exclusion probes remain required. These are the listed manual checks behind the
conditional disposition and are not new content-pass defects.

**The source is ready after the following manual checks.**
