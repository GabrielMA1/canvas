# RielArt Focused Refinement - QA Report

**QA date:** July 28, 2026
**Environment:** Local static server, repository audit tools, and Codex in-app browser
**Result:** Final source passes the static audit, local HTTP crawl, JavaScript syntax check, diff check, and the rendered responsive matrix. Production-only, external-delivery, cross-browser, 200-percent zoom, and runtime reduced-motion checks remain explicitly open.

## Automated static-site audit

Command:

```powershell
python -B tools/site_audit.py
```

| Check | Final result |
|---|---:|
| HTML files | 32 |
| Indexable pages | 22 |
| Sitemap URLs and last-modified values | 22 |
| Asset references | 214 |
| Images checked for alt text and dimensions | 51 |
| JSON-LD blocks | 32 |
| Forms | 1 |
| Orphan indexable pages | 0 |
| Approved visible pricing markers | 2/2 |
| Redirect rules | 14 |
| GitHub Pages exclusions | 27 |
| Internal artifacts excluded | 20 |
| Client Portal URL occurrences | 76 |
| Formspree endpoint occurrences | 1 |
| Calendly URL occurrences | 1 |
| Approved email-link occurrences | 27 |
| Approved LinkedIn URL occurrences | 25 |
| Public Stripe Payment Links | 0 |
| Global Get Started links checked | 60 |
| Custom-scope inquiry links checked | 1 |
| Public PostalAddress schemas | 0 |
| Organization address properties | 0 |
| Potential unsupported numerical claims | 0 |
| Warnings | 0 |
| Critical failures | 0 |

**Status: PASS**

The refinement assertions cover retired location fragments and `<address>` elements, CTA labels and targets, unchanged service-specific CTAs, removed hero copy, exact two-offer integrity, neutral pricing language, custom-scope behavior, exact contact metadata/schema/H1, the four preserved form choices, hidden custom context, prices, commitments, integrations, canonicals, sitemap, redirects, and schema parsing.

## Local HTTP smoke crawl

Command:

```powershell
python -B tools/http_smoke.py --base-url http://127.0.0.1:4173
```

| Check | Final result |
|---|---:|
| Routes checked | 34 |
| Successful HTTP 200 routes | 33 |
| Intentional 404 route | 1 |
| HTML routes | 31 |
| Aggregate HTML response bytes | 317,109 |
| Maximum HTML allowed per route | 61,440 bytes |
| CSS | 78,013 / 83,968 bytes |
| JavaScript | 15,551 / 20,480 bytes |
| Images | 643,390 / 665,600 bytes |
| Logo | 8,587 / 10,240 bytes |
| Failures | 0 |

**Status: PASS**

Additional source checks:

- `node --check assets/js/site.js`: PASS
- `git diff --check`: PASS; only normal Git line-ending advisories were printed
- targeted public-HTML searches for the retired CTA, street-location fragments, hero trust line, old comparison headline, and “Approved projects”: no matches
- shared asset references: all 24 full pages use `20260728r1`

## Rendered responsive QA

The local site was rendered at every requested viewport:

- 320 × 568
- 360 × 800
- 390 × 844
- 430 × 932
- 768 × 1024
- 1024 × 768
- 1280 × 720
- 1440 × 900
- 1920 × 1080

Two measured matrices covered 126 page-and-viewport combinations.

Core routes at all nine sizes:

- `/`
- `/services/`
- `/pricing/`
- `/contact/`

Supporting routes at all nine sizes:

- `/about/`
- `/process/`
- `/portfolio/`
- `/faq/`
- `/services/brand-website-launch/`
- `/services/focused-ads-management/`
- `/blog/`
- `/blog/website-maintenance-checklist/`
- `/privacy-policy/`
- `/404.html`

Results:

- no page-level horizontal overflow;
- no detected clipped main content after excluding the intentional screen-reader-only and pre-reveal states;
- offer-card header, price, note, list, and action regions align while side by side;
- homepage Google and Meta action links align at the desktop/tablet two-column breakpoints;
- Google/Meta detail-card final notes share the same top and bottom at 1024, 1280, 1440, and 1920 widths;
- contact information and form panels share the same top position at 1280, 1440, and 1920 widths;
- contact panels stack at 1024 and narrower with natural height and no dark background slab;
- the four contact service choices render at equal height in their two-column layout;
- offer and platform cards return to natural height when stacked;
- practical button targets are at least 44 pixels high in the final CSS;
- the pricing table remains inside its own 720-pixel scroll surface at narrow widths rather than widening the page.

Representative visual screenshots were inspected for:

- light homepage at 1440 × 900;
- dark homepage at 1440 × 900;
- contact composition at 1440 × 900;
- contact composition at 320 × 568;
- pricing hero and aligned offer actions at 1440 × 900.

## Theme, navigation, and focus QA

### Theme

- Light-to-dark and dark-to-light switching was exercised on the homepage.
- The root `data-theme`, button label, pressed state, and computed body background changed correctly.
- The contact form panel was checked in dark mode; its surface and text colors changed without overflow.
- The browser session was restored to light mode.

### Mobile navigation

- At 390 × 844, the menu opened with `aria-expanded="true"` and `aria-hidden="false"`.
- The first mobile-navigation link received focus.
- Escape closed the menu, removed the body lock, restored the hidden/expanded attributes, and returned focus to the menu button.

### Keyboard/focus structure

- The skip link is first in DOM order and points to a focusable `#main-content`.
- Global `:focus-visible` styling remains in place.
- The narrow pricing comparison is a focusable `region` named **Service comparison**; at 320 pixels it measured 271 pixels wide with 720 pixels of scrollable table content and successfully received focus.
- Full keyboard traversal, native Enter/Space activation, and arrow-key scrolling could not be conclusively exercised through the available automation key surface and remain manual checks.

## Contact-form QA

The exact four visible choices remain:

1. Brand & Website Launch
2. Focused Ads Management
3. Both services
4. I am not sure yet

Query and conditional-state checks:

| Query | Selected choice | Advertising fields | Hidden context |
|---|---|---|---|
| `brand-website-launch` | Brand & Website Launch | Hidden and disabled | Empty |
| `focused-ads-management` | Focused Ads Management | Visible and enabled | Empty |
| `both-services` | Both services | Visible and enabled | Empty |
| `not-sure` | I am not sure yet | Hidden and disabled | Empty |
| `custom-scope` | I am not sure yet | Hidden and disabled | `Custom scope inquiry` |

The empty form exposed the expected native invalid states for name, business name, email, country, business description, improvement goal, target market, desired timeline, message, and privacy consent. The radio requirement was already satisfied by each tested query preselection.

Preserved integration facts:

- Form action remains `https://formspree.io/f/xojrdoel`.
- Success route remains `https://rielart.com/thanks/`.
- Client Portal, Calendly, email, and LinkedIn URLs remain in the audited source.
- No real Formspree submission was sent because it would create an external email/business side effect.

## Browser console

After the responsive, theme, menu, comparison, and contact-state checks, the browser console returned:

- errors: 0
- warnings: 0

## Accessibility and motion disposition

Verified:

- one H1 and heading/landmark/form-label rules through the static audit;
- visible focus CSS;
- form required states and disabled conditional fields;
- 44-pixel shared small-button minimum;
- equal, fully clickable service-choice labels;
- descriptive contact links and secure external-link attributes;
- logical contact DOM order;
- no duplicated or screen-reader-announced filler copy in offer-card spacing;
- labelled horizontal comparison region;
- responsive reflow down to 320 pixels.

Static implementation only:

- the `prefers-reduced-motion: reduce` rule disables nonessential reveal/orbital animation;
- min-height rather than fixed-height card regions allow text growth;
- stacked layouts remove structural note/header minimums.

Not claimed as runtime passes:

- 200-percent browser zoom;
- operating-system reduced-motion emulation;
- screen-reader output;
- automated axe/Lighthouse results.

## Remaining manual or production-only checks

1. Deploy to the production host and verify the exact built source and asset version.
2. Verify all `_redirects` rules as real production 301 responses.
3. Run a specifically authorized Formspree production submission and confirm mailbox delivery, all fields, hidden custom context, spam handling, and `/thanks/`.
4. Open and verify the production Client Portal, Calendly, email, LinkedIn, privacy, and terms destinations.
5. Test current Edge, Firefox, and Safari.
6. Complete full keyboard-only traversal, Enter/Space activation, and horizontal table scrolling.
7. Test at actual 200-percent browser zoom.
8. Test with the operating system/browser reduced-motion preference enabled.
9. Run a screen reader and, if desired, axe and Lighthouse.
10. Complete owner and qualified-counsel review in `RIELART-MANUAL-REVIEW.md`.

## Final QA disposition

The focused refinement is ready in local source for owner/legal review and a controlled release. Pricing, offers, Formspree, Client Portal, Calendly, URLs, and the static architecture were preserved. No deployment, external submission, account mutation, payment action, or production-only validation was performed or implied.
