"""
10. Write a function that takes camel-cased strings (i.e.
ThisIsCamelCased), and converts them to snake case (i.e.
this_is_camel_cased). Modify the function by adding an argument,
separator, so it will also convert to the kebab case
(i.e.this-is-camel-case) as well.
"""


def camel_to_snake(usr_str):
    created_string = ""
    first = 1
    for letter in usr_str:
        if letter.isupper():
            if first and usr_str[0] == letter:
                first = 0
                created_string += letter.lower()
            else:
                created_string += "_" + letter.lower()
        else:
            created_string += letter
    return created_string


print(camel_to_snake(input("What word do you want to check?")))
