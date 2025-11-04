def fun(n):
    i=1
    s=0
    while(i<=n):
        #print(n//i)
        s=s+(n//i)
        i=i*2
    return s
n=int(input())
print(fun(n))
