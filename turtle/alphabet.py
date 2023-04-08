f=open('alphabet.txt','r+')
index=int(input('Index : '))
alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in alphabet:
    f.write(i)
f.seek(index)
print(f.readline())
f.close()