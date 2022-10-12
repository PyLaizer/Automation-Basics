#Chap 5: Fantasy Game Inventory

superGinger = {
   'helmet_duration':120,'magnet_duration':94,
   'plane_duration':130,'double_bars_duration':127,
   'free_save_me_per_run':1 
}

def displayInventory(inventory):
    print("Inventory:")
    total = 0
    for k,v in inventory.items():
        print(str(v) + " " + k)
        total += v
    print("Total number of times: " + str(total))
        

displayInventory(superGinger)

gameloot = ['magnet_duration','magnet_duration','double_bars_duration',
            'magnet_duration','free_save_me_per_run','double_bars_duration',
            'double_bars_duration','magnet_duration']

def addToInventory(inventory,addedItems):
    print("Inventory:")
    total = 0
    for k,v in inventory.items():
        for item in addedItems:
            if k == item:
                v += 1
        print(str(v) + " " + k)
        total += v  
    print("Total number of items: " + str(total))    

addToInventory(superGinger,gameloot)         

