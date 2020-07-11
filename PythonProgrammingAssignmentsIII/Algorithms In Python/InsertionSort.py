from randomListGenerator import random_list
import unittest


def perform_insertion_sort(c_usr_list):
    for i in range(len(c_usr_list)):
        temp = c_usr_list[i]
        # print("Temp", temp)
        position = -1
        for j in range(i - 1, -1, -1):
            if c_usr_list[j] > temp:
                # print("User list item", c_usr_list[j])
                # print(" Shifting", c_usr_list[j], "to", c_usr_list[j + 1], end=",")
                c_usr_list[j + 1] = c_usr_list[j]
                position = j
        if position != -1:
            # print("Changing position", c_usr_list[position])
            c_usr_list[position] = temp

        # print("\n", c_usr_list)
    return c_usr_list


if __name__ == '__main__':
    usr_list = random_list()
    print(usr_list)
    perform_insertion_sort(usr_list)
    print(usr_list)


class TestSortedList(unittest.TestCase):

    def test_sorted(self):
        t_list = random_list()
        sorted_list = t_list.copy()
        sorted_list.sort()
        self.assertEqual(perform_insertion_sort(t_list), sorted_list)
