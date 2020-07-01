"""
8. Write a function, is_prime, that takes an integer and returns True if
the number is prime and False if the number is not prime.
"""

from math import sqrt


def is_prime(user_number):
    if user_number > 1:
        for n in range(2, int(sqrt(user_number))+1):
            if user_number % n == 0:
                return False
        else:
            return True
    else:
        return False


if __name__ == '__main__':
    result = is_prime(int(input("Which Number DO You want to check?")))
    print(result)
