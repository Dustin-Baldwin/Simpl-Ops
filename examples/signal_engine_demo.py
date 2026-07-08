"""Portfolio-safe signal engine demo.

This module intentionally uses fake data and generic placeholder formulas. It is
not the production Simpl Ops signal engine and does not include proprietary
thresholds, scoring logic, prompts, customer workflows, or recovery rules.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

SignalStatus = Literal["healthy", "watch", "attention"]


@dataclass(frozen=True)
class OperationalSnapshot:
    """Fake weekly activity snapshot used by the public demo."""

    client_id: str
    business_type: str
    leads: int
    bookings: int
    available_slots: int
    completed_jobs: int
    follow_up_tasks: int
    avg_response_hours: float


@dataclass(frozen=True)
class SignalResult:
    """Public-safe signal output for the demo dashboard."""

    client_id: str
    signal_name: str
    status: SignalStatus
    value: float
    summary: str


def _safe_ratio(numerator: int | float, denominator: int | float) -> float:
    """Return a rounded ratio while avoiding division-by-zero errors."""

    if denominator == 0:
        return 0.0
    return round(float(numerator) / float(denominator), 2)


def evaluate_booking_movement(snapshot: OperationalSnapshot) -> SignalResult:
    """Evaluate a generic bookings-to-leads ratio using public demo thresholds."""

    ratio = _safe_ratio(snapshot.bookings, snapshot.leads)

    if ratio >= 0.55:
        status: SignalStatus = "healthy"
        summary = "Booking movement is strong relative to demo activity volume."
    elif ratio >= 0.35:
        status = "watch"
        summary = "Booking movement is acceptable but worth monitoring."
    else:
        status = "attention"
        summary = "Booking movement appears low relative to demo activity volume."

    return SignalResult(
        client_id=snapshot.client_id,
        signal_name="Booking Movement Demo",
        status=status,
        value=ratio,
        summary=summary,
    )


def evaluate_capacity_pressure(snapshot: OperationalSnapshot) -> SignalResult:
    """Evaluate a generic completed-jobs-to-capacity ratio."""

    ratio = _safe_ratio(snapshot.completed_jobs, snapshot.available_slots)

    if ratio >= 0.9:
        status: SignalStatus = "attention"
        summary = "Capacity appears tight in the demo snapshot."
    elif ratio >= 0.7:
        status = "watch"
        summary = "Capacity usage is elevated but not yet critical in the demo snapshot."
    else:
        status = "healthy"
        summary = "Capacity appears available for additional demo work."

    return SignalResult(
        client_id=snapshot.client_id,
        signal_name="Capacity Pressure Demo",
        status=status,
        value=ratio,
        summary=summary,
    )


def evaluate_follow_up_load(snapshot: OperationalSnapshot) -> SignalResult:
    """Evaluate generic follow-up pressure with intentionally simple logic."""

    value = float(snapshot.follow_up_tasks)

    if snapshot.follow_up_tasks >= 20 or snapshot.avg_response_hours >= 24:
        status: SignalStatus = "attention"
        summary = "Follow-up load may need attention in the public demo snapshot."
    elif snapshot.follow_up_tasks >= 10 or snapshot.avg_response_hours >= 12:
        status = "watch"
        summary = "Follow-up load is moderate in the public demo snapshot."
    else:
        status = "healthy"
        summary = "Follow-up load appears manageable in the public demo snapshot."

    return SignalResult(
        client_id=snapshot.client_id,
        signal_name="Follow-Up Load Demo",
        status=status,
        value=value,
        summary=summary,
    )


def evaluate_snapshot(snapshot: OperationalSnapshot) -> list[SignalResult]:
    """Run all public-safe demo checks for a fake operational snapshot."""

    return [
        evaluate_booking_movement(snapshot),
        evaluate_capacity_pressure(snapshot),
        evaluate_follow_up_load(snapshot),
    ]
