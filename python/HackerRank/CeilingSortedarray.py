def fun(n,l,x):
    for i in l:
        if i>=x:
            return i
    return -1 
n= int(input())
l=list(map(int,input().split()))
x=int(input())
c=fun(n,l,x)
if c==-1:
    print(c)
else:
    print(l.index(c))
