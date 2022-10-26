#Without Regex
# A program to check if a string is an appropraite phone number

import re

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True


print(isPhoneNumber('410-555-4342')) 
print(isPhoneNumber('123-445-abac'))  



message = 'Call me at 415-555-1011 tomorrow. 410-555-9896 is my office.'
for i in range(len(message)):
    m_chunk = message[i:i+12]
    if isPhoneNumber(m_chunk):
        print('Phone number found: '+ m_chunk)
print('Done')        


# WITH REGEX

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search('My number is 415-555-4332')
print(mo.group())

#Grouping with Paentheses

phoneNumberRegex2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo1 = phoneNumberRegex2.search('My number is 415-555-4332')
print('\n'+ mo.group())
print(mo1.group(1))
print(mo1.group(2))
print(mo1.groups())

areaCode, mainNumber = mo1.groups()
print(areaCode)

phoneNumberRegex = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
mo2 = phoneNumberRegex.search('My number is (415)-555-4332')
print('\n' + mo2.group())
print(mo2.group(1))
print(mo2.group(2))

#Matching multiple groups with the pipe

heroRegex = re.compile(r'Batman|Superman')
mo3 = heroRegex.search('Batman and Superman')
print(mo3.group())

mo4 = heroRegex.search('Superman and Batman')
print(mo4.group())

batRegex = re.compile(r'Bat(man|mobile|girl|cave)|Super(man|boy|woman|girl)')
bat_mo = batRegex.search('The Supergirl just arrived')
print(bat_mo.group(1))
print(bat_mo.group(2))
print(bat_mo.groups())

batRegex2 = re.compile(r'Bat(man|mobile|girl|cave)')
bat_mo2 = batRegex2.search('The Batgirl just arrived')
print(bat_mo2.group(1))
print(bat_mo2.groups())

#Optional Matching with the Question Mark

batRegex3  = re.compile(r'Bat(wo)?man')
mo5 = batRegex3.search('Batman is intelligent')
print(mo5.group())

mo6 = batRegex3.search('Batwoman is coming')
print(mo6.group())

phoneNumberRegex4 = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneNumberRegex4.search('My number is 415-555-4332')
mo7 = phoneNumberRegex4.search('My number is 555-4567')
print(mo1.group())
print(mo1.group(1))

print('\n'+ mo7.group())
print(mo7.group(1))


#Matching Zero or more with the star
batRegex5  = re.compile(r'Bat(wo)*man')
mo8 = batRegex5.search('Batwowowoman is intelligent')
print(mo8.group())

#Matching one or more with the plus
batRegex6  = re.compile(r'Bat(wo)+man')
mo9 = batRegex6.search('Batwowoman is intelligent')
print(mo9.group())

#Matching Specific repetitions with curly brackets
haRegex = re.compile(r'(Ha){,3}')
ha_mo = haRegex.search('HaHaHa')
print(ha_mo.group())

ha_mo2 = haRegex.search('Ha')
print(ha_mo2.group())


haRegex2 = re.compile(r'(Ha){3,5}')
ha_mo = haRegex2.search('HaHaHa')
ha_mo2 = haRegex2.search('HaHaHaHa')
ha_mo3 = haRegex2.search('HaHaHaHaHa')
print(ha_mo.group())
print(ha_mo2.group())
print(ha_mo3.group())

greedyHaRegex = re.compile(r'(Ha){3,5}')
ha_mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(ha_mo1.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
ha_m1 = nongreedyHaRegex.search('HaHaHaHaHa')
print(ha_m1.group())


#The findall() method
phoneNumberRegex10 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegex10.findall('My number is 415-555-4332, 215-555-4213')
print(mo)

#---findall() method with groups
phoneNumberRegex11 = re.compile(r'((\d\d\d)-(\d\d\d)-(\d\d\d\d))')
mo = phoneNumberRegex11.findall('My number is 415-555-4332, 215-555-4213')
print(mo)

xmasRegex = re.compile(r'\d+\s\w+')
result = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies')
print(result)

# This will match all vowels both upper and lower case in a string
vowelRegex = re.compile(r'[aeiouAEIOU]')
result = vowelRegex.findall('My name is Anonymous suomynona')
print(result)

# This will match all the non-vowels (i.e Consonants) both upper and lower case in a string
vowelRegex = re.compile(r'[^aeiouAEIOU]')
result = vowelRegex.findall('Anonymous suomynona')
print(result)


#Caret and dollar sign characters

beginsWithHello = re.compile(r'^Hello')
bo = beginsWithHello.search('Hello World')
print(bo.group())

# bo1 = beginsWithHello.search('World Hello')
# print(bo1.group())



