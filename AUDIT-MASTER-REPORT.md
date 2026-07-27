# RielArt Production Website Audit — Master Report

**Audit date:** 2026-07-27  
**Repository baseline:** `3ebf603` (`main`, “Site Rebuilt”)  
**Production site:** <https://rielart.com/>  
**Local review origin:** `http://127.0.0.1:4173/`

> Audit integrity: this report and `AUDIT-FINDINGS.json` were created before the implementation pass. Results marked “Baseline” describe the unmodified `3ebf603` tree; final results describe the audited working tree after implementation and regression testing.

## Executive conclusion

The rebuilt site is ready for owner review as a credible, professional production candidate. It did not need another broad visual rewrite. The implementation instead removed the highest-value friction: project and free-review intent now remain distinct, the paid audit is clearly separated from the no-cost initial review, form errors are announced and recover correctly, contact typography uses intentional three-word lines, service and article paths are more specific, empty or inconsistent taxonomy was removed, and the most wasteful global image was reduced by more than 90%. Following owner visual review, the text-heavy homepage priority panel was also replaced with a decorative floating orbital mark, leaving the hero copy as the only message in that composition.

No confirmed P0 failure was found. The final static audit reports **0 critical failures and 0 warnings**, the local HTTP crawl reports **0 failures**, and the final browser matrix reports **0 failures across 100 route/viewport combinations**. All approved production integration values and all six Stripe prices/links remain unchanged.

The remaining work is deliberately outside a safe static-repository change: owner-controlled Formspree and Stripe checks, legal review, analytics/vendor approval, real Safari/iOS/Android/Firefox/Edge and screen-reader testing, and any hosting/CDN change needed for security headers or true server redirects. The site was not deployed during this audit.

## Pre-change executive baseline

At the recorded baseline, the rebuilt local site was a strong foundation and materially better than the production site visible on the audit date. It had clearer positioning, a readable three-line homepage proposition, an accessible interactive priority panel, a user-controlled animated capability marquee, more concise process cards, better contact typography, honest representative-work disclosures, international service wording, and the approved business mailing address. The no-framework architecture remains fast, portable, crawlable, and easy to deploy.

The baseline did **not** need another broad visual rewrite. Its most valuable remaining improvements were:

1. Preserve visitor intent between a project CTA and the contact form.
2. Separate the free preliminary offer from the paid Audits & Advisory service.
3. Make form validation state easier to understand with assistive technology.
4. Reduce avoidable image weight and defer genuinely below-the-fold photos.
5. Remove an empty blog filter and correct a small number of terminology inconsistencies.
6. Refresh sitemap modification dates for pages materially changed in the rebuild.
7. Document account-, policy-, proof-, analytics-, payment-, and hosting-level decisions that cannot be resolved safely in static files.

No confirmed P0 failure was found. Payment checkout, production form delivery, legal adequacy, account settings, real-device/browser coverage, and hosting response headers were identified as manual or external checks.

## Scope and method

The audit covers business positioning, copy, trust, conversion, service architecture, pricing, technical and content SEO, structured data, accessibility, performance, security, privacy, measurement, responsive behavior, browser compatibility, and maintainability.

The work sequence is:

1. Repository inventory and Git-state capture.
2. Existing static audit.
3. Local HTTP server and internal crawl.
4. Selective production comparison.
5. Pre-change baseline documentation.
6. High-confidence implementation.
7. Static, HTTP, interaction, responsive, and performance regression checks.
8. Final evidence and manual-review handoff.

The audit does not submit production forms, complete Stripe purchases, create analytics accounts, change third-party account settings, or invent business proof.

## Baseline inventory

| Item | Baseline |
|---|---:|
| HTML files | 30 |
| Indexable HTML routes | 25 |
| Sitemap URLs | 25 |
| Non-indexable legacy/utility routes | 3 |
| Stylesheets | 1 |
| JavaScript files | 1 |
| Python audit scripts | 1 |
| Repository files excluding `.git` | 58 |
| Repository payload in baseline commit | 1,317,910 bytes |
| CSS payload | 60,906 bytes |
| JavaScript payload | 13,286 bytes |
| Image payload | 727,177 bytes |

