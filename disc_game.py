red = 1
blue = 1
turn = 15

rand = {}
rand[(0,0)] = 1
for i in range(turn):
	tmp_rand = {}
	for k in rand.keys():
		new_k = (k[0],k[1]+1)
		if tmp_rand.has_key(new_k):
			tmp_rand[new_k] += rand[k]*red
		else:
			tmp_rand[new_k] = rand[k]*red

		new_k = (k[0]+1,k[1])
		if tmp_rand.has_key(new_k):
			tmp_rand[new_k] += rand[k]*blue
		else:
			tmp_rand[new_k] = rand[k]*blue

	rand = tmp_rand
	print rand
	red +=1

all_ = 0
win_ = 0
for k in rand.keys():
	all_ += rand[k]
	if k[0] > k[1]:
		win_ += rand[k]

print win_,all_
