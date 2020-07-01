"""
5. Create a tuple with your first name, last name, and age. Create a list,
people, and append your tuple to it. Make more tuples with the
corresponding information from your friends and append them to the
list. Sort the list. When you learn about sort method, you can use the
key parameter to sort by any field in the tuple, first name, last name,
or age.
"""
import copy

users = []


def add_user(user_info):
    users.append(user_info)


def create_user():
    firstname = input("Give me firstname\n")
    lastname = input("Give me lastname\n")
    age = int(input("Give me age\n"))
    return tuple([firstname, lastname, age])


def sort_user_list():
    print("Sorting based on age")
    sorted_list = users.copy()
    sorted_list.sort(key=lambda a: a[2])
    return sorted_list


add_user(create_user())
add_user(create_user())
add_user(create_user())

print(sort_user_list())