Important production integrations found in the source:

- Client Portal: `https://portal.rielart.com`
- Formspree: `https://formspree.io/f/xojrdoel`
- Form success route: `https://rielart.com/thanks/`
- Calendly: `https://calendly.com/gabrielmacovei001/15min?hide_gdpr_banner=1`
- Email: `hello@rielart.com`
- LinkedIn: `https://www.linkedin.com/in/gabrielmacovei/`
- Six approved Stripe payment links

These values are treated as invariants and will be compared after implementation.

## Baseline automated results

### Existing static audit

`python tools/site_audit.py`

- 30 HTML documents parsed.
- 25 indexable pages and 25 sitemap URLs.
- No missing internal files, assets, or fragments.
- No missing required canonical, title, description, or H1 on indexable pages.
- No duplicate canonical URLs or titles.
- No image-alt, duplicate-ID, or unsafe `target="_blank"` findings.
- All six expected Stripe links found.
- No placeholder, local-development URL, lorem ipsum, or competitor-token warnings.
- Exit status: **0**.

### Local HTTP crawl

- 31 resources reviewed: all sitemap pages, `404.html`, the three legacy/utility routes, `robots.txt`, and `sitemap.xml`.
- All returned HTTP 200 from the local static server.
- All indexable HTML pages had one H1.
- Total crawled response payload: **437,078 bytes**.
- No broken local route or missing local image was found.

### Production comparison

- All 25 sitemap URLs returned HTTP 200.
- All 25 declared a matching canonical URL.
- All 25 had one H1.
- Total production HTML across those URLs: **448,898 bytes**.
- The local candidate is approximately **2.6% lighter in HTML** overall and substantially leaner on several primary commercial pages.
- HTTP redirects work from HTTP to HTTPS and from `www` to the apex domain.
- Unknown production URLs return a 404.
- GitHub Pages serves HSTS, but the checked responses did not include CSP, `X-Content-Type-Options`, `Referrer-Policy`, `Permissions-Policy`, frame protection, or cross-origin isolation headers.
- The legacy `privacy-policy.html`, `terms.html`, and `/packages/` paths return 200 documents containing noindex/canonical/redirect behavior because GitHub Pages does not apply the repository’s Netlify-style `_redirects` file.

## What is already strong

### Positioning and conversion

- The homepage explains the integrated offer within the first screen.
- The new headline avoids the awkward one- or two-word line wrapping of the previous version.
- Visitors can choose a project inquiry or a no-cost preliminary route.
- Primary and secondary calls to action are visible at logical decision points.
- Pricing is public, denominated in USD, and separates fixed work, custom work, and recurring support.
- Contact information, the Client Portal, Calendly, LinkedIn, and the mailing address are easy to find.

### Trust and honesty

- Representative solution models are explicitly labelled as illustrative, not client case studies.
- The website does not use fabricated testimonials, client logos, awards, statistics, scarcity, or guarantees.
- The mailing address is labelled as a business mailing address rather than an office.
- International service language avoids misleading local-office claims.
- Process, ownership, documentation, handoff, dependencies, limitations, and third-party costs receive meaningful coverage.

### UX and accessibility

- There is a skip link and consistent landmark structure.
- The mobile menu has an accessible name, focus management, focus containment, Escape support, and focus restoration.
- At the recorded baseline, the homepage priority interface used a tab pattern with arrow, Home, and End support.
- FAQ buttons expose state and controlled regions.
- At the recorded baseline, the capability marquee had a Pause/Resume control and respected reduced-motion preferences.
- Form controls have explicit labels, required-state instructions, autocomplete attributes, consent wording, and a live submission-status region.
- Light and dark themes are first-class and persist locally without blocking operation if storage fails.

### SEO and structured data

- Indexable pages have titles, descriptions, canonical URLs, Open Graph metadata, Twitter metadata, and a meaningful H1.
- Sitemap and indexable-page coverage match.
- Utility and legacy documents are excluded from the sitemap and set to noindex.
- Organization, WebSite, Service, Article, BreadcrumbList, FAQPage, and Person data are present where supported by visible content.
- The address is represented as a mailing address under Organization rather than an unsupported LocalBusiness claim.

