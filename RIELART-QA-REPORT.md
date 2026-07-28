# RielArt Commercial Remodel - QA Report

**QA date:** July 27, 2026  
**Environment:** Local static server and Codex in-app browser  
**Result:** Automated repository and HTTP checks pass. Representative responsive and interactive browser checks pass. Production-only and owner-controlled checks remain open and are listed below.

## Automated static-site audit

Command:

```powershell
python -B tools/site_audit.py
```

Final result:

| Check | Result |
|---|---:|
| HTML files | 32 |
| Indexable pages | 22 |
| Sitemap URLs and last-modified values | 22 |
| Asset references | 214 |
| Images checked for alt text and dimensions | 51 |
| JSON-LD blocks | 32 |
| Forms | 1 |
| Orphan indexable pages | 0 |
| Approved visible price markers | 2/2 |
| Redirect rules | 14 |
| GitHub Pages exclusions | 26 |
| Internal artifact exclusions | 19 |
| Client Portal URL occurrences | 76 |
| Formspree endpoint occurrences | 1 |
| Calendly URL occurrences | 1 |
| Approved email-link occurrences | 27 |
| Approved LinkedIn URL occurrences | 25 |
| Public Stripe Payment Links | 0 |
| Potential unsupported numerical claims | 0 |
| Warnings | 0 |
| Critical failures | 0 |

**Status: PASS**

The audit includes commercial-model assertions, SEO/schema checks, canonical and sitemap checks, internal links, local and remote assets, image attributes, legal dates, forms, orphan pages, exclusions, redirect configuration, integration URLs, and banned legacy/public claims.

## Local HTTP smoke crawl

Command:

```powershell
python -B tools/http_smoke.py
```

Final result:

| Check | Result |
|---|---:|
| Routes checked | 34 |
| Successful HTTP 200 routes | 33 |
| Intentional 404 route | 1 |
| HTML routes | 31 |
| Aggregate HTML response bytes | 319,743 |
| Maximum allowed HTML per route | 61,440 bytes |
| CSS | 81,847 / 83,968 bytes |
| JavaScript | 15,038 / 20,480 bytes |
| Images | 643,390 / 665,600 bytes |
| Logo | 8,587 / 10,240 bytes |
| Failures | 0 |

**Status: PASS**

## Browser QA completed

The following checks were performed in the Codex in-app browser against the local site.

### Responsive layout

- **1440 × 1000:** homepage, pricing, contact, FAQ, Focused Ads detail, articles, thank-you, and 404 routes checked.
- **768 × 1000:** homepage checked with no page-level horizontal overflow.
- **320 × 900:** homepage, pricing, and contact checked with no page-level horizontal overflow.
- Homepage headline remained exactly three phrase lines at all three QA widths.
- The transparent orbital logo animation remained contained at 320 pixels.
- Contact headline rendered as three balanced lines at 320 pixels.
- Pricing cards were equal height on desktop.
- The mobile pricing comparison remains intentionally contained in its labelled horizontal-scroll wrapper rather than overflowing the page.

### Theme and motion-related implementation

- Light and dark themes were visually checked at 320 pixels.
- Theme button state, label, and pressed state updated correctly.
- The browser session was restored to light mode after testing.
- Static CSS verification confirmed that `prefers-reduced-motion: reduce` disables nonessential reveal and orbital animation.

### Navigation and keyboard-related behavior

- Mobile navigation opened with the correct expanded/hidden states.
- Escape closed the menu, unlocked the page, and restored focus to the menu button.
- The skip link is the first focusable element in DOM order.
- The skip link becomes visible when focused.
- Its target is `#main-content`; every full page now gives that target `tabindex="-1"`, and target activation transfers focus to main content.
- Visible focus styling and semantic button/link structure were preserved.

### Contact form

