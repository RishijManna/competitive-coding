#https://www.hackerrank.com/contests/classroomtech-coding-contest/challenges/sum-of-elements-in-a-subarray-prefix-sum/copy-from/1395366460

n,q=map(int,input().split())
l=list(map(int,input().split()))
l1=[0]*(n+1)
l1[0]=0
l1[1]=l[0]
for j in range(1,n):
    l1[j+1]=l1[j]+l[j]

for i in range(q):
    x,y=map(int,input().split())
    print(l1[y]-l1[x-1])
    
    
  
