from iso4217 import Currency as cur


def validate_iso_code(code):
    return code in [currency.code for currency in cur]
