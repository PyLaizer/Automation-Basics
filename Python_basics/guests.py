
allGuests = {
    'Uche':{'cakes':5,'beer':8,'fried_chicken':6},
    'Nico':{'peppered_meat':10,'bottle_water':8,'juice':4},
    'Laizer':{'bottle_water':5,'malt_drink':8,'fried_turkey':5,'shawarma':4},
}

def totalBrought(guests,item):
    num_brought = 0
    for k,v in guests.items():
        num_brought = num_brought + v.get(item,0)
    return num_brought

print("Number of things brought:")
print(" - Bottle Water: " + str(totalBrought(allGuests,"bottle_water")))  
print(" - Fried Chicken: " + str(totalBrought(allGuests,"fried_chicken")))
print(" - Fried Turkey: " + str(totalBrought(allGuests,"fried_turkey")))
print(" - Eggs: " + str(totalBrought(allGuests,"egg")))  