'''5.

Write a program to print the Hollow square pattern.

Input Format

Input consists of 1 integer.

Output Format

Refer sample output.

Sample Input

3

Sample output

* * *
*    *
* * *

Case 1

Input (stdin)

3

Output (stdout)

* * *
*   *
* * *

Case 2

Input (stdin)

4

Output (stdout)

* * * *
*     *
*     *
* * * *

'''

n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1:
            print('* ',end='')
        else:
            if j==0 or j==n-1:
                print('* ',end='')
            else:
                print('  ',end='')
            
    print()
    print()
        
            
