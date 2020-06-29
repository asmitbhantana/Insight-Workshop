"""
41.​ Write a Python program to convert a tuple to a string.
"""


def tuple_to_string(user_tuple: tuple):
    baked_string = ""
    for item in user_tuple:
        baked_string += f'{item}'
    return baked_string


if __name__ == '__main__':
    print(tuple_to_string(((1, 3), 'a', 'b', 'c', 'd')))
