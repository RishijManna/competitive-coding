n,m=map(int,input().split())
mat=[]
for i in range(n):
    l=list(map(int,input().split()))
    mat.append(l)
re=[]

for d in range(n+m-1):   #m+n-1  = no of diagonal of m*n matrix hoe
    row=min(d,n-1)
    col=d-row   # we know , m+n-1  = no of diagonal of m*n matrix hoe. So ai equation e 'n-1' er jagae row bosale d=m+row  hoe. So m= d-row.  (m holo akhane col) 

    while row>=0 and col<m:
        re.append(mat[row][col])
        row-=1
        col+=1


print(*re)
