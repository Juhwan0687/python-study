a=0
def f():
    global a
    global b
    print(a)
    a=10
    b=20
f()
print(a)
print(b)