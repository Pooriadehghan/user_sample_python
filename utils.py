import re


def phone_validator(phone_number, massage):
    if isinstance(phone_number,str) and re.match(r"(09|\+989)\d{9}", phone_number):
        return phone_number
    else:
        raise ValueError(massage)