from randomListGenerator import random_list, random_search_key


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


if __name__ == '__main__':
    usr_list = random_list()
    usr_list.sort()
    print("Answer is in index",perform_binary_search(usr_list, random_search_key()))
