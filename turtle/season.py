a=int(input())
def season(n):
    if n<=5 and n>=3:
        print('Spring')
    elif n<=8 and n>=6:
        print('Summer')
    elif n>=9 and n<=11:
        print('Fall')
    elif n==12:
        print('Winter')
    elif n>=1 and n<=2:
        print('Winter')
season(a)