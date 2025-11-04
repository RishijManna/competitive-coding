l=list(map(int,input().split()))
n=int(input())
n1=len(l)
ans=[]
for i in range(n1-n+1):
    ans.append(max(l[i:i+n]))
    
print(*ans)
