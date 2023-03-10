def get_sum(n):
    s=0
    for i in range(n):
        s+=int(input())
    return s
n=int(input('Enter integer n : '))
print('sum :',end=str(get_sum(n)))