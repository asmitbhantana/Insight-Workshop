"""
19. Write a Python class to find validity of a string of parentheses, '(',
')', '{', '}', '[' and ']. These brackets must be close in the correct order,
for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid
"""


def check_for_complete_brackets(user_str):
    opening_bracket_stack = []
    for s in user_str:
        if "{([".__contains__(s):
            opening_bracket_stack.append(s)
        elif "})]".__contains__(s):
            if s == '}':
                if '{' != opening_bracket_stack.pop():
                    return False
            elif s == ']':
                if '[' != opening_bracket_stack.pop():
                    return False
            elif s == ')':
                if '(' != opening_bracket_stack.pop():
                    return False
    return True


print(check_for_complete_brackets("({}[](){[})"))
print(check_for_complete_brackets("({}[](){[]})"))
print(check_for_complete_brackets("([{}{(){[)})"))