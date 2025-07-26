
link -> https://www.hackerrank.com/contests/classroomtech-coding-contest/challenges/case-insensitive-character-frequency-with-sorting/submissions/code/1394914158
s=input()
s=s.lower()
d=[]
d1=[]
for i in s:
    if i.isalnum():
        if i not in d1:
            d1.append(i)
            d.append([i,s.count(i)])
d.sort()
for i in d:
    print(i[0],":",i[1])
