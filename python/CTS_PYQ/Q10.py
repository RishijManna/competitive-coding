n=int(input())
if n>=0 :
	s=str(n)
	if s==s[::-1]:
		print('Palindrome')
	else:
		print('Not a Palindrome')
		
else:
	print("Provide valid input")
	
