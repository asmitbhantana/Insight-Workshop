"""
31.​ Write a Python program to iterate over dictionaries using for loops.
"""


def iterate_over_dict(user_dict):
    for key in user_dict:
        print("key=", key, "value=", user_dict[key])


if __name__ == '__main__':
    iterate_over_dict({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60})
