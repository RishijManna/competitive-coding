#https://www.hackerrank.com/contests/classroom-coding-challenge/challenges/rabbits-in-forest-2/submissions/code/1395241887
def numRab(ans):
    f={}
    t=0
    for i in ans:
        if i==0:
            t+=1  
        elif i not in f:
            f[i]=1 
            t+=i+1  
        else:
            f[i]+=1
            if f[i]>i+1:
                f[i]=1
                t+=i+1
    return t

T=int(input())
for i in range(T):
    n=int(input())
    l=list(map(int,input().split()))
    print(numRab(l))
