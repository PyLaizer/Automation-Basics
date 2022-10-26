#Chap 6: Table Printer

tableData = [
    ['Coca-cola','Pepsi','Fanta','Malt','Monster'],
    ['Sausage','Doughnut','Shawarma','Meatpie','Cake'],
    ['Fried-rice','Spaghetti','Noodles','Meat','Chicken']
]


def printTable(data):
    final = ''
    i = 0
    index = 0
    while i < len(data[0]):
        for item in data:
            x = item[index].rjust(11)
            final = final + x
        print(final)    
        i += 1
        index += 1
        final = ''

printTable(tableData)