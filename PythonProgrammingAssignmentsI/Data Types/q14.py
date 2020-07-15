"""
14.​ Write a Python function to create the HTML string with tags around the
word(s).
Sample function and result :add_tags('i', 'Python') -> '<i>Python</i>'
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
"""


def add_tags(word, tag):
    return f"<{tag}>{word}</{tag}>"


if __name__ == '__main__':
    print(add_tags("Python Tutorial",'b'))