from random import*
com=randint(1,3)
user=int(input('1:가위, 2:바위, 3:보\n'))
if user==1:
    user='가위'
elif user==2:
    user='바위'
else:
    user='보'
if com==1:
    com='가위'
elif com==2:
    com='바위'
else:
    com='보'
print('COM(%s) : USER(%s)'%(com,user))
if user==com:
    print('Draw!') #보:보, 가위:가위, 바위:바위
elif com=='가위' and user=='보':
    print('Com Wins!')#가위:보
elif user=='가위' and com=='보':
    print('User Wins!')#보:가위
elif com=='가위' and user=='바위':
    print('User Wins!')#가위:바위
elif com=='바위' and user=='가위':
    print('Com Wins!')#바위:가위
elif com=='보' and user=='바위':
    print('Com Wins!')#보:바위
elif com=='바위' and user=='보':
    print('User Wins!')#바위:보