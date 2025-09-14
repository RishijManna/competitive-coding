n=int(input())
l=list(map(int,input().split()))
ans=[]
for i in range(n):
    c=0
    if l[(i-1+n)%n]>l[i]:
        c=c+1
    if l[(i+1+n)%n]>l[i]:
        c=c+1
    ans.append(c)
    
print(ans)
