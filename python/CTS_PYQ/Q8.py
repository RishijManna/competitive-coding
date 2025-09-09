n=int(input("Enter the no of tickect:"))
s=input("Do you want refreshment:")
s1=input('Do you have coupon code:')
c=input('Enter the circle:')
cost=0
if n<5 or n>40:
	print("Minimum of 5 and Maximum of 40 Tickets") 
elif c=='q' or c=='k':
	if c=='k':
		cost=75*n
		if n>=20:
			cost=cost-((cost*10)/100)
		if s1=='y':
			cost=cost-((cost*2)/100)
		
		if s=='y':
			cost=cost+n*50
	elif c=='q':
		cost=150*n
		if s1=='y':
			cost=cost-((cost*2)/100)
		if n>=20:
			cost=cost-((cost*10)/100)
		if s=='y':
			cost=cost+n*50
	print(cost)
else:
	print("Invalid Input")

	
