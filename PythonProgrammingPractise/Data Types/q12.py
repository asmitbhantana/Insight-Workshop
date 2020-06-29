"""
12. ​ Write a Python script that takes input from the user and displays that input
back in upper and lower cases.
"""


def lower_upper_of(word: str):
    return word.upper(), word.lower()


if __name__ == '__main__':
    word = input("What's the word?\n")
    result = lower_upper_of(word)
    print(result[0], result[1])
