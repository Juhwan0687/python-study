from random import*
a=randint(1,6)
b=randint(1,6)
c=randint(1,6)
d=randint(1,6)
print('\n==첫 번째 주사위==\nA(%d) : B(%d)'%(a,b))
print('\n==두 번째 주사위==\nA(%d) : B(%d)\n'%(c,d))
if a+c>=10:
    if b+d>=10:
        if a+c>b+d:
            print('==경기 결과==\nA(%d) : B(%d)\n'%(a+c,b+d))
            print('A님 승리!\n')
        else:
            print('==경기 결과==\nA(%d) : B(%d)\n'%(a+c,b+d))
            print('B님 승리!\n')
    else:
        print('==경기 결과==\nA(%d) : B(%d)\n'%(a+c,b+d))
        print('A님 승리!\n')
elif a+c==b+d and (a+c>=10 and b+d>=10):
    print('==경기 결과==\nA(%d) : B(%d)\n'%(a+c,b+d))
    print('비겼습니다.\n')
elif b+d>=10:
    print('==경기 결과==\nA(%d) : B(%d)\n'%(a+c,b+d))
    print('B님 승리!\n')
elif a+c<10 and b+d<10:
    print('==경기 결과==\nA(%d) : B(%d)\n'%(a+c,b+d))
    print('모두 실패하셨습니다.\n')