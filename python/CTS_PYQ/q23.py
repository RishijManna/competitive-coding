def perm(s,ans='',l=None):
    if l is None:
        l=[]
    if len(s)==0:
        l.append(ans)
        return l
    for i in range(len(s)):
        ch=s[i]
        val=s[:i]+s[i+1:]
        perm(val,ans+ch,l)
    return l


s = 'RishijMannA'
s1 = ''

for i in s:
    if i in ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']:
        pass
    else:
        s1=s1+i
l=perm(s1)
print(len(l))
