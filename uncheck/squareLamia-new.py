mx = 1000000
#mx = 100
cc=0
dic ={}
	
for n in range((mx+4)//4 , 2,-1):
	nt = (n-2)*4 + 4
	sq = nt
	while sq <= mx:
		#print sq,n-2
		cc +=1
		nt +=8
		#if nt <=4:
		#	break
	
		if dic.has_key(sq):
			dic[sq]+=1
		else:
			dic[sq]=1
		sq += nt

print cc
k = dic.keys()
s=0
for i in k:
	if dic[i]<=10 and dic[i]>0:
		s+=1
print s	
	
