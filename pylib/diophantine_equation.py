from gcd import gcd
from extended_euclidean import extended_euclidean
from parametric_eq import parametric_eq
from quadratic_eq import quadratic_eq
from prime import factoring
import math

class diophantine_Eq:
    def __init__(self,cof):
        while len(cof) < 6:
            cof.append(0)

        self.cof = cof
        self.A = int(cof[0])
        self.B = int(cof[1])
        self.C = int(cof[2])
        self.D = int(cof[3])
        self.E = int(cof[4])
        self.F = int(cof[5])
        


    def print_eq(self):
        factor = ["x*x","xy","y*y","x","y",""]
        for c in range(self.nFac):
            if c!=0:
                print str(c)+" ",

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

    def simple_hyperbolic(self):
        #case Bxy + Dx + Ey + F = 0
        '''
         Bxy + Dx + Ey + F   =   0
         Bxy + Dx + Ey   =   -F
         B2xy + BDx + BEy    =   -BF
         B2xy + BDx + BEy + DE   =   DE - BF
         (Bx + E) (By + D)   =   DE - BF
        '''

        B = self.B
        D = self.D
        E = self.E
        F = self.F
        if D*E - B*F ==0:
            eq = []
            if E%B ==0:
                x = (-1*E)/B
                eq.append( parametric_eq([x],[]) )

            if D%B ==0:
                y = (-1*D)/B
                eq.append( parametric_eq([],[y]) )

            return eq
        else:
            fac = factoring(D*E-B*F,True)
            eq = []
            for d in fac:
                x = ((d-E)*1.0)/B
                y = (((D*E-B*F)/d - D)*1.0) / B
                if int(x) == x and int(y)==y:
                    eq.append( parametric_eq([int(x)],[int(y)]) )
            return eq

    def elliptical(self):
        # case Ax**2 + Bxy + Cy**2 + Dx + Ey + F = 0 ,, B**2 - 4AC < 0 ;
        '''
         Ax**2 + Bxy + Cy**2 + Dx + Ey + F = 0 
         Cy**2 + (Bx + E)y + (Ax**2 + Dx + F) = 0
         solve y's >> quadratic eq
        '''
        A = self.A
        B = self.B
        C = self.C
        D = self.D
        E = self.E
        F = self.F

        a = (B*B - 4*A*C)
        b = 2*(B*E - 2*C*D)
        c = (E*E - 4*C*F) 
        quad_sol = quadratic_eq(a,b,c).solve()
        if len(quad_sol)!=2:
            raise Exception("what happen with ellipticall case")

        lower = 0
        upper = 0
        if quad_sol[0] < quad_sol[1]:
            lower = int(quad_sol[0])
            upper = int(quad_sol[1])
        else:
            lower = int(quad_sol[1])
            upper = int(quad_sol[0])

        eq = []
        for x in range(lower,upper+1):
            a = C
            b = B*x+E
            c = A*x*x + D*x + F
            lst_y = quadratic_eq(a,b,c).solve()
            for y in lst_y:
                if int(y)==y:
                    eq.append( parametric_eq([int(x)],[int(y)]) )
        return eq

    def parabolic(self):
        A = self.A
        B = self.B
        C = self.C
        D = self.D
        E = self.E
        F = self.F

        g = gcd(A,C)
        a = A/g
        b = B/g
        c = C/g

        if a < 0:
            a = a*(-1)
        if b < 0:
            b = b*(-1)
        if c < 0:
            c = c*(-1)

        sqrt_a = int(math.sqrt(a))
        sqrt_c = int(math.sqrt(c))
        if B/A < 0:
            sqrt_c *= -1


        if sqrt_c*D - sqrt_a*E == 0:
            qa = sqrt_a*g
            qb = D
            qc = sqrt_a*F
            U = quadratic_eq(qa,qb,qc).solve()
            eq = []
            for u in U:
                tmp = diophantine_Eq([0,0,0,sqrt_a,sqrt_c,u*(-1)]).solve()
                eq.extend(tmp)
            return eq
        else:
            cond = sqrt_c*D - sqrt_a*E
            eq = []
            for u in range(int( math.fabs(cond))):
                if (sqrt_a*g*u*u + D*u + sqrt_a*F )%cond ==0:
                    eq.append( parametric_eq(   [ ((sqrt_c*g*u*u + E*u+sqrt_c*F)*(-1))/cond , (-1)*(E+2*sqrt_c*g*u) , sqrt_c*g*(-1)*cond], 
                                                [ (sqrt_a*g*u*u + D*u+sqrt_a*F)/cond ,        (D+2*sqrt_a*g*u) ,      sqrt_a*g*cond  ] ))
            return eq

    def homogeneous(self):
        A = self.A
        B = self.B
        C = self.C
        D = self.D
        E = self.E
        F = self.F
        eq = []
        k = math.sqrt(B*B - 4*A*C)
        if F ==0:
            eq.append(parametric_eq([0],[0]))
            if k == int(k):
                eq.extend(diophantine_Eq([0,0,0,2*A,B+int(k),0]).solve())
                eq.extend(diophantine_Eq([0,0,0,2*A,B-int(k),0]).solve())
            else:
                return eq
        else:
            if cond == int(cond):

                fac = factoring(-4*A*F,True)
                eq = []
                for u in fac:
                    y = (u + (4*A*F)*(1.0)/u) / (2*k)
                    x = (u - (B+k)*y*(1.0)) / (2*A)
                    if int(x) == x and int(y)==y:
                        eq.append( parametric_eq([int(x)],[int(y)]) )
                return eq
            else:
                g = gcd(gcd(A,B),C)
                if F%g !=0:
                    return []
                A = A/g
                B = B/g
                C = C/g
                D = D/g
                E = D/g
                F = F/g

                if 4*F*F < B*B - 4*A*C:
                    # convergents of the continued fraction of the roots of the equation At2 + Bt + C = 0
                    print "next"
                else:
                    


        return eq


    def hyperbolic(self):
        A = self.A
        B = self.B
        C = self.C
        D = self.D
        E = self.E
        F = self.F
        return []


    def solve(self):
        A = self.A
        B = self.B
        C = self.C
        D = self.D
        E = self.E
        F = self.F
        # Ax2 + Bxy + Cy2 + Dx + Ey + F = 0
        if A==B and B==C and C==0:
            return self.linear()
        elif A==C and C==0 and B!=0:
            return self.simple_hyperbolic()
        elif B*B - 4*A*C < 0:
            return self.elliptical()
        elif B*B - 4*A*C == 0:
            return self.parabolic()
        elif B*B - 4*A*C > 0 :
            return self.hyperbolic()
        else:
            return []

    def cal_eq(self,p):
        (x,y) = p
        return self.A * x*x + self.B*x*y+self.C*y*y +self.D*x+self.E*y+self.F


dio = diophantine_Eq([8,-24,18,5,4,18])
eq = dio.solve()
for e in eq:
    e.print_eq()
    exp = e.example(True)
    for p in exp:
        if dio.cal_eq(p) !=0:
            print p,dio.cal_eq(p)
            raise Exception("False result")
    print " -------- "
    


