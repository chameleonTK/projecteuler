#!/usr/bin/env python

from itertools import ifilter

def isPrime(n):
    d = 2
    while d**2 <= n:
        if n % d == 0: return False
        d += 1
    return True

def subsetsGen(setOr):
    for s in subsetsGenAux(list(setOr), set([]), 0):
        yield s

def subsetsGenAux(xs, partial, n):
    if n >= len(xs):
        yield partial
    else:
        for s in subsetsGenAux(xs, partial, n+1): yield s
        partial.add(xs[n])
        for s in subsetsGenAux(xs, partial, n+1): yield s
        partial.remove(xs[n])

def factorsInList(n, ps):
    for p in ps:
        while n % p == 0: n //= p
    return n == 1

def mcm(ns):
    output = 1
    for el in ns: output = mcm2(output, el)
    return output

def mcm2(a, b):
    return (a * b) // gcd2(a, b)

def gcd2(a, b):
    if a > b: return gcd2aux(a, b)
    return gcd2aux(b, a)

def gcd2aux(a, b):
    while b: (a, b) = (b, a%b)
    return a

def polyProd(p1, p2, max=-1):
    '''Returns the product of the polynomials p1 and p2, except
    for those terms with degree greater that max.'''
    p = {}
    for (deg1, coef1) in p1.iteritems():
        for (deg2, coef2) in p2.iteritems():
            newdef = deg1 + deg2
            if max<0 or newdef <= max:
                p[newdef] = p.get(newdef, 0) + coef1*coef2
    return p

def polySet(s, max):
    p = {0:1}
    for el in s: p = polyProd(p, {0:1, el:1}, max)
    return p

def isValid(numer, denom, p):
    '''Returns whether the numerator has at least two more ps than
    the denominator, in the prime factor decompositions.'''
    while numer%p == 0 and denom%p == 0:
        numer //= p
        denom //= p
    return numer % (p**2) == 0


def possibleP(p):
    '''Generates the sets I such that p * I could be part of a solution.

    For example, for p = 7 we get [], [1,4,5], etc. This means that
    (7, 28, 35) could be part of a solution.'''
    for s in subsetsGen(range(1, limit//p + 1)):
        sumNs = sum(val[i] for i in s)
        if isValid(sumNs, mcmTot, p): yield s


## ****************** MAIN ******************

limit = 80
cands = range(2, limit + 1)
denoms = [x**2 for x in cands]
mcmTot = mcm(denoms)

## Global variable, used everywhere. The cases 0 and 1 are manually set.
val = [None, mcmTot] + [mcmTot // d for d in denoms]

## Removing candidates that don't appear in any combination:
sRemove = set([])
for p in ifilter(isPrime, xrange(5, limit + 1)):
    sFound = set(range(p, limit + 1, p))
    for s in possibleP(p):
        sFound.difference_update(p*el for el in s)
    sRemove.update(sFound)
for el in sRemove: cands.remove(el)

print "Candidates: %s" % cands
## Now, we divide the candidates in approx. 2 halves:
denoms1 = [x**2 for x in cands[:len(cands)//2]]
denoms2 = [x**2 for x in cands[len(cands)//2:]]
mcm_1 = mcm(denoms1)
mcm_2 = mcm(denoms2)
mcmTot = mcm([mcm_1, mcm_2])
mcmTot2 = mcmTot // 2
s1 = [mcmTot // d for d in denoms1]
s2 = [mcmTot // d for d in denoms2]
p1 = polySet(s1, mcmTot2)
p2 = polySet(s2, mcmTot2)
print "Sums in part 1: %s" % len(p1)
print "Sums in part 2: %s" % len(p2)

counter = 0
for (g1, coef1) in p1.iteritems():
    counter += coef1 * p2.get(mcmTot2 - g1, 0)
print "Number of solutions: %s" % counter