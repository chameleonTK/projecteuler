
def nextN(s):
	for i in range(len(s)):
		if s[i]=="1":
			return i
	return -1

def OPT(s):
	print "input ",s
	i=0
	nx = nextN(s[1:])+1
#	raw_input()
#	print nx
	if nx!=0:
		k2 = len(s)-nx-1
		k1 = len(s)-1
		print k1,k2
		N = OPT(s[nx:])
		print N,"---"
		return (k1-k2)*N
	else:
		k1 = len(s)
		return k1

n = int(raw_input())
ans = []
ans.append(0)
x = str(bin(n))[2:]

#print OPT("10011")
print OPT(x)
