s='3435346456547566345436457867978'
n=len(s)
s1=0
s2=0
for i in range(n):
    if i%2==0:
        s1=s1+int(s[i])
    else:
        s2=s2+int(s[i])
        
if s2>=s1:
    print((s2-s1)%11)
else:
    print((s1-s2)%11)    
    
        
