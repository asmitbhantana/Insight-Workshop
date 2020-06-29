"""
16.​ Write a Python program to square and cube every number in a given list of
integers using Lambda.
"""

square_list = lambda user_list: list(map(lambda x: x ** 2, user_list))

if __name__ == '__main__':
    print(square_list([1, 2, 3, 4, 5, 6, 5]))
