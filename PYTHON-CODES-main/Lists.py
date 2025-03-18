
#Question LInk: https://www.hackerrank.com/challenges/python-lists/problem

N = int(input())
l=[]
for i in range(0,N):
    com = list(map(str,input().split()))
    if com[0] == "insert":
        l.insert(int(com[1]), int(com[2]))
    elif com[0] == "print":
        print(l)
    elif com[0] == "remove":
        l.remove(int(com[1]))
    elif com[0] == "append":
        l.append(int(com[1]))
    elif com[0] == "sort":
        l.sort()
    elif com[0] == "pop":
        l.pop()
    elif com[0] == "reverse":
        l.reverse()
