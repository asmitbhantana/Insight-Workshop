"""
30.​ Write a Python script to check whether a given key already exists in a
dictionary
"""


def check_key(user_dict, check_availability_of_key):
    try:
        user_dict[check_availability_of_key]
    except KeyError:
        return False
    return True


if __name__ == '__main__':
    print(check_key({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}, 3))
