# RielArt Measurement Plan

**Prepared:** 2026-07-27  
**Current state:** No analytics or advertising measurement platform detected. Nothing was installed during this audit.

## Measurement objective

Measure whether qualified visitors understand the offer, reach the most relevant service, and complete an appropriate next step—without collecting form contents or inflating success with low-value clicks.

### Primary conversions

1. Successful project inquiry.
2. Successful free initial review request.
3. Authorized Stripe checkout completion, measured in Stripe or through a verified server/account integration rather than a simple outbound click.

### Secondary conversions

- Calendly consultation started/completed.
- Qualified email click.
- Service-page visit from an article.
- Pricing-package or subscription checkout click.
- Client Portal click by an existing client.

Outbound clicks are intent indicators, not completed business outcomes.

## Implementation principles

- Obtain owner approval for platform and consent requirements first.
- Use one maintainable event adapter, not scattered vendor calls.
- Keep event names stable and parameters low-cardinality.
- Never send names, emails, phone numbers, company names, URLs entered in forms, messages, budgets, free-text search, or other personal/sensitive values.
- Record the selected inquiry type only as `project` or `review`.
- Distinguish `click`, `attempt`, and verified `success`.
- Treat Client Portal and Stripe destinations as sensitive commercial flows; record only approved metadata.
- Preserve page performance and reduced-motion/accessibility behavior.
- Update the Privacy Policy before production measurement begins.

## Recommended event layer

After approval, add a small site-owned adapter such as:

```js
window.rielartMeasure?.("primary_cta_click", {
  page_path: window.location.pathname,
  cta_location: "hero",
  inquiry_intent: "project"
});
```

The site-owned function should validate an allowlist of event names/parameters and forward to the selected platform. Site components should never call a vendor-specific global directly.

## Event specification

| Event | Business objective | Trigger | Allowed parameters | Pages | Sensitivity | Test |
|---|---|---|---|---|---|---|
| `primary_cta_click` | Measure high-intent project navigation | Click on a primary “Start a Project” CTA | `page_path`, `cta_location`, `inquiry_intent=project` | Sitewide | Low | Debug event once per deliberate click; destination retains `inquiry=project` |
| `free_review_click` | Measure interest in the preliminary offer | Click on “Free Initial Review” | `page_path`, `cta_location`, `inquiry_intent=review` | Home, services, pricing, articles | Low | Event fires once; destination selects review |
| `contact_form_start` | Find form-entry drop-off | First interaction with a non-honeypot form control | `page_path`, `form_id`, `inquiry_intent` | Home, contact | Medium | One event per page/form session; no field value captured |
| `contact_form_attempt` | Measure submit attempts | Valid submit event immediately before native Formspree navigation | `page_path`, `form_id`, `inquiry_intent` | Home, contact | Medium | Fires only when native validation passes; do not test in production without authorization |
| `contact_form_error` | Identify validation friction | Native invalid event batch | `page_path`, `form_id`, `error_type=client_validation`, `invalid_field_count` | Home, contact | Medium | One batched event per attempt; never send field names/values if not needed |
| `contact_form_success` | Count completed inquiries | Landing on `/thanks/` with an approved non-PII success mechanism | `page_path`, `form_id`, `inquiry_intent` if safely preserved | Thanks | Medium | Confirm direct visits are excluded or separately classified |
| `calendly_click` | Measure scheduling intent | Click on approved Calendly link | `page_path`, `cta_location` | Home, contact | Low | One event and correct outbound URL |
| `client_portal_click` | Measure existing-client navigation, not acquisition | Click on Client Portal | `page_path`, `cta_location` | Sitewide | Medium | Exclude from lead conversion reporting |
| `pricing_package_click` | Compare offer interest | Click a pricing-card primary CTA | `page_path`, `package_id`, `billing_type` | Pricing | Medium | IDs use allowlisted slugs, never URL query/payment identifiers |
| `stripe_checkout_click` | Measure checkout intent | Click an approved Stripe link | `page_path`, `package_id`, `billing_type`, `currency=USD` | Pricing | Medium | Verify exactly one event and unchanged approved destination |
| `email_click` | Measure direct-contact intent | Click `mailto:hello@rielart.com` | `page_path`, `cta_location` | Sitewide | Low | Do not include the visitor’s email or message |
| `service_cta_click` | Understand service consideration | Click from a hub/related section to a service | `page_path`, `service_id`, `cta_location` | Home, services, portfolio, FAQ | Low | Destination and service ID agree |
| `blog_service_click` | Measure editorial-to-commercial flow | Click an article’s related-service CTA | `page_path`, `article_slug`, `service_id` | Articles | Low | Each article maps to its documented related service |
| `blog_filter_use` | Understand topic interest | Click a blog category filter | `page_path`, `category` | Blog | Low | Only canonical visible categories allowed |
| `blog_search_use` | Understand search adoption without collecting terms | First non-empty search state | `page_path`, `result_count_bucket` | Blog | Medium | Never send the search string |
| `outbound_social_click` | Measure LinkedIn interest | Click approved LinkedIn link | `page_path`, `network=linkedin`, `cta_location` | Sitewide/about/contact | Low | Correct outbound URL |
| `404_view` | Identify broken inbound paths | A real 404 response/view | `page_path`, `referrer_origin_category` | 404 | Medium | Strip query strings and full external referrers |

