#!/usr/bin/python3.6
p2Blockers=[5,3,2,1,1,1]
p2Units=[3,3,3]

def smartDefending(attackValue,blockers,units):
	if not attackValue>=blockers[0]:
		return blockers,units

	if attackValue<sum(blockers):
		blockPower=blockers[0]
		numOfBlockers=len(blockers)
		if numOfBlockers==2:
			if attackValue>=blockers[1]:
				attackValue-=blockers
				blockers=[blockers[0]]
				return blockers,units

		for a in range(1,numOfBlockers):
			if attackValue>=blockers[-1]:
				attackValue-=blockers[-1]
				blockers=blockers[:-1]

			if not attackValue>=blockers[0]:
				return blockers,units

	else:
		attackValue-=sum(blockers)
		blockers=[]
		print("attackValue",attackValue)
		for a in units:
			if attackValue>=a:
				attackValue-=a
				units=units[1:]

			else:
				return blockers,units



for i in range(0,30):	
	print("i=",i)	
	print(smartDefending(i,p2Blockers,p2Units),"\n")

	