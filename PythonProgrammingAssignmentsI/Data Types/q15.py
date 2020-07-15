"""
15.​ Write a Python function to insert a string in the middle of a string.
Sample function and result :
insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
"""


def insert_string_middle(main_string, word):
    if len(main_string) % 2 != 0:
        raise Exception("The given main string contains odd number of characters")
    mid_point = int(len(main_string) / 2)
    return main_string[:mid_point] + word + main_string[mid_point:]


if __name__ == '__main__':
    try:
        print(insert_string_middle("raar", 'd'))
    except Exception as e:
        print(e.__str__())
