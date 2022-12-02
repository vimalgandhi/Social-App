import random
import string


class CommonHelper:
    def random_string(length: int = 6):
        return ''.join(random.choices(string.digits, k=length))
