n = 1000000
#n = 100
nx = [0]*(n+1)
for h in range(n//4,0,-1):
  nt = h*4 + 4
  sumx = nt
  while sumx <= n:
   # print sumx,h
    nx[sumx] += 1
    nt = nt + 8
    sumx = sumx + nt

for i in range(11):
	#if nx[i]!=0:
	print i,nx.count(i)
print "Answer to pe173 & pe174 =", sum(nx), sum([nx.count(i) for i in range(1,11)])
