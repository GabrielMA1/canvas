# RielArt Audit — Manual Review Register

**Prepared:** 2026-07-27  
**Scope:** Decisions or tests that cannot be completed safely from the static repository alone.

This document is a technical and operational handoff, not legal advice. No production form was submitted, no payment was completed, no analytics account was changed, and no third-party account setting was inferred from a public link.

## Release-blocking owner checks

### 1. Stripe checkout and agreement acceptance

**Priority:** Manual P0 before promoting checkout links

The repository still contains the same six approved Stripe URLs and the same visible prices. An authorized owner should open each checkout without completing a real charge and verify:

- Product name matches the pricing card.
- Amount, USD currency, one-time/monthly cadence, and tax treatment are correct.
- Subscription renewal, cancellation, and refund wording match the accepted agreement and Terms.
- The buyer must accept the applicable proposal/service agreement before a charge, or the checkout language clearly establishes the governing terms.
- Advertising spend is separate from the management fee.
- Third-party software, hosting, domain, API, usage, premium-asset, and platform costs are handled as described.
- The success/cancel destinations are correct.
- The post-payment intake, notification, and Client Portal onboarding reach the right people.
- Test-mode traffic cannot be confused with a real order.

The pricing page now tells visitors to contact RielArt before ordering when page count, platform, integrations, content, access, or timing is unclear. That safeguard does not replace account-level verification or a complete scope.

### 2. Formspree delivery and abuse controls

**Priority:** Manual P0 before launch

Run one clearly labelled, owner-authorized test through each visible form and verify:

- The exact expected mailbox receives the message.
- The `inquiry_type`, name, email, company, website, primary need, message, timeline, budget, and consent fields arrive correctly.
- Project and free-review submissions can be distinguished.
- The Thank-you route appears after success.
- Duplicate clicks do not generate duplicate messages.
- Spam/honeypot behavior and Formspree rate limits are appropriate.
- Reply-to and notification routing do not expose or misroute personal data.
- Failed submissions have an account-level recovery/monitoring path.
- Test records are removed or labelled according to the retention practice.

Automated QA intentionally stopped at native client-side validation and did not send production spam.

## Business and credibility decisions

### 3. Approved proof

The representative work is disclosed as illustrative, not client work. The remaining credibility gap is the absence of an approved, attributable case study, testimonial, or outcome.

Owner decision:

- Keep the current **Work** label with the visible disclosure; or
- Rename it **Solution Examples** until real proof is approved.

If proof is added, obtain written permission for the client name, logo, quote, screenshots, scope, and every result. Do not use anonymous testimonials, unsupported statistics, or work performed for an employer as though it were a RielArt client engagement.

### 4. People information and image rights

Confirm Daniel Patel’s:

- Identity and current relationship to RielArt.
- “Web and AI Partner” title.
- Description of his support across selected projects.
- Permission to use the displayed name and image.
- Image licence/source and accessibility description.

Also confirm that Gabriel’s displayed role, profile links, photo, and Person schema remain current.

### 5. Location and address representation

The supplied address is displayed as:

> Business mailing address  
> 135-21320 Gordon Way  
> Suite #N297790  
> Richmond, BC V6W 1J8  
> Canada

The site says “Working with businesses internationally” and does not call this address an office. Confirm that public display is still approved. Do not add LocalBusiness schema, a Richmond office claim, a Toronto office claim, directions, opening hours, or storefront language unless deliberately approved and true.

### 6. Response-time promise

The forms promise a reply with a next step but do not promise a specific number of hours or days. Add a response-time commitment only if it can be met consistently across holidays, workload changes, and spam filtering.

## Pricing and service decisions

### 7. Fixed-scope package boundaries

The pricing page lists deliverables and one revision round, but a confident buyer still needs owner-approved limits for:

- Number and type of website pages.
- Platform and hosting assumptions.
- Copywriting/content responsibilities.
- Brand deliverable depth and file formats.
- Number and nature of integrations.
- What “one workflow automation” includes.
- Data migration, training, testing, and support boundaries.
- Accessibility, SEO, analytics, and legal-content responsibilities.
- Delivery timing and what pauses a schedule.
- What counts as a revision versus new scope.
- Exclusions and the path when intake shows the package does not fit.

Do not invent these limits in public copy. Confirm them against the actual agreement and Stripe product before publishing more detail.

### 8. Monthly-plan configuration

For each subscription, confirm:

- Monthly allowance and overage/change-request handling.
- Renewal date, cancellation notice, unused allowance, and pause policy.
- Support channel and response expectations.
- Included account/platform count.
- Advertising media spend and creative-production limits.
- Automation-monitoring responsibility and incident boundaries.
- Handoff/termination access and ownership.

### 9. Paid audit versus free initial review

The public copy now separates:

- **Free Initial Review:** a brief outside perspective delivered by email.
- **Audits & Advisory / In-Depth Audit:** a paid, scoped evidence and decision engagement.

Confirm that the free response actually matches that description and that the paid audit has a repeatable scoping, price, evidence, deliverable, and approval process.

## Legal and privacy review

### 10. Policy review

Have the owner and qualified counsel review the current Terms and Privacy Policy against actual practice, including:

- Accepted proposal/agreement timing for direct checkout.
- Refunds, cancellation, recurring billing, renewal, and charge disputes.
- Governing law, venue, and consumer-protection requirements.
- International data processing and retention.
- Formspree, Calendly, Cloudflare, Resend, Stripe, and any portal subprocessors.
- Cookies/storage set after opening third-party services.
- AI-generated material, approved knowledge, human review, and limitations.
- Advertising-result limitations and platform-policy responsibility.
- Client-provided content, legal permissions, accessibility, and intellectual property.
- Portfolio-use permission and confidentiality.
- Incident notification, deletion requests, and record retention.

