"""
10.​ Write a Python program to print the even numbers from a given list.
Sample List : ​ [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result ​ : [2, 4, 6, 8]
"""


def even_number_finder(user_list):
    baked_list = []
    for i in user_list:
        if i % 2 == 0:
            baked_list.append(i)
    return baked_list


if __name__ == '__main__':
    print(even_number_finder([1, 2, 3, 4, 5, 6, 7, 8, 9]))
