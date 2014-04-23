

def rule1(inp):
	allset = []
	for i in range(2**len(inp)):
		tmp=i
		j=0
		ss=0
		while tmp!=0:
			if tmp&1 != 0:
				ss += inp[j]
			j +=1		
			tmp = tmp >> 1
		allset.append(ss)
	
#	for i in range(len(allset)):
#		print bin(i),allset[i]
	allset.sort()
	for i in range(len(allset)-1):
		if allset[i]==allset[i+1]:
			#print allset[i]
			return False
	return True

def rule2(inp):
	for i in range(1,len(inp)):
		minS=0
		for j in range(i):
			minS += inp[j]

		maxS=0
		for j in range(i-1):
			maxS += inp[len(inp)-j-1]

		#print minS,maxS,i
		if minS < maxS:
			return False
	return True

S = 0;
for i in range(100):
	inp = [int(i) for i in raw_input().split(',')]
	inp.sort()
	if rule1(inp):
		#print inp
		if rule2(inp):
			S += sum(inp)

print S	
