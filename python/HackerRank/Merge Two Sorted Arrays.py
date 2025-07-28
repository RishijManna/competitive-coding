# link ->https://www.hackerrank.com/contests/classroomtech-coding-contest/challenges/merge-two-sorted-arrays-24
n1=int(input())
l1=list(map(int,input().split()))
n2=int(input())
l2=list(map(int,input().split()))
for i in l2:
    l1.append(i)
l1.sort()
print(*l1
