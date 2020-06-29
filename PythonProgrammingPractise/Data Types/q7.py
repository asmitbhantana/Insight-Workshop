"""
7.Write a Python function that takes a list of words and returns the length of the
longest one.
"""


def count_length_longest_word_of(wordlist):
    max_length_count = len(wordlist[0])
    for word in wordlist:
        if max_length_count < len(word):
            max_length_count = len(word)
    return max_length_count


if __name__ == '__main__':
    given_words = []
    for i in range(5):
        word = input("Give the {} word:\t".format(i + 1))
        given_words.append(word)
    print(count_length_longest_word_of(given_words))
