#https://www.hackerrank.com/contests/classroomtech-coding-contest/challenges/subset-sum-problem-2-2

n,S=map(int, input().split())
arr=list(map(int, input().split()))
dp=[False]*(S+1)
dp[0]=True
for i in arr:
    for j in range(S,i-1,-1):
        if dp[j-i]:
            dp[j]=True
if dp[S]:
    print("YES")
else:
    print("NO")
