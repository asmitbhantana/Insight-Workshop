'''
Write a Python program to add 'ing' at the end of a given string (length should
be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
string length of the given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
'''


def bake_word(word: str):
    if len(word) > 3:
        if word.endswith("ing"):
            return word + "ly"
        else:
            return word + "ing"

    return word


if __name__ == '__main__':
    print(bake_word("bake"))
