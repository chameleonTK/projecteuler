import math

class quadratic_eq:
    def __init__(self,a,b,c):
        self.a = a*1.0
        self.b = b*1.0
        self.c = c*1.0

    def solve(self):
        a = self.a
        b = self.b
        c = self.c

        if a!=0:
            if b*b - 4*a*c < 0:
                return []
            else:
                sq = math.sqrt(b*b - 4*a*c)
                return [ (-1*b + sq)/(2*a) , (-1*b - sq)/(2*a) ]
        else:
            if b!=0:
                return [ -c/b ]
            elif c==0:
                raise Exception("infinity solution")
            else:
                return []

    def print_eq(self):

        a = self.a
        b = self.b
        c = self.c

        if a!=0:
            print str(a)+"x**2 ",

        if b<0 :
            print str(b)+"x ",
        elif b>0:
            print "+"+str(b)+"x ",
        
        if c<0 :
            print str(c),
        elif c>0:
            print "+"+str(c),
        print ""