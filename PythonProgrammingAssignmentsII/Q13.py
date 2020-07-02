"""
13. Write a function to write a comma-separated value (CSV) file. It
should accept a filename and a list of tuples as parameters. The
tuples should have a name, address, and age. The file should create
a header row followed by a row for each tuple. If the following list of
tuples was passed in:
[('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
it should write the following in the file:
name,address,age
George,4312 Abbey Road,22
John,54 Love Ave,21
"""


def create_csv(filename, user_tuples_list):
    try:
        usr_file = open("q13/"+filename+".csv", "w")
        usr_file.writelines("name,address,age")
        for usr_tuple in user_tuples_list:
            usr_file.writelines(f"\n{usr_tuple[0]},{usr_tuple[1]},{usr_tuple[2]}")
        usr_file.close()
        return "Successfully created and appended the data in " + filename + ".csv"
    except Exception as e:
        return e


print(create_csv("test_csv", [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]))