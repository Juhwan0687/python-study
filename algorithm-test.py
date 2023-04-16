

1번

a=input()
print(a[0:1])
print(a[2:3])
print(a[4:])
if a[0:1]==a[2:3] and a[2:3]==a[4:]:
    b=1000*int(a[2:3])
    print(b+10000)
elif a[0:1]==a[2:3]:
    b=int(a[0:1])*100
    print(b+1000)
elif a[0:1]==a[4:]:
    b=int(a[0:1])*100
    print(b+1000)
elif a[2:3]==a[4:]:
    b=int(a[2:3])*100
    print(b+1000)
else:
    if a[0:1]>a[2:3] and a[0:1]>a[4:]:
        print(int(a[0:1])*100)
    elif a[2:3]>a[0:1] and a[2:3]>a[4:]:
        print(int(a[2:3])*100)
    else:
        print(int(a[4:])*100)
        
       
      
      
2번

c=int(input())
score=input()
a=[]
b=-1
d=score[b+1:]
b=d.index(' ')
a.append(score[0:b])
a.append(score[b+1:])
a.sort()
print(int(a[1])-int(a[0]))


4번
n=int(input())
n2=int(input())
a=[]
time=0
floor=0
for i in range(n):
    a.append(input())
    a.append(int(input()))
while n!=floor:
    if a[len(a)-1]+a[len(a)-3]==n2:
        time+=0
        floor+=1
    else:
        d=n2-a[len(a)-1]+a[len(a)-3]
        time+=d
        floor+=1
    if floor==1:
        if a[len(a)-3]+a[len(a)-3]-d==n2:
            time+=0
            floor+=1
        else:
            d=n2-d-a[len(a)-3]+a[len(a)-5]
            time+=d
            floor+=1
    for i in range(n-floor):
        if a[len(a)-3]+a[len(a)-3]-d==n2:
            time+=0
            floor+=1
        else:
            d=n2-d-a[len(a)-3]+a[len(a)-5]
            time+=d
            floor+=1
print(time)            
       
