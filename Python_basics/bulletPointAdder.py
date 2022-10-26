#! python3
# Bulletpointadder.py - Adds Wikipedia bullet point to the start of each line of text on the clipboard

import pyperclip
text = pyperclip.paste()

#Seperate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '*'+ lines[i]

text = '\n'.join(lines)
pyperclip.copy(text)

