f=open('fruit.txt','r+')
fruit=['apple','banana','orange','grape','kiwi','strawberry','wildberry','watermelon','mango','papaya','coconut']
for i in fruit:
    f.write(i)
    f.write('\n')
data=f.readline()
data2=f.readline()
data3=f.readline()
data4=f.readline()
data5=f.readline()
data6=f.readline()
data7=f.readline()
data8=f.readline()
data9=f.readline()
data10=f.readline()
data11=f.readline()
f.seek(0)
if len(data)>=10:print(data)
if len(data2)>=10:print(data2)
if len(data3)>=10:print(data3)
if len(data4)>=10:print(data4)
if len(data5)>=10:print(data5)
if len(data6)>=10:print(data6)
if len(data7)>10:print(data7)
if len(data8)>=10:print(data8)
if len(data9)>=10:print(data9)
if len(data10)>=10:print(data10)
if len(data11)>=10:print(data11)
f.close()