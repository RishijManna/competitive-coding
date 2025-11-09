n=list(map(str,input().split()))

l=len(n)
s=0
for i in n:
    s=s+int(i)
print(s//l)
