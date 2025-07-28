#Link -> https://www.hackerrank.com/contests/classroom-coding-challenge-strings-problems/challenges/remove-consecutive-characters-5

def fun(l):
    s=''
    for i in l[0]:
        s=s+i
        for j in l:
            if s not in j:
                return s[:-1]
    return s
n=int(input())
l=[]
for i in range(n):
    l.append(input().lower())
print(fun(l))
