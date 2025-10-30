#https://www.hackerrank.com/contests/classroom-coding-challenge-14325/challenges/minimize-marked-fruits-1-1/problem
n=int(input())
l=list(map(int,input().split()))
if n==1:
    print(l[0])
else:
    ans=[]
    for i in range(n):
        if i==0:
            ans.append(l[1])
        elif i==n-1:
            ans.append(l[n-2])
        else:
            ans.append(l[i-1]+l[i+1])
    print(*ans)
