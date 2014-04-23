import itertools
from prime import miller_rabin

s = ""
def OPT(st,k):
	if st==len(s):
#		print "..... WOW..."
		return 1
	
	n=0
	count=0
	for i in range(st,len(s)):
		n= n*10+int(s[i])
		if n>k and isPrime(n):
#			print n
			count += OPT(i+1,n)
	return count

dicPrime = {}
def isPrime(n):
	if dicPrime.has_key(n):
		return dicPrime[n]
	else:
		dicPrime[n] = miller_rabin(n)
		return dicPrime[n]

#print OPT(0,-1)

x = list(itertools.permutations(["1","2","3","4","5","6","7","8","9"]))
#permu=[]
ans=0
print "per accept ...."
cc=0
for ele in x:
	s=""
	for e in ele:
		s+=e
	ans += OPT(0,-1)
	cc+=1
	if cc%1000==0:
		print cc
print ans

