#https://www.hackerrank.com/contests/classroomtech-coding-contest/challenges/range-sum-query-and-point-update-using-segment-tree

n,q=map(int,input().split())
l=list(map(int,input().split()))
dp=[0]*(n+1)
for i in range(1,n+1):
    dp[i]=dp[i-1]+l[i-1]
for i in range(q):
    k,le,r=map(int,input().split())
    if k==2:
        ans=dp[r]-dp[le-1]
        print(ans)
    elif k==1:
        a=r-l[le-1]
        for g in range(le,n+1):
            dp[g]+=a
            
