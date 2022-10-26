#Chap 7
import re

def passwordfunc(pw):
    passwordRegex = re.compile(r'([a-zA-Z0-9]+){8,}')
    p_match = passwordRegex.search(pw)
    print(p_match.group())

passwordfunc('q1P0w2O9er45t6YU78iop')

