#The collatz sequence

def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1

# print(collatz(12))           

print('Type any number')
while True:
    try:
        x = int(input())
    except ValueError:
        print('Invalid Number: Type a proper integer')   
    else:     
        value = (collatz(x))
        print(value)
        if value == 1:
            break
