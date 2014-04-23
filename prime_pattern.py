	
import random

def is_prime(n):

    if n <2:
    	return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False
    
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)
 
    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite

    for i in range(10):
        a = random.randrange(2, n)
        if try_composite(a):
            return False
 
    return True # no base tested showed n as composite


def gen_ignor(prime,add):
	ignor_case = {}

	for i in range(len(prime)):
		ignor_case[prime[i]] = {}
		
	for i in range(len(prime)):
		for n in range(prime[i]):
			flag = False
			for off in add:
				if (n*n + off) % prime[i] ==0:
					flag = True
					break
			ignor_case[prime[i]][n] = flag

	return ignor_case

add = [1,3,7,9,13,27]
basic_prime = [2,3,5,7,11,13,17,19,23,29]
ignor_case = gen_ignor(basic_prime,add)

limit = 150000000
sum_ = 0
for n in xrange(limit):
	#basic check
	if n% 1000000==0:
		print n

	basic_pass = True
	for p in basic_prime:
		if ignor_case[p][n%p]:
			basic_pass = False
			break

	if not basic_pass:
		continue

	normal_pass = True
	for off in add:
		if not is_prime(n*n+off):
			normal_pass = False
			break

	if normal_pass:
		sum_ += n

print "ans ",sum_



