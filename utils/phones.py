import re


def get_phone(text):
    return re.findall(r'(\+?\d?[\(\s\-]*\d{3}[\)\s\-]*\d{3}[\-\s]*\d{2}[\-\s]*\d{2}\b)', text)
