#376

import poker

class Card:
	suit,val=None,None
	def __init__(self,val,suit):
		self.suit=suit
		self.val=val

	def printCard(self):
		#if self.suit=='S':
		#	print self.val,unichr(9824)
		#elif  self.suit=='C':
		#	print self.val,unichr(9831)
		#elif  self.suit=='H':
		#	print self.val,unichr(9829)
		#else:
		#	print self.val,unichr(9830)
		print self.val,self.suit

class Player:
	deck,listCard,rank,order=None,None,None,None
	def __init__(self,P,s,t):
		self.deck=[]
		for i in range(s,t):
			if(P[i][0]=="T"):
				(self.deck).append(Card(10,P[i][1]))
			elif(P[i][0]=="J"):
				(self.deck).append(Card(11,P[i][1]))
			elif(P[i][0]=="Q"):
				(self.deck).append(Card(12,P[i][1]))
			elif(P[i][0]=="K"):
				(self.deck).append(Card(13,P[i][1]))
			elif(P[i][0]=="A"):
				(self.deck).append(Card(14,P[i][1]))
			else:
				(self.deck).append(Card(int(P[i][0]),P[i][1]))

		self.sortDeck()
		self.listCard = [0 for i in range(15)]
		for i in self.deck:
			self.listCard[i.val]+=1

		self.getRank()
			


	def isFlush(self):
		for i in range(1,len(self.deck)):
			if self.deck[i-1].suit!=self.deck[i].suit:
				return False
		return True

	def isStraight(self):		
		for i in range(1,len(self.deck)):
			if self.deck[i-1].val+1!=self.deck[i].val:
				return False
		return True

	def printDeck(self):
		print "++++++++++++",poker.getStrRank(self.rank),"++++++++++++++"
		for i in self.deck:
			i.printCard()

	def sortDeck(self):
		def comparator(x, y):
			return x.val-y.val
		self.deck.sort(comparator)	

	def getSuitOrder(suit):
		if suit == 'S':
			return 4
		elif suit == 'H':
			return 3
		elif suit == 'D':
			return 2
		else:
			return 1

	def getRank(self):
		self.order = []
		if self.listCard[10]!=0 and self.isStraight() and self.isFlush() :
			self.rank =  poker.royal
			self.order.append(getSuitOrder(self.deck[0].suit))
		elif self.isStraight() and self.isFlush() :
			self.rank = poker.straightflush
			self.order.append(self.deck[len(self.deck)-1].val)
			self.order.append(getSuitOrder(self.deck[0].suit))
		elif 4 in self.listCard :
			self.rank = poker.fourkind
			self.order.append(self.listCard.index(4))
			self.order.append(self.listCard.index(1))
		elif 3 in self.listCard and 2 in self.listCard :
			self.rank = poker.fullhouse
			self.order.append(self.listCard.index(3))
			self.order.append(self.listCard.index(2))
		elif self.isFlush() :
			self.rank = poker.flush
			self.order = [self.deck[i].val for i in range(len(self.deck)-1,-1,-1)]
		elif self.isStraight() :
			self.rank = poker.straight
			self.order.append(self.deck[len(self.deck)-1].val)
		elif 3 in self.listCard :
			self.rank = poker.threekind
			self.order.append(self.listCard.index(3))
			tmp = [i.val for i in self.deck if self.listCard[i.val]==1]
			tmp.sort(reverse=True)
			self.order.extend(tmp)
		elif self.listCard.count(2) == 2 :
			self.rank = poker.twopair
			tmp = [i.val for i in self.deck if self.listCard[i.val]==2]
			tmp.sort(reverse=True)
			self.order.extend(tmp)
			self.order.append(self.listCard.index(1))
		elif 2 in self.listCard :
			self.rank = poker.onepair
			self.order.append(self.listCard.index(2))
			tmp = [i.val for i in self.deck if self.listCard[i.val]==1]
			tmp.sort(reverse=True)
			self.order.extend(tmp)
		else:
			self.rank = poker.hightcard
			self.order = [self.deck[i].val for i in range(len(self.deck)-1,-1,-1)]
		
win = 0
for loop in range(1000):

	allPlayer = raw_input().split(' ')
	P1 = Player(allPlayer,0,5)
	P2 = Player(allPlayer,5,10)

	if P1.rank > P2.rank:
		win+=1
		isWin=True

	elif P1.rank == P2.rank:
		isEnd=False
		for i in range(len(P1.order)):
			if P1.order[i]>P2.order[i]:
				win+=1
				isWin=True
				isEnd=True
				break
			elif P1.order[i]<P2.order[i]:
				isEnd=True
				break
		if not isEnd:
			print "Error Define"
			P1.printDeck()
			print P1.order,"       ,,,,"
			P2.printDeck()
			print P2.order,"       ,,,,"

#	if not isWin:
#		print ".................."

print win

