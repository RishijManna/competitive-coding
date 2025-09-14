s=input()
n=len(s)
c=0
for i in range(n-1):
    dif=abs(ord(s[i])-ord(s[i+1]))
    c=c+dif
    
print(c)
