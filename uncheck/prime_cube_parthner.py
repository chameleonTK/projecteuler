import math

#n**3 + (n**2)*p = k**3
#n**3( (n+p)/n ) = k**3
#n( sqrt3 ( (n+p)/n) = k**3

#because k in Z
#sqrt3(n+p) in Z and sqrt3(n) in Z
#for n+p = x**3 and n=y**3
#p = x**3-y**3 = (x-y)(x**2+x*y+y**2)
#so p is prime x-y == 1 or x**2+xy+y**2 == 1
#for x,y > 0 soo 
#consider only x-y == 1 so that is p = (i+1)**3 - i**3

#for p <= 1 000 000 ,, i <= 576


def isPrime(n):
    if n < 2:
        return False
    elif n <= 3:
        return True

    limit = int(math.sqrt(n))
    for i in range(2,limit+1):
        if n%i == 0:
            return False
    return True

count =0
for i in range(1,580):
    j = i+1
    if isPrime(j**3 - i**3):
        count+=1
print count
        
