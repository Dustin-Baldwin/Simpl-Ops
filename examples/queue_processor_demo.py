"""Portfolio-safe queue processor demo.

This is a minimal example of event-driven thinking. It is not connected to any
production workflow, webhook, automation service, customer account, or private
Simpl Ops routing logic.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Callable, Literal
from uuid import uuid4

JobStatus = Literal["pending", "processing", "completed", "failed"]
EventHandler = Callable[[dict[str, Any]], dict[str, Any]]


@dataclass
class DemoJob:
    """A fake job record for the public queue demo."""

    event_type: str
    payload: dict[str, Any]
    job_id: str = field(default_factory=lambda: str(uuid4()))
    status: JobStatus = "pending"
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    processed_at: datetime | None = None
    error: str | None = None
    result: dict[str, Any] | None = None


class DemoQueue:
    """Small in-memory queue used only for the public portfolio demo."""

    def __init__(self) -> None:
        self.jobs: list[DemoJob] = []
        self.handlers: dict[str, EventHandler] = {}

    def register_handler(self, event_type: str, handler: EventHandler) -> None:
        self.handlers[event_type] = handler

    def enqueue(self, event_type: str, payload: dict[str, Any]) -> DemoJob:
        job = DemoJob(event_type=event_type, payload=payload)
        self.jobs.append(job)
        return job

    def next_pending(self) -> DemoJob | None:
        return next((job for job in self.jobs if job.status == "pending"), None)

    def process_next(self) -> DemoJob | None:
        job = self.next_pending()
        if job is None:
            return None

        job.status = "processing"
        try:
            if not job.payload:
                raise ValueError("Payload is empty")

            handler = self.handlers.get(job.event_type, default_demo_handler)
            job.result = handler(job.payload)
            job.status = "completed"
            job.processed_at = datetime.now(timezone.utc)
        except Exception as exc:  # noqa: BLE001 - demo captures processing failure
            job.status = "failed"
            job.error = str(exc)
        return job


def default_demo_handler(payload: dict[str, Any]) -> dict[str, Any]:
    """Return a safe placeholder result for a fake event payload."""

    return {
        "accepted": True,
        "client_id": payload.get("client_id", "UNKNOWN"),
        "message": "Processed by public demo handler.",
    }


if __name__ == "__main__":
    queue = DemoQueue()
    queue.enqueue("weekly_owner_update_received", {"client_id": "DEMO-001"})
    processed = queue.process_next()
    print(processed)
