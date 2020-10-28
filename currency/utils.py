import re


def validate_iso_code(code):
    if len(code) != 3:
        return False

    if re.search("[A-Z]{3}", code) is None:
        return False

    return True
