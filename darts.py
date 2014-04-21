multiply = ["S","D","T"]
score = [i for i in range(1,21)] + [25]

darts = []
for s in score:
	for m in multiply:
		if m=="T" and s==25:
			continue
		darts.append( (m,s))

def getScore(d):
	if d[0]=="S":
		return d[1]
	elif d[0]=="D":
		return d[1]*2
	elif d[0]=="T":
		return d[1]*3
	else:
		return 0

cc =0
limit = 100
for d in darts:
	if d[0]=="D" and getScore(d) < 100:
		cc+=1

for d in darts:
	for dd in darts:
		if dd[0]=="D" and getScore(d)+getScore(dd) < 100:
			cc+=1

for i in range(len(darts)):
	d = darts[i]
	for ii in range(i,len(darts)):
		dd = darts[ii]
		for ddd in darts:
			if ddd[0]=="D" and getScore(d)+getScore(dd)+getScore(ddd) < 100:
				cc+=1

print cc

