"""
42.​ Write a Python program to convert a list to a tuple.
"""


def list_to_string(user_list: list):
    baked_string = ""
    for item in user_list:
        baked_string += f'{item}'
    return baked_string


if __name__ == '__main__':
    print(list_to_string([(1, 3), 'a', 'b', 'c', 'd']))
