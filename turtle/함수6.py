def number(x):
    if x%2==0:
        s='Even'
        return s
    else:
        s='Odd'
        return s
x=int(input())
print(number(x))