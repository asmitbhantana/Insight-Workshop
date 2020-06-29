"""
14.​ Write a Python program to sort a list of dictionaries using Lambda.
"""

sort_dictionary_list_using_lambda = lambda user_dict: sorted(user_dict, key=lambda a: a['color'])

if __name__ == '__main__':
    user_list_with_dict = [{'make': 'Nokia', 'model': 'Nokia Keypad', 'color': 'Black'},
                           {'make': 'Mi A1', 'model': 'tissot', 'color': 'Gold'},
                           {'make': 'Samsung Fold', 'model': 'flexi', 'color': 'Blue'}]
    sort_dictionary_list_using_lambda(user_list_with_dict)
    print(user_list_with_dict)
