
lim = 10000
#lim=100
n = [i for i in range(1,lim+1)]

queue=[1,2]
ans=0
#while len(n)>0:
#	x = queue.pop(0)
#	for i in range(3):
#		queue.append(x*10+i)
#	lis=[]
#	for i in n:
#		if x%i==0:
#			lis.append(i)
#	for i in lis:
#		print i,x,len(n)
#		ans+= x/i
#		n.remove(i)
#		if len(n)<15:
#			print n
#print ans	

#999, 1998, 2997, 3996, 4995, 5994, 6993, 7992, 8991, 8999, 9899, 9989, 9990, 999

def check(n):
	while n>0:
		if n%10 >2:
			return False
		n= n//10
	return True

def func(n):
	q = []
#	for i in range(10):
#		if (i*n)%10<=2:
#			q.append((i,1))
	s = str(n)
	L = 10**len(s)
#	print L
	for i in range(L):
		t = (i*n)%L
	#	print i*n,t,check(t)
		if check(t):
			q.append((i,len(s)))


	ans=-1
	cc=-1
	#print q
	while True:
		if len(q)==0:
			return ans

		tmp = q.pop(0)
		x = tmp[0]
		count=tmp[1]
		#if x==39278:
		#	raw_input()
		if cc!=-1:
			if cc!=count:
				return ans

#		print x,x*n,n,check(x*n),cc

		if x!=0 and check(x*n):
			if ans==-1:
				ans = x
				cc=count
			else:
				if ans>x:
					ans=x
					cc=count

		else:
			carry = ((x*n)//(10**count))%10
			for i in range(10):	
				if x==0 and i==0:
					continue
				if (i*n+carry)%10<=2:
					t = (i*(10**count) + x)
					if i==0 and x==0:
						continue
					q.append((t,count+1))
#					print t,x,i,t*n
		#if x%100000==39278:
		#	raw_input()
#		raw_input()
SS=3
for i in range(3,10001):
	print i,"----->"
	t = func(i)
	print t*i,t
	SS+=t
#	raw_input()

