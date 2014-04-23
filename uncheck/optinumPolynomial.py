class polynomial:
	eq = None,None
	def __init__(self,eq):
		self.eq = eq

	def mul(self,eq):
		newEq = [0 for i in range(len(eq)+len(self.eq)+1)]
		for i in range(len(eq)):
			for j in range(len(self.eq)):
				newEq[i+j]+=eq[i]*self.eq[j]
		self.eq = newEq

	def plus(self,eq):
		newEq = [0 for i in range(max(len(eq),len(self.eq)))]
		for i in range(len(newEq)):
			if i < len(eq):
				newEq[i]+=eq[i]
			if i < len(self.eq):
				newEq[i]+=self.eq[i]
		self.eq = newEq

	def polyValue(self,x):
		y=0
		for i in range(len(self.eq)):
			y+= self.eq[i]*(x**i)
		return y

def show(eq):
	s=""
	for i in range(len(eq)):
		if i==0:
			s+=str(eq[i])
		else:
			if eq[i]==1:
				s+=" + "+"x^"+str(i);
			elif eq[i]!=0 and eq[i]>0:
				s+=" + "+str(eq[i])+"x^"+str(i);
			elif eq[i]!=0 and eq[i]<0:
				if eq[i]==-1:
					s+=" - "+"x^"+str(i);
				else:
					s+=" - "+str(eq[i]*-1)+"x^"+str(i);
	return s


p = polynomial([1,-1,1,-1,1,-1,1,-1,1,-1,1])
#seq = [(i+1,p.polyValue(i+1)) for i in range(11)]
#p = polynomial([0,0,0,1])

x = [i+1.0 for i in range(11)]
y = [p.polyValue(i+1) for i in range(11)]


def l(k,j):
	res = polynomial([1])
	for m in range(k+1):
		if m!=j:
			d = (x[j]-x[m])
			res.mul([(-1.0)*x[m]/d,1/d])
	return res.eq

ans=0
for k in range(len(p.eq)-1):
	OP = polynomial([0])
	for j in range(k+1):
		yj = polynomial([y[j]])
		yj.mul(l(k,j))
#		print yj.eq,j
		OP.plus(yj.eq)
	print "===== "
	ans += OP.polyValue(k+2)
	print OP.polyValue(k+2)
print "ans : ",ans
