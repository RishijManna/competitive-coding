#https://www.hackerrank.com/contests/classroomtech-coding-contest/challenges/second-distinct-largest-element-in-an-array
n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
l1.sort()
n1=len(l1)
if n1>1:
    print(l1[-2])
else:
    print("NO SECOND LARGEST")
