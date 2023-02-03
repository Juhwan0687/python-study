from random import*
b=int(input('1~5'))
a=['1','2','3','4','5']
print(choices(a,[1,1,10,1,1]))
print(choices(a,k=b))