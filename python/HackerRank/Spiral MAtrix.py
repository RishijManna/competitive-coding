#https://www.hackerrank.com/contests/classroomtech-coding-challenge-2d-array-problem/challenges/spiral-matrix-83-1/submissions/code/1396010288
def spiralOrder(matrix):
    l,t=0,0
    m=len(matrix)
    n=len(matrix[0])
    r=n-1
    b=m-1
    ans=[]  
    while l<=r and t<=b:
        for i in range(l,r+1):
            ans.append(matrix[t][i])
        t+=1
        for i in range(t,b+1):
            ans.append(matrix[i][r])
        r-=1

        if t<=b:
            for i in range(r,l-1,-1):
                    
                ans.append(matrix[b][i])
            b-=1

        if l<=r:
            for i in range(b,t-1,-1):
                ans.append(matrix[i][l])
            l+=1
    print(*ans)
    
n,k=map(int,input().split())
m=[]
for i in range(n):
    l=list(map(int,input().split()))
    m.append(l)

spiralOrder(m)
