from main import detect_missed_heartbeat


EXPECTED_INTERVAL = 60
ALLOWED_MISSES = 3


def test_working_test_case():
    events = [
        {"service": "email", "timestamp": "2025-08-04T10:00:00Z"},
        {"service": "email", "timestamp": "2025-08-04T10:01:00Z"},
        {"service": "email", "timestamp": "2025-08-04T10:02:00Z"},
        {"service": "email", "timestamp": "2025-08-04T10:06:00Z"},
    ]

    res = detect_missed_heartbeat(events, EXPECTED_INTERVAL, ALLOWED_MISSES)

    assert res == [{"service": "email", "alert_at": "2025-08-04T10:03:00Z"}]


def test_near_miss_test_case():
    events = [
        {"service": "email", "timestamp": "2025-08-04T10:00:00Z"},
        {"service": "email", "timestamp": "2025-08-04T10:01:00Z"},
        {"service": "email", "timestamp": "2025-08-04T10:02:00Z"},
        {"service": "email", "timestamp": "2025-08-04T10:05:00Z"},
    ]

    res = detect_missed_heartbeat(events, EXPECTED_INTERVAL, ALLOWED_MISSES)

    assert res == []
