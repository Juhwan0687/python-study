from random import*
com= randint(1,2)
user=int(input('odd:1,even:2\n'))
print('com(%d):user(%d)'%(com,user))
if com==user:
    print('correct')
else:
    print('incorrect')