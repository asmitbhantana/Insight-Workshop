"""
18.​ Write a Python program to get the largest number from a list.
"""


def get_largest_number_of(num_list):
    i = num_list[0]
    for n in num_list:
        n = str(n)
        if not n.isdigit():
            raise Exception("List is not valid, contains non-digit items")
        n = int(n)
        if i < n:
            i = n
    return i


if __name__ == '__main__':
    try:
        print(get_largest_number_of([1, 3, 4, 5, 6, 1]))
    except Exception as e:
        print(e.__str__())
