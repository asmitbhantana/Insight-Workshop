import random


def random_list(size=100, limit=1000):
    usr_list = []
    for i in range(size):
        usr_list.append(random.randint(1, limit))
    return usr_list


def random_search_key():
    return random.randint(1, 1000)
