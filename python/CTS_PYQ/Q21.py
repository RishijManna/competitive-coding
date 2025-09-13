i1=int(input())
i2=int(input())
i3=int(input())
l=list(map(int,input().split()))
ma=0
mi=0
c=0
for i in l:
    if i<i2 or i>i3:
        c=c-1
    else:
        c=c+1
    ma=max(ma,c)
    mi=min(mi,c)
    
print(ma,mi)
