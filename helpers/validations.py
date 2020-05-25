import re
from datetime import datetime


def validate_iso8601(str_val):
    # taken from https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch04s07.html
    regex = r'^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])T(2[0-3]|[01][0-9]):([0-5][0-9]):' \
            r'([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[0-3]|[01][0-9]):[0-5][0-9])?$'
    match_iso8601 = re.compile(regex).match
    try:
        if match_iso8601(str_val) is not None:
            return True
    except:
        pass
    return False


def validate_default_datetime(str_val):
    try:
        datetime.strptime(str_val, '%Y-%m-%d-%H:%M:%S')
    except ValueError:
        return False

    return True