## Recommended parameters and values

Use allowlisted slugs:

- `cta_location`: `header`, `mobile_nav`, `hero`, `section`, `article_aside`, `footer`, `contact_shortcut`.
- `inquiry_intent`: `project`, `review`.
- `service_id`: `brand`, `web`, `automation`, `growth`, `audit`.
- `billing_type`: `one_time`, `monthly`, `custom`.
- `category`: `brand`, `web_ux`, `ai_automation`, `seo_analytics`, `operations`.
- `result_count_bucket`: `0`, `1_3`, `4_8`, `9_plus`.

Do not send full outbound URLs, Stripe tokens, Formspree IDs, or Client Portal account details as parameters.

## Funnel definitions

### Project inquiry

`primary_cta_click` → `contact_form_start` with `project` → `contact_form_attempt` → verified `contact_form_success`

### Free initial review

`free_review_click` → `contact_form_start` with `review` → `contact_form_attempt` → verified `contact_form_success`

### Direct package

Pricing view → `pricing_package_click`/`stripe_checkout_click` → verified Stripe completion from an authorized account source

Do not report an outbound Stripe click as revenue.

### Article-assisted inquiry

Article view → `blog_service_click` → service view → project/review CTA → verified form success

Use an attribution window approved for the selected platform; do not claim causal impact from a last-click path alone.

## Platform and consent decision

Before implementation, document:

- Selected analytics platform and account owner.
- Data region and retention.
- Consent mode/banner requirement by visitor jurisdiction.
- Whether advertising/remarketing is in scope.
- IP/location and user-signals settings.
- Cross-domain needs for Portal, Calendly, Stripe, and Formspree.
- Referral-exclusion strategy so third-party returns do not overwrite acquisition.
- Internal, developer, and test-traffic filters.
- Privacy Policy update and effective date.

GA4 is suitable when integration with Google Ads/Search data is genuinely needed and consent/configuration can be managed. A privacy-focused product can reduce data collection, but still requires a processor and consent review. The audit does not select a vendor for the owner.

## Search measurement

### Google Search Console

- Submit the canonical sitemap.
- Track indexed pages, exclusions, queries, countries, devices, Core Web Vitals, manual actions, and security issues.
- Annotate deployment dates and major page/offer changes.
- Review commercial pages separately from articles.

### Bing Webmaster Tools

- Submit the same sitemap.
- Review indexing, crawl issues, search terms, and backlinks.

### Monthly search report

- Qualified organic inquiries, not only clicks.
- Service-page impressions/clicks by intent.
- Article-to-service navigation.
- Queries with strong impressions but weak click-through.
- Pages with indexing or canonical changes.
- Field Core Web Vitals when sufficient data exists.

## QA procedure before release

1. Enable platform debug/test mode only.
2. Verify consent state before and after a user choice.
3. Test each event once on desktop and mobile.
4. Confirm allowed parameters and absence of personal data.
5. Confirm no duplicate event listeners or duplicate page views.
6. Confirm project/review intent remains correct.
7. Confirm direct `/thanks/` visits are not counted as verified submissions.
8. Confirm Stripe/Calendly/Portal links remain unchanged.
9. Confirm internal and test traffic can be excluded.
10. Compare network requests and performance before/after analytics.
11. Update the Privacy Policy and retain approval evidence.

## Reporting cadence

### Weekly during the first month

- Form attempts, errors, verified success, and delivery failures.
- Project versus review mix.
- Checkout click versus verified checkout.
- 404 paths and broken campaign URLs.
- Unexpected duplicate events.

### Monthly

- Qualified inquiries by landing-page group and service.
- Article-assisted commercial journeys.
- Pricing-package interest and verified purchases.
- Search visibility and indexed-page changes.
- Mobile versus desktop completion.
- Form validation rate.
- Performance/field Core Web Vitals.

### Quarterly

- Event usefulness and data minimization.
- Consent and policy accuracy.
- Account access/ownership.
- Retention and stale audiences.
- Whether each tracked event still supports a business decision.

