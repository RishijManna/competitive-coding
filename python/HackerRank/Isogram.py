#https://www.hackerrank.com/contests/classroom-coding-challenge-14325/challenges/isogram-3-1
def iso(s):
    for i in s:
       
        if s.count(i)>1:
            return 0
    return len(s)
s1=input()
s=[]
for i in s1:
    s.append(i.lower())  

print(iso(s))

