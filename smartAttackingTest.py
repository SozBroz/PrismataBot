#!/usr/bin/python3.6
def smartDefending(attackValue,blockers,units):
	#print("attackValue:",attackValue)
	#print("blockers:",blockers)
	if attackValue<sum(blockers):
		if not attackValue>=blockers[0]:
			return blockers,units

		blockPower=blockers[0]
		numOfBlockers=len(blockers)
		if numOfBlockers==2:
			if attackValue>=blockers[1]:
				attackValue-=blockers[1]
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
		#print("attackValue",attackValue)
		if attackValue>=sum(units):
			return [],[]

		for a in units:
			if attackValue>=a:
				attackValue-=a
				units=units[1:]

	return blockers,units


def smartClicking(initAttackValue,clickAbleOtherUnits,blockers,units,previousValue):
	#only works if all attack values are the same
	unitsNames=[]
	count=[]
	attackValueOfUnit=[]
	tempBlockers=blockers
	tempUnits=units
	initLengthOfBlockersPlusUnits=len(blockers+units)
	possibleAttackValue=0
	fullAttacklen=0
	tracker=0
	possibleCombinationsOfAttacks=[]
	for unit in unitsList:
		if cooldown
		if str(unit) in unitsNames:
			count[unitsNames.index(str(unit))]+=1
		else:
			unitsNames.append(str(unit))
			count.append(1)
			attackValueOfUnit.append(unit.onClickDict["attack"])
			
		possibleAttackValue+=unit.onClickDict["attack"]
	tempBlockers,tempUnits=smartDefending(possibleAttackValue+initAttackValue,blockers,units)
	fullAttacklen=len(tempBlockers,tempUnits)
	
	for unitPosition in range(0,len(count)):
		attackValue=0
		for i in range(0,count[unitPosition])
			tempBlockers,tempUnits=smartDefending(initAttackValue+attackValue)
			if len(tempBlockers+tempUnits)==fullAttacklen:
				return tracker
			attackValue+=attackValueOfUnit[i]
			tracker+=1



