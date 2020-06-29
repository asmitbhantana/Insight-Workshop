"""
4. Create a list. Append the names of your colleagues and friends to it.
Has the id of the list changed? Sort the list. What is the first item on
the list? What is the second item on the list?
"""

my_list = []
prev_id = id(my_list)
user_input = input("Keep typing name of your friend to add in the list or 'no' to stop adding!\n")
while user_input != 'no':
    if user_input != "":
        my_list.append(user_input)
        user_input = input()

new_id = id(my_list)
print("The friend list is ", my_list)
print("Has the list id changed? ", prev_id is new_id)
print("Here is the sorted list: ", sorted(my_list))
