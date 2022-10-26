#R  E   G   E   X
import re

#case-insensitive matching with re.I or re.IGNORECASE
regex1 = re.compile(r'robocop',re.I)
result = regex1.search('Robocop vs Raiden')
result2 = regex1.search('RoboCOP vs Wolverine')
result3 = regex1.search('ROBOCOP vs Scorpion')
print(result.group())
print(result2.group())
print(result3.group())

#Substituring strings with sub() method
nameRegex = re.compile(r'Agent \w+')
result = nameRegex.sub('Assasin', 'Agent Sharpp has major intel about Agent Conway')
print(result)

#To censor the name of secret agent
nameRegex = re.compile(r'Agent (\w)\w*')
result = nameRegex.sub(r'\1****', 'Agent Sharpp has major intel about Agent Conway')
print(result)

#Managing complex regexes
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                  #area code
    (\s|-|\.)?                          #seperator
    \d{3}                               #first 3 digits
    (\s|-|\.)                           #seperator
    \d{4}                               #last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?        #extension
    )''',re.VERBOSE)

#Combining re.IGNORECASE, re.DOTALL and re.VERBOSE
someRegex = re.compile(r'foo',re.IGNORECASE|re.DOTALL|re.VERBOSE)
result = someRegex.search('FOO')
print(result.group())    

