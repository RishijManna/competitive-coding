'''An astrologer gives a matrix to De'villiers and tells him to add the largest row sum and largest column sum of the given matrix. The number which appears as a result is his lucky number for the final match jersey.

Write a program that adds up the largest row sum and the largest column sum from an N- rows*M-columns array of numbers to help De'villiers find his lucky number for the final match jersey.

As a preliminary phrase, you should reformat the sequence of numbers as a matrix, whose number of rows and columns are to be specified as arguments.

Input Specification:

Input 1: Integer for row dimension of the array

Input 2: Integer for column dimension of the array

Input 3: Array elements to be entered in row major.

Output Specifications:

Largest row sum+ Largest column sum

Example 1:

Input1:4

Input2: 4

Input3: {1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4}

Output: 26

Explanation:

The array has 4 rows (input1) and 4 columns (input2). The largest sum among the four columns is 10 and the largest sum among the four rows is 16. We get the final sum of 26 (10+16).

Example 2:

Input 1:2

Input 2: 2

Input 3: {1,2,5,6}

Output: 19

Explanation:

The array has 2 rows (input1) and 2 columns (input2). The elements in the first row are 1 and 2 and the elements in the second row are 5 and 6 (input3). The largest sum among the two columns is 8(2+6) By adding those two up. We get the final sum of 19 (11+8).

Example 3:

Input 1: 3

Input 2: 3

Input 3: {3,6,9,1,4,7,2,8,9}
'''
r=int(input())
c=int(input())
l=list(map(int,input().split()))
ar=[]
n=0
for i in range(r):
    k=[]
    for j in range(c):
        k.append(l[n])
        n=n+1
    ar.append(k)
s1=0
s2=0
s1max=0
s2max=0
for i in range(r):
    for j in range(c):
        s1=s1+ar[i][j]
        s2=s2+ar[j][i]
    s1max=max(s1max,s1)
    s2max=max(s2max,s2)
    s1=0
    s2=0
print(s1max+s2max)
    

