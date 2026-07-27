# RielArt Audit — Regression Report

**Audit date:** 2026-07-27  
**Baseline commit:** `3ebf603` (`main`, “Site Rebuilt”)  
**Final target:** Audited working tree after the 2026-07-27 implementation pass  
**Local review origin:** `http://127.0.0.1:4173/`

## Result

The final regression pass found **no confirmed P0 issue**.

- Static audit: **0 warnings, 0 critical failures**
- HTTP smoke test: **0 failures**
- Browser matrix: **0 failures across 100 route/viewport combinations**
- Browser console after representative navigation/interactions: **0 errors, 0 warnings**
- JavaScript syntax: **PASS**
- Git whitespace/error check: **PASS**
- Approved production integration values: **unchanged**

The remaining checks require owner-controlled accounts, real devices, software that was unavailable in the review environment, professional legal review, or deployment authorization. They are listed under **Unavailable and deliberately excluded tests**.

## Final static audit

Command:

```powershell
& "C:\Users\Gabriel\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" tools/site_audit.py
```

| Check | Final result |
|---|---:|
| HTML documents parsed | 30 |
| Indexable pages | 25 |
| Sitemap URLs | 25 |
| Sitemap `lastmod` values checked | 25 |
| Local references checked | 242 |
| Images checked for alt text and dimensions | 59 |
| JSON-LD blocks parsed | 35 |
| Contact forms checked | 2 |
| Redirect rules checked | 4 |
| GitHub Pages exclusions checked | 17 |
| Internal artifact paths safely excluded | 17 |
| Approved Stripe links found | 6/6 |
| Warnings | 0 |
| Critical failures | 0 |

The audit also confirmed the required page metadata, canonicals, H1 coverage, internal files, local assets, fragments, image alternatives, duplicate-ID rules, safe new-tab attributes, form destinations, redirect declarations, structured-data syntax, sitemap coverage, and deployment exclusions.

## Final local HTTP smoke test

Command:

```powershell
& "C:\Users\Gabriel\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" tools/http_smoke.py --base-url http://127.0.0.1:4173/
```

| Check | Final result |
|---|---:|
| Routes requested | 32 |
| Routes expected to return HTTP 200 | 31 |
| HTML responses inspected | 29 |
| Aggregate HTML response payload | 436,358 bytes |
| Status, H1, title, canonical, or local-image failures | 0 |

The same run enforced the raw-file budgets:

| Budget | Final / maximum |
|---|---:|
| HTML per ordinary route | Largest route below 61,440 B |
| CSS | 62,760 / 66,560 B |
| JavaScript | 14,012 / 20,480 B |
| Image library | 643,390 / 665,600 B |
| Global logo | 8,587 / 10,240 B |

All route and budget expectations passed, including the deliberately missing-route check. No form was submitted and no checkout was started.

## Final responsive browser matrix

The final Chromium matrix covered ten routes at ten viewport widths, for **100 route/viewport combinations**.

### Routes

1. `/`
2. `/services/`
3. `/services/web-design-development/`
4. `/pricing/`
5. `/portfolio/`
6. `/process/`
7. `/contact/`
8. `/blog/`
9. `/blog/website-maintenance-checklist/`
10. `/404.html`

### Viewports

1. 320 px
2. 360 px
3. 390 px
4. 430 px
5. 768 px
6. 1024 px
7. 1280 px
8. 1440 px
9. 1920 px
10. 2560 px

| Browser assertion | Failures |
|---|---:|
| Horizontal overflow | 0 |
| Broken rendered images | 0 |
| Missing or duplicate route H1 | 0 |
| Incorrect mobile/desktop breakpoint state | 0 |
| Viewport/render setup mismatch | 0 |

At 1440 px, the homepage hero rendered as exactly three deliberate lines with no overflow:

> Build a stronger brand.  
> Create a clearer website.  
> Run a smarter business.

Each line contains exactly four words.

The contact heading rendered as the intended two lines at desktop:

> Share what needs  
> to work better.

Each line contains exactly three words. The 320 px and 390 px checks found no heading or page overflow.

Representative homepage and contact captures were taken at desktop and mobile sizes during the browser session and inspected for spacing, wrapping, image integrity, card alignment, focus presentation, and theme consistency. No visual regression was recorded. Screenshot binaries were not added to the deploy repository; the reproducible routes, dimensions, assertions, and measurements are recorded here instead.

