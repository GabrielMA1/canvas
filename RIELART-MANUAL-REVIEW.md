# RielArt Remodel - Manual Review Register

**Prepared:** July 27, 2026  
**Purpose:** Record legal, owner, account, privacy, and operational decisions that cannot be verified from the static repository alone.

This register is an implementation handoff, not legal advice. The public Privacy Policy and Terms describe the intended operating model but require review against actual agreements, accounts, data flows, target markets, and business practices before launch.

## Confirmed repository facts

- The public website is static and currently uses local storage to remember the light or dark theme.
- No analytics platform, Google advertising tag, Meta Pixel, or Conversions API implementation is active in the static public-site source reviewed for this remodel.
- Contact forms use Formspree and currently route successful submissions to `/thanks/`.
- Calendly is an optional outbound scheduling service.
- The Client Portal, Cloudflare infrastructure, Resend login email, and Stripe billing references already appear in the site's privacy disclosures.
- The approved commercial model has two public services:
  - Brand & Website Launch - $599 USD one time.
  - Focused Ads Management - $349 USD per month with a three-month initial commitment.
- Advertising spend is separate and is paid by the client directly to Google or Meta.
- No public Stripe checkout or subscription link is approved for the remodeled offers.

These facts must be rechecked against the deployed production site and relevant provider accounts before release.

## P0 - Release-blocking legal and owner decisions

### 1. Contracting identity, location, and governing terms

Confirm with the owner and qualified counsel:

- the legal entity or individual entering client agreements;
- whether and how the RielArt operating name should be stated;
- the approved use of the Richmond, British Columbia business mailing address;
- the relationship between the Toronto operating identity and the Richmond mailing address;
- governing law, venue, dispute process, and required business-identification disclosures;
- whether any U.S., Canadian provincial, or selected international consumer-protection rules apply.

Do not describe RielArt as U.S.-based, as having a U.S. office, or as operating from offices that do not exist. Do not add LocalBusiness schema or office claims without verified facts.

### 2. Brand & Website Launch agreement

The agreement must confirm:

- payment timing, taxes, refunds, cancellations, and charge disputes;
- when the estimated three-to-five-week schedule begins and what pauses it;
- the approved four-page structure and what counts as a page;
- client content, access, feedback, and approval responsibilities;
- the limits of messaging guidance and copywriting;
- the exact brand and website file handoff;
- ownership, licences, portfolio permission, and third-party assets;
- what counts as the included revision round;
- treatment of hosting, domains, premium software, plugins, fonts, and stock assets;
- change-request and out-of-scope approval procedures.

The public $599 description is not a substitute for these terms.

### 3. Focused Ads Management commercial terms

The advertising agreement must settle, without relying on assumptions:

- when the $349 monthly fee is first charged;
- when the three-month initial commitment begins;
- whether billing is monthly in advance or in arrears;
- renewal after the initial period;
- cancellation notice and effective date;
- pauses, suspensions, late or failed payments, refunds, and charge disputes;
- early termination and any remaining payment obligation;
- what happens when the client removes access or stops platform funding;
- the handoff process and date on which RielArt access is removed;
- support channel, response expectations, and the monthly review-call process;
- approval and pricing for work outside the standard scope.

Do not imply month-to-month renewal, easy cancellation, automatic renewal, or refund rights until the agreement establishes them and counsel confirms the required disclosure and consent process.

### 4. Advertising-account ownership and access

Confirm the operating procedure for each platform:

- Google Ads Manager Account linking for existing client-owned accounts;
- Meta business partner or task access for client-owned assets;
- the minimum permissions RielArt needs;
- which party creates a new account and who is its initial administrator;
- business, advertiser, domain, billing, and identity-verification responsibilities;
- the process for lost access, account restrictions, appeals, or recovery;
- offboarding and confirmation that the client retains an administrator;
- secure storage and removal of exported reports or local account information.

RielArt should not request personal passwords. A client account should not be created under RielArt ownership when it should belong to the client. Any exceptional need for administrative ownership requires express approval and documentation.

### 5. Advertising spend, payment methods, and platform charges

Confirm that the client:

- adds and controls the Google or Meta payment method;
- is the party charged by the platform;
- is responsible for sufficient funding, taxes, currency conversion, and billing disputes;
- understands that platform charges can vary with delivery and platform billing rules;
- approves the campaign budget and any later change.

Confirm how RielArt responds to failed charges, exhausted funding, platform over-delivery, spend caps, budget changes, and accidental or unauthorized changes. The approximately $500 monthly budget reference is not a sufficiency promise or a lead guarantee.

### 6. Privacy-law roles and client data

Qualified privacy counsel should determine RielArt's role for each data flow, including whether RielArt acts as a controller/business, processor/service provider, independent business, or another legally defined role.

Review:

