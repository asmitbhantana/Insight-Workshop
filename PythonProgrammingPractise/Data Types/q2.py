'''
2. Write a Python program to get a string made of the first 2 and the last 2 chars
from a given a string. If the string length is less than 2, return instead the
empty string.
Sample String : 'Python'
Expected Result : 'Pyon'
Sample String : 'Py'
Expected Result : 'PyPy'
Sample String : ' w'
Expected Result : Empty String
'''


def bake_string(word):
    if len(word) >= 2:
        first = word[:2]
        last = word[-2:]
        return first + last
    else:
        return "Empty String"


if __name__ == '__main__':
    print(bake_string(""))