Comparable repeated cards aligned to equal heights within their desktop grid rows: service cards measured 438 px, representative model cards 398 px, person cards 682 px, and monthly-support cards 600 px. The inquiry-only connected pricing card occupies its own section and is intentionally not forced to match the fixed-package row.

## Interaction and accessibility regression

### Inquiry intent and forms

- A project CTA carrying `?inquiry=project` selected **Project inquiry**.
- A free-review CTA carrying `?inquiry=review` selected **Free initial review**.
- Without a query override, each form retained its documented HTML default: the standalone Contact form defaults to **Project inquiry**, while the homepage review form defaults to **Free initial review**.
- Invalid submission attempts marked invalid controls with `aria-invalid="true"` and announced: “Please review the highlighted required fields.” through the polite live region.
- Correcting an invalid control removed its invalid state; correcting all invalid controls cleared the live-region error.
- Form submission recovery restored the submit button and cleared busy/status state on page restoration.
- The checks stopped before native Formspree submission, so no inquiry was sent.

### Keyboard interactions

- Mobile navigation focus wrapped from the last focusable item to the first and from the first to the last with Shift+Tab.
- Escape closed the mobile navigation and restored focus to the menu control.
- The replacement homepage visual is decorative, hidden from assistive technology, and contains no rendered text or interactive controls.
- Timed observation confirmed that the hero orbit and path-flow animations changed state. The reduced-motion stylesheet disables those animations.
- No visible Pause/Resume control remains in the capability strip. Keyboard focus on the strip paused the ticker and exposed the screen-reader instruction that the list also pauses while hovered.
- The capability ticker’s computed animation was `capability-marquee`; its transform changed during a 360 ms observation, directly confirming visible right-to-left motion.
- FAQ interaction preserved a single-open item within each group.

### Blog behavior

- The filter controls returned the expected non-featured article counts:

| Filter | Results |
|---|---:|
| All | 8 |
| Brand | 1 |
| Web & UX | 2 |
| AI & Automation | 2 |
| SEO & Analytics | 2 |
| Operations | 1 |

- The featured guide remained separately visible and was not incorrectly counted by the filter result status.
- Visible category labels, filter slugs, card categories, and article taxonomy matched the approved dictionary.
- All nine article pages exposed a visible Gabriel Macovei byline linked to the About profile.
- Article and index CTAs resolved to the documented related service, and free-review CTAs preserved `inquiry=review`.
- The former empty Advertising filter was absent.

## Syntax and repository checks

Commands:

```powershell
node --check assets/js/site.js
git diff --check
```

Both commands passed. The integration-preservation checks also found the exact approved Formspree endpoint, Thank-you destination, Client Portal URL, Calendly URL, email address, LinkedIn URL, six Stripe payment links, and visible Stripe prices unchanged from the baseline.

The browser console log collected after the representative page and interaction pass contained **0 errors and 0 warnings**.

## Required functional checklist

| Function | Final evidence |
|---|---|
| Light/dark mode | Local toggle changed `data-theme` from `light` to `dark` and updated its accessible label; PASS |
| Mobile menu | Open/close state, two-way focus wrap, Escape, and focus restoration; PASS |
| Hero animation | Decorative and text-free; orbit and path motion observed; reduced-motion static state present; PASS |
| Capability ticker | Running right-to-left animation; no visible Pause control; hover/focus pause and reduced-motion static state; PASS |
| FAQ | Correct state and single-open behavior; PASS |
| Blog filters | Five populated categories plus All, correct counts, no empty Advertising filter; PASS |
| Contact form | Project default, local native/error/live-region/recovery behavior; PASS without external submission |
| Free initial review form/path | Review query selection and matching visible language; PASS without external submission |
| Thank-you page | Expected local HTTP 200, utility-page noindex, and current next-step content; PASS |
| Client Portal | Exact approved URL preserved; bounded read-only destination check succeeded; account behavior not tested |
| Calendly | Exact approved URL preserved; bounded read-only destination check succeeded; no booking created |
| Stripe | Six exact approved URLs and prices preserved; two bounded probes returned 200, four were inconclusive; no checkout/account claim |
| Email links | `hello@rielart.com` preserved and structurally valid; no email client action sent |
| Sitemap | 25/25 parity and valid current `lastmod` values; PASS |
| Robots | Present, crawlable-site rules and sitemap destination checked; PASS |
| Legacy redirects | Four rules/documents internally consistent; GitHub Pages still serves compatibility documents instead of true server 301s |
| Custom 404 | Included in the final browser matrix with one H1, no overflow, and no broken image; PASS |