### Performance and maintainability

- The website has one dependency-free CSS file and one small deferred JavaScript file.
- No framework, external font request, embedded video, autoplay media, or unnecessary third-party runtime is present.
- Most content images use efficient modern formats and explicit dimensions.
- JavaScript is progressively defensive and avoids placing secrets in the client.

## Prioritized baseline findings

The machine-readable source of record is `AUDIT-FINDINGS.json`.

### P0 Critical

No confirmed P0 was found in the static source or read-only production checks. The Stripe acceptance flow and Formspree delivery must still be verified manually before they can be cleared.

### P1 High

- **CONV-001:** “Start a Project” routes to a form preselected as a free email audit, creating an avoidable intent mismatch.
- **OFFER-001:** Free-offer naming overlaps with the paid Audits & Advisory service, especially on the paid audit page.
- **PRICE-001:** Direct Stripe checkout cannot be fully approved from static HTML; scope boundaries, agreement acceptance, product configuration, and post-payment intake need owner/account verification.

### P2 Medium

- **A11Y-001:** Native form validation is present, but invalid-state changes are not announced in the existing live region.
- **PERF-001:** The 512×512 logo is much larger than its 30–34 px rendered size.
- **SEO-001:** Rebuilt commercial pages still use 2026-07-26 sitemap modification dates.
- **SEO-002:** Three legacy routes return 200 redirect documents on GitHub Pages instead of server redirects.
- **SEC-001:** Several defense-in-depth response headers cannot be configured in the current GitHub Pages repository.
- **PRIV-001:** The privacy policy describes major processors but does not name optional Calendly scheduling.
- **CONTENT-001:** The blog offers an Advertising filter with no matching article.
- **CONTENT-004:** Article pages rely on schema for authorship and do not consistently provide a visible byline plus a topic-specific service path.
- **CONTENT-005:** Buyer-facing copy overuses “practical,” “constraint,” and “useful next step,” weakening an otherwise specific professional tone.
- **SERVICE-001:** Several service pages describe dependencies but do not state what controls timing as directly as the web service page.
- **SCHEMA-001:** Article taxonomy is not fully aligned between visible blog categories and Article JSON-LD.
- **MAINT-001:** A Python bytecode cache is tracked and therefore deployable.
- **MAINT-002:** Audit reports and development tooling are not explicitly excluded from the GitHub Pages build, and important release checks are not yet consolidated into one repeatable audit.

### P3 Low

- **PERF-002:** Two below-the-fold About photos load eagerly.
- **CONTENT-002:** “Business result” is better expressed as “Intended outcome.”
- **CONTENT-003:** “Work email” is unnecessarily restrictive for solo operators.
- **SEO-003:** The homepage Twitter description and process-page title can better reflect the rebuilt content.

### Manual Review

- **TRUST-001:** The Work page is honest but has no approved client proof; decide whether to rename it “Solution Examples” until a real case study is available.
- **TRUST-002:** Confirm Daniel Patel’s displayed identity, role, image permission, and relationship wording.
- **LEGAL-001:** Review the Terms and Privacy Policy against Stripe, cancellation, recurring billing, refund, AI, advertising, international processing, and governing-law practices.
- **ANALYTICS-001:** No analytics platform is present; approve a privacy-aware measurement approach before implementation.
- **ACCOUNT-001:** Verify Formspree delivery/spam handling and every Stripe product/account setting without generating unwanted transactions or messages.
- **COMPAT-001:** Safari, iOS Safari, Android Chrome, assistive-technology, and real-device checks require appropriate environments.

## Terminology dictionary

