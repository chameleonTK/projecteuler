from fractions import gcd
MAX = 120000
#MAX = 1000

RAD = [[1,i] for i in range((MAX+1))]
def init():
	for i in range(2,len(RAD)):
		if RAD[i][0]==1:	
			tmp = i
			while tmp < len(RAD):
				RAD[tmp][0]*=i
				tmp+=i

def rad(a,b,c):
	return RAD[a][0]*RAD[b][0]*RAD[c][0]

def compare(x,y):
	return x[0]-y[0]

init()
RAD2 = [RAD[i][0] for i in range((MAX+1))]
RAD.sort(compare)


count=0
ans=0
#for a in range(1,MAX):
#	if a%2==0:
#		rm=2
#	else:
#		rm=1
#	for b in range(a+1,MAX,rm):
#		c = a+b
#		if c>MAX:
#			continue
#		if gcd(a,b)==1:
#			if rad(a,b,c) < c:
#				count+=1
#				ans+=c
#
#	if a%100==0:
#		print a


for c in range(MAX):
	radC = RAD2[c]
	for Xa in RAD:
		a = Xa[1]
		radA = Xa[0]

		if radA*radC > c//2:
			break
		if a > c//2:
			continue
	
		b = c-a

		radB = RAD2[b]
		if radA*radB*radC < c and gcd(a,b)==1:
			count+=1
			ans+=c
	if c%1000==0:
		print c		
print count,ans
			
