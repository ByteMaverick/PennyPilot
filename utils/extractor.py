import re
import random

def month_extractor(date):
    """
    Extract month from given date.
    :param date: Date given.
    :return: Month of date.
    """
    pattern = r"(\d{2})/\d{2}/\d{4}"
    match = re.search(pattern, date)
    return match.group(1)

def generate_key():
    """
    Generate random key for overrideKey.
    :return: String of 10 characters.
    """
    keys = "asdfghjklpoiuytrewqzxcvbnmm1234567890!@#$%^&*~"
    key =""
    for i in range(10):
        key += random.choice(keys)

    return key


