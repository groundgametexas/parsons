import re


def format_phone_number(phone_number):
    # Remove all non-digit characters
    formatted_number = re.sub(r"\D", "", phone_number)
    return formatted_number