- The exact four approved service choices are present.
- Brand & Website Launch hides and disables all advertising-only fields.
- Focused Ads Management reveals and enables those fields.
- Both services reveals and enables those fields.
- `?service=focused-ads-management` correctly preselects the advertising path.
- Submitting an empty form keeps the visitor on the page, focuses the name field, provides the status message “Please review the highlighted required fields,” and marks required controls invalid.
- The configured success path is `/thanks/`.

No real Formspree submission was sent because that would create an external email and business-side effect.

### Interactive and content checks

- FAQ disclosure opened and exposed the correct Google-versus-Meta answer.
- Blog search for “WordPress” returned one matching article and updated its result status.
- AI article calls to action lead to current services or the general inquiry.
- Website article calls to action lead to Brand & Website Launch.
- Representative browser console checks returned no errors or warnings.
- Thank-you and 404 pages are non-indexable and have no horizontal overflow.

### Legacy-route browser fallbacks

The local static fallback behavior was verified:

- `/services/brand-strategy-identity/` → `/services/brand-website-launch/`
- `/services/ai-automation-operations/` → `/services/`
- `/packages/` → `/pricing/`

Production 301 behavior is configured in `_redirects` and must still be verified on the actual host.

## Accessibility checks completed

- One H1 per full page and logical heading hierarchy are enforced by the static audit.
- Form labels, required states, conditional-field disabling, and error status were checked.
- Image alt text and dimensions are enforced.
- Skip link and main-content targets are present.
- Mobile-menu state and Escape/focus restoration were checked.
- Light/dark contrast was visually reviewed on representative pages.
- Page-level horizontal overflow was checked at 320, 768, and 1440 pixels.
- Reduced-motion handling is present in CSS.

## SEO and structured-data checks completed

- Every indexable page has one canonical URL and unique core metadata under the audit rules.
- Sitemap and indexable-page counts match at 22.
- New service routes are indexable; retired service fallbacks are not.
- Service schema contains only the two approved service names and prices.
- No unsupported LocalBusiness, office, review, rating, team-size, or client-count claims were added.
- No public Stripe checkout URL remains.

## Checks not performed or requiring manual verification

These items are deliberately not reported as passed:

1. **Production deployment:** no source was deployed during this task.
2. **Production redirects:** `_redirects` is configured, but actual host-level 301 responses were not available on the local static server.
3. **Real Formspree delivery:** no live form submission or email delivery was triggered.
4. **External destinations:** Client Portal, Calendly, email, LinkedIn, Google, and Meta URLs were structurally verified but not opened or modified.
5. **Cross-browser coverage:** Edge, Firefox, and Safari were not available in this QA run.
6. **200 percent browser zoom:** not emulated in the available browser control surface.
7. **Runtime reduced-motion emulation:** the CSS rule was inspected, but the media preference was not emulated at runtime.
8. **Automated Lighthouse or axe scan:** not run; no result is implied.
9. **Assistive-technology screen-reader testing:** not performed.
10. **Legal approval:** Privacy Policy, Terms, service agreement, international-market, consent, billing, and platform-policy decisions require owner and qualified-counsel review.
11. **Advertising accounts and tracking:** no Google Ads, Meta, analytics, pixel, tag, Conversions API, or client account was connected or changed.
12. **Payment flow:** no public payment link was added and no test or real charge was attempted.

## Recommended pre-release verification

1. Review and close the applicable entries in `RIELART-MANUAL-REVIEW.md`.
2. Test production builds in current Edge, Firefox, and Safari at mobile and desktop widths.
3. Test keyboard navigation and 200 percent zoom on the deployed site.
4. Test with reduced-motion enabled at the operating-system level.
5. Submit one approved production Formspree test and verify the email, redirect, and spam controls.
6. Verify every `_redirects` rule as an actual 301 after deployment.
7. Open and verify the production Client Portal, Calendly, email, LinkedIn, privacy, and terms destinations.
8. Re-run both automated audit commands against the final source state.

## Final QA disposition

The local source is ready for owner/legal review and a controlled production release. Automated checks are clean, representative responsive/browser interactions pass, and all untested external or production-only items are explicitly recorded rather than assumed.
