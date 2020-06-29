"""
9. ​ Write a Python program to change a given string to a new string where the first
and last chars have been exchanged.
"""


def swap_first_last_chars_of(word):
    return word[-1] + word[1:-1] + word[0]


if __name__ == '__main__':
    print(swap_first_last_chars_of("Asmit"))
