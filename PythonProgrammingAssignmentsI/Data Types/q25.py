"""
25.​ Write a Python program to check whether all dictionaries in a list are empty or
not.
Sample list : [{},{},{}]
Return value : True
Sample list : [{1,2},{},{}]
Return value : False
"""


def check_empty_dictionaries_in(user_list):
    for item in user_list:
        if len(item):
            return False
    else:
        return True


if __name__ == '__main__':
    print(check_empty_dictionaries_in([{1,2,3}, {}, {}]))
