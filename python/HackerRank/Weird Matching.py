#https://www.hackerrank.com/contests/classroom-coding-challenge-17896/challenges/weird-matching-1

def ma(a,b):
    n=len(a)
    for i in range(n):
        if a[i]!=b[i]:
            if a[i]=="*":
                pass
            elif b[i]=='*':
                pass
            else:
                return "No"
    return 'Yes'
a=input()
b=input()
print(ma(a,b))
