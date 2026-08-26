# RielArt redesign handoff — August 26, 2026

Status: implemented and verified in the testing clone. Nothing was deployed, pushed, submitted, or changed in production or any external service. QA artifacts were kept outside the tracked clone.

## Design direction

The redesign is called **The Turn**. It grows from the folded-ribbon geometry of the existing RielArt mark: a business becomes recognizable through its brand, credible through its website, and easier to choose through a clear customer pathway.

- Warm paper and deep ink replace the previous glow-heavy presentation.
- RielArt blue leads the hierarchy; cyan is reserved for the end of the pathway and select accents.
- Selective folded corners, angled cuts, structural rules, open layouts, and whitespace echo the logo without turning the site into an industrial diagram or a ruled ledger.
- Light and dark themes are intentional counterparts, not simple inversions.
- Motion is limited to the logo-derived homepage pathway, navigation, FAQs, and the theme control. Reduced-motion preferences collapse these transitions.
- The site remains static HTML, CSS, and vanilla JavaScript with a system font stack and no new dependency.

## Commercial and technical contracts preserved

- Exactly two primary offers remain public: Brand & Website Launch at $599 USD one time, and Focused Ads Management at $349 USD per month with a three-month initial commitment and advertising spend separate.
- Business Email & Workspace Setup remains a subordinate optional setup from $149 USD one time.
- Existing URLs, canonicals, structured data, sitemap coverage, redirect rules, Client Portal links, Calendly link, Formspree endpoint, inquiry query states, accessibility landmarks, light/dark theme behavior, and legal content remain intact.
- A simple Meta short-form variation may be assembled from suitable approved or client-provided assets within the standard creative allowance; filming and full or ongoing custom video production remain separately scoped.
- The Work page uses the existing RielArt mark and CSS-native Turn geometry for one clearly labelled internal RielArt feature. Every other example remains explicitly classified as representative concept or solution model, not client work.

## Performance results

- Shared CSS: 92,044 bytes before; 58,766 bytes after.
- Shared JavaScript: 20,479 bytes before; 19,868 bytes after.
- Image library: 11,869,058 bytes before; 377,834 bytes after (96.8% reduction). Social images now match their declared 1200 × 630 dimensions.
- No external font, framework, build step, or third-party runtime was introduced.

## Verification completed

- Static audit: 32 HTML files, 22 indexable pages, 22 sitemap URLs, 217 asset references, 53 image checks, 32 JSON-LD blocks, one form, 14 redirects, zero warnings, and zero critical failures.
- HTTP crawl: 34 routes requested, 33 expected HTTP 200 responses, 31 HTML routes, and every HTML/CSS/JavaScript/image/logo budget passed.
- Browser matrix: 11 high-risk routes × 11 viewports × 2 themes = 242 rendered cases and 8,110 assertions, all passing. Reviewed widths were 1440, 1280, 1180, 1081, 1080, 1024, 820, 768, 430, 390, and 320 CSS pixels.
- Hero pixel and geometry review passed all 22 light/dark width combinations, including text-range safe zones and clip hit-tests after the restrained pathway motion completed.
- Thirteen interaction suites passed for theme persistence, desktop dropdown and Escape behavior, closed/open mobile-menu focus handling and breakpoint reset, current-page navigation, FAQ behavior, Insights filtering/search, reduced motion, no-JavaScript navigation and form use, 720px 200%-equivalent reflow, visible keyboard focus, and mocked form states.
- Independent pixel and visible-text contrast review covered Home, Portfolio, Insights, a long article, Contact, and FAQ at 1440, 820, and 390 pixels in both themes, plus high-risk Home and Portfolio views at 320 pixels. No visual blocker or low-ratio rendered-text hit remained.
- The contact success state was tested with the Formspree request intercepted locally. No real inquiry was submitted.
- All 24 public page shells use the `20260826final1` CSS and JavaScript cache key.
- JavaScript syntax and Git whitespace checks passed.

## Manual production checks still required

1. Confirm the production host implements the 14 rules in `_redirects` as real permanent redirects. A static local server cannot prove host-level 301 behavior, and GitHub Pages does not natively consume Netlify-style `_redirects` rules.
2. Confirm the Formspree project retains the intended non-JavaScript post-submit destination. The source-controlled form endpoint is correct, but dashboard behavior is external to this clone.
3. Confirm the final Meta creative wording in the signed service agreement. The repository now consistently limits the included option to a simple asset-based short-form variation and separately scopes full video production.
