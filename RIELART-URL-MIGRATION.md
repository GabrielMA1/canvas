# RielArt URL Migration Plan

## Principles

- Preserve useful, indexable routes when their purpose remains current.
- Consolidate retired service categories into the nearest of the two approved offers.
- Keep local noindex fallback pages for legacy routes because the current static host may not apply `_redirects` in every environment.
- Do not include compatibility routes in the sitemap.
- Do not create redirect chains or loops.
- Keep canonical URLs aligned with the sitemap and visible page purpose.

## Final indexable architecture

| Route | Purpose |
|---|---|
| `/` | Primary positioning and conversion page |
| `/services/` | Consolidated “Brand, Website & Advertising” overview |
| `/services/brand-website-launch/` | Detailed $599 one-time offer |
| `/services/focused-ads-management/` | Detailed $349/month offer, Google and Meta sections |
| `/pricing/` | Two-offer pricing and comparison |
| `/process/` | How It Works |
| `/portfolio/` | Accurately labelled work |
| `/about/` | Company approach and operating principles |
| `/faq/` | Detailed two-offer FAQ |
| `/contact/` | Project inquiry |
| `/thanks/` | Noindex inquiry confirmation |
| `/blog/` | Insights index |
| Existing article routes | Retained educational content with current CTAs |
| `/privacy-policy/` | Privacy notice |
| `/terms/` | Terms |
| `/404.html` | Noindex not-found page |

Google and Meta explanations use:

- `/services/focused-ads-management/#google-search-ads`
- `/services/focused-ads-management/#meta-ads`

They are explanatory anchors, not separate packages.

## Legacy service decisions

| Existing route | Decision | Destination/reason |
|---|---|---|
| `/services/brand-strategy-identity/` | Retire as a standalone offer; noindex compatibility redirect | `/services/brand-website-launch/` |
| `/services/web-design-development/` | Retire as a standalone offer; noindex compatibility redirect | `/services/brand-website-launch/` |
| `/services/digital-growth-management/` | Retire as a standalone offer; noindex compatibility redirect | `/services/focused-ads-management/` |
| `/services/ai-automation-operations/` | Retire as a public offer; noindex compatibility redirect | `/services/` |
| `/services/audits-advisory/` | Retire as a public offer; noindex compatibility redirect | `/services/` |

AI articles may remain indexable when accurate. Their calls to action will point to a current offer or the general inquiry. The AI service route itself no longer has independent commercial or SEO value under the approved model.

## Package and extension compatibility

| Existing route | Decision |
|---|---|
| `/packages/` and `/packages/*` | Noindex compatibility redirect to `/pricing/` |
| `/privacy-policy.html` | Noindex compatibility redirect to `/privacy-policy/` |
| `/terms.html` | Noindex compatibility redirect to `/terms/` |

## Sitemap and canonical policy

- Include only indexable final routes.
- Exclude thank-you, 404, compatibility, internal configuration, tools, and documentation.
- Each indexable HTML document has one self-referencing canonical.
- Each compatibility document has `noindex,follow` and points users and crawlers to the final destination.
- Article canonicals remain unchanged unless an article is separately consolidated.

## Redirect implementation

The `_redirects` file will contain direct, single-hop mappings for hosts that support it. Each retired route will also retain a lightweight local HTML fallback with:

- `noindex,follow`;
- a canonical link to the destination;
- an immediate meta refresh;
- a visible destination link;
- no commercial offer or outdated price.

## Internal-link migration

All headers, footers, homepage cards, pricing CTAs, article CTAs, related links, metadata, breadcrumbs, and structured data must point directly to final destinations rather than relying on redirects.

## Verification

The final audit must confirm:

- sitemap and canonical agreement;
- no redirect loops or chains;
- valid internal links and anchors;
- no legacy service route in navigation, footer, sitemap, or structured service data;
- no outdated public Stripe URL or commercial price;
- every compatibility route resolves to an intentional final destination.
