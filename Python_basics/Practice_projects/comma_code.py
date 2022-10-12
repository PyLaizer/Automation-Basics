#Chap 4: Comma Code

spam = ['apples', 'bananas', 'tofu', "cats", "dogs", "chicken","veggies"]

def commafunc(value):
    x = ''
    last_item = value[-1]
    for item in value:
        if item == last_item:
            x += "and " + item + "."
        else:    
            x += item + ", "
    print("\n" + x)  

commafunc(spam)    