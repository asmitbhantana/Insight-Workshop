"""
13.​ Write a Python program to sort a list of tuples using Lambda.
"""

sort_using_lambda = lambda user_list :  user_list.sort()

if __name__ == '__main__':
    user_list = [(1, 3), (4, 5), (6, 1),(3,2),(0,9),(3,4)]
    sort_using_lambda(user_list)
    print(user_list)
