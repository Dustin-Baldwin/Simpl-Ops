# Sanitized Data Model

This document describes a public-safe data model that demonstrates the shape of the system without exposing production schemas, sensitive fields, real integrations, or customer records.

## Portfolio-Safe Tables

### `clients_demo`

Represents fake companies used only for demonstration.

| Field | Type | Description |
|---|---:|---|
| client_id | string | Fake demo identifier |
| business_type | string | Generic service category |
| market | string | Fictional or broad market label |
| active | boolean | Demo status flag |

### `operational_snapshots_demo`

Represents weekly fake activity snapshots.

| Field | Type | Description |
|---|---:|---|
| client_id | string | Fake demo identifier |
| business_type | string | Generic service category |
| week_start | date | Start of the fake sample week |
| leads | integer | Fake activity count |
| bookings | integer | Fake booking count |
| available_slots | integer | Fake capacity measure |
| completed_jobs | integer | Fake completion count |
| follow_up_tasks | integer | Fake open follow-up count |
| avg_response_hours | float | Fake response-time measure |

### `signals_demo`

Represents safe signal outputs generated from fake data.

| Field | Type | Description |
|---|---:|---|
| client_id | string | Fake demo identifier |
| signal_name | string | Generic public signal category |
| status | string | `healthy`, `watch`, or `attention` |
| value | float | Demo calculation result |
| summary | string | Owner-readable safe output |

## Why the Real Schema Is Not Published

A production schema may reveal implementation strategy, prioritization model, workflow boundaries, integration assumptions, or proprietary product design. For that reason, this public repo uses a simplified fake model that demonstrates engineering structure without giving away the actual system design.
