from randomListGenerator import random_list
import unittest


def perform_partition(list1, first, last):
    pivot = list1[first]

    left, right = first+1, last
    while True:
        while left <= right and list1[left] <= pivot:
            left += 1

        while left <= right and list1[right] >= pivot:
            right -= 1

        if left > right:
            break
        else:
            list1[left], list1[right] = list1[right], list1[left]

    list1[right], list1[first] = list1[first], list1[right]
    return right


def perform_quick_sort(list0, first, last):
    if first < last:
        key = perform_partition(list0, first, last)
        perform_quick_sort(list0, first, key)
        perform_quick_sort(list0, key + 1, last)


if __name__ == '__main__':
    usr_list = random_list(10)
    print(usr_list)
    perform_quick_sort(usr_list, 0, len(usr_list) - 1)
    print(usr_list)


class TestSortedList(unittest.TestCase):

    def test_sorted(self):
        t_list = random_list(11)
        sorted_list = t_list.copy()
        sorted_list.sort()
        perform_quick_sort(t_list, 0, len(t_list) - 1)
        self.assertEqual(sorted_list, t_list)
