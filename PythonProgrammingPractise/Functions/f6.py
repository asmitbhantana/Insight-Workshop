"""
6.​ Write a Python function to check whether a number is in a given range.
"""


def is_in_range(number, start, end):
    if start <= number <= end:
        return True
    return False


if __name__ == '__main__':
    print(is_in_range(1, 1, 8))