- contact-form and inquiry information;
- Client Portal data;
- campaign-account and performance data;
- website events and conversion records;
- lead-form submissions and call-event information;
- customer lists, enhanced conversions, offline conversions, or advanced matching if later proposed;
- client-provided audiences or customer information;
- data-subject request handling;
- confidentiality, security, breach notice, retention, deletion, and audit obligations;
- provider and cross-border processing terms.

Use a data-processing addendum when required. Do not send names, email addresses, form messages, or sensitive inquiry content to analytics or advertising platforms unless a documented, lawful, and approved implementation specifically requires it.

### 7. Cookies, tags, pixels, and consent

No analytics or advertising-measurement technology is currently active in the reviewed static public-site source. Before enabling any technology on RielArt's site, approve:

- the exact platform and purpose;
- the events and parameters collected;
- whether advertising measurement, remarketing, or audience creation is involved;
- applicable jurisdictions and consent requirements;
- a consent-management method where required;
- default consent state and withdrawal controls;
- IP, location, retention, Google Signals, data-sharing, and user-provided-data settings;
- provider contracts and policy wording;
- performance, accessibility, and failure behavior;
- owner and recovery access to the measurement accounts.

Update the Privacy Policy to present-tense facts at activation. Do not leave a policy saying a tag "may" be used while deploying an undisclosed active implementation, and do not claim that a pixel or tag is active before it is installed and tested.

Client-site tracking requires a separate review of the client's privacy notice, cookie controls, platform, target markets, and legal instructions. The existence of RielArt's own Privacy Policy does not satisfy a client's obligations.

### 8. Campaign claims, assets, approvals, and platform policies

The agreement should allocate responsibility for:

- truth and substantiation of business, price, result, testimonial, comparison, and promotional claims;
- licences and permissions for logos, photos, videos, fonts, trademarks, music, and other supplied assets;
- offer conditions, availability, refunds, disclaimers, and landing-page accuracy;
- campaign, copy, creative, audience, location, and budget approvals;
- privacy notices and consent for lead collection and measurement;
- platform-policy compatibility and advertiser verification;
- responding to comments, messages, complaints, and leads;
- changes made by the client or another provider during active management.

RielArt should retain a documented right to decline, pause, or require correction of unsupported, unsafe, unlawful, misleading, or policy-incompatible material. Counsel should approve the language; it does not eliminate RielArt's own legal or professional responsibilities.

### 9. Regulated and sensitive advertising

Decide whether the standard service excludes or separately reviews:

- health, medical, mental-health, and pharmaceutical claims;
- credit, financial services, insurance, and investment offers;
- housing, employment, and other restricted targeting categories;
- alcohol, cannabis, gambling, weapons, and age-restricted products;
- political, election, or social-issue advertising;
- advertising directed to children or involving minors' data;
- legal services or other jurisdiction-regulated professions;
- sensitive personal information, uploaded customer lists, or inferred traits.

Do not accept one of these engagements solely because the platform interface permits campaign creation.

### 10. Website-edit allowance and third-party websites

Operational terms must define:

- how the included hour is measured and recorded;
- whether there is a minimum billing increment;
- the monthly reset date and confirmation that unused time does not roll over;
- who prioritizes work when requests exceed the allowance;
- the approval path and price for additional work;
- required backups, staging, rollback, and access;
- responsibility for licences, plugins, themes, hosting, security, and pre-existing defects;
- work RielArt may refuse because it cannot be completed safely;
- client approval before changes to claims, forms, tracking, or privacy controls.

Confirm whether the hour is an effort allowance rather than a guaranteed number of completed changes, and state that distinction in the agreement if intended.

## P0 - Provider and integration verification

### 11. Formspree

After the remodeled inquiry fields are live, run an owner-authorized production test and verify:

- delivery to the intended mailbox;
- the exact approved endpoint remains in use;
- service interest and conditional advertising fields arrive correctly;
- hidden conditional fields are not submitted with misleading values;
- the "not sure" options remain valid;
- the consent value and privacy link are present;
- reply-to, spam controls, rate limits, duplicate handling, and failure recovery;
- the `/thanks/` redirect;
- Formspree account ownership, retention, deletion, and notification settings.

Add a concise just-in-time disclosure near the form that Formspree processes the submission. The Privacy Policy alone may not provide sufficient notice for every jurisdiction.

### 12. Calendly

Confirm:

- the scheduling URL and account owner;
- whether scheduling remains part of the new inquiry flow;
- Calendly's current cookie, storage, retention, and international-processing behavior;
- the appropriate just-in-time disclosure before the visitor opens Calendly;
- whether the existing `hide_gdpr_banner=1` parameter remains appropriate for the intended markets.

### 13. Stripe and future payment links

Remove obsolete public checkout and subscription links for legacy offers. Preserve old URLs only in internal records where necessary.

