a=int(input())
def f(n):
    print(n)
    if n>1:
        f(n-1)
f(a-1)