import itertools

sq = [[(x*x)/10,(x*x)%10] for x in range(1,10)]
for i in sq:
	if i[0]==9:
		i[0]=6
	
	if i[1]==9:
		i[1]=6
print sq

def check(i,j):
	D1 = allDice[i]
	D2 = allDice[j]

	for s in sq:
		#print s[0] in D1,s[0]
		#print s[1] in D2,s[1]
		
		if  ( s[0] in D1) and ( s[1] in D2):
			continue
		else:
		##	print "aaa"
			if ( s[1] in D1) and ( s[0] in D2):
				continue
			else:
				return False

	return True

lst = [i for i in range(10)]
lst[9] = 6
allDice =  [ list(x) for x in itertools.combinations(lst, 6)]


ans = 0
for i in range(len(allDice)):
	for  j in range(i+1,len(allDice)):
		if check(i,j):
		#	print allDice[i]
		#	print allDice[j]
		#	print ".................."
			ans+=1
		#	raw_input()
print ans
