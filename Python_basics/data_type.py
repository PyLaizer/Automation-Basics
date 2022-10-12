# from this import d

#string type
name = 'Audrey'
x = name.index('d')
print(x)
print(name)

#Tuple datatype
y = ("aiden",)
print(type(y))

#converting types
a = "Volcano"
b = ["volume","violin","viola"]
c = ("Vini","Volks","vault")

print(list(a))
print(tuple(a))

print(tuple(b))

print(list(c))

# R E F E R E N C E S 
#immutable
num1 = "Better"
num2 = num1
num1 = "Bitter"
print(num1)
print(num2)

# Mutable
alist = {1,3,5,7,9}
blist = alist
alist.add(11)
print(alist)
print(blist)

def eggs(num):
    num.append(7)

clist = [1,3,5]
eggs(clist)
print(clist)    

#The copy Module
import copy
vowels = ["a","e","i","o","u"]
alpha = copy.copy(vowels)
alpha.append("ae")
print(alpha)
print(vowels)


bacon = [3.14, 'cat', 11, 'cat', True]
bacon.remove('cat')
print(bacon)
