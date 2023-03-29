import hashlib


def generate_reg_id(str_input):
    return hashlib.md5(str_input.encode()).hexdigest()

