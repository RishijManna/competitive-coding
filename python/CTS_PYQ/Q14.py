n = int(input("Enter no of course"))
if n<=0 or n>20:
    print("Invalid Range")
else:  
	c=[]
	print("Enter the course names")
	for i in range(n):
		c.append(input())
	s=input("Enter the course to be searched")
	if s in c:
		print(s,"course is available ")
	else:
		print(s,"course is not available")
