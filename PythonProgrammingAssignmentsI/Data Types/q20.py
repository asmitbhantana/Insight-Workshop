"""
20.​ Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given list of
strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
"""


def count_strings_same_first_last_character(string_list):
    count = 0
    for string in string_list:
        if string[0] == string[-1]:
            count += 1
    return count


if __name__ == '__main__':
    print(count_strings_same_first_last_character(['abc', 'xyz', 'aba', '1221']))
