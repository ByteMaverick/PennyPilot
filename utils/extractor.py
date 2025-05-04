import re

def date_extractor(timestamp):
    pattern = r"\d{4}-\d{2}-\d{2}"
    match = re.search(pattern, timestamp)
    return match.group() if match else None

def time_extractor(timestamp):
    pattern = r"\d{2}:\d{2}"
    match = re.search(pattern,timestamp)
    return match.group() if match else None


def month_extractor(timestamp):
    pattern = r"\d{4}-(\d{2})-\d{2}"
    match = re.search(pattern, timestamp)
    return match.group(1)
