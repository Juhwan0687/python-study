def plus(x):
    if x>0:
        a='True'
        return a
    elif x<0:
        a='False'
        return a
x=int(input('정수를 입력하세요.\n'))
result=plus(x)
print(result)