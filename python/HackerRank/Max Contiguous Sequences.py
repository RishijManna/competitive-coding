n=int(input())
l=list(map(int,input().split()))
ans=[]
s=0
for i in l:
    if i>=0:
        s=s+i
    else:
        ans.append(s)
        s=0
print(max(ans))
