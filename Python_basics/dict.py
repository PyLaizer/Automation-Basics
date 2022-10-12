import pprint

#The get() method
foodstuffs = {
    'soda':5,
    'pancakes':3,
}

x = "Here are the " + str(foodstuffs.get('soda', 8)) + " sodas."
y = "Here are the " + str(foodstuffs.get('cheesecakes', 2)) + " cheesecakes."
print(x)
print(y)

#The setdefault() method
foodstuffs.setdefault('beers',16)
print(foodstuffs['beers'])

foodstuffs.setdefault('pancakes',8)
print(foodstuffs['pancakes'])

print(foodstuffs)

text = "Welcome To Jumaji, I will be exicted to assist you in your journey Dr Bravestone"
count = {}

for char in text:
    count.setdefault(char,0)
    count[char] = count[char] + 1
print(count)
pprint.pprint(count)
# print(sorted(count.values(),reverse=True))  

# print(text)

pprint.pprint(text)
#OR
print(pprint.pformat(text))