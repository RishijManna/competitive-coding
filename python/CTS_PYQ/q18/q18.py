def perm(s,ans='',l=None):
    if l is None:
        l=[]
    if len(s)==0:
        l.append(ans)
        return l
    for i in range(len(s)):
        ch=s[i]
        val= s[:i]+s[i+1:]
        perm(val,ans+ch,l)
    return l
    
s='indraNil'
s1=''
for i in s:
    if i=='a' or i=='A' or i=='e' or i=='E' or i=='i' or i=='I' or i=='o' or i=='O' or i=='u' or i=='U':
        pass
    else:
        s1=s1+i
l=perm(s1)
print(len(l))
