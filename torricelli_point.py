import math

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

def genpair_a2_ab_c2(limit):
	limit_sq = int(math.sqrt(limit))+1
	pairs = []
	for m in xrange(1,limit_sq):
		for n in xrange(1,m):
			if gcd(m,n) != 1:
				continue
			if (m-n)%3 ==0:
				continue
			a = 2*m*n+n*n
			b = m*m-n*n
			k=1
			while k*a+k*b<=limit:
				pairs.append( (k*a,k*b))
				pairs.append( (k*b,k*a))
				k+=1


	return pairs

limit = 120000
pairs = genpair_a2_ab_c2(limit)
data_dict = {}
for x,y in pairs:
	if not data_dict.has_key(x):
		data_dict[x] = []
	data_dict[x].append(y)

ans = {}
for a,b in pairs:
	for c in data_dict[a]:
		if data_dict.has_key(b) and c in data_dict[b]:
			#print b," >> ",data_dict[b]
			if not ans.has_key(a+b+c):
				#print a,b,c
				ans[a+b+c] = True

sum_ = 0
for s in ans.keys():
	if s < limit:
		sum_ += s

print sum_