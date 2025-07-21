''' Question Link:  www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true  '''

#Python Code: 
x = int(input())
y = int(input())
z = int(input())
n = int(input())
l=[]
for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
            l1=[i,j,k]
            if sum(l1)!= n:
                l.append(l1)
print(l)
