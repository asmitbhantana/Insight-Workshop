from randomListGenerator import random_list, random_search_key
from InsertionSort import perform_insertion_sort


def perform_interpolation_search(sorted_usr_list, first, end, search_key):
    if first <= end and sorted_usr_list[first] <= search_key <= sorted_usr_list[end]:

        pos = first + ((end - first) // (sorted_usr_list[end] - sorted_usr_list[first]) * (search_key -
                                                                                           sorted_usr_list[first]))

        if sorted_usr_list[pos] == search_key:
            return pos

        if sorted_usr_list[pos] < search_key:
            return perform_interpolation_search(sorted_usr_list, pos + 1, end, search_key)

        if sorted_usr_list[pos] > search_key:
            return perform_interpolation_search(sorted_usr_list, first, pos - 1, search_key)

    return -1


if __name__ == '__main__':
    usr_list = random_list(15, 25)
    perform_insertion_sort(usr_list)
    print(usr_list)
    searching_key = random_search_key()
    print("Searching for...", searching_key)
    print("Found in index ", perform_interpolation_search(usr_list, 0, len(usr_list) - 1, searching_key))
