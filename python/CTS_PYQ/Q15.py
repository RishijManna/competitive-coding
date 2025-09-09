n=int(input())
if n==0:
	print("No Factors")
elif n<0:
	n=n*(-1)
	l=[]
	c=-1
	for i in range(1,int(n**0.5)+1):
		if n%i==0:
			l.append(i)
			c=c+1
	for i in range(c,-1,-1):
		l.append(n//l[i])
	n=len(l)
	for i in range(n):
		if i==n-1:
			print(l[i])
		else:
			print(l[i],end=', ')
