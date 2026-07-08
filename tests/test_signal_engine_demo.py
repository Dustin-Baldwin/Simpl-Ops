from examples.signal_engine_demo import OperationalSnapshot, evaluate_snapshot


def test_evaluate_snapshot_returns_three_demo_signals():
    snapshot = OperationalSnapshot(
        client_id="DEMO-001",
        business_type="HVAC",
        leads=40,
        bookings=20,
        available_slots=30,
        completed_jobs=21,
        follow_up_tasks=8,
        avg_response_hours=6.5,
    )

    results = evaluate_snapshot(snapshot)

    assert len(results) == 3
    assert {result.signal_name for result in results} == {
        "Booking Movement Demo",
        "Capacity Pressure Demo",
        "Follow-Up Load Demo",
    }


def test_attention_status_for_low_booking_movement():
    snapshot = OperationalSnapshot(
        client_id="DEMO-LOW",
        business_type="Roofing",
        leads=30,
        bookings=5,
        available_slots=20,
        completed_jobs=10,
        follow_up_tasks=4,
        avg_response_hours=3.0,
    )

    results = evaluate_snapshot(snapshot)
    booking = next(r for r in results if r.signal_name == "Booking Movement Demo")

    assert booking.status == "attention"


def test_attention_status_for_high_follow_up_load():
    snapshot = OperationalSnapshot(
        client_id="DEMO-FOLLOWUP",
        business_type="Cleaning",
        leads=30,
        bookings=20,
        available_slots=35,
        completed_jobs=20,
        follow_up_tasks=25,
        avg_response_hours=8.0,
    )

    results = evaluate_snapshot(snapshot)
    follow_up = next(r for r in results if r.signal_name == "Follow-Up Load Demo")

    assert follow_up.status == "attention"
