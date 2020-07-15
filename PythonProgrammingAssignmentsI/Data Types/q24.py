"""
24. ​ Write a Python program to clone or copy a list.
"""


def copy_list(user_list):
    new_list = user_list.copy()
    return new_list


if __name__ == '__main__':
    print(copy_list([1, 2, 4, 5, 7, 8, 9, 9]))
