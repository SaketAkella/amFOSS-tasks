city=int(input("Cities to be attacked"))
for i in range(city):
    heroes=int(input("Heroes stationed there"))
    lvl=list(input("Level of Heroes: ").split())
    
    hero=False
    for j in lvl:
        lvl.count(j)# similar lvl heroes in list
        if lvl.count(j)>1:
            hero=True
            break
        else:
            continue
    if "0" in lvl: #if there is 0 element in list lvl
        print(heroes-lvl.count("0"))
    elif hero==True: #if there are same element in list lvl
        print(heroes)
    else:# if there is nither same level heros nor o lvl hero
        print(heroes+1) 
    
        