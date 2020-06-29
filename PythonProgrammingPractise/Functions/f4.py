"""
4.​ Write a Python program to reverse a string.
Sample String ​ : "1234abcd"
Expected Output ​ : "dcba4321"
"""


def reverse_string(user_word: str):
    char_list = []
    for char in user_word:
        char_list.append(char)
    char_list.reverse()
    return ''.join(char_list)


if __name__ == '__main__':
    print(reverse_string("1234abcd"))
