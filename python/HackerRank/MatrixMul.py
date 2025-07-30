#https://www.hackerrank.com/contests/classroomtech-coding-contest/challenges/matrix-multiplication-64-1
p,q,r=map(int,input().split())
l=[]
l1=[]
for i in range(p):
    temp=list(map(int,input().split()))
    l.append(temp)
for i in range(q):
    temp=list(map(int,input().split()))
    l1.append(temp)
ans=[]
for i in range(p):
    c=[0]*r
    ans.append(c)

    
for i in range(p):
    for j in range(r):
        for k in range(q):
            ans[i][j]+=l[i][k]*l1[k][j]
for i in ans:
    print(*i)
