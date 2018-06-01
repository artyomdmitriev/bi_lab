import re

# find all email addresses in string
line = input("Enter a string to find email addresses: ")
match = re.findall(r'[\w\.-]+@[\w\.-]+', line)
print(match)

# find all three, four, five characters long words in a string
line = input('Enter a string to find 3-, 4-, 5-characters long words: ')
match = re.findall(r'\b[\w]{3,5}\b', line)
print(match)

# separate and print numbers of a given string
line = input('Enter a string to find numbers: ')
match = re.findall(r'\d+', line)
print(match)

# replace whitespaces with an underscore and vice versa
line = input('Enter a string to replace underscores and spaces: ')
print(re.sub(r'\s', '_', line))
print(re.sub('_', ' ', line))
