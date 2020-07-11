from randomListGenerator import random_list


def perform_bubble_sort(usr_list):
    for j in range(len(usr_list)):
        for i in range(0, len(usr_list) - 1 - j):
            if usr_list[i] > usr_list[i + 1]:
                temp = usr_list[i + 1]
                usr_list[i + 1] = usr_list[i]
                usr_list[i] = temp


if __name__ == '__main__':
    usr_list = random_list()
    print(usr_list)
    perform_bubble_sort(usr_list)
    print(usr_list)

