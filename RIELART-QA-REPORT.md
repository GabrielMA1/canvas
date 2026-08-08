# RielArt Focused Refinement - QA Report

**QA date:** July 28, 2026
**Environment:** Local static server, repository audit tools, and Codex in-app browser
**Result:** Final source passes the content-consistency assertions, static audit, local HTTP crawl, JavaScript syntax check, diff check, and focused browser validation. The previously open rendered pricing-inclusion review was completed in the later release-gate report; the current Insights/404 changes were separately rendered and verified below.

## July 28 content-consistency release-gate recheck

### Static audit

The exact requested command was attempted:

```powershell
python -B tools/site_audit.py
```

It could not start because `python` is not available on this machine's
`PATH`. The same script was then run with the bundled Python executable.

| Check | Final result |
|---|---:|
| HTML files | 32 |
| Indexable pages | 22 |
| Sitemap URLs and last-modified values | 22 |
| Asset references | 216 |
| Images checked for alt text and dimensions | 52 |
| JSON-LD blocks | 32 |
| Forms | 1 |
| Orphan indexable pages | 0 |
| Approved visible pricing markers | 2/2 |
| Redirect rules | 14 |
| GitHub Pages exclusions | 30 |
| Internal artifacts excluded | 23 |
| Public Stripe Payment Links | 0 |
| Global Get Started links checked | 60 |
| Custom-scope inquiry links checked | 1 |
| Approved 404 positioning statements | 2 |
| Insights editorial entries | 9 |
| Current shared CSS cache references | 24/24 |
| Warnings | 0 |
| Critical failures | 0 |

**Status: PASS**

New assertions verify:

- both approved 404 sentences and the absence of the two retired AI-primary
  phrases;
- exact Insights title, description, Open Graph, Twitter, image, canonical,
  Blog schema description, Blog schema image, and nine-item schema order;
- the website-leads feature image, title, URL, category, alt text, and
  accessible link label;
- the absence of the automation article from the featured card;
- the visible eight-card index order following the featured article;
- the All, Brand, Websites, and Practical Technology filters;
- matching visible and structured categories for all nine real articles;
- continued access to every AI/automation article;
- exactly two public commercial services and unchanged prices, Formspree,
  Client Portal, CTA hierarchy, schema, canonicals, sitemap, and no-Stripe
  state.

No RSS or feed file exists in the repository, so no feed update was required.

### Local HTTP smoke crawl

The local server ran at `http://127.0.0.1:4173/`.

| Check | Final result |
|---|---:|
| Routes checked | 34 |
| Successful HTTP 200 routes | 33 |
| Intentional missing-route HTTP 404 | 1 |
| HTML routes | 31 |
| Aggregate HTML response bytes | 317,723 |
| Maximum HTML allowed per route | 61,440 bytes |
| CSS | 80,143 / 83,968 bytes |
| JavaScript | 15,551 / 20,480 bytes |
| Images | 643,390 / 665,600 bytes |
| Logo | 8,587 / 10,240 bytes |
| Failures | 0 |

**Status: PASS**

Additional source checks:

- `node --check assets/js/site.js`: PASS
- `git diff --check`: PASS; only Git line-ending advisories were printed
- all 24 full pages use CSS `20260728r4`; no `r3` reference remains
- targeted public-source scans found no retired 404 phrases, legacy package
  name, legacy price, public Stripe link, founder-led wording, or global
  `Start Your Project` action

### Focused rendered browser QA

Actual browser checks covered the changed Insights and 404 surfaces at:

- 1440 × 900
- 390 × 844
- 320 × 568

Verified:

- light and dark themes update the root state, toggle label, pressed state, and
  rendered colors;
- the featured website guide has one responsive image, correct accessible
  label, no clipping, and no broken media;
- desktop Insights cards align by row, share bottom action positions, and keep
  comparable heading/description regions;
- mobile cards use natural content height with no fixed-height clipping;
- the category filter returns the expected four Website articles and updates
  its live status to `4 articles shown.`;
- the 320-pixel filter row fits without horizontal scrolling;
- mobile navigation opens, moves focus to the first link, closes with Escape,
  and returns focus to the menu button;
- the refined 404 copy is visible in both themes and all three destination
  cards reflow without clipping;
- one AI supporting article opened at its canonical route with one H1,
  Practical Technology categorization, no broken image, and no overflow;
- page-level horizontal overflow failures: 0;
- broken-image failures: 0;
- clipped-card failures: 0;
- browser console warnings/errors: 0.

The browser environment does not provide true 200-percent zoom, Safari/iOS,
NVDA, VoiceOver, or Lighthouse. Those results are not claimed.

### Content decisions recorded

- The website-leads article was chosen over automation because it is a real,
  commercially aligned article and the brief ranked it first.
- Local SEO is the third editorial entry because it addresses customer
  acquisition; it remains categorized as Websites rather than being
  misleadingly labelled Advertising.
