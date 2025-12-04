import os, json
from typing import List, Dict, Any


DATE_FORMAT = "%Y-%m-%dT%H:%M:%SZ"


def detect_missed_heartbeat(events: List[Dict[str, Any]], expected_interval_seconds: int, allowed_misses: int) -> List[Dict[str, str]]:
    pass


if __name__ == "__main__":

    if not os.path.exists('./events.json'):
        print("Please provide the events.json file.")
        exit(0)

    with open("events.json", "r", encoding="utf-8") as file:
        events = json.load(file)

    detect_missed_heartbeat(events, 60, 3)