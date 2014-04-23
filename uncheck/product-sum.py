from findPrime import seive
import math
lim = 12000
prime = seive(lim*2)
allFac=[]
for i in range(lim*2+1):
	allFac.append([[i]])

def Fac(n):
	global allFac

	if n in prime:
		return allFac[n]
	else:
		if len(allFac[n])!=1:
			return allFac[n]
#	print n,",,,"
	sq = math.sqrt(n)
	i=2
	while i<=sq:
		if n%i==0:
			Fac(n//i)
			subFac = allFac[n//i]
#			print subFac,i,n//i
			for s in subFac:
				allFac[n].append([i]+s)
#				print [i]+s,n,i
		i+=1
	return allFac[n]

mps = [-1 for i in range(lim+1)]
count = 0

for i in range(lim*2):
	FactorSet =	Fac(i)
	for sub in FactorSet:
		if len(sub)==1:
			continue
		else:
			p =1
			s =0
			for f in sub:
				p*=f
				s+=f
			k = p-s+len(sub)
			if k<=lim and mps[k]==-1:
				print k,sub
				mps[k]=i
				count+=1	
	if count>=lim:
		break

#for i in range(lim+1):
#	print i,mps[i]
mps.sort()
ans=0


for i in range(lim+1):
	if mps[i]!=-1:
		if mps[i]!=mps[i-1]:
			ans+=	mps[i]
#for i in range(lim+1):
#	print i,mps[i]
#	raw_input()
print ans
print "END"
