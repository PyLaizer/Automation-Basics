#Some REGEX Practice Questions
import re

#18
numRegex = re.compile(r'\d+')
result = numRegex.sub('X', '12 drummers, 11 pipers, eight boys, 3 hens')
print(result)

#20
exRegex = re.compile(r'\d{0,3}(\,\d{3})*')
result = exRegex.search('1,234')
print(result.group())

#21
nakamotoRegex = re.compile(r'[A-Z]{1}([a-zA-Z]*\s)Nakamoto')
result = nakamotoRegex.search('Satoshi Nakamoto')
print(result.group())

#22
sentenceRegex = re.compile(r'((Alice|Bob|Carol)\s)((eats|pets|throws)\s)((apples|cats|baseballs)\.)',re.IGNORECASE)
s_result = sentenceRegex.search('BOB EATS CATS.')
print(s_result.group())