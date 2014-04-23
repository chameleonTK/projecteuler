from prime import miller_rabin
def isPrime(n):
	return miller_rabin(n)

isFindPrime=False
FindPrime=0
def recur(n,rep,s):
	#print s,digit
	global FindPrime
	global isFindPrime

	if len(s)>digit:
		return False
	if len(s)+rep > digit:
		return False

	if len(s)==digit and rep==0:
		#print s,len(s),"aa"
		x = int(s)
		if isPrime(x):
			isFindPrime=True	
			FindPrime+=x
		#print x
		return True
	else:
		for i in range(10):
			if i!=n:
				recur(n,rep,s+str(i))
			else:
				recur(n,rep-1,s+str(i))
		
def gen(n,rep):
	global FindPrime
	global isFindPrime
	isFindPrime=False
	FindPrime=0
	for i in range(1,10):
		if i!=n:
			recur(n,rep,str(i))
		else:
			recur(n,rep-1,str(i))
	if isFindPrime:
		return FindPrime
	else:
		return -1
ans=0
digit=10
for i in range(10):
	for rep in range(digit,-1,-1):
		s = gen(i,rep)
		if s!=-1:
			ans+=s
			break

print ans
	
	
