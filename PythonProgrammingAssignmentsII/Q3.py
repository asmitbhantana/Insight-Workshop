"""
3. Write code that will print out the anagrams (words that use the same
letters) from a paragraph of text.
"""

user_input_paragraph = input("What paragraph do you want to check?\n")
user_word = input("What word do you want to check for?\n")
user_paragraph_list = user_input_paragraph.split(' ')
anagrams_list = []
for word in user_paragraph_list:
    if sorted(word) == sorted(user_word):
        anagrams_list.append(word)
print(anagrams_list)
