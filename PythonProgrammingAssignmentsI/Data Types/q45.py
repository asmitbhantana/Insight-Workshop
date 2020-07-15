"""
45.​ Write a Python program to find the index of an item of a tuple.
"""


def find_item_index(user_tuple: tuple, item):
    for i in range(len(user_tuple)):
        if user_tuple[i] is item:
            return i
    return None


if __name__ == '__main__':
    print(find_item_index((1, 2, 3, 4, 5, 2, 3, 5, 6, 15), 15))
