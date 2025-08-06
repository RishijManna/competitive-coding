#https://www.hackerrank.com/contests/classroomtech-coding-contest/challenges/detect-cycle-in-a-linked-list-2-1
class Node:
def __init__(self,val):
        self.val=val
        self.next=None

    def cir(self,n,l,pos):
       
        nodes=[]
        for i in range(n):
            nodes.append(Node(l[i]))

        for i in range(n-1):
            nodes[i].next=nodes[i+1]

        if pos!=-1:
            nodes[-1].next=nodes[pos]

        slow=fast=nodes[0]
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return "true"
        return "false"

n=int(input())
l=list(map(int, input().split()))
p=int(input())
obj=Node(0)
print(obj.cir(n,l,p))
