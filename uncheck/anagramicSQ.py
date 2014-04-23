
def initString(data):
	dicS = {}
	for i in data:
		s = "".join(sorted(i))
		if not dicS.has_key(s):
			dicS[s]=[i]
		else:
			dicS[s].append(i)
	
	key = dicS.keys()
	for i in key :
	  	if len(dicS[i])==1:
			del dicS[i]
	return dicS

def initNum():
	dicN = {}
	for i in range(10**5):
		s = "".join(sorted(str(i*i)))
		if not dicN.has_key(s):
			dicN[s]=[i*i]
		else:
			dicN[s].append(i*i)
	
	key = dicN.keys()
	for i in key :
	  	if len(dicN[i])==1:
			del dicN[i]

	dic = [{} for i in range(15)]
	for i in dicN:
		dic[len(i)][i] = dicN[i]
	return dic

def change(s1,s2,i):
	x = str(i)
	dic={}
	for i in range(len(x)):
		if not dic.has_key(x[i]):
			dic[x[i]]=s1[i]
		else:
			if s1[i]!=dic[x[i]]:
				return -1
		

	lis = [-1 for i in range(len(s1))]
	for a in range(len(s1)):
		for b in range(len(s2)):
			if s1[a]==s2[b]:
				lis[b]=int(x[a])
				break	
	num=0
	for i in lis:
		num=num*10+i
		if i==-1:
			return -1
#	print s1,s2,x,num," ]]"
	return num

def check(s1,s2):
	l=len(s1)
	MAX=-1
	
	for key in dicN[l]:
		run = dicN[l][key]
		for i in run:
			x = change(s1,s2,i)
			if x in run:
				MAX = max(MAX,x,i)
				print s1,s2,x,i
	return MAX

def compare(x,y):
	return len(y)-len(x)

data = raw_input().replace("\"","").split(',')
data.sort(compare)
#print data,"aa"

dicS = initString(data)
dicN = initNum()

keys = dicS.keys()
keys.sort(compare)

for s in keys:
	run = dicS[s]
	for i in range(len(run)):
		for j in range(i+1,len(run)):
			x = check(run[i],run[j])
			#if x!=-1:
			#	print x
			#print s
#			

