
def maxContiguousSubsequence(A):
	maxSoFar = 0
	maxEndingHere = 0
	for a in A:
		maxEndingHere = max(maxEndingHere + a,0)
		maxSoFar = max(maxSoFar,maxEndingHere)
	return maxSoFar

def generateTable():
	global N
	S = {}	
	for i in range(N):
		for j in range(N):
			k = i*N + j +1
			if k <= 55:
				S[k] = ((100003 - 200003*k + 300007*(k**3)) % 1000000) - 500000
			else:
				S[k] = ((S[k-24] + S[k-55] + 1000000) % 1000000) - 500000

	if S[10] != -393027 or S[100] != 86613:
		raise Exception("error generate table")

	print "Fine generate"
	return S

def get_S(i,j):
	global S,N
	k = i*N+j+1
	if not S.has_key(k):
		print " Noo ",k
		return -1
	return S[k]

N = 2000
S = generateTable()

#N = 10
#S = {}
#for i in range(1,N*N+1):
#S[i] = i

max_ = 0
for i in range(N):
	s = [ get_S(i,j) for j in range(N) ] 
	max_ = max(maxContiguousSubsequence(s) , max_)

for j in range(N):
	s = [ get_S(i,j) for i in range(N)]
	max_ = max(maxContiguousSubsequence(s) , max_)

print " --------- "
for i in range(N):
	row , col = 0 ,i
	s = [ get_S(row+off,col+off) for off in range(N) if row+off < N and col+off < N]
	max_ = max(maxContiguousSubsequence(s) , max_)
	row , col = i , 0 
	s = [ get_S(row+off,col+off) for off in range(N) if row+off < N and col+off < N]
	max_ = max(maxContiguousSubsequence(s) , max_)

print " --------- "
for i in range(N):
	row , col = i , 0
	s = [ get_S(row-off,col+off) for off in range(N) if row-off >= 0 and col+off < N]
	max_ = max(maxContiguousSubsequence(s) , max_)
	
	row , col = N-1 , i 
	s = [ get_S(row-off,col+off) for off in range(N) if row-off >= 0 and col+off < N]
	max_ = max(maxContiguousSubsequence(s) , max_)


print "ans : ", max_
