from randomListGenerator import random_list
import unittest


def perform_merge_sort(usr_list):
    if len(usr_list) > 1:
        mid = len(usr_list) // 2

        left_list = usr_list[:mid]
        right_list = usr_list[mid:]

        perform_merge_sort(left_list)
        perform_merge_sort(right_list)

        i, j, k = 0, 0, 0

        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                usr_list[k] = left_list[i]
                i += 1
                k += 1
            else:
                usr_list[k] = right_list[j]
                j += 1
                k += 1

        while i < len(left_list):
            usr_list[k] = left_list[i]
            i += 1
            k += 1
        while j < len(right_list):
            usr_list[k] = right_list[j]
            j += 1
            k += 1


if __name__ == '__main__':
    usr_list = random_list(10)
    print(usr_list)
    perform_merge_sort(usr_list)
    print(usr_list)


class TestSortedList(unittest.TestCase):

    def test_sorted(self):
        t_list = random_list()
        sorted_list = t_list.copy()
        sorted_list.sort()
        perform_merge_sort(t_list)
        self.assertEqual(t_list, sorted_list)
