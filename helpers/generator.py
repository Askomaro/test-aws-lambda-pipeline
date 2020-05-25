import random
import string


def get_id(size=6, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return __generator(size, chars)


def ger_str(size=6, chars=string.ascii_uppercase + string.ascii_lowercase):
    return __generator(size, chars)


def __generator(size, chars):
    return ''.join(random.choice(chars) for _ in range(size))
