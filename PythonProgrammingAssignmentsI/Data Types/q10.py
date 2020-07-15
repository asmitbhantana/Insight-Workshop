"""
10. ​ Write a Python program to remove the characters which have odd index
values of a given string.
"""


def remove_odd_index_string(word):
    new_word = ""
    for i in range(len(word)):
        if i % 2 == 0:
            new_word += word[i]
    return new_word


if __name__ == '__main__':
    print(remove_odd_index_string("hello world"))