## Performance and payload comparison

These are raw public-source sizes, not compressed network-transfer measurements. Lighthouse was unavailable, so this report does not invent lab timing or score data.

### Public source by asset type

| Asset group | Baseline | Final | Change |
|---|---:|---:|---:|
| Public source total | 1,245,018 B | 1,167,849 B | -77,169 B (-6.20%) |
| HTML | 439,611 B | 443,640 B | +4,029 B (+0.92%) |
| CSS | 60,906 B | 62,760 B | +1,854 B (+3.04%) |
| JavaScript | 13,286 B | 14,012 B | +726 B (+5.46%) |
| Images | 727,177 B | 643,390 B | -83,787 B (-11.52%) |
| `images/logo.png` | 92,374 B | 8,587 B | -83,787 B (-90.71%) |

The modest JavaScript increase supports intent routing, announced validation state, and form recovery; obsolete hero-tab and marquee-button logic was removed. The CSS increase contains the code-native hero animation and responsive/reduced-motion treatment. The optimized logo more than offsets these additions.

### Representative raw initial-route payloads

The figures count one HTML request plus the shared CSS, JavaScript, logo, and favicon. Repeated uses of the same logo URL are counted once.

| Route | Baseline | Final | Requests | Change |
|---|---:|---:|---:|---:|
| Home | 214,221 B | 132,085 B | 5 | -82,136 B (-38.34%) |
| Process | 190,989 B | 109,896 B | 5 | -81,093 B (-42.46%) |
| Contact | 193,431 B | 112,420 B | 5 | -81,011 B (-41.88%) |
| Portfolio | 188,391 B | 107,297 B | 5 | -81,094 B (-43.05%) |
| Pricing | 196,886 B | 116,159 B | 5 | -80,727 B (-41.00%) |
| About, initial | — | 111,853 B | 5 | — |
| About, after both lazy photos load | 318,730 B | 237,753 B | 7 | -80,977 B (-25.41%) |

No external font, framework, autoplay video, or third-party application runtime is required for the initial local render.

## External read-only checks

- Two Stripe checkout URLs returned HTTP 200 during the bounded read-only probe.
- The completed non-Stripe endpoint checks, including Calendly, returned HTTP 200.
- Four Stripe requests and one Google reference request timed out or were cancelled. Those results are **inconclusive**, not evidence of a broken link.
- LinkedIn returned HTTP 999, its anti-automation response. This is **not proof that the public profile is broken**.
- Static source verification confirmed all approved external destinations and integration invariants exactly unchanged.

The audit did not retry indefinitely, bypass anti-bot controls, sign in, submit personal information, begin a charge, or alter any external account.

## Unavailable and deliberately excluded tests

The following are not represented as passed:

- Lighthouse was not installed, so no Lighthouse Performance, Accessibility, Best Practices, SEO, LCP, CLS, or TBT result is claimed.
- axe was not installed, so no automated axe violation count is claimed.
- A standards-conformance HTML validator was not installed; the repository audit parsed every document and checked structural/metadata invariants, but this is not presented as a full WHATWG conformance result.
- No real Safari or iOS Safari test was available.
- No real Android Chrome test was available.
- No real Firefox test was available.
- No real Microsoft Edge test was completed.
- No NVDA, VoiceOver, JAWS, TalkBack, or other screen-reader test was completed.
- No production Formspree submission or mailbox-delivery test was performed.
- No Stripe payment, subscription, product-setting, success-route, cancellation, refund, or account-level test was performed.
- No Calendly booking, LinkedIn action, email action, or Client Portal account action was completed.
- No analytics or advertising account was created or changed.
- No professional legal review was performed.
- No deployment, DNS, hosting, CDN, cache, security-header, or production rollback action was performed.

These exclusions leave owner/account verification, real-device compatibility, assistive-technology review, legal adequacy, and production deployment as explicit handoff items. They do not change the automated conclusion: **no confirmed P0 defect was found in the audited working tree**.
