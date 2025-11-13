N,t=map(int,input().split())
l=list(map(int,input().split()))
ans=-1
for i in range(-1,-N-1,-1):
    if l[i]==t:
        ans=N+i+1
        break
print(ans)
        
