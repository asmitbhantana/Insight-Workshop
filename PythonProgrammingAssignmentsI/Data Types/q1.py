"""
1. Write a Python program to count the number of characters (character
frequency) in a string. Sample String : google.com'
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
"""
def slice_and_count_letters(word):
    count = {}
    for c in word:
        try:
            count[c] += 1
        except KeyError:
            count[c] = 1
    print(count)


if __name__ == '__main__':
    slice_and_count_letters("google.com")
