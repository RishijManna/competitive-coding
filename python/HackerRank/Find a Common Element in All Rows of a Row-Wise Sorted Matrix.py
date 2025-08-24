#
def fun(a,m,n):
    for i in a[0]:
        for j in range(1,m):
            if i not in a[j]:
                break
            if j==m-1:
                return i
    return -1

m,n= map(int,input().split())
a=[]
for i in range(m):
    ar=list(map(int,input().split()))
    a.append(ar)
print(fun(a,m,n))

