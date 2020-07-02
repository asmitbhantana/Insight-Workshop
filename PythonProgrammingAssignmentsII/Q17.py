"""
17. Write a program that serves as a basic calculator. It asks for two
numbers, then it asks for an operator. Gracefully deal with input that
doesn't cleanly convert to numbers. Deal with division by zero errors.
"""


def calculate(math_expression):
    try:
        return eval(math_expression)
    except Exception as e:
        return "Error occurred: "+e


def take_user_commands():
    user_input = input('Type "no" to stop otherwise follow instruction!\n')
    a = ""
    b = ""
    c = ""
    while not user_input == "no":
        a = input("Type value for a\n")
        b = input("Type value for b\n")
        c = input("Type in the code +,/,*,-\n")
        if not (a == "no" or b == "no" or c == "no"):
            print(calculate(a + c + b))
        else:
            break

take_user_commands()