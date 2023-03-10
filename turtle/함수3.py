def get_sum(a,b):
    s=0
    for i in range(a,b+1):
        s=s+i
    return s
a=int(input())
b=int(input())
print('%d부터 %d까지의 합은 %d입니다.'%(a,b,get_sum(a,b)))