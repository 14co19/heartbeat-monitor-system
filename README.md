# Heartbeat-Monitor-System
A simple yet effective heartbeat alert service that detects when a service misses 3 consecutive expected heartbeats — and raises a single alert per service.

---

## Overview

Heartbeat-Monitor-System processes a stream of “heartbeat” events for one or more services. When a service fails to send the expected number of heartbeats (misses 3 in a row), the system flags this as a potential outage and emits an alert.  

Key behavior:
- The alert is triggered if the time gap between two successive received heartbeats for a service is **≥ expected_interval × (allowed_misses + 1)**.  
- The timestamp of the alert is the time of the **first missed heartbeat**, not the last received one.  
- Events can arrive unordered — the system sorts them by timestamp per service before processing, so order in the input doesn’t matter.  
- Malformed events (missing `service` or `timestamp`, or invalid timestamp format) are safely ignored, never crashing the program.  

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

## What’s Included (Structure)

```
.  
├── main.py             # Main script to run the heartbeat monitor  
├── requirements.txt    # Python dependencies  
├── events.json         # Sample input events data  
├── test_heartbeat.py   # Unit tests for heartbeat logic  
├── .gitignore          
└── README.md           # This file  
```

---

## Getting Started (Local Development)
**Prerequisites**
- Python 3.10+
- pip package manager


**Installation**
1. Clone the repository:
    ```
    git clone <repo_url>
    cd <repo_dir>
    ````
2. Create and activate a virtual environment:
     ```
     python -m venv venv
     source venv/bin/activate  # Linux / Mac
     venv\Scripts\activate     # Windows
     ```
3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

---

## Usage
**Running the script Locally**
```
python main.py
```

**Running Test**
```
pytest or pytest test_heartbeat.py
```

---

## Example Behaviour

Assume:

- `expected_interval = 60 seconds`  
- `allowed_misses = 3`  

If a service’s last heartbeat was at `t = 0`, and the next is at `t = 240 seconds (4 minutes)`, then your monitor will trigger an alert — because 240 ≥ 60 × (3 + 1).  

The alert timestamp will be `0 + 60 = 60s` (first missed heartbeat), not `240s`.  

---

