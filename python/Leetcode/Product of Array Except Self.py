#https://leetcode.com/problems/product-of-array-except-self/description/
def fun(l,n):
    ans=[0]*n
    p=1
    s=1
    for i in  range(n):
        ans[i]=p
        p=p*l[i]
    for i in range(n-1,-1,-1):
        ans[i]=ans[i]*s
        s=s*l[i]
    return ans
n=int(input())
l=list(map(int,input().split()))
print(*fun(l,n))
