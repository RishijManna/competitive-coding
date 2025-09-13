s=input()
l=[]
c=[]
temp=[]
me=0
k=10000
for i in s:
    l.append(i)
    if i not in temp:
        temp.append(i)
for i in temp:
    c.append(l.count(i))
print(c)
for i in c: 
    c1=c.count(i)
    if c1>=me:
        me=c1
        if k>i:
            k=i

print(k)    



#ACABDDABDCDACFAEGFDA
#ACABABCCA
