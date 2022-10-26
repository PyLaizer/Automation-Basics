# REGEX

import re

#The wildcard character or dot character
atRegex = re.compile(r'.at')
result = atRegex.findall('The cat sat on the mat which was at the porch')
print(result)

#Matching everything with Dot-star
nameRegex = re.compile(r'First Name:(.*) Last Name:(.*)')
result2 = nameRegex.findall('First Name: James Last Name: Daniel')
print(result2)

result3 = nameRegex.search('First Name: John Last Name: Micheal')
print(result3.group(1))

#Non-greedy with Dot-star
nonGRegex = re.compile(r'<.*?>')
result2 = nonGRegex.search('<To serve Nigeria> with all my strength>')
print(result2.group())

#mathing newlines with the dot character
nonNewLineRegex = re.compile(r'.*')
result4 = nonNewLineRegex.search('To serve Nigeria\nwith\n all my strength>')
print(result4.group())

NewLineRegex = re.compile(r'.*',re.DOTALL)
result5 = NewLineRegex.search('To serve Nigeria\nwith\nall my strength')
print(result5.group())

