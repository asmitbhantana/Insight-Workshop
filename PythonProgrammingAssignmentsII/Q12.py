"""
12. Create a function, is_palindrome, to determine if a supplied word is
the same if the letters are reversed.
"""


def is_palindrome(usr_str):
    traverse_index = -1
    for _ in range(len(usr_str)):
        traverse_index += 1
        if usr_str[traverse_index] == usr_str[-(1 + traverse_index)]:
            # print("Checking", usr_str[traverse_index] )
            continue
        else:
            return "Not a palindrome"
    else:
        return "It is Palindrome"


print(is_palindrome(input("What string do you want to check for palindrome:\n")))
