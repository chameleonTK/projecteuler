lim = 10**4

def isPalin(n):
	s = str(n)
	for i in range(len(s)):
		if s[i]!=s[len(s)-1-i]:
			return False
	return True

ans=0
lis=[]
for i in range(1,lim):
	SUM=i*i
	for j in range(i+1,lim):
		SUM+= j*j
		if SUM >= lim*lim:
			break
		if isPalin(SUM):
			if not SUM in lis:
				print SUM
				ans+=SUM
				lis.append(SUM)
#	if i%100==0:
#		print i

print ans

