"""
12.​ Write a Python program to create a function that takes one argument, and
that argument will be multiplied with an unknown given number.
"""

import random


def mul_by_unknown(user_number):
    return user_number * random.random()


if __name__ == '__main__':
    print(mul_by_unknown(67))
