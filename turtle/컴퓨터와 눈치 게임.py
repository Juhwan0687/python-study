from random import*
com=randint(1,2)
user=int(input('odd:1 even:2\n'))
if user==1:
    user='odd'
else:
    user='even'
if com==1:
    com='odd'
else:
    com='even'
print('COM(%s):USER(%s)'%(com,user))
if com==user:
    print('Correct!')
else:
    print('Incorrect!')