- No Advertising filter or article was fabricated because the repository has
  no published advertising article.
- AI and automation articles remain accessible supporting content under
  Practical Technology.
- The homepage FAQ was not shortened. Future reduction remains a post-traffic
  optimization.

## Earlier focused-refinement static audit (superseded)

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

## Earlier focused-refinement HTTP smoke crawl (superseded)

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
| Aggregate HTML response bytes | 317,224 |
| Maximum HTML allowed per route | 61,440 bytes |
| CSS | 79,273 / 83,968 bytes |
| JavaScript | 15,551 / 20,480 bytes |
| Images | 643,390 / 665,600 bytes |
| Logo | 8,587 / 10,240 bytes |
| Failures | 0 |

**Status: PASS**

Additional source checks:

- `node --check assets/js/site.js`: PASS
- `git diff --check`: PASS; only normal Git line-ending advisories were printed
- targeted public-HTML searches for the retired CTA, street-location fragments, hero trust line, old comparison headline, “Included item,” the retired comparison table, and “Approved projects”: no matches
- shared asset references: all 24 full pages use CSS `20260728r2`; JavaScript remains `20260728r1`

## Rendered responsive QA

The matrix below was completed for the preceding focused refinement before the row-by-row pricing table was replaced. It remains valid for unchanged routes and components. The new two-column pricing inclusion component was validated through source assertions and the HTTP crawl, but no new browser-rendered pass is claimed for it.

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
- the former pricing-table result is superseded by the new independent inclusion-list layout and is not claimed as a current browser result.

Representative visual screenshots were inspected for:

- light homepage at 1440 × 900;
- dark homepage at 1440 × 900;
- contact composition at 1440 × 900;
- contact composition at 320 × 568;
- pricing hero and aligned offer actions at 1440 × 900 before the inclusion-list follow-up.

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
- The current pricing inclusions use two semantic articles with ordinary unordered lists; no focusable horizontal-scroll region remains.
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

After the preceding responsive, theme, menu, and contact-state checks, the browser console returned:

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
- semantic, independently labelled pricing inclusion articles and lists;
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
6. Complete full keyboard-only traversal and verify the pricing inclusion
   columns at true 200-percent browser zoom.
7. Test at actual 200-percent browser zoom.
8. Test with the operating system/browser reduced-motion preference enabled.
9. Run a screen reader and, if desired, axe and Lighthouse.
10. Complete owner and qualified-counsel review in `RIELART-MANUAL-REVIEW.md`.

## Final QA disposition

The focused refinement is ready in local source for owner/legal review and a controlled release. Pricing, offers, Formspree, Client Portal, Calendly, URLs, and the static architecture were preserved. No deployment, external submission, account mutation, payment action, or production-only validation was performed or implied.

## July 29, 2026 — inline Contact submission QA

No real Formspree request was sent. The browser test server injected a local
`fetch` mock before the unchanged production JavaScript and recorded the
request contract in the local test document.

### Automated results

| Scenario | Result |
|---|---|
| Successful HTTP response with an empty/malformed JSON body | One intercepted request; URL remained `/contact/?mock=empty`; form content hidden; success card shown and focused; form reset; busy/submitting state cleared; button restored; Home and Pricing links correct |
| Formspree validation error | Form remained visible; values remained intact; success stayed hidden; button and label restored; `aria-busy` removed; concise status focused; retry sent a second mocked request |
| Network failure | Same recovery behavior; the approved general error was shown without technical output |
| Empty-form validation | Zero fetch requests; 14 invalid controls marked by the existing handler; existing validation status announced |
| Double submission while pending | One request only after click plus a second Enter attempt; `aria-busy="true"`, disabled `Sending…` button, and `Your request is being sent.` status remained intact |
| Native no-JavaScript contract | Action remains `https://formspree.io/f/xojrdoel`; method remains POST; `_next` is absent; `/thanks/index.html` remains present |

The mocked successful request contained the unchanged endpoint, POST method,
`Accept: application/json`, and the expected `FormData` field names. It did
not contain advertising fields when the non-advertising choice kept those
conditional controls disabled.

### Accessibility and responsive checks

- Success card starts with `hidden`, `role="status"`, `aria-live="polite"`,
  `aria-atomic="true"`, an `aria-labelledby` heading relationship, and
  `tabindex="-1"`.
- Focus moved to the revealed card; the form's disabled state was removed
  after success; logical link order is Return Home then View Pricing.
- At 320 × 568, the card used natural height, both actions filled the
  available width, the heading aligned below the sticky header, and page-level
  horizontal overflow was false.
- The same state reflowed without horizontal overflow at effective 720- and
  360-CSS-pixel widths, representing 200% and 400% layout reflow from a
  1440-pixel viewport. The explicit 320-pixel check is narrower than the
  400%-equivalent case.
- Light and dark computed surfaces/text were checked. The dark success
  heading was white and supporting text used the existing muted dark-theme
  token.
