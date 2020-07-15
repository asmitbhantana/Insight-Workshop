'''
3. Write a Python program to get a string from a given string where all
occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
'''


def replace_first_char_except_itself(word, char_to_replace):
    new = word.replace(word[0], char_to_replace)
    return new.replace(new[0], word[0], 1)


if __name__ == '__main__':
    print(replace_first_char_except_itself("restart", "$"))
