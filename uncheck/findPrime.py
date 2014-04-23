def seive(n):
	isPrime = [True for i in range(n)]
	isPrime[0]=False
	isPrime[1]=False
	prime = []
	for i in range(2,n):
		if isPrime[i]:
			tmp = i+i
			prime.append(i)
			while tmp<n:
				isPrime[tmp]=False
				tmp+=i
	return prime
			
