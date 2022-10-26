spam = "There's fire on the mountain"
print(spam)

#Escape characters
text1 = 'Say Hi to Jason\'s mother'
print(text1)

print("Hello dear\nTrust you are having a great day\nWish you all the best in the world.☺️")

#Raw Strings
print(r'Say Hi to Jason\'s mother')

#Multiline strings
print(""" I am BLACK,

I am White,
I am Pale,
I am RED.""")


x = "redty12"
print(x.upper())

y = "45"
print(y.isalnum())

#Justifying text with rjust(),ljust() and center

print('hello'.rjust(10,"+"))
print('hello'.ljust(10,"+"))
print('hello'.center(10,"+"))

#Removing whitespace and text with strip(), rstrip() and lstrip()
spam1 = "AreAreAreYouAreaveryHandsomemanAreAreAre"
print(spam1.strip('Are'))