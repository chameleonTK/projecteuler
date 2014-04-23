def find(mx,s):
	cc=0
	cc += func(mx,s,0,2,-1)
	cc += func(mx,s,1,1,0)
	return cc

def func(mx,s,tdel,typ,add):
	cc=0
	for i in range(s-tdel,tdel,-2):
		n = i*i-typ**2
		if n >= mx:
			j=typ
			while n > mx and j < i:
				n -= j*4 + 4
				j+=2
			cc += (i-j)//2
			if (i-j)//2 !=0:
				print i,j
		else:
			cc += i//2  + add
			print i,i//2 + add
	return cc
		

def findS(mx,s):
	cc=0
	lst = []
	for i in range(s,0,-2):
		for j in range(i-2,0,-2):
			if i*i - j*j <= mx:
				#print i,j,i*i-j*j
				lst.append( [i,j,i*i-j*j])
				
				cc+=1
	for i in range(s-1,0,-2):
		for j in range(i-2,0,-2):
			if i*i - j*j <= mx:
				#print i,j,i*i-j*j
				lst.append( [i,j,i*i-j*j])
				cc+=1
	lst.sort()
	for i in lst:
		print i
	return cc

#print find(1000000,50000)
print find(100,100)
print "--------------------------------------"
print findS(100,100)
