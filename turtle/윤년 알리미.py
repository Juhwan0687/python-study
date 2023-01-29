a=int(input('연도를 입력하세요:'))
if a%4==0 and a%100!=0:
    print('\nleap year\n')
else:
    print('\ncommon year\n')