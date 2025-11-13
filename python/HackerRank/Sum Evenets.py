#Sum Evenets  https://www.hackerrank.com/contests/classroom-coding-challenge-17896/challenges/arin-is-given-an-integer-n-all-day-he-plays-with-this-integer-seeing-this-his-dad-gives-him-a-problem-to-solve-he-wants-arin-to-calculate-the-sum-of-all-the-integers-upto-n-which-are-even-

n=int(input())
s=0
for i in range(2,n+1,2):
    s=s+i 
print(s)
