class hi:
	def chek(n):
		l=[]
		for i in range(n):
			l.append(int(input()))
		mark=[]
		for i in l:
			m=[]
			for j in range(i):
				z=int(input())
				if z<0 or z>100:
					return False
				m.append(z)
			mark.append(m)
		for i in mark:
			print(max(i))
		return True
		
	
n=int(input())
if not hi.chek(n):
	print("invalid")
