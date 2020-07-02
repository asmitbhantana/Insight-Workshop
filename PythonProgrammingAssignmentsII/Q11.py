"""
11. Create a variable, filename. Assuming that it has a three-letter
extension, and using slice operations, find the extension. For
README.txt, the extension should be txt. Write code using slice
operations that will give the name without the extension. Does your
code work on filenames of arbitrary length?
"""


def split_that_path(user_path):
    user_path_list = user_path.split(".")
    return user_path_list[-1]


file_path = "/usr/ak/Desktop/background.jpg"
print(split_that_path(file_path))
# yes it works for file names with arbitrary lenght
