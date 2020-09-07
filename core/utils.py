import random
import string

ALPHANUMERIC_CHARS = string.ascii_lowercase + string.digits
STRING_LENGHT = 6


def generate_random_string(chars=ALPHANUMERIC_CHARS, lenght=STRING_LENGHT):
    return "".join(random.choice(chars) for _ in range(lenght))
