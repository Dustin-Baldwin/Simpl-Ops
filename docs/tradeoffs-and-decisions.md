# Tradeoffs and Engineering Decisions

This document explains the reasoning behind the public architecture and the types of decisions made while building Simpl Ops.

## Decision 1: Start Lightweight Before Overbuilding

A small-business SaaS MVP benefits from fast iteration. A lightweight dashboard and simple data layer can validate the workflow before investing in a larger database, account system, or enterprise integration layer.

**Tradeoff:** lightweight tools can create scaling limits.

**Mitigation:** design clear event boundaries and queue-like processing so the system can migrate later without changing the entire product concept.

## Decision 2: Event-Driven Workflow Instead of Static Reporting

Static dashboards show information. Event-driven workflows can react to changes and push owner attention toward the next useful action.

**Tradeoff:** event routing creates more moving parts.

**Mitigation:** keep event names clear, normalize inputs, and separate intake from processing.

## Decision 3: Owner-Readable Outputs Over Analyst-Only Metrics

The target user often needs an answer, not a spreadsheet. Signals must be translated into plain language and prioritized.

**Tradeoff:** summarization can oversimplify nuance.

**Mitigation:** preserve supporting context behind each recommendation and allow deeper inspection when needed.

## Decision 4: Public Portfolio Replica Instead of Production Code

Publishing the real implementation would create unnecessary business risk. A safe replica can still show engineering maturity, product thinking, and code quality.

**Tradeoff:** the public repo is less complete than the private system.

**Mitigation:** include strong documentation, realistic fake data, safe demo code, tests, diagrams, and explicit security boundaries.

## Decision 5: Generic Demo Logic Instead of Product Logic

The public code uses simple placeholder formulas because the goal is to demonstrate code structure, typing, testing, and workflow design—not to publish the product’s private decision model.

**Tradeoff:** the demo logic is intentionally less powerful than the private product.

**Mitigation:** explain the boundary clearly and keep the public examples focused on maintainability and reviewability.
