import random

board = {"GO":0	,"A1":1	,"CC1":2	 ,"A2":3	 ,"T1":4,
			"R1":5	,"B1":6	,"CH1":7	 ,"B2":8	 ,"B3":9,
			"JAIL":10,"C1":11	,"U1":12	 ,"C2":13 ,"C3":14,
			"R2":15	,"D1":16	,"CC2":17 ,"D2":18 ,"D3":19,
			"FP":20	,"E1":21	,"CH2":22 ,"E2":23 ,"E3":24,
			"R3":25	,"F1":26	,"F2":27	 ,"U2":28 ,"F3":29,
			"G2J":30	,"G1":31 ,"G2":32  ,"CC3":33,"G4":34,
			"R4":35	,"CH3":36,"H1":37	 ,"T2":38 ,"H2":39,
			0:"GO"	,1:"A1"	,2:"CC1"	 ,3:"A2"	 ,4:"T1",
			5:"R1"	,6:"B1"	,7:"CH1"	 ,8:"B2"	 ,9:"B3",
			10:"JAIL",11:"C1"	,12:"U1"	 ,13:"C2" ,14:"C3",
			15:"R2"	,16:"D1"	,17:"CC2" ,18:"D2" ,19:"D3",
			20:"FP"	,21:"E1"	,22:"CH2" ,23:"E2" ,24:"E3",
			25:"R3"	,26:"F1"	,27:"F2"	 ,28:"U2" ,29:"F3",
			30:"G2J"	,31:"G1" ,32:"G2"  ,33:"CC3",34:"G4",
			35:"R4"	,36:"CH3",37:"H1"	 ,38:"T2" ,39:"H2"}


class activity:
	deck,pos = None,None
	def __init__(self,what):
		if what=="chance":
			self.deck = ["GO","JAIL","C1","E3","H2","R1","nextR","nextR","nextU","back3",0,0,0,0,0,0]
		elif what=="chest":
			self.deck = ["GO","JAIL",0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		self.pos=0

	def get(self,pos):
		nextPos=0
		if self.deck[self.pos]==0:
			nextPos = pos
		elif self.deck[self.pos]=="nextR":
			if pos == board["CH1"]:
				nextPos = board["R2"]
			elif pos == board["CH2"]:
				nextPos = board["R3"]
			elif pos == board["CH3"]:
				nextPos = board["R1"]
		elif self.deck[self.pos]=="nextU":
			if pos == board["CH2"]:
				nextPos = board["U2"]
			else:
				nextPos = board["U1"]
		elif self.deck[self.pos]=="back3":
			nextPos = pos-3
		else:
			nextPos = board[self.deck[self.pos]]
		self.pos +=1
		if self.pos >=16 :
			self.pos=0
		return nextPos


class Dice:
	d1,d2,double=None,None,None
	nSide=None
	def __init__(self,nSide):
		self.double=0
		self.nSide=nSide

	def roll(self,pos):
		self.d1 = random.randint(1,self.nSide)
		self.d2 = random.randint(1,self.nSide)
#		print self.d1,self.d2
		if self.d1==self.d2:
			self.double+=1
		else:
			self.double=0

		if self.double>2:
			self.double=0
			return board["JAIL"]
		return (pos+self.d1+self.d2)%40		

chance = activity("chance")
chest = activity("chest")

prob = [0 for i in range(40)]
pos=0
dice = Dice(4)
for i in range(1000000):
	passs = pos
	pos = dice.roll(pos)
	#print board[passs]," to ",board[pos]
	if pos == board["CH1"] or pos == board["CH2"] or pos==board["CH3"]:
		pos = chance.get(pos)
	if pos == board["CC1"] or pos == board["CC2"] or pos==board["CC3"]:
		pos = chest.get(pos)
	if pos == board["G2J"]:
		pos = board["JAIL"]
	#print board[pos]
	prob[pos]+=1
	#raw_input()
print prob
for i in range(3):
	maxx = 0
	where = -1
	for j in range(len(prob)):
		if prob[j] > maxx:
			maxx = prob[j]
			where = j
	print board[where],prob[where],where
	prob[where]=0
