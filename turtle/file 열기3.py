f=open('example.txt','a')
alphabet=['A','B','C','D','E']
f.write('\n')
for c in alphabet:
    f.write(c)
    f.write(' ')
f.close()