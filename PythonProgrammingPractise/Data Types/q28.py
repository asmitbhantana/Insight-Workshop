"""
28. ​ Write a Python script to add a key to a dictionary.Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}
"""


def add_key(user_dict: dict, key, value):
    user_dict[key] = value
    return user_dict


if __name__ == '__main__':
    print(add_key({0: 10, 1: 20}, 2, 30))
