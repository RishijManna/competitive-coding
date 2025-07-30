# https://www.codechef.com/START197D/problems/BOWLBALL
T=int(input())
for i in range(T):
    N,X,Y=map(int,input().split())
    l=list(map(int,input().split()))
    c=0
    for i in l:
        if i>=X and i<=Y:
            c=c+1
    print(c)
