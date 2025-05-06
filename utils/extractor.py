import re
import random

def month_extractor(date):
    pattern = r"(\d{2})/\d{2}/\d{4}"
    match = re.search(pattern, date)
    return match.group(1)

def generate_key():
    keys = "asdfghjklpoiuytrewqzxcvbnmm1234567890!@#$%^&*~"
    key =""
    for i in range(10):
        key += random.choice(keys)

    return key


