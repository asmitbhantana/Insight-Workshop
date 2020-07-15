"""
11. ​ Write a Python program to count the occurrences of each word in a given
sentence.
"""


def slice_and_count_word(sentence):
    formatted_sentence = sentence.replace(".", "")
    word_list = formatted_sentence.split(" ")
    count = {}
    for word in word_list:
        try:
            count[word] += 1
        except KeyError:
            count[word] = 1
    return count


if __name__ == '__main__':
    print(slice_and_count_word("Hello How are you guys doing. I hope you are doing fine. I am good too"))
