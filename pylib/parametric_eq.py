class parametric_eq:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def print_eq(self,eq):
        flag = True
        s = ""
        for i in range(len(eq)-1,-1,-1):
            if eq[i]==0:
                continue
            if i==0:
                s += str(eq[i])
            else :
                if eq[i]==1:
                    s += "t^"+str(i)
                elif eq[i]==-1:
                    s += "-t^"+str(i)
                else:
                    s += str(eq[i])+"*t^"+str(i)

            if i >= 1 and eq[i-1] <0:
                s += ""
            else:
                s += "+"
        print s[0:-1]

    def print_x(self):
        print "x = ",
        if len(self.x)==0:
            print "all x"
        else:
            self.print_eq(self.x)

    def print_y(self):
        print "y = ",
        if len(self.y)==0:
            print "all y"
        else:
            self.print_eq(self.y)

    def print_(self):
        print " == equation =="
        self.print_x()
        self.print_y()

    def cal_eq(self,eq,t):
        if len(eq) == 0:
            return "*"

        ans = 0
        for i in range(len(eq)):
            ans += eq[i]*(t**i)
        return ans

    def example(self):
        ex = set()
        for t in range(10):
            x = self.cal_eq(self.x,t)
            y = self.cal_eq(self.y,t)
            ex.add( (x,y) )

        sort = sorted(ex)
        for p in sort:
            print p , " ",

