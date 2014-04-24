
from collections import defaultdict
import math

num = [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 24, 25, 27, 28, 30, 32, 35, 36, 40, 42, 45, 48, 49, 50,52, 54, 56, 60, 63, 64, 70, 72, 75, 80]
   
#num = [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, *   18, 20, 21, 24,         28, 30, *   35, 36, 40, 42, 45, *                  56, 60, 63, *   70, 72]

common_lcm = 4480842240000

target = 0.5

print len(num)


limit = int(target*common_lcm)
W = [int(common_lcm//(i*i)) for i in num]
sum_ = defaultdict(int)

#initial
sum_[0] = 1
maxx = sum(W)

for w in W:
	update = defaultdict(int)

	keys = sum_.keys()
	keys.sort()
	print math.sqrt(common_lcm/w),len(keys)
	
	for s in keys:
		if s+w > limit:
			print "upper bound"
			break

		update[s+w] += sum_[s]

	#update sum_
	keys = update.keys()
	for u in keys:
		sum_[u] += update[u]


	for s in keys:
		if s+maxx < limit:
			sum_.pop(s, None)

	maxx -= w

print sum_[limit]
print sum_[2209304160000]
