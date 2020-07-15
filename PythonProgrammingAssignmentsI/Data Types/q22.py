"""
22. ​ Write a Python program to remove duplicates from a list.
"""


def remove_duplicates(user_list):
    required_list = set(user_list)
    return list(required_list)


if __name__ == '__main__':
    print(remove_duplicates(["hello", "world", "hello"]))
