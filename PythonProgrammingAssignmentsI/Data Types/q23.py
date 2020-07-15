"""
23. ​ Write a Python program to check a list is empty or not.
"""


def check_for_empty(user_list: list):
    if len(user_list):
        return "Not Empty"

    return "Empty"


if __name__ == '__main__':
    print(check_for_empty([]))
