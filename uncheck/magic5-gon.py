import itertools

lst = [i for i in range(10,0,-1)]
allType =  [ list(x) for x in itertools.permutations(lst)]

print "START"
ans=[]
for i in allType:
	x = i[0]+i[1]+i[2]
	if x!=i[3]+i[2]+i[4]:
		continue
	if x!=i[5]+i[4]+i[6]:
		continue
	if x!=i[7]+i[6]+i[8]:
		continue
	if x!=i[9]+i[8]+i[1]:
		continue

#	x = i[0]+i[1]+i[2]	
#	if x!=i[3]+i[2]+i[4]:
#		continue
#	if x!=i[5]+i[1]+i[4]:
#		continue
	a=[]
	a.append(i[0]*100+i[1]*10+i[2])
	a.append(i[3]*100+i[2]*10+i[4])
	a.append(i[5]*100+i[4]*10+i[6])
	a.append(i[7]*100+i[6]*10+i[8])
	a.append(i[9]*100+i[8]*10+i[1])
#	print "WOW",a
	ans.append(a)
#	raw_input()
print "END"

def compare(x,y):
	return min(y)-min(x)

ans.sort(compare)
for i in ans:
	print i
	raw_input()
