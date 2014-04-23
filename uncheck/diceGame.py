
def genDicePoint(face,n,PP,dictP):
	#print PP
	if len(PP)==n:
		S = sum(PP)
		if dictP.has_key(S):
			dictP[S] += 1
		else:
			dictP[S] = 1
	else:
		for i in range(1,face+1):
			genDicePoint(face,n,PP+[i],dictP)	


pyr = {}
cub = {}
genDicePoint(4,9,[],pyr)
genDicePoint(6,6,[],cub)
w=0
for i in range(1*9,4*9 +1):
	for j in range(1*6,6*6+1):
		if i > j:
			print i,j
			w += pyr[i]*cub[j]

t =(4**9)*(6**6)
print w,t
