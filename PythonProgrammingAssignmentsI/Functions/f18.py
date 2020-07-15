"""
18.​ Write a Python program to check whether a given string is number or not
using Lambda.
"""

check_is_number = lambda user_string: not user_string.isalpha() and (isinstance(float(user_string), float) or isinstance(int(user_string), int))

if __name__ == '__main__':
    print(check_is_number('-1000.000'))
