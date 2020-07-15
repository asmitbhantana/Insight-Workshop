"""
17.​ Write a Python program to multiplies all the items in a list.
"""


def mul_list(num_list):
    i = 1
    for n in num_list:
        n = str(n)
        if not n.isdigit():
            raise Exception("List is not valid, contains non-digit items")
        i *= int(n)
    return i


if __name__ == '__main__':
    try:
        print(mul_list([1,3,4,5,6,1]))
    except Exception as e:
        print(e.__str__())
