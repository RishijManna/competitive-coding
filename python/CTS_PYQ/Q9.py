'''Problem Statement – To speed up his composition of generating unpredictable rhythms, Blue Bandit wants the list of prime numbers available in a range of numbers.Can you help him out?

Write a java program to print all prime numbers in the interval [a,b] (a and b, both inclusive).

Note

Input 1 should be lesser than Input 2. Both the inputs should be positive. 
Range must always be greater than zero.
If any of the condition mentioned above fails, then display “Provide valid input”
Use a minimum of one for loop and one while loop
Sample Input 1:

2

15

Sample Output 1:

2 3 5 7 11 13

Sample Input 2:

8

5

Sample Output 2:

Provide valid input'''

def check(n):
	if n<2:
		return 0
	for i in range(2,int(n**0.5)+1):
		if n%i==0:
			return 0
	return 1
n=int(input())
n1= int(input())
if n1>n and n>=0 and n1>=0:
	while(n<=n1):
		if check(n):
			print(n,'',end='')
		n+=1
		
else:
	print("Provide valid input")