Before adding a future payment link:

- use the documented private configuration location;
- verify product name, price, USD currency, one-time or monthly cadence, taxes, and customer statement descriptor;
- confirm agreement acceptance occurs before or as part of payment;
- verify renewal, cancellation, refund, receipt, success, and cancellation behavior;
- verify notification, onboarding, and Client Portal handoff;
- test without completing an unauthorized real charge.

The Privacy Policy may name Stripe for approved client billing where applicable, but public copy must not imply that a current checkout is available when it is not.

### 14. Cloudflare, Resend, and Client Portal

Confirm current account ownership, subprocessors, data locations, retention, authentication, access logs, security contacts, recovery access, and incident-handling procedures. Portal content and provider records must match the accepted agreement and actual service delivery.

## P1 - International, reporting, and operational decisions

### 15. International service limits

The standard advertising service includes one country or one clearly defined regional market, one language, and one primary offer.

Before accepting a selected international market, review:

- platform and payment availability;
- advertising, consumer, privacy, cookie, and direct-marketing requirements;
- sanctions, restricted-party, and prohibited-product concerns;
- language capability and who approves translations;
- local claims, disclosures, currencies, taxes, time zones, and landing pages;
- data-transfer and data-location implications;
- whether local counsel or a specialist is required.

Do not use "worldwide agency," "global offices," "international team," or language implying unlimited international management.

### 16. Reporting and attribution

Define:

- source platform, reporting period, timezone, and currency;
- the meaning of a lead, conversion, qualified inquiry, sale, and revenue;
- attribution window and model;
- handling of delayed, duplicated, modeled, invalid, or unverified conversions;
- platform-versus-analytics discrepancies;
- whether phone-call events identify callers or record calls;
- report retention and access after termination.

Reports should distinguish platform-reported events from verified business outcomes. A monthly summary is not an independent financial or performance audit.

### 17. Phone-call tracking

Before enabling phone-call conversion tracking, confirm:

- whether only call events or actual recordings are collected;
- number ownership and portability;
- caller notice and consent requirements in every target jurisdiction;
- retention, access, security, and deletion;
- provider terms and subprocessors;
- offboarding and restoration of the client's normal telephone path.

Do not record calls unless the legal, technical, and notice requirements have been separately approved.

### 18. Conversions API and advanced integrations

The standard Meta scope includes only a review of Conversions API where supported. Before implementation, document:

- event source and exact data fields;
- lawful basis and required consent;
- data minimization and hashing behavior;
- event deduplication;
- server, gateway, or partner ownership;
- access, security, retention, and deletion;
- test-versus-production separation;
- platform terms and data-use restrictions.

Enhanced conversions, offline conversion imports, CRM implementation, Customer Match, custom audiences, and advanced funnel systems require separate scope and legal/privacy review.

## Release verification

Before publishing the legal updates:

1. Have the owner review every operational statement against actual practice.
2. Have qualified counsel review the Privacy Policy, Terms, service agreement, data-processing terms, and international/consent decisions.
3. Confirm that public pages contain only the two approved offers and prices.
4. Confirm all obsolete public Stripe links are removed.
5. Confirm the Privacy Policy does not say a tag or pixel is active.
6. Confirm no tag or pixel has been added without the approved consent and policy work.
7. Confirm Google and Meta account-access procedures preserve client ownership.
8. Confirm advertising spend is visibly separate from the RielArt fee.
9. Confirm the three-month commitment and no-guarantee wording match the agreement.
10. Test Formspree, the thank-you route, Calendly if retained, the Client Portal, privacy and terms links, keyboard access, mobile layout, and 200% zoom.
11. Record the reviewer, decision date, evidence, and any accepted risk for every item closed in this register.

## Approval record

| Area | Decision owner | Status | Evidence or decision date |
|---|---|---|---|
| Contracting identity and address | Owner / counsel | Open | |
| Brand & Website Launch agreement | Owner / counsel | Open | |
| Focused Ads commitment and renewal | Owner / counsel | Open | |
| Google account-access procedure | Owner | Open | |
| Meta account-access procedure | Owner | Open | |
| Platform billing and budget procedure | Owner | Open | |
| Privacy roles and data-processing terms | Privacy counsel | Open | |
| RielArt-site analytics and consent | Owner / privacy counsel | Open | |
| Client-site tracking procedure | Owner / privacy counsel | Open | |
| Regulated-industry acceptance policy | Owner / counsel | Open | |
| Website-edit operational terms | Owner | Open | |
| Formspree production delivery | Owner | Open | |
| Calendly disclosure and configuration | Owner / privacy counsel | Open | |
| Future Stripe configuration | Owner | Open | |
| International-market acceptance process | Owner / counsel | Open | |
| Final Privacy Policy and Terms approval | Qualified counsel | Open | |
