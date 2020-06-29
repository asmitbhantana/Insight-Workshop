"""
17.​ Write a Python program to find if a given string starts with a given character
using Lambda.
"""

is_given_string_start_with_prefix = lambda user_word,prefix : user_word.startswith(prefix)

if __name__ == '__main__':
    print(is_given_string_start_with_prefix("Hello friend","Hell"))