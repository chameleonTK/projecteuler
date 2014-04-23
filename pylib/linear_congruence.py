from extended_euclidean import extended_euclidean
from gcd import gcd

def linear_congruence(a,b,n):
    d = gcd(a,n)
    if b%d !=0:
        return []

    if a < n:
        s,r = extended_euclidean(a,n)
    else:
        r,s = extended_euclidean(a,n)
    
    x0 = r*b/d
    c = n/d
    while x0 < 0:
        x0 += c

    if x0 >=n:
        while x0 > 0:
            x0 -= c
        x0+=c

    x=[]
    while x0 < n:
        x.append(x0)
        x0 += c

    return x

#print linear_congruence(12,20,28)
