import os, json
from datetime import datetime
from typing import List, Dict, Any


DATE_FORMAT = "%Y-%m-%dT%H:%M:%SZ"

def parsed_timestamp(timestamp: str) -> (Any | None):
    try:
        # parse timestamp with Z value
        return datetime.strptime(timestamp, DATE_FORMAT)
    except:
        return None


def detect_missed_heartbeat(events: List[Dict[str, Any]], expected_interval_seconds: int = 60, allowed_misses: int = 3) -> List[Dict[str, str]]:
    # validate and group events based on service
    grouped = dict()

    for event in events:
        service = event.get('service')
        timestamp = event.get('timestamp')

        # check service or timestamp
        if not service or not timestamp:
            continue

        # check invalid timestamp
        ptimestamp = parsed_timestamp(timestamp)
        if not ptimestamp:
            continue

        grouped.setdefault(service, []).append(ptimestamp)


if __name__ == "__main__":

    if not os.path.exists('./events.json'):
        print("Please provide the events.json file.")
        exit(0)

    with open("events.json", "r", encoding="utf-8") as file:
        events = json.load(file)

    detect_missed_heartbeat(events)