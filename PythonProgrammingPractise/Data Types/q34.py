"""
34.​ Write a Python script to merge two Python dictionaries.
same as 29
"""


def concat_dictionary(*args):
    z = {}
    z = args[0].copy()
    for arg in args:
        z.update(arg)
    return z


if __name__ == '__main__':
    print(concat_dictionary({1: 10, 2: 20}, {3: 30, 4: 40}, {5: 50, 6: 60}))
