"""
1.​ Write a Python function to find the Max of three numbers.
"""


def max_number(a, b, c):
    max_abc = a
    if a > c:
        if a > b:
            max_abc = a
        else:
            max_abc = b
    else:
        if c > b:
            max_abc = c
        else:
            max_abc = b
    return max_abc


if __name__ == '__main__':
    print(max_number(44, 2202, 39))