| Concept | Preferred term |
|---|---|
| Company | A Canadian digital studio working with businesses internationally |
| Primary commercial audience | Growing businesses |
| Editorial audience | Small businesses, when the topic genuinely applies |
| Brand offer | Brand Strategy & Identity |
| Brand strategy | Positioning, audience, offer, message, and decision framework |
| Visual identity | Logo, colour, typography, imagery, and practical identity rules |
| Website offer | Web Design & Development |
| Website design | Information structure, content hierarchy, interface, and responsive experience |
| Website development | Production implementation, forms, metadata, integrations, testing, and deployment |
| AI offer | AI Automation & Operations |
| AI systems | Approved-knowledge assistants, search, classification, or decision support with defined limits |
| Automation | A repeatable workflow that reduces manual routing, follow-up, reporting, or handoff work |
| Integrations | Controlled connections between forms, CRM, email, data, reporting, or operating tools |
| Growth offer | Digital Growth & Ongoing Management |
| Digital growth | Ongoing website, SEO, analytics, advertising, and conversion improvement |
| Advertising management | Campaign planning, implementation, monitoring, and reporting; media spend is separate |
| Paid diagnosis | Audits & Advisory / In-depth Audit |
| Audit | A scoped evidence review that identifies findings, priorities, risks, and recommendations |
| Advisory | Decision support based on the approved evidence, constraints, and business goal |
| Preliminary no-cost route | Free Initial Review, described as a brief initial review delivered by email |
| Primary conversion | Start a Project / Project inquiry |
| Project | A written scope with defined deliverables, responsibilities, milestones, and approval points |
| Ongoing support | A defined monthly allowance for maintenance, monitoring, or prioritized improvement |
| Engagement models | Focused project / Connected project / Monthly support |
| Process | Assess / Define / Build / Validate / Launch & Improve |
| Outcome label | Intended outcome |
| Portal | RielArt Client Portal, then Client Portal |
| Location | Working with businesses internationally |
| Address | Business mailing address |
| Currency | USD / All prices are in USD |
| Blog taxonomy | Brand / Web & UX / AI & Automation / SEO & Analytics / Operations |

Avoid overusing “connected,” “constraint,” “practical,” “useful next step,” “ownership,” and “handoff.” Use them only where they add concrete meaning.

## Page-to-intent map

