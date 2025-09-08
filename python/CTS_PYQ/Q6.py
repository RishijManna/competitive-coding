a=int(input())
b=int(input())
c=int(input())
if a<0 or b<0 or c<0:
	print("Invalid Input")
elif a==b and b==c:
	print("None of the department has got the highest placement")
elif a==b:
		print("Highest placement")
		print('CSE')
		print('ECE')
elif c==b:
		print("Highest placement")
		print('ECE')
		print('MECH')
elif a==c:
	
else:
	if a==max(a,b,c):
		print("Highest placement")
		print('CSE')
	elif b==max(a,b,c):
		print("Highest placement")
		print('ECE')
	else:
		print("Highest placement")
		print('MECH')
		
