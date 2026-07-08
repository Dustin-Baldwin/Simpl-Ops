from examples.queue_processor_demo import DemoQueue


def test_queue_processes_valid_demo_job():
    queue = DemoQueue()
    queue.enqueue("weekly_owner_update_received", {"client_id": "DEMO-001"})

    job = queue.process_next()

    assert job is not None
    assert job.status == "completed"
    assert job.result is not None
    assert job.result["accepted"] is True
    assert job.result["client_id"] == "DEMO-001"


def test_queue_marks_empty_payload_as_failed():
    queue = DemoQueue()
    queue.enqueue("weekly_owner_update_received", {})

    job = queue.process_next()

    assert job is not None
    assert job.status == "failed"
    assert job.error == "Payload is empty"
