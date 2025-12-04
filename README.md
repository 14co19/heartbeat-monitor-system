# Heartbeat-Monitor-System
An heartbeat alert service that detects when a service misses 3 consecutive expected heartbeats and raises a single alert per service.

An alert is triggered when:
(time gap between two received heartbeats) ≥ expected_interval_seconds × (allowed_misses + 1)

The alert timestamp is the **first missed heartbeat**, not the last received one.

---

## How "3 Missed Heartbeats" Is Defined

If:
- expected interval = 60 seconds
- allowed misses = 3

Then an alert triggers if:
gap ≥ 60 × (3 + 1) = 240 seconds

The alert time is:
last_received_time + expected_interval

---

## How Unordered Events Are Handled

All events are:
- Grouped by service
- Sorted chronologically before processing

This guarantees correct detection regardless of input order.

---

## How Malformed Events Are Treated

Any heartbeat is ignored if it:
- Is missing `service`
- Is missing `timestamp`
- Has an invalid timestamp format

Malformed events never crash the program.

---

## Installation

```
pip install -r requirements.txt
```

## How to Run
```
python main.py
```

## How to Test
```
pytest or pytest test_heartbeat.py
```



