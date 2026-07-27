# rielart.com

Static, dependency-free production website for RielArt. Deploy the contents of this repository at the domain root.

## Site structure

- `index.html` — connected-system homepage with free-initial-review and project-inquiry form
- `services/` — service overview plus five detailed service routes
- `portfolio/` — clearly labeled representative solution models
- `process/` — five-phase delivery process and Client Portal overview
- `pricing/` — fixed-scope projects, monthly support, comparison tables, and live Stripe Payment Links
- `about/` — studio approach, team, and international service overview
- `blog/` — searchable, filterable Insights index and nine articles
- `faq/` — grouped service, process, pricing, ownership, AI, and support questions
- `contact/` — the same inquiry form used on the homepage
- `privacy-policy/`, `terms/` — legal pages
- `thanks/`, `404.html` — noindex utility pages
- `assets/css/site.css` — consolidated site design system
- `assets/js/site.js` — theme, navigation, FAQ, filter, reveal, and form behavior
- `tools/site_audit.py` — local static-site audit
- `tools/http_smoke.py` — local HTTP crawler for route, resource, and response checks
- `AUDIT-*.md`, `AUDIT-FINDINGS.json` — current production audit evidence and handoff
- `_config.yml` — prevents audit and development artifacts from being published by GitHub Pages

## Preserved production integrations

- Client Portal: `https://portal.rielart.com`
- Formspree: `https://formspree.io/f/xojrdoel`
- Thank-you destination: `https://rielart.com/thanks/`
- Consultation scheduling: `https://calendly.com/gabrielmacovei001/15min?hide_gdpr_banner=1`
- Email: `hello@rielart.com`
- LinkedIn: `https://www.linkedin.com/in/gabrielmacovei/`

The Pricing page preserves six live Stripe-hosted Payment Links:

- Digital Foundation — USD $497
- Focused Automation Setup — USD $247
- Digital Presence Care — USD $149/month
- AI Automation Care — USD $249/month
- Online Ads Management — USD $399/month
- Growth Systems Partner — USD $699/month

The custom Connected System remains inquiry-only.

## Local review

From the repository root, run a simple static server, for example:

```powershell
python -m http.server 4173
```

Then open the local address printed by the server.

Run the repository audit with:

```powershell
python tools/site_audit.py
```

With the local server still running, run the HTTP smoke test with:

```powershell
python tools/http_smoke.py --base-url http://127.0.0.1:4173
```

## Publishing checklist

- Review the Git diff in GitHub Desktop.
- Confirm current prices, scopes, billing terms, and third-party-cost notes.
- Test all six Stripe links in the intended Stripe mode.
- Confirm Formspree delivery and the `/thanks/` redirect.
- Confirm the Client Portal, email, LinkedIn, and scheduling destinations.
- Add only approved client proof, testimonials, and case-study results. Representative examples must remain labeled until real, permissioned work replaces them.

See `AUDIT-MASTER-REPORT.md`, `AUDIT-IMPLEMENTATION-LOG.md`, `AUDIT-MANUAL-REVIEW.md`, `AUDIT-MEASUREMENT-PLAN.md`, and `AUDIT-REGRESSION-REPORT.md` for the current production audit and implementation pass. These internal files remain in the repository but are excluded from the GitHub Pages build.
