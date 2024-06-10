# initialising a variable
string_list = ["coder", "academy", "champion"]
result = 0

for string in string_list:
    for letter in string:
        if letter in "aAeEiIoOuU":
            result += 1

print("the total occurance of vowels in the list:", result)
