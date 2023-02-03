from random import*
a=[1,2,3,4,5,6,7,8,9,10]
n=choices(a,[1,1,1,1,1,1,10,1,1,1],k=3)
if 3==n.count(7):
    print('Lucky!')
elif 2==n.count(7):
    print('Good~')
elif 1==n.count(7):
    print('So so.')