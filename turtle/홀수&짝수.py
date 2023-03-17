a=int(input('정수를 입력하세요.'))
def f(n):
    print(n)
    if n>2:
        f(n-2)
f(a)