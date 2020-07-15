"""
8. ​ Write a Python program to remove the n​ th​ index character from a nonempty
string.
"""


def remove_nth_char_from(string, index):
    return string[:index] + string[index+1:]


if __name__ == '__main__':
    print(remove_nth_char_from("Hello Asmit Bhantana", 8))
