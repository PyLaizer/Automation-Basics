
picnicDict = {'cakes':5,'beer':8,'fried_chicken':6,
            'peppered_meat':10,'bottle_water':8,'juice':4}

def picnicfunc(itemDict,leftwidth,rightwidth):
    print('PICNIC ITEMS'.center(leftwidth + rightwidth, "-"))
    for k,v in itemDict.items():
        print(k.ljust(leftwidth,'.') + str(v).rjust(rightwidth))


picnicfunc(picnicDict,20,3)

