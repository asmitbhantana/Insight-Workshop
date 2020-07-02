"""
14. Write a function that reads a CSV file. It should return a list of
dictionaries, using the first row as key names, and each subsequent
row as values for those keys.
For the data in the previous example it would return:
[{'name': 'George', 'address': '4312 Abbey Road', 'age': 22}, {'name':
'John', 'address': '54 Love Ave', 'age': 21}]
"""


def read_csv(filename):
    try:
        usr_file = open("q13/" + filename + ".csv", "r")
        usr_tuple_list = []
        for file_line in usr_file.readlines():
            file_line = file_line.replace("\n", "")
            usr_tuple_list.append(tuple(file_line.split(",")))
        return usr_tuple_list[1:]
    except Exception as e:
        return e


print(read_csv("test_csv"))
