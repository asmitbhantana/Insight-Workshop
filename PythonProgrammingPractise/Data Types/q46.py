"""
46.​ Write a Python program to find the length of a tuple
"""


def find_tuple_length(user_tuple: tuple):
    return len(user_tuple)


if __name__ == '__main__':
    print(find_tuple_length((1, 2, 3, 4, 5, 6, 7)))
