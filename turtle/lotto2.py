from random import*

def lotto():
    lot=[]
    while True:
        n=randint(1,45)
        if n not in lot:
            lot.append(n)
            if len(lot)==6:
                break
    lot.sort()
    print(lot)
lotto()