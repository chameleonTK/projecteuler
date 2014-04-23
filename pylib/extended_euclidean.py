from gcd import gcd

def extended_euclidean(a,b):
    if a < b:
        tmp = a
        a = b
        b = tmp
   
    r = [a,b]
    s = [1,0]
    t = [0,1]
    q = [0,0]
    i=2
    while r[i-1] > 0:
        q.append( r[i-2] // r[i-1] )
        r.append( r[i-2] - q[i]*r[i-1] )
        s.append( s[i-2] - q[i]*s[i-1] )
        t.append( t[i-2] - q[i]*t[i-1] )
		#print i," : ",q[i],r[i],s[i],t[i]
        i += 1
    x = s[i-2]
    y = t[i-2]
    if x*a + b*y != gcd(a,b):
        print "gcd ",gcd(a,b)
        print "ans ",x*a+b*y
        raise Exception("ans not accept")
    return (x,y)

#print "test:: "
#print "(a,b) = (240,46)"
#print "result:: "
#print "(x,y) =",extended_euclidean(240,46)
#print "(x,y) =",extended_euclidean(12,18)

