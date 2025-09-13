s=input()
l=[]
c=[]
me=10000000
mo=0
for i in s:
    l.append(i)
for i in l:
    n=l.count(i)
    if n%2==0:
        me=min(me,n)
    elif n%2==1:
        mo=max(mo,n)
print(abs(mo-me))
