from itertools import islice
 
def primegen(n):
	flag = [True for i in range(n+1)]
	prime = []
	i = 2
	while i < n:
		if flag[i]:
			j = i*2
			prime.append(i)
			while j < n:
				flag[j]=False
				j+=i
		i+=1
	return prime
		

def hamming2():
    h = 1
    _h=[h]    # memoized
    multipliers  = primegen(100)
    multindeces  = [0 for i in multipliers] # index into _h for multipliers
    multvalues   = [x * _h[i] for x,i in zip(multipliers, multindeces)]
    yield h
    while True:
        h = min(multvalues)
        _h.append(h)
        for (n,(v,x,i)) in enumerate(zip(multvalues, multipliers, multindeces)):
            if v == h:
                i += 1
                multindeces[n] = i
                multvalues[n]  = x * _h[i]
        # cap the memoization
        mini = min(multindeces)
        if mini >= 1000:
            del _h[:mini]
            multindeces = [i - mini for i in multindeces]
        #
        yield h




limit = 10**9
#ret = list(islice(hamming2(), 5000000))
#cc = 1
#for n in ret:
#	if n > limit:
#		print "answer : ",cc
#		break
#	cc +=1
#print "last",ret[-1]

i=0
while i < limit:
	#print i
	i+=1

print "end"
