"""
37.​ Write a Python program to multiply all the items in a dictionary.
"""


def mul_all_item_in_dic(user_dict):
    i = 1
    for key in user_dict:
        i = i * key * user_dict[key]
    return i


if __name__ == '__main__':
    print(mul_all_item_in_dic({1: 10, 2: 20, 3: 40, 4: 50}))
