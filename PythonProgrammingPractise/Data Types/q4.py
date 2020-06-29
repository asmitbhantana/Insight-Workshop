""" Write a Python program to get a single string from two given strings, separated
by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'"""


def bake_string(words):
    last_word = words[0]
    first_word = words[1]

    return first_word[:-1] + last_word[-1:] + " " + last_word[:-1] + first_word[-1:]


if __name__ == '__main__':
    given_words = []
    for i in range(2):
        word = input("Give the {} word:\t".format(i + 1))
        given_words.append(word)
    print(bake_string(given_words))
