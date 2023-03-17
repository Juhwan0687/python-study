from random import*

def lotto():
    lot=[]
    for i in range(6):
        lot.append(randint(1,45))

    lot.sort()
    a=set(lot)
    if len(a)!=6:
        for j in range(6-len(a)):
            lot.append(randint(1,45))
        lot.sort()
    print(lot)
lotto()