n=int(input())
f=open('example.txt','w')
for i in range(1,n+1):
    f.write('Line %d\n'%i)
f.close()