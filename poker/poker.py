hightcard=1
onepair=2
twopair=3
threekind=4
straight=5
flush=6
fullhouse=7
fourkind=8
straightflush=9
royal=10

def getStrRank(rank):
	if rank == hightcard:
		return "hightcard"
	elif rank == onepair:
		return "onepair"
	elif rank == twopair:
		return "twopair"
	elif rank == threekind:
		return "threekind"
	elif rank == straight:
		return "straight"
	elif rank == flush:
		return "flush"
	elif rank == fullhouse:
		return "fullhouse"
	elif rank == fourkind:
		return "fourkind"
	elif rank == straightflush:
		return "straightflush"
	elif rank == royal:
		return "royal"
