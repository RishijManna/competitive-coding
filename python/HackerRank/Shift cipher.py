s=input()
ans=''
for i in s:
    if i.isupper():
        ans+=chr(((ord(i)-65+3)%26)+65)
    elif i.islower():
        ans+=chr(((ord(i)-97+3)%26)+97)
print(ans)
