from randomListGenerator import random_list, random_search_key


def perform_linear_search(usr_list_l, search_key):
    for i in usr_list_l:
        if i == search_key:
            return i
    return -1


if __name__ == '__main__':
    usr_list = random_list()
    usr_key = random_search_key()
    print("Searching ", usr_key, "...")
    print(perform_linear_search(usr_list, usr_key))