| Route | Purpose | Intended audience | Search intent | Primary topic | Supporting topics | Conversion | Parent / related | Cannibalization or content gap |
|---|---|---|---|---|---|---|---|---|
| `/` | Integrated commercial overview | Growing business evaluating a digital partner | Navigational / commercial | Connected brand, web, and AI support | Trust, process, representative models, pricing paths | Project inquiry or Free Initial Review | Root; all services, Work, Process, Pricing | Keep as overview; do not duplicate each service page |
| `/services/` | Compare five offers | Buyer choosing a starting point | Commercial investigation | RielArt digital services | Problems, deliverables, fit, connected engagements | Open best-fit service or inquire | Home; five service children | Maintain distinct service boundaries |
| `/services/brand-strategy-identity/` | Explain the brand offer | Business with unclear positioning or inconsistent identity | Commercial | Brand strategy and visual identity | Positioning, messaging, identity system, handoff | Discuss a brand project | Services; Web, Audits | Avoid competing with broad homepage brand copy; future proof gap |
| `/services/web-design-development/` | Explain the website offer | Business needing a clearer, more effective website | Commercial | Website strategy, design, and development | UX, content structure, responsive build, SEO foundations | Discuss a website project | Services; Growth, Audits | Distinguish project build from monthly maintenance |
| `/services/ai-automation-operations/` | Explain practical automation | Team repeating manual work or using fragmented tools | Commercial | AI systems and workflow automation | Intake, routing, knowledge, integrations, safeguards | Discuss an automation project | Services; Audits, Growth | Avoid generic AI claims; more approved implementation proof needed |
| `/services/digital-growth-management/` | Explain ongoing support | Business needing maintenance, analytics, SEO, ads, or iteration | Commercial | Digital growth and ongoing management | Website care, reporting, advertising, automation monitoring | Discuss monthly support | Services; Web, AI, Pricing | Keep management fee separate from ad spend and project work |
| `/services/audits-advisory/` | Explain paid diagnosis | Decision-maker needing evidence before committing | Commercial | In-depth audits and advisory | Priorities, evidence, roadmap, risk, decision support | Discuss an In-Depth Audit | Services; every execution service | Must remain visibly distinct from Free Initial Review |
| `/pricing/` | Compare engagement and checkout options | Buyer assessing fit and budget | Transactional | RielArt pricing in USD | One-time/recurring, scope, third-party costs, intake | Inquire or use approved Stripe link | Home; Services, Terms, Contact | Account/policy verification remains; package-boundary detail is an owner gap |
| `/portfolio/` | Show representative solution thinking | Buyer seeking examples | Commercial investigation | Representative solution models | Brand/web, web/growth, AI/operations, connected system | Start a related project | Home; Services | “Work” can imply case studies; no approved real proof yet |
| `/process/` | Reduce delivery uncertainty | Buyer evaluating project management | Commercial investigation | Five-phase delivery process | Decisions, validation, ownership, portal, launch | Start a Project | Home; Services, About | Keep detailed activities here rather than repeating long process copy |
| `/about/` | Verify entity and people | Buyer checking accountability and reach | Navigational / commercial | RielArt studio and responsible people | International work, approach, mailing address, Client Portal | Contact RielArt | Home; Process, Contact | Daniel role/photo and public address need owner confirmation |
| `/faq/` | Resolve purchase objections | Buyer seeking operational answers | Informational / commercial | RielArt service and engagement FAQ | Scope, timing, ownership, AI, pricing, support | Choose service or contact | Home; Services, Pricing, Terms | Answers must remain synchronized with policy/account decisions |
| `/contact/` | Capture a qualified inquiry | Visitor ready to describe a need | Transactional / navigational | Project inquiry or Free Initial Review | Need, desired outcome, timing, budget, privacy | Submit one appropriate form path | Sitewide CTA destination | Preserve intent; production delivery remains unverified |
| `/blog/` | Organize editorial discovery | Research-stage small/growing business | Informational | RielArt Insights | Brand, Web & UX, AI, SEO, Operations | Read article, then visit relevant service | Home; nine article children | Publishing cadence and future gaps should follow real buyer questions |
| `/blog/ai-chatbot-small-business/` | Explain practical chatbot use | Small business considering support automation | Informational | AI chatbot for small business | Use cases, limits, data, implementation | AI service or Free Initial Review | Blog; AI service | Overlaps chatbot comparison article; keep this page implementation-focused |
| `/blog/ai-chatbot-vs-live-chat/` | Compare two support models | Buyer choosing customer-support tooling | Comparative informational | AI chatbot versus live chat | Coverage, escalation, cost, customer experience | AI service or Free Initial Review | Blog; AI service | Keep comparison distinct from general chatbot guide |
| `/blog/brand-identity-mistakes/` | Diagnose brand inconsistency | Business owner questioning current brand | Informational | Brand identity mistakes | Positioning, consistency, usability, governance | Brand service or Free Initial Review | Blog; Brand service | Future examples need approved visuals/proof |
| `/blog/core-web-vitals-small-business/` | Explain performance signals | Business owner evaluating website speed | Informational | Core Web Vitals for small business | LCP, INP, CLS, measurement, business relevance | Web service or Free Initial Review | Blog; Web/Growth services | Keep current with Google definitions and field-data changes |
| `/blog/local-seo-checklist-toronto/` | Provide local-search checklist | Toronto-area service business researching visibility | Local informational | Local SEO checklist for Toronto | Google Business Profile, pages, reviews, citations, measurement | Growth service or Free Initial Review | Blog; Growth service | Avoid implying a Toronto office or creating doorway-city pages |
| `/blog/small-business-automation-ideas/` | Generate useful workflow ideas | Small business team identifying repetitive work | Informational | Small-business automation ideas | Intake, follow-up, reporting, knowledge, integrations | AI service or Free Initial Review | Blog; AI service | Add depth through concrete decision criteria, not a longer generic list |
| `/blog/website-builder-vs-wordpress/` | Compare platform choices | Buyer planning a website | Comparative informational | Website builder versus WordPress | Ownership, maintenance, flexibility, cost, fit | Web service or Free Initial Review | Blog; Web service | Revalidate product facts as platforms change |
| `/blog/website-costing-you-leads/` | Diagnose conversion leakage | Business with traffic but weak inquiries | Informational / commercial | Website problems that reduce leads | Clarity, trust, UX, forms, performance | Web service or Free Initial Review | Blog; Web/Audit services | Closest commercial overlap with Web service; keep article diagnostic |
| `/blog/website-maintenance-checklist/` | Provide recurring operating checklist | Site owner responsible for upkeep | Informational | Monthly website maintenance | Backups, updates, forms, analytics, security, accessibility | Growth service or Free Initial Review | Blog; Growth service | Keep distinct from the Growth service by remaining a self-service checklist |
| `/privacy-policy/` | Explain data handling | Visitor/customer reviewing privacy | Navigational / legal informational | RielArt privacy practices | Forms, providers, scheduling, storage, rights | Understand practices or contact | Footer; Contact, Terms | Owner/counsel must confirm legal adequacy and processors |
| `/terms/` | Explain commercial terms | Buyer reviewing purchase conditions | Navigational / legal informational | RielArt terms of use/service | Billing, third parties, IP, liability, governing terms | Understand terms or contact | Footer; Pricing, Privacy | Must match Stripe/account agreements and actual operations |

