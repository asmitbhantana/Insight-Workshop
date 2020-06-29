"""
43.​ Write a Python program to remove an item from a tuple.
"""


def remove_item(user_tuple: tuple, remove_item):
    bake_tuple = ()
    for item in user_tuple:
        if item is not remove_item:
            bake_tuple += (item,)
    return bake_tuple


if __name__ == '__main__':
    print(remove_item((1, 2, 3, 4, 5, 6), 6))
