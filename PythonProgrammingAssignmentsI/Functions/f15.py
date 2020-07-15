"""
15.​ Write a Python program to filter a list of integers using Lambda.
"""


filter_integer_list  = lambda user_list : filter(lambda x : isinstance(x,int),user_list)

if __name__ == '__main__':
    print(list(filter_integer_list([1,4,5,'a',34,1.00,34,'b'])))