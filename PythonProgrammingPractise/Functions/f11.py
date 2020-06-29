"""
11.​ Write a Python program to create a lambda function that adds 15 to a given
number passed in as an argument, also create a lambda function that multiplies
argument x with argument y and print the result.
"""

add = lambda a : a+15

mul = lambda x,y : print(x*y)

if __name__ == '__main__':
    print(add(10))
    mul(4,5)
