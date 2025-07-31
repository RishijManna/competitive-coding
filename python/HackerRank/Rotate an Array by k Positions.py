#Link -> https://www.hackerrank.com/contests/classroomtech-coding-contest/challenges/rotate-an-array-by-k-positions-1
n,k=map(int,input().split())
l=list(map(int,input().split()))
ans=l[n-k:]+l[:n-k]
print(*ans)