The privacy policy was technically aligned to name optional Calendly scheduling and external-service storage. Counsel should approve legal adequacy.

## Analytics and search accounts

### 11. Analytics and consent

No analytics or advertising pixel was found or installed. Before implementation, approve:

- Platform choice (for example GA4 or a privacy-focused alternative).
- Jurisdictions and consent/banner requirements.
- Whether advertising measurement or remarketing will be used.
- Retention, IP/location settings, Google Signals, user-provided data, and data sharing.
- Internal/test traffic filters.
- Privacy-policy wording and processor list.
- Who owns the account and recovery access.

Use the event plan in `AUDIT-MEASUREMENT-PLAN.md`. Never send names, email addresses, form messages, budget text, company data, or other personal/sensitive form values to analytics.

### 12. Search Console and Bing Webmaster Tools

With authorized account access:

- Verify the canonical HTTPS apex property.
- Submit `https://rielart.com/sitemap.xml`.
- Inspect the homepage, service hub, each service page, pricing, contact, portfolio, and representative articles.
- Review indexing exclusions, duplicate canonical reports, Core Web Vitals field data, manual actions, security issues, queries, and backlinks.
- Confirm old routes consolidate to the intended canonical pages.
- Record the submission date and responsible account owner.

## Hosting and security

### 13. Response headers

GitHub Pages supplied HTTPS and HSTS during the review but did not expose repository-configurable CSP, `X-Content-Type-Options`, `Referrer-Policy`, `Permissions-Policy`, frame protection, or cross-origin policy headers.

If a configurable CDN/edge layer is approved:

1. Inventory required origins: RielArt, Client Portal, Formspree, Calendly, Stripe, LinkedIn, and any future analytics host.
2. Start with a report-only CSP and collect violations through normal traffic.
3. Account for the inline theme bootstrap and existing inline style attributes before enforcement; prefer nonces/hashes or refactoring over broad `unsafe-inline` where practical.
4. Add `X-Content-Type-Options: nosniff`.
5. Add an appropriate `Referrer-Policy`.
6. Add a minimal `Permissions-Policy`.
7. Add frame protection with CSP `frame-ancestors` when supported.
8. Stage, test every external flow, then enforce.

Do not paste a restrictive CSP into a meta tag without this validation.

An initial **report-only** header for a configurable edge is:

```text
Content-Security-Policy-Report-Only: default-src 'self'; base-uri 'self'; object-src 'none'; frame-ancestors 'none'; img-src 'self' data:; style-src 'self' 'unsafe-inline'; script-src 'self' 'unsafe-inline'; connect-src 'self' https://formspree.io; form-action 'self' https://formspree.io; upgrade-insecure-requests; report-uri https://<approved-report-endpoint>/csp-report
```

This is a staged starting point, not an enforcement-ready promise. Replace the reporting placeholder with an approved collector, inspect violations, and retest Formspree plus every page. Calendly, Stripe, the Client Portal, LinkedIn, and email are top-level navigation destinations rather than embedded runtime dependencies, but they must still be included in the regression checklist. Remove temporary `'unsafe-inline'` allowances only after the theme bootstrap and inline-style inventory has been refactored or given validated hashes/nonces.

Candidate companion headers for the same staged edge review are:

```text
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: camera=(), microphone=(), geolocation=()
```

Test cross-origin opener/frame policy separately before adding it; the site intentionally opens several approved external destinations.

### 14. Server-side legacy redirects

GitHub Pages does not apply the current Netlify-style `_redirects` file. The compatibility documents for `/privacy-policy.html`, `/terms.html`, and `/packages/` therefore return HTTP 200 and perform noindex/canonical/client-side redirection.

Preserve them while inbound links may exist. If hosting gains edge/server rules, replace this behavior with tested one-hop 301 redirects and keep an audit of old inbound URLs.

### 15. Deployment and cache verification

The production site inspected on 2026-07-27 was still the older design. After deployment:

- Confirm the deployed commit matches the reviewed tree.
- Purge or wait for GitHub Pages/CDN cache expiry.
- Re-run the production crawl, canonical and integration invariants.
- Confirm the optimized logo and current CSS/JS are served.
- Recheck the 404 response.
- Verify the new `_config.yml` exclusions are honored and no `AUDIT-*`, source-report, or `tools/` artifact is published.

## Compatibility and assistive technology

### 16. Real browser/device matrix

Chromium viewport emulation covered 320, 360, 390, 430, 768, 1024, 1280, 1440, 1920, and 2560 px. Complete real or hosted tests for:

- Current Chrome and Edge.
- Current Firefox.
- Current Safari on macOS.
- iOS Safari on at least one current iPhone.
- Android Chrome on at least one current device.
- 200% and 400% browser zoom.
- Text-spacing overrides.
- Reduced motion and forced/high-contrast modes.
- Print where customer-facing content may be printed.

### 17. Screen-reader checks

Test at least:

- NVDA + Chrome or Firefox on Windows.
- VoiceOver + Safari on macOS/iOS.

Verify the skip link, page landmarks, navigation state, decorative hero treatment, capability-strip focus/pause instruction, FAQ expansion, blog results announcement, form required/error announcements, radio-group intent, privacy consent, and Thank-you page.

## Close-out record

For every manual item, record:

- Reviewer and date.
- Environment/account.
- Evidence or screenshot location.
- Decision.
- Follow-up owner.
- Retest date.
