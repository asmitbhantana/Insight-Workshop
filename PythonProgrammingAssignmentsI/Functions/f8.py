"""
8.​ Write a Python function that takes a list and returns a new list with unique
elements of the first list.
Sample List : ​ [1,2,3,3,3,3,4,5]
Unique List : ​ [1, 2, 3, 4, 5]
"""


def give_unique_list(user_list: list):
    unique_set = set(user_list)
    return list(unique_set)


if __name__ == '__main__':
    print(give_unique_list([1, 2, 3, 4, 434, 3, 4, 45, 45, 435, 435, 3, 33, 3]))
