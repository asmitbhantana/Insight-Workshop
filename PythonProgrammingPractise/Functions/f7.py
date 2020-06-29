"""
7.​ Write a Python function that accepts a string and calculate the number of
upper case letters and lower case letters.Sample String ​ : 'The quick Brow Fox'
Expected Output : ​
No. of Upper case characters : 3
No. of Lower case Characters : 12
"""


def count_upper_lower_case(sentence: str):
    upper = 0
    lower = 0
    for i in sentence:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
    return upper, lower


if __name__ == '__main__':
    result = count_upper_lower_case("The quick Brow Fox")
    print(f"No. of Upper case characters : {result[0]}\nNo. of Lower case Characters : {result[1]}")
