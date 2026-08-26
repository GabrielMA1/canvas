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

- Shared CSS: 92,044 bytes before; 58,205 bytes after.
- Shared JavaScript: 20,479 bytes before; 19,868 bytes after.
- Image library: 11,869,058 bytes before; 377,834 bytes after (96.8% reduction). Social images now match their declared 1200 × 630 dimensions.
- No external font, framework, build step, or third-party runtime was introduced.

## Verification completed

- Static audit: 32 HTML files, 22 indexable pages, 22 sitemap URLs, 217 asset references, 53 image checks, 32 JSON-LD blocks, one form, 14 redirects, zero warnings, and zero critical failures.
- The final precision pass removes only the compact homepage-hero price strip. The View Pricing action remains, and approved prices remain visible in the homepage service section, Pricing, both primary service pages, and relevant commercial content.
- The semantic Advertising Details fieldset now keeps its legend visually inside the panel, aligns differently wrapped desktop labels through shared grid rows, and returns to natural stacked labels on mobile. Hidden, Ads, Both, and switch-away states all passed.
- HTTP crawl: 34 routes requested, 33 expected HTTP 200 responses, 31 HTML routes, and every HTML/CSS/JavaScript/image/logo budget passed.
- Final browser matrix: 14 requested routes × 15 viewports × 2 themes = 420 rendered cases and 20,330 assertions, all passing. Reviewed widths were 1600, 1440, 1366, 1280, 1180, 1081, 1080, 1024, 820, 768, 430, 390, 375, 360, and 320 CSS pixels.
- Hero pixel and geometry review passed all 30 light/dark width combinations after the pricing removal, including text-range safe zones and clip hit-tests after the restrained pathway motion completed.
- Twenty-two final interaction checks passed for theme, navigation, mobile-menu, FAQ, Insights, form, reduced-motion, reflow, focus, and conditional-field behavior.
- Independent alignment review covered the full requested route matrix. Header/container/footer edges, service and pricing cards, buttons, portfolio rows, FAQ controls, form panels, mobile gutters, and content wrapping passed with no horizontal overflow, clipping, or unexplained drift.
- Desktop offer headers now reserve a responsive shared label zone only above 820 pixels, keeping price and action baselines aligned without imposing desktop whitespace on stacked mobile cards.
- At 380 pixels and below, the compact header wordmark remains available as the link's accessible name while the footer wordmark stays visible. The 320-pixel Contact required marker also stays with its label text.
- The contact success state was tested with the Formspree request intercepted locally. No real inquiry was submitted.
- All 24 public page shells use the `20260826final2` CSS and JavaScript cache key.
- JavaScript syntax and Git whitespace checks passed.

## Manual production checks still required

1. Confirm the production host implements the 14 rules in `_redirects` as real permanent redirects. A static local server cannot prove host-level 301 behavior, and GitHub Pages does not natively consume Netlify-style `_redirects` rules.
2. Confirm the Formspree project retains the intended non-JavaScript post-submit destination. The source-controlled form endpoint is correct, but dashboard behavior is external to this clone.
3. Confirm the final Meta creative wording in the signed service agreement. The repository now consistently limits the included option to a simple asset-based short-form variation and separately scopes full video production.
