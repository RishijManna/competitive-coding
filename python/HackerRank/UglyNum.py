def ugly(n):
    for p in [2,3,5]:
        while n%p==0:
            n//=p
    return n==1

t=int(input())
for i in range(t):
    n=int(input())
    c=0
    num=1
    while True:
        if ugly(num):
            c+=1
            if c==n:
                print(num)
                break
        num+=1
