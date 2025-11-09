s=input()
#print(s)
l=len(s)
ans=[]
for i in range(l-4+1):
    s1=''
    if s[i].isdigit() and s[i+1].isdigit() and s[i+2].isdigit() and s[i+3].isdigit():
        s1=s1+s[i]
        s1=s1+s[i+1]
        s1=s1+s[i+2]
        s1=s1+s[i+3]
        
        if s1 not in ans:
            ans.append(s1)
            #print(ans)
print(len(ans))
