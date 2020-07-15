"""
9.​ Write a Python function that takes a number as a parameter and check the
number is prime or not.
Note : A prime number (or a prime) is a natural number greater than 1 and that
has no positive divisors other than 1 and itself.
"""
from math import sqrt


def check_prime_number(user_number):
    if user_number > 1:
        for n in range(2, int(sqrt(user_number))+1):
            if user_number % n == 0:
                return False
        else:
            return True
    else:
        return False


if __name__ == '__main__':
    result = check_prime_number(137)
    print(result)

