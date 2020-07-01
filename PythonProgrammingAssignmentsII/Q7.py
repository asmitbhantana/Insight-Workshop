"""
7. Create a list of tuples of first name, last name, and age for your
friends and colleagues. If you don't know the age, put in None.
Calculate the average age, skipping over any None values. Print out
each name, followed by old or young if they are above or below the
average age.
"""

friends_list = [('Ram', 'Bhatta', 12), ('Ramu', 'Gojar', 16), ('Ramesh', None, None), ('Mausam', 'Adhikari', 24)]

age_sum = 0

for friend in friends_list:
    if friend[2] is not None:
        age_sum += friend[2]
avg_age = age_sum/len(friends_list)

print("Average age is", avg_age)

for friend in friends_list:
    if friend[2] is not None:
        if friend[2] >= avg_age:
            print(f"He is {friend[0]} {friend[1]}. He is older than average.")
        else:
            print(f"He is {friend[0]} {friend[1]}. He is younger than average.")
    else:
        print(f"He is {friend[0]} {friend[1]}. We don't know his age.")

