import math


def gcd()

def genpair_a2_ab_c2(limit):
	limit_sq = int(math.sqrt(limit))+1
	pairs = []
	for m in xrange(limit_sq):
		for n in xrange(m):
			if gcd(m,n) != 1:
				continue
			if (m-n)%3 ==0:
				continue
			a = 2*m*n+n*n
			b = m*m-n*n
			pairs.append( (a,b))
	return pairs

limit = 120000
