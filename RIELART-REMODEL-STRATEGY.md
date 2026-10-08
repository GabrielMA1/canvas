# RielArt Remodel Strategy

## Decision

RielArt will present one simple commercial sequence:

1. Build the brand.
2. Launch the website.
3. Reach potential customers.

The public website will sell exactly two primary services:

- **Brand & Website Launch — $599 USD one time**
- **Focused Ads Management — $349 USD per month**

These services are separate. A qualified business may buy either service or both. The website will not create a third bundle or publish a Stripe checkout until an approved payment link exists.

The sole approved optional setup is **Business Email & Workspace Setup — from $149 USD one time**. It remains visually and commercially subordinate to the two primary services and does not expand RielArt into managed IT or a broad add-on catalogue.

## Five-second message

**Headline:** Build your brand. Launch your website. Reach more customers.

**Supporting message:** RielArt creates clear brands and professional websites for growing businesses, then helps bring the right people to them through managed online advertising.

**Market statement:** Serving businesses in the United States, Canada, and selected international markets.

The primary action is **Get Started**, which opens the general inquiry. Pricing is the secondary action.

## Audience and positioning

The primary audience is an owner or decision-maker at a growing service business who needs a credible online presence, focused customer acquisition, or both. Copy should be understandable without design, development, automation, or advertising expertise.

RielArt will be presented as a professional company with:

- clear scope and straightforward pricing;
- brand, website, and advertising decisions planned in one direction;
- organized delivery through the Client Portal;
- client-owned accounts, assets, and data;
- transparent third-party costs;
- practical measurement and reporting.

The website must not imply a U.S. office, Canadian office, global team, particular team size, unsupported results, or founder-led delivery. The public site does not publish a street or mailing address and must not invent a replacement location. Legal and policy questions route to `hello@rielart.com`.

## Information architecture

Primary navigation:

- Services dropdown: All Services, the two primary services, and the Google/Meta advertising explanations
- Work
- Pricing
- Learn dropdown: How It Works, About RielArt, Insights, and FAQ
- Contact
- Client Portal
- Get Started

The Services and Learn dropdowns organize the existing routes without adding commercial offers. `/services/` remains the consolidated explanation page. Two detailed service routes support evaluation and search intent without creating additional primary offers:

- `/services/brand-website-launch/`
- `/services/focused-ads-management/`

Google Search Ads and Meta Ads are explanatory sections within the Focused Ads Management route, not separate packages.

## Homepage plan

Updated October 8, 2026 for the "Printed in one ink" redesign. The order follows the customer's questions, and the prices are no longer buried:

1. Hero — the approved headline, supporting message, **Get Started** and **View Pricing**, plus a price list that names both services with their prices (Brand & Website Launch $599; Focused Ads Management $349/month, ad spend separate). This deliberately reverses the September "no prices in the hero" decision: published pricing is RielArt's clearest differentiator.
2. The business problem ("Your business should look as professional online as the work you provide.") — the former three-step sequence was removed from the homepage because it repeated the headline line for line; it remains on About.
3. Two services as one price board
   - Compact Business Email & Workspace Setup callout—not a third card
4. Truthful operational reasons to choose RielArt (`#why-rielart`): three lead commitments (flat fee, client ownership, creative included) set large, five supporting points beneath
5. Google or Meta explanation
6. Four-step process, with a compact Client Portal strip
7. Accurately labelled work
8. Ten concise FAQs
9. Final project CTA

## Content principles

- Lead with the business outcome, then explain scope.
- Use short paragraphs and selective lists.
- Keep the two prices and payment structures consistent.
- Explain advertising budget separately from RielArt’s management fee.
- Recommend Google or Meta after reviewing the business; do not force the visitor to decide.
- Label completed work, internal work, concepts, and solution models accurately.
- Preserve useful AI articles as educational content, but remove AI as a primary offer.
- Use one concise no-guarantee statement where it is contextually useful.
- Avoid artificial urgency, unsupported social proof, and performance promises.
- Present Business Email & Workspace Setup as the one approved optional setup. Present other work beyond the two primary services only as a separately reviewed custom-scope inquiry, never as another package or priced add-on catalogue.

## Visual principles

Preserve the RielArt logo, premium blue-and-navy language, light/dark themes, responsive behaviour, accessible focus states, and reduced-motion support.

Typography is self-hosted Archivo (all UI, headings, and prices; condensed widths for statements) with Newsreader for article body text only (both SIL OFL 1.1). The visual system is "Printed in one ink" (see `REDESIGN-NOTES.md`):

- one ink: the logo's deep ultramarine used flat, as full fields with paper-coloured type and as the colour of prices, links, and focus — no gradients outside the logo;
- warm paper and a deeper warm paper for panels; dark mode as a designed counterpart;
- one signature device, the dotted price-list leader, used only where something has a price;
- square corners; rules instead of cards; a heavy rule only on price boards and scope boundaries;
- small labels above headings only where they carry information (optional setup, work classification, article category);
- clear tables and accordions where comparison or detail benefits from them.

## Conversion flow

All commercial CTAs lead to `/contact/`.

- **Start Your Launch** preselects Brand & Website Launch.
- **Start Advertising** preselects Focused Ads Management and reveals the advertising questions.
- **Get Started** opens the general inquiry form.
- **Ask About Business Email** uses `/contact/?service=business-email-workspace#project-inquiry`, maps the primary choice to “I am not sure yet,” checks the separate optional setup field, and preserves `Business Email & Workspace Setup inquiry` as form context.
- **Ask About a Custom Scope** uses `/contact/?service=custom-scope#project-inquiry`, maps to “I am not sure yet,” and preserves the separate inquiry context without creating another primary service.

The form submits to the existing Formspree endpoint and returns to the existing thank-you route. The thank-you page explains review, recommendation, fit, onboarding, access, and payment steps without implying automatic acceptance.

## Technical approach

- Preserve dependency-free static HTML, CSS, and JavaScript.
- Preserve the Client Portal, theme toggle, mobile menu, skip link, keyboard support, Formspree, email, LinkedIn, and approved Calendly use.
- Use canonical URLs, matching sitemap entries, accurate structured data, and local fallback redirect pages.
- Keep third-party checkout configuration internal until approved links exist.
- Extend the existing audit and smoke-test scripts instead of adding a new build chain.

## Baseline recorded on 2026-07-27

- Existing static audit: 30 HTML files, 25 indexable URLs, 25 sitemap URLs, 35 JSON-LD blocks, 2 forms, 4 redirects, 0 warnings, 0 critical failures.
- Local HTTP smoke crawl: 32 routes checked, 31 successful HTTP routes, 29 HTML routes, 435,330 HTML response bytes, 0 failures.
- Existing public commercial model: five service categories and six Stripe-linked offers.
- Existing public offer prices include $497, $247, $149/month, $249/month, $399/month, and $699/month.

The previous audit passed its own rules, but those rules describe the superseded offer model and therefore must be replaced.

## Completion criteria

The remodel is complete when:

- the public site consistently presents exactly two primary services plus the one approved subordinate Business Email & Workspace Setup;
- all commercial CTAs use the inquiry flow;
- old public Stripe links and outdated commercial prices are absent;
- advertising scope, limits, ownership, spend, and commitment are clear;
- legacy routes remain intentional and non-broken;
- metadata, structured data, canonicals, sitemap, and visible copy agree;
- automated and manual QA results are recorded without overstating browser or tool coverage;
- the global CTA is **Get Started**, and no public street or mailing address is present.
