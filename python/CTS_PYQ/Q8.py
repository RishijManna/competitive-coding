def check(n,s,s1,p):
	cost=p*n
	if n>=20:
		cost=cost-((cost*10)/100)
	if s1=='y':
		cost=cost-((cost*2)/100)
		
	if s=='y':
		cost=cost+n*50
	return cost

n=int(input("Enter the no of tickect:"))
s=input("Do you want refreshment:")
s1=input('Do you have coupon code:')
c=input('Enter the circle:')
cost=0
if n<5 or n>40:
	print("Minimum of 5 and Maximum of 40 Tickets") 
elif c=='q' or c=='k':
	if c=='k':
		print(check(n,s,s1,75))
	elif c=='q':
		print(check(n,s,s1,150))
		
else:
	print("Invalid Input")
