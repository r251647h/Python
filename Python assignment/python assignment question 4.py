from datetime import datetime
from collections import Counter


def find_peak_usage(logs):
    hours = []
    for timestamp in logs:
        dt = datetime.fromisoformat(timestamp)
        hours.append(dt.hour)

    hour_counts = Counter(hours)
    max_count = max(hour_counts.values())

    # Find the earliest hour with the maximum count
    for hour in range(24):
        if hour_counts.get(hour, 0) == max_count:
            return hour