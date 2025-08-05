#https://www.hackerrank.com/contests/classroomtech-coding-contest/challenges/minimum-number-of-coins-for-a-given-amount/copy-from/1395443353
n,v= map(int,input().split())
l=list(map(int,input().split()))
dp=[10000]*(v+1)
dp[0]=0
for i in range(1,v+1):
    for j in l:
        if i>=j:
            dp[i]=min(dp[i],dp[i-j]+1)

if dp[v]==10000:
    print(-1)
else:
    print(dp[-1]) 
    
    
    
