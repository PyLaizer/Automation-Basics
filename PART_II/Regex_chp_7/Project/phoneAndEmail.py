#! python3
#phoneAndEmail.py Finds phone numbers and email addresses on the clipboard

import pyperclip, re

#create a phone regex
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?          #area code
    (\s|-|\.)?                  #seperator
    (\d{3})                     #first 3 digits
    (\s|-|\.)                   #separator
    (\d{4})                         #last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?      #extension
)''', re.VERBOSE)

#Create email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       #username
    @                       #@ symbol
    [a-zA-Z0-9._]+          #domain name
    (\.[a-zA-Z]{2,4})       #dot something
)''', re.VERBOSE)

#Finding matches in clipboard text
text = str(pyperclip.paste())
matches = []

for group in phoneRegex.findall(text):
    phoneNum = '-'.join([group[1], group[3], group[5]])
    if group[8] != '':
        phoneNum += ' x' + group[8] 
    matches.append(phoneNum)  

for group in emailRegex.findall(text):
    matches.append(group[0])  

#copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print("No phone numbers or addresses was found")    