- The reveal uses no animation and scrolls with `behavior: "auto"`, preserving
  reduced-motion behavior.
- Browser console warnings/errors after the mocked matrix: 0.

### Command and HTTP results

- `python -B tools/site_audit.py`: unavailable because `python` is not on this
  workstation's PATH.
- Bundled Python `-B tools/site_audit.py .`: PASS with 32 HTML files, 22
  indexable and sitemap URLs, 216 asset references, 52 images, 32 JSON-LD
  blocks, one form, zero warnings, and zero critical failures.
- Local HTTP smoke: `/contact/`, `/assets/js/site.js`,
  `/assets/css/site.css`, and `/thanks/` all returned HTTP 200.
- `node --check assets/js/site.js`: PASS.
- `git diff --check`: PASS apart from Git's existing line-ending advisories.

### Required production step

Owner action required in Formspree: Set the form's Thank You redirect to
`https://rielart.com/thanks/` so non-JavaScript submissions also remain within
the RielArt website. Codex cannot configure the external Formspree dashboard.

After publication, send one controlled, owner-authorized production inquiry
to verify Formspree acceptance, mailbox delivery, the JavaScript inline state,
and the configured no-JavaScript redirect. No production submission was sent
during this QA pass.

## August 7, 2026 — Business Email & Workspace Setup QA

### Source and commercial-integrity results

- Bundled Python static audit: **PASS** — 32 HTML files, 22 indexable and
  sitemap URLs, 216 asset references, 52 images, 32 JSON-LD blocks, one form,
  zero warnings, and zero critical failures.
- The audit found exactly two primary services on Home, Services, and Pricing;
  the optional setup uses no `.offer-card`, `data-primary-service`, Service
  schema, or Offer schema.
- Approved optional coverage: four marked public callouts, four inquiry CTAs,
  one Pricing offer/price occurrence, and 24 footer links.
- `$149` is restricted to marked Business Email & Workspace Setup elements and
  the exact synchronized FAQPage strings. No `$149/month`, Managed IT
  Services, retired commercial price, or extra primary-service marker remains.
- FAQ visible copy and FAQPage JSON-LD remain synchronized.

### Contact-form state matrix

The test loaded the real local production JavaScript and did not send a
Formspree request.

| State | Advertising questions | Result |
|---|---|---|
| Optional setup only | Hidden and disabled | PASS |
| Focused Ads Management | Visible and enabled | PASS |
| Both services | Visible and enabled | PASS |
| Brand & Website Launch | Hidden and disabled | PASS |
| I am not sure yet | Hidden and disabled | PASS |

With the `business-email-workspace` query, desktop light mode and 320-pixel
dark mode both selected `I am not sure yet`, checked the optional checkbox,
showed the prepared-inquiry status, and set the hidden context to exactly
`Business Email & Workspace Setup inquiry`. Mocked `FormData` contained the
optional value `Business Email & Workspace Setup — from $149`; disabled
advertising fields were excluded. Unchecking the optional setup hid the status
and cleared the hidden context; rechecking it restored both while advertising
fields remained hidden and disabled.

### Responsive, theme, and keyboard checks

- Headless Chrome covered Home, Services, Pricing, Brand & Website Launch,
  Contact, and FAQ in ten desktop/mobile light/dark cases, including 320-pixel
  layouts. No case produced horizontal overflow or a console warning/error.
- Optional sections stacked at natural height, and the Contact checkbox kept a
  visible 3-pixel focus outline in both tested themes.
- Source review confirmed a semantic labelled checkbox, no new dependency,
  and unchanged Formspree submission code.

### Command and HTTP results

- Bundled Python `-B tools/site_audit.py .`: PASS.
- `node --check assets/js/site.js`: PASS.
- `git diff --check`: PASS.
- Local HTTP crawl: 34 routes checked; 33 HTTP 200 responses; 31 HTML pages;
  aggregate HTML 399,759 bytes; all route HTML limits PASS.
- JavaScript: 20,479 / 20,480 bytes — PASS.
- Logo: 8,587 / 10,240 bytes — PASS.
- CSS: 92,044 / 83,968 bytes — FAIL against the existing budget.
- Combined image library: 11,869,058 / 665,600 bytes — FAIL against the
  existing budget.

The CSS and image budgets were already over limit before this change; the
optional-service pass adds no image asset and keeps JavaScript under budget.
These known performance-budget failures make the final disposition a
**CONDITIONAL PASS**, not a functional or commercial-integrity failure.

### Remaining production-only checks

- Complete owner/legal review of the updated operational terms and provider
  responsibilities.
- After publication, verify the deployed cache key, routes, footer anchor,
  production redirects, and external destinations.
- Send one separately authorized production inquiry to confirm Formspree and
  mailbox delivery; no real submission was sent during this QA pass.
- Confirm tenant/domain ownership, delegated access, recovery, DNS rollback,
  migration boundaries, retention, and offboarding procedures before accepting
  the first live setup engagement.
