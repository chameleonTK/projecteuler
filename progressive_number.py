import math

def isSquare(n):
	sqrt = int(math.sqrt(n))
	return sqrt*sqrt == n
	
limit = 10**12
limit_c = 10**4
ans = set()
for a in xrange(1,limit_c):
	if a%100==0:
		print a
	for b in xrange(1,a):
		c = 1
		n = c*c*a*a*a*b + c*b*b
		while n < limit:
			if isSquare(n):
				ans.add(n)

			c+=1 
			n = c*c*a*a*a*b + c*b*b

print "ans ",sum(ans)



