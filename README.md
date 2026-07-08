# Simpl Ops — Public Portfolio Replica

**Simpl Ops** is an operational intelligence SaaS concept for service businesses. The private product is designed to help owners turn messy operational activity into clearer priorities, bottleneck visibility, and practical next actions.

This repository is a **public portfolio replica**. It is not the production Simpl Ops codebase. It was rebuilt with fake data, generic demo logic, and safe documentation so hiring managers can evaluate the engineering approach without exposing proprietary implementation details.

> **Why this repo exists:** the real Simpl Ops build contains private workflow design, production code, integration details, customer-facing logic, access-control patterns, and business-critical intellectual property. This public version demonstrates the same *types of engineering decisions*—event intake, normalization, queue processing, signal evaluation, dashboard presentation, testing, and documentation—without publishing anything that could be used to recreate the private system.

## What Hiring Managers Should Notice

- **Business-to-technical translation:** converts ambiguous owner pain into measurable operational categories and user-facing guidance.
- **Systems thinking:** models intake, normalization, queue processing, signal evaluation, and dashboard consumption.
- **Pragmatic MVP judgment:** shows how a lightweight SaaS workflow can be validated before a larger database-backed or enterprise-grade buildout.
- **Security judgment:** separates portfolio value from private production logic, customer data, live integrations, tokens, and workflow details.
- **Communication:** includes case-study documentation, architecture diagrams, tradeoff notes, and interview-ready explanations.

## Repository Map

```text
Simpl-Ops/
├── README.md
├── docs/
│   ├── product-case-study.md
│   ├── architecture-overview.md
│   ├── event-driven-workflow.md
│   ├── data-model-sanitized.md
│   ├── tradeoffs-and-decisions.md
│   ├── security-boundary.md
│   ├── hiring-manager-notes.md
│   └── portfolio-review-checklist.md
├── diagrams/
│   ├── architecture-flow.md
│   └── event-lifecycle.md
├── examples/
│   ├── __init__.py
│   ├── dashboard_mockup.py
│   ├── signal_engine_demo.py
│   ├── queue_processor_demo.py
│   └── data/no_pii_operational_sample.csv
├── tests/
│   ├── test_queue_processor_demo.py
│   └── test_signal_engine_demo.py
├── requirements.txt
├── .gitignore
└── GITHUB_UPLOAD_INSTRUCTIONS.md
```

## Public Demo Highlights

This replica includes:

- A Streamlit dashboard mockup using fake operational data
- A typed Python signal engine using generic placeholder formulas
- A small queue processor that demonstrates event-driven workflow thinking
- Sanitized sample data with no real clients, URLs, tokens, or business records
- Mermaid diagrams for architecture and event lifecycle
- Tests for the public demo logic
- Documentation written for both technical and non-technical review

## What Is Intentionally Not Included

This repo does **not** include:

- Production `app.py` or private dashboard code
- Live data source URLs, Sheet IDs, webhook URLs, tokens, API keys, or secrets
- Customer/client names, emails, activity, revenue, or operational records
- Make.com blueprints, exact automation routing, or private scenario logic
- Stripe implementation details or billing configuration
- Proprietary scoring logic, prioritization rules, recovery formulas, prompts, or advisory logic
- Production access-control patterns, deployment details, or internal operations docs

See [`docs/security-boundary.md`](docs/security-boundary.md) for the full public/private boundary.

## Run the Demo Locally

```bash
pip install -r requirements.txt
streamlit run examples/dashboard_mockup.py
```

Run the safe demo tests:

```bash
pytest
```

## Best Way to Review This Repo

Start with:

1. [`docs/product-case-study.md`](docs/product-case-study.md) — business problem and product thesis
2. [`docs/architecture-overview.md`](docs/architecture-overview.md) — system design pattern
3. [`examples/signal_engine_demo.py`](examples/signal_engine_demo.py) — typed demo logic
4. [`examples/queue_processor_demo.py`](examples/queue_processor_demo.py) — event-driven processing example
5. [`docs/tradeoffs-and-decisions.md`](docs/tradeoffs-and-decisions.md) — engineering judgment and tradeoffs

## Positioning for Employers

This repo is best viewed as a founder/operator technical portfolio project. It demonstrates the ability to understand a business problem, design a safe MVP, document system architecture, write clean Python examples, test logic, and protect sensitive implementation details while still showing meaningful technical work.
