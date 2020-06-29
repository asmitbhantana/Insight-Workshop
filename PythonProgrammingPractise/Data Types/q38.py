"""
38.​ Write a Python program to remove a key from a dictionary.
"""


def remove_key(user_dict: dict, key):
    baked_dict = user_dict.copy()
    baked_dict.pop(key)
    return baked_dict


if __name__ == '__main__':
    print(remove_key({1: 10, 2: 20, 3: 40, 4: 50}, 4))
