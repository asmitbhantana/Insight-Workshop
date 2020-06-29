"""
20.​ Write a Python program to find intersection of two given arrays using
Lambda.
"""

find_intersection = lambda first_array,second_array : set(first_array).intersection(set(second_array))

if __name__ == '__main__':
    print(list(find_intersection([2,3,4,5],[4,5,6])))
