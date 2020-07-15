"""
21.​ Write a Python program to get a list, sorted in increasing order by the last
element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
"""


def get_second_element(item):
    return item[len(item)-1]


def get_sorted_list(user_list: list):
    user_list.sort(key=get_second_element)

    return user_list


if __name__ == '__main__':
    print(get_sorted_list([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
