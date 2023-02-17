a=str(input('정수를 입력해주세요.'))
sum=0
i=1
b=len(a)
c=int(a)
for i in range(b+1):
    d=c%10
    sum+=d
    d=c/10
print(int(sum/2))