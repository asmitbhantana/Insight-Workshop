"""
39.​ Write a Python program to unpack a tuple in several variables.
"""


def unpack_tuple(user_tuple: tuple):
    a, b = user_tuple
    print(a, b)


if __name__ == '__main__':
    unpack_tuple((1, 2))
