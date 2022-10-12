
#LIST
alist = ['cat','dog','cow']
print(alist)

#List Concatenation and list Replication
spam = [1,2,3] 
spam2 = [4,5,6]
spam3 = spam + spam2
print(spam3)

spam4 = spam3 * 3
print(spam4)

#Multiple Assigmnent with List
student_list = ["Jide","Samuel",24,"Nigeria"]
firstName = student_list[0]
lastName = student_list[1]
age = student_list[2]
country = student_list[3]

#           OR

firstName,lastName,age,country = student_list
print(firstName,  lastName , age , country)

#Augumented assignment operators
greeting = "Good Morning"
greeting += " Sam"
print(greeting)

food = 'Bread '
food *= 3
print(food)

#Finding a value in a list with the index() method
names = ["Lola","Hailey","Aurora","Laura"]
haileyIndex = names.index('Hailey')
print(haileyIndex)

names2 = ["Henry","Bailey","Arnold","Lawson","Bailey"]
baileyIndex = names2.index('Bailey')
print(baileyIndex)