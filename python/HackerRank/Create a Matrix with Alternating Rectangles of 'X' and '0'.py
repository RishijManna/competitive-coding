#https://www.hackerrank.com/contests/classroomtech-coding-challenge-2d-array-problem/challenges/create-a-matrix-with-alternating-rectangles-of-x-and-0/problem

def spiralOrder(m,n):
    l,t=0,0
    r=n-1
    b=m-1
    ans=[]
    for i in range(m):
        a=['0']*n 
        ans.append(a)
    z=1
    while l<=r and t<=b:
        for i in range(l,r+1):
            if z%2==1:
                ans[t][i]="X"
            else:
                ans[t][i]="0"
        t+=1
        for i in range(t,b+1):
            if z%2==1:
                ans[i][r]="X"
            else:
                ans[i][r]="0"
        r-=1

        if t<=b:
            for i in range(r,l-1,-1):
                if z%2==1:
                    ans[b][i]="X"
                else:
                    ans[b][i]="0"
            b-=1

        if l<=r:
            for i in range(b,t-1,-1):
                if z%2==1:
                    ans[i][l]="X"
                else:
                    ans[i][l]="0"
            l+=1
        z=z+1
    return ans
    
m,n=map(int,input().split())
ans=spiralOrder(m,n)
for i in range(m):
    print(*ans[i])
