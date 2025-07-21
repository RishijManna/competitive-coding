def fun(n,k,l):
    l1=[]
    for i in range(0,n-1):
        
        s=l[i]
        for j in range(i+1,n):
            s=s+l[j]
            if s%k==0:
                
                l1.append(j-i+1)
    return(max(l1))

n,k= map(int,input().split())
l=list(map(int,input().split()))
print(fun(n,k,l))
