class Cal:
	def __init__(self,n,r):
		self.n=n
		self.r=r
	def fun(self):
		if self.r>=0 and self.r<=3:
			self.n=self.n+(self.n*10)/100
		
		elif self.r>=3.1 and self.r<=4:
			self.n=self.n+(n*25)/100
		elif self.r>=4.1 and self.r<=5:
			self.n=self.n+(self.n*30)/100
		return int(self.n)
n=int(input())
r=float(input())
ob=Cal(n,r)
print(ob.fun())
