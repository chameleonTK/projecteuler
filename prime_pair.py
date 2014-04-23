from pylib.prime import genprime
from pylib.linear_congruence import linear_congruence

def count_digit(n):
    return len(str(n))

limit = 1000000
primes = genprime(limit+limit//2)
S = 0
for i in range(2,len(primes)-1):
    if primes[i] >= limit:
        break
    a = 10**count_digit(primes[i])
    b = primes[i+1]-primes[i]
    n = primes[i+1]
    x = linear_congruence(a,b,n)
    S += x[0]*a+primes[i]
    if (x[0]*a+primes[i]) % primes[i+1] !=0:
        raise Exception("false result")
        raw_input()
print "ans: ",S
