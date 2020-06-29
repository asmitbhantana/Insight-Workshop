"""
14.​ Write a Python program to sort a list of dictionaries using Lambda.
"""

sort_dictionary_list_using_lambda = lambda user_dictionary_list: user_dictionary_list.sort()

if __name__ == '__main__':
    user_list_with_dict = [{0, 9, 2, 34, 342, 343, 45, 345, 32, 5, 43, 5}, {121., 12, 12, 12, 1},
                           {21223, 4234, 23423, 4, 32}]
    sort_dictionary_list_using_lambda(user_list_with_dict)
    print(user_list_with_dict)
