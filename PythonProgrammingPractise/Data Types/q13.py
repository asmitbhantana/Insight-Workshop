"""
13. ​ Write a Python program that accepts a comma separated sequence of words
as input and prints the unique words in sorted form (alphanumerically).
"""


def sort_comma_seperated_words(sentence):
    if not sentence.__contains__(","):
        raise Exception("Only Comma Separated sentences is Accepted!")
    slitted_list = sentence.split(",")
    slitted_list.sort()
    return slitted_list


if __name__ == '__main__':
    try:
        print(sort_comma_seperated_words("hello should throw error"))
    except Exception as e:
        print(e)
