"""
44.​ Write a Python program to slice a tuple.
"""


def slice_tuple(user_tuple, start, end):
    baked_list = []
    for i in range(start, end):
        baked_list.append(user_tuple[i])

    return tuple(baked_list)


if __name__ == '__main__':
    print(slice_tuple((1, 3, 4, 5, 6, 7, 8, 2), 3, 5))
