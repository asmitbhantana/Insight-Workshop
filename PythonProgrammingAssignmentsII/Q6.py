"""
6. Create a list with the names of friends and colleagues. Search for the
name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.
"""
friend_list = ['John','Malik','Elliot','Darlene','Anderson','Tyrell','Angelia']
search_keyword = input("Whom do you want to search?\n")
for word in friend_list:
    if search_keyword == word:
        print("Found", word)
        break
else:
    print("Not found")