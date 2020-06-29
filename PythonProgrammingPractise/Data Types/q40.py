"""
40.​ Write a Python program to add an item in a tuple.
"""


def add_on_tuple(user_tuple: tuple, item):
    return user_tuple+(item,)


if __name__ == '__main__':
    print(add_on_tuple((1, 2, 3, 4), 5))
