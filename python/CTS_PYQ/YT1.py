# Online Python compiler (interpreter) to run Python online.
n1=int(input())
l1=list(map(int,input().split()))
n2=int(input())
l2=list(map(int,input().split()))
s1=set(l1)
s2=set(l2)
s3= s1.intersection(s2)
l=list(s3)
if l:
    print(*l)
else:
    print("No common employees")
