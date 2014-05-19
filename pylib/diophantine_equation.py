from gcd import gcd
from extended_euclidean import extended_euclidean
from parametric_eq import parametric_eq

# Ax2 + Bxy + Cy2 + Dx + Ey + F = 0

class diophantine_Eq:
    def __init__(self,cof):
        while len(cof) < 6:
            cof.append(0)

        self.cof = cof
        self.A = cof[0]
        self.B = cof[1]
        self.C = cof[2]
        self.D = cof[3]
        self.E = cof[4]
        self.F = cof[5]
        


    def print_eq(self):
        factor = ["x*x","xy","y*y","x","y",""]
        for c in range(self.nFac):
            if c!=0:
                print str(c)+" ",

    def solve(self):
        A = self.A
        B = self.B
        C = self.C
        D = self.D
        E = self.E
        F = self.F

        if A==B and B==C and C==0:
            return self.linear()
        else:
            return []

    def linear(self):
        E = self.E
        D = self.D
        F = self.F
        #case F = 0
        if D==0 and E==0:
            if F==0:
                return [parametric_eq([],[])]
            else:
                return []

        #case Ey + F =0
        elif D==0 and E!=0:
            y = -F/E
            if F%E == 0 :
                return [parametric_eq([],[y])]
            else:
                return []

        #case Dx + F =0
        elif D!=0 and E==0:
            x = -F/D
            if F%D == 0 :
                return [parametric_eq([x],[])]
            else:
                return []

        #case Dx + Ey + F =0
        else:
            g = gcd(D,E)
            if F%g !=0:
                return []
            else:
                f = F/g
                d = D/g
                e = E/g
                (u,v) = extended_euclidean(d,e)
                if d < e:
                    tmp = u
                    u = v
                    v = tmp

                return [parametric_eq([(-1)*f*u,e],[(-1)*f*v,(-1)*d])]

dio = diophantine_Eq([0,0,0,1,3,5])
eq = dio.solve()
for e in eq:
    e.print_()
    e.example()