### Recommended editorial roadmap

Create new content only when RielArt can add first-hand operational detail, diagrams, screenshots, or a genuinely useful decision framework. The strongest current gaps are:

1. **What to prepare before a website redesign** — content, access, integrations, approvals, analytics, and decision ownership.
2. **AI workflow readiness checklist for a small service business** — process stability, data quality, escalation, privacy, and human review.
3. **Website inquiry-path audit** — how to review navigation, offer clarity, forms, follow-up, and measurement without promising conversion gains.
4. **Advertising management fee versus media spend** — responsibilities, assets, tracking, platform costs, and realistic limitations.
5. **How to choose between a focused project, connected project, and monthly support** — a buyer-facing decision guide linked to Pricing.

Do not publish city-variant pages, generic “top tools” lists, or multiple near-duplicate AI articles merely to increase volume.

## Decision log

- Preserve the rebuilt visual system, light/dark modes, logo, typography, Client Portal treatment, and static architecture.
- Following owner review, replace the text-heavy homepage priority panel with a text-free decorative animation. Remove the visible marquee button, make the capability loop continuous and seamless, and retain a static reduced-motion presentation.
- Do not invent testimonials, case studies, results, offices, partnerships, guarantees, or staff claims.
- Do not change prices, Stripe links, Formspree, Thank-you, Calendly, email, LinkedIn, or Client Portal values during this pass.
- Do not install analytics without explicit owner approval.
- Do not add an enforcing CSP in page markup. The site uses inline theme bootstrap code and inline styles, and a safe policy needs hosting-level reporting and staged validation.
- Do not submit production forms or payments as part of automated QA.
- Preserve legacy URL documents while GitHub Pages cannot apply `_redirects`; removing them would create broken inbound URLs.

## Performance budget for regression testing

| Budget | Threshold | Enforcement |
|---|---:|---|
| Raw HTML per ordinary page | 60 KiB | `tools/http_smoke.py` |
| Raw CSS total | 65 KiB | `tools/http_smoke.py` |
| Raw JavaScript total | 20 KiB | `tools/http_smoke.py` |
| Total local image library | 650 KiB | `tools/http_smoke.py` |
| Global logo | 10 KiB | `tools/http_smoke.py` |
| Representative primary initial route | 150 KiB / 5 core requests | Regression measurement |
| About after lazy team photos | 250 KiB / 7 requests | Regression measurement |
| Broken internal URLs | 0 | Static audit + HTTP crawl |
| Missing local assets | 0 | Static audit |
| Indexable pages with missing/duplicate title, description, canonical, or H1 | 0 | Static audit |
| Invalid JSON-LD documents | 0 | Static audit |
| Horizontal overflow at required viewport widths | 0 | Browser matrix |
| Console errors during representative interactions | 0 | Browser console review |

Lab-performance and accessibility scores will be recorded after the available tooling is confirmed. Field INP and real-user Core Web Vitals cannot be established from a repository audit alone.

## Final implementation outcome

### Business, content, and conversion

- All “Start a Project” paths now carry `inquiry=project`; free-review paths carry `inquiry=review`; `/contact/` defaults to Project inquiry.
- “Free Initial Review” is the single preliminary-offer name. The paid service uses Audits & Advisory / In-depth Audit and a distinct discussion CTA.
- Pricing now tells uncertain buyers to confirm scope before ordering and explains the post-checkout intake/access dependency without changing any price or checkout link.
- The global growth-service name is “Digital Growth & Ongoing Management.”
- Service timing statements now identify scope, access, content, decisions, integrations, media, and third-party dependencies without inventing delivery promises.
- Blog taxonomy has no empty Advertising filter. Article schema uses the visible five-category taxonomy, bylines connect to Gabriel’s About profile, and each article offers its relevant service plus the Free Initial Review.
- The former hero “Business result” panel was removed in favor of a decorative, text-free animation; required email fields use “Email.”
- A restrained buyer-facing tone pass made 51 exact edits across 11 pages, reducing generic repetition of “practical,” “constraint,” and “useful next step” while retaining “Practical AI” where it names the established offer.
- The homepage and contact conversion sections use a deliberate two-line heading with three words on each line: “Share what needs / to work better.”

### UX and accessibility

- Invalid required controls receive `aria-invalid="true"` and the existing live region announces one concise review message.
- Invalid state and the announcement clear as controls become valid, including radio groups.
- Query-driven form selection is progressive and leaves the native Formspree submission path unchanged.
- Existing skip-link, mobile-menu focus containment, Escape/focus restoration, FAQ state, and theme support were preserved. The hero visual is decorative and hidden from assistive technology. The capability ticker has no visible Pause button, runs as a continuous loop, exposes only one semantic copy of the list, and becomes static under reduced-motion preferences.

### SEO, privacy, performance, and maintainability

- Materially changed non-article sitemap dates now use `2026-07-27`; unchanged editorial publication/modification dates remain intact.
- The privacy policy factually names optional Calendly scheduling and third-party storage/cookie behavior; legal adequacy remains for owner/counsel review.
- The global logo changed from 512×512 / 92,374 bytes to 128×128 / 8,587 bytes after visual inspection, a **90.71% reduction**.
- Two below-the-fold About photos now use lazy loading and asynchronous decoding.
- Versioned CSS and JavaScript URLs ensure this release is not hidden behind an older browser cache.
- Tracked Python bytecode was removed and future cache files are ignored.
- `_config.yml` excludes audit reports, source documentation, and tools from the GitHub Pages build.
- `tools/site_audit.py` now checks local assets referenced by HTML, Open Graph, Twitter, and schema; JSON-LD; metadata parity; forms; sitemap dates; redirects; representative-work disclosure; legal dates; deploy artifacts; and GitHub Pages exclusions.
- `tools/http_smoke.py` provides a reusable dependency-free local HTTP crawl.

## Final validation summary

| Check | Final result |
|---|---:|
| Static HTML files / indexable pages / sitemap URLs | 30 / 25 / 25 |
| Sitemap lastmod values | 25 valid |
| Asset references | 242 checked |
| Images checked for alt behavior and dimensions | 59 |
| JSON-LD blocks | 35 valid |
| Forms / redirect rules | 2 / 4 |
| GitHub Pages exclusions / covered internal artifacts | 17 / 17 |
| Approved Stripe links | 6 of 6 |
| Static warnings / critical failures | 0 / 0 |
| HTTP routes / expected HTTP 200 / HTML routes | 32 / 31 / 29 |
| HTTP crawl failures | 0 |
| Responsive checks | 100 |
| Overflow / broken-image / H1 / breakpoint / viewport failures | 0 / 0 / 0 / 0 / 0 |
| Browser console errors / warnings | 0 / 0 |

The browser matrix covered 320×568, 360×800, 390×844, 430×932, 768×1024, 1024×768, 1280×720, 1440×900, 1920×1080, and 2560×1080 across the homepage, Services, Web Design detail, Pricing, Work, Process, Contact, Insights, a large article, and the custom 404 page.

