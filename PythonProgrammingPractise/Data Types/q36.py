"""
36.​ Write a Python program to sum all the items in a dictionary.
"""


def sum_all_item_in_dic(user_dict):
    return sum(user_dict.values())+sum(user_dict)


if __name__ == '__main__':
    print(sum_all_item_in_dic({1: 10, 2: 20, 3: 40, 4: 50}))
