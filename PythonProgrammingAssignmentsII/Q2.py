"""
2. Write an if statement to determine whether a variable holding a year
is a leap year.
"""

year = int(input("Which year do you want to check?\n"))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Year", year, " is a LeapYear")
else:
    print("Year", year, " is not a LeapYear")
