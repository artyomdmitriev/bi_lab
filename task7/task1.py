import re

# find all email addresses in string
line = input("Enter string to find all emails: ")
match = re.findall(r'[\w\.-]+@[\w\.-]+', line)
print(match)

# find all three, four, five characters long words in a string
line = input('Enter string to words: ')
match = re.findall(r'\b[\w]{3,5}\b', line)
print(match)

# separate and print numbers of a given string
line = input('Enter a string')
match = re.findall(r'\d+', line)
print(match)

# replace whitespaces with an underscore and vice versa
line = input('Enter a string')
print(re.sub(' ', '_', line))
print(re.sub('_', ' ', line))
