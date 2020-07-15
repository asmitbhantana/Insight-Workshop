"""
27.​ Write a Python program to replace the last element in a list with another list.
Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
"""


def replace_last_with_list(first_list, second_list):
    return first_list[:-1] + second_list


if __name__ == '__main__':
    print(replace_last_with_list([1, 3, 5, 7, 9, 10], [2, 4, 6, 8]))