Interaction regression checks confirmed:

- Project, review, and default inquiry selection.
- Empty-submit focus on the first invalid field, five programmatically marked invalid controls, and the live announcement.
- Complete clearing of invalid state after locally entering valid test values; no form was submitted.
- Mobile menu backward/forward focus wrap, Escape closure, and focus restoration.
- The homepage hero remains exactly three deliberate four-word lines at 1440 px. Its replacement visual contains no rendered text or panel background; the orbit, satellite, core-pulse, and ticker transforms all changed during timed observation.
- The visible marquee button is absent. Four synchronized list copies maintain full coverage through the loop, all three measured copy boundaries have a 0 px gap, and the animation remained `running` with an `infinite` iteration count after more than one complete cycle. Reduced-motion still presents one static semantic list. FAQ single-open behavior, final blog filters, linked Gabriel byline, relevant article CTAs, and matching Article taxonomy also passed.
- The revised contact heading remains two intentional lines at desktop, 390 px, and 320 px with no horizontal overflow.

JavaScript syntax and `git diff --check` passed. The latter reported only the repository’s expected Windows LF-to-CRLF notices.

## Final payload comparison

| Asset group | Baseline | Final | Change |
|---|---:|---:|---:|
| Public source payload | 1,245,018 B | 1,165,235 B | −79,783 B (−6.41%) |
| HTML | 439,611 B | 442,612 B | +3,001 B |
| CSS | 60,906 B | 61,174 B | +268 B |
| JavaScript | 13,286 B | 14,012 B | +726 B |
| Images | 727,177 B | 643,390 B | −83,787 B |
| Logo | 92,374 B | 8,587 B | −83,787 B (−90.71%) |

Conservative uncompressed local initial payloads are 129,471 bytes for Home, 108,310 for Process, 110,834 for Contact, 105,711 for Work, and 114,573 for Pricing, each in five core requests. About is 110,267 bytes initially and 236,167 bytes after its two lazy images load. These are raw local-file comparisons, not compressed production transfer sizes.

Lighthouse, axe, and a standards-conformance HTML validator were not installed in the available environment, so no score, violation count, or formal conformance result is fabricated. Every HTML document was still parsed by the repository audit and subjected to its structural, metadata, schema, and link invariants. Field Core Web Vitals, INP, real-device timing, and production cache/compression behavior also require deployed or field tooling.

## Remaining owner and external review

1. Run an owner-authorized Formspree test and verify inbox routing, spam handling, reply workflow, and `/thanks/`.
2. Review all six Stripe products without completing an unintended purchase; confirm price/mode, scope, taxes, agreement acceptance, recurring cancellation, refund alignment, receipts, and post-payment intake.
3. Obtain legal review of Terms and Privacy against actual Canadian/international operations and third-party settings.
4. Confirm Daniel Patel’s identity, current role, relationship wording, photo permission, and consent.
5. Decide whether “Work” should remain the navigation label until an approved attributable case study is available.
6. Approve an analytics and consent approach before adding measurement code.
7. Test current Safari, iOS Safari, Android Chrome, Firefox, Edge, and at least one screen reader.
8. If stronger headers or true 301 legacy redirects are required, place a configurable CDN/edge layer in front of GitHub Pages and stage CSP in report-only mode.

## Deliverables

- `AUDIT-MASTER-REPORT.md` — audit conclusion, baseline, scope, decisions, implementation, results, and outstanding work.
- `AUDIT-FINDINGS.json` — structured finding register with final implementation status and remaining risk.
- `AUDIT-IMPLEMENTATION-LOG.md` — file-by-file change and validation record.
- `AUDIT-MANUAL-REVIEW.md` — owner, account, legal, compatibility, and hosting review scripts.
- `AUDIT-MEASUREMENT-PLAN.md` — event, funnel, privacy, KPI, and performance-budget plan.
- `AUDIT-REGRESSION-REPORT.md` — final static, HTTP, browser, interaction, and payload evidence.
