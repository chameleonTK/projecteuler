

fo = open("network.txt",'r')
edges = []
list_edges = []
i=0
cost = 0
for line in fo:
	lst = line.strip().split(",")
	j=0
	for l in lst:
		if l != "-":
			list_edges.append( (i,j,int(l),) )
			cost += int(l)
		j+=1
	edges.append(lst)
	i+=1


N = len(edges)

def comparator(x,y):
	return x[2]-y[2]

list_edges.sort(comparator)
node_set = [[i] for i in range(N)]
flag = [i for i in range(N)]

sum_weight = 0
for e in list_edges:
	node_i = e[0]
	node_j = e[1]
	weight = e[2]
	if flag[node_i] != flag[node_j]:
		#print flag
		A = node_set[flag[node_i]]
		B = node_set[flag[node_j]]
		if len(B) > len(A):
			tmp = B
			B = A
			A = tmp


		len_b = len(B)
		for b in range(len_b):
			n = B.pop()
			flag[n]=flag[A[0]]
			A.append(n)
		#print node_i," >> ",node_j,"  : ",weight
		#print A,"    ",B
		#print flag
		#print " ====== "
		sum_weight += weight

print sum_weight
print cost/2
print "ans :",cost/2-sum_weight
