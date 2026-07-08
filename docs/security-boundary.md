# Security Boundary

This repository is intentionally safe for public viewing. It demonstrates skill without publishing the production Simpl Ops implementation.

## Included Publicly

- High-level architecture documentation
- Generic event-driven workflow examples
- Fake sample data
- Safe placeholder signal logic
- Streamlit dashboard mockup
- Public case-study documentation
- Tradeoff and design-decision notes
- Tests for the public demo logic

## Excluded From Public Repo

- Production dashboard code
- Live data source URLs
- Integration IDs
- API keys or secrets
- Webhook URLs
- Dashboard tokens or access-control values
- Real client names, emails, activity, revenue, or records
- Make.com blueprints and exact scenario logic
- Stripe implementation notes
- Proprietary scoring, prioritization, or recovery logic
- Private prompts or advisory logic
- Internal operations docs
- Deployment infrastructure details

## Public Documentation Principle

The public repo should answer:

> “Can this person design, document, and reason about a real system?”

It should not answer:

> “How exactly can I rebuild this person’s product?”

## Security Review Applied

Before publication, the repo was reviewed for:

- Hardcoded secrets
- Live URLs or webhook endpoints
- Real customer or business data
- Proprietary implementation details
- Production filenames that could imply private structure
- Overly specific workflow, scoring, or routing logic

## Hiring Manager Note

This boundary is intentional. It demonstrates practical security judgment: the ability to show meaningful work while protecting production systems, customers, and business-critical intellectual property.
