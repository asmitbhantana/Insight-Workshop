"""
9. Write a binary search function. It should take a sorted sequence and
the item it is looking for. It should return the index of the item if found.
It should return -1 if the item is not found.
"""


def perform_binary_search(arr, key, index=0):
    result = -1
    print(arr, key)

    if len(arr):
        mid = len(arr) // 2
        mid_item = arr[mid]
        index += mid

        if mid_item == key:
            result = index

        elif key < mid_item:
            left_arr = arr[:mid]
            return perform_binary_search(left_arr, key, index - mid)

        elif key > mid_item:
            right_arr = arr[mid + 1:]
            return perform_binary_search(right_arr, key, index + 1)

    return result


arr = [1, 2, 4, 5, 6, 8, 9, 10, 11, 12, 13]
key = 9
print(perform_binary_search(arr, key))
