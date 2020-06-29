"""
5.​ Write a Python function to calculate the factorial of a number (a non-negative
integer). The function accepts the number as an argument.
"""


def calculate_factorial(number):
    fact = 1
    for i in range(1, number + 1):
        fact *= i
    return fact


if __name__ == '__main__':
    print(calculate_factorial(6))
