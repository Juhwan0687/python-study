f=open('profile.txt','w')
name=input('이름을 입력하세요 : ')
age=input('나이를 입력하세요 : ')
f.write('Name : %s\n'% name)
f.write('Age : %s\n'% age)
f.close()