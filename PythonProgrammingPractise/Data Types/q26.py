"""
26.​ Write a Python program to insert a given string at the beginning of all items in
a list.
Sample list : [1,2,3,4], string : emp
Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
"""


def insert_string_in(user_list, user_string):
    baked_list = []
    for item in user_list:
        baked_list.append(f"{user_string}{item}")
    return baked_list


if __name__ == '__main__':
    print(insert_string_in([1, 2, 3, 4], 'emp'))
