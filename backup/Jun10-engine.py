#!/usr/bin/python3.6
import sys #Probably for exits on future try catchs or someshit

from prismataUnits import *
def initializeMapFromFile(fileName):
	p1INIT=[]
	with open(fileName) as f:
		for line in f:
			p1INIT.append(line.split(","))
	return p1INIT

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

def canBuyUnitCheck(resourcesList,unit):
	#print("canBuyUnitCheck:")
	#print("resourcesList:",resourcesList)
	#print("unit:",unit)
	#UNIT=CAPITALIZED UNIT NAME
	##print("unit:",unit)
	for resource in unitCostDict[unit]:
		if resourcesList[resource]<unitCostDict[unit][resource]:
			#print("return: False")
			return(False)
	#print("return: True")
	return(True)

def stateCopy(sourcePlayer):
	pass
	#return

def unitStrToClassFromFile(owner,initUnitOptions): #
	#print("unitStrToClassFromFile")
	#print("owner:",owner)
	#print("initUnitOptions",initUnitOptions)
	for i in range(0,int(initUnitOptions[1])):

		owner.unitStrToClass(initUnitOptions[0])
		if initUnitOptions[0] in unitResList:
			owner.resUnits[-1].cooldown=int(initUnitOptions[2].strip())
		elif initUnitOptions[0] in unitResOnClickList:
			owner.resUnitsClick[-1].cooldown=int(initUnitOptions[2].strip())
		elif initUnitOptions[0] in unitOtherList:
			owner.otherUnits[-1].cooldown=int(initUnitOptions[2].strip())
		elif initUnitOptions[0] in unitOtherOnClickList:
			owner.otherUnitsClick[-1].cooldown=int(initUnitOptions[2].strip())
		else:
			print("unitStrToClassFromFile: Not in any list")
			print("unit:",initUnitOptions[0])
			sys.exit(1)

	#print("return:",owner)
	return(owner)
	
def attacking(p1,p2Blockers,p2Units):
	#print("attacking")
	#print("p1:",p1)
	#print("p2Blockers,p2Units:",p2Blockers,p2Units)
	p2Blockers,p2Units=smartDefending(p1.resDict["attack"],p2Blockers,p2Units)
	#print("return p1,p2")
	#print("p1:",p1)
	#print("p2Blockers,p2Units:",p2Blockers,p2Units)	
	return p1,p2Blockers,p2Units

def moveIncrementer(player):
	#print("moveIncrementer")
	#print("player:",player)
	#print("turnCounter:",turnCounter)
	boughtUnit=True #Tracks if progress was made ###INITIALIZE AS TRUE TO ENTER WHILE LOOP
	try:
		toBeBoughtThisTurn=turnHistory[turnCounter][:-1] #what was bought this turn last time INITIALIZATION
		doneWithUnitsUpTo=masterUnitList[turnCounter].index(turnHistory[turnCounter][-1])#remember which unit was bought last
	except IndexError:
		toBeBoughtThisTurn=[]
		doneWithUnitsUpTo=-1

	for unit in toBeBoughtThisTurn:
		player.buyUnit(unit)

	while boughtUnit:
		boughtUnit=False
		#print(masterUnitList[turnCounter])
		tempUnitList=[]
		for unit in masterUnitList[turnCounter][doneWithUnitsUpTo+1:]:
			#print(turnCounter)
			#print(unitList)
			if unit not in unitList[:turnCounter]:
		 		tempUnitList.append(unit)

		for unit in tempUnitList:
			if canBuyUnitCheck(player.resDict,unit):
				player.buyUnit(unit)
				boughtUnit=True
				toBeBoughtThisTurn.append(unit)
				break

	if turnCounter<turnLimit-2:
		if len(toBeBoughtThisTurn)<len(turnHistory[turnCounter]):
	 		unitList[turnCounter]=masterUnitList[turnCounter][doneWithUnitsUpTo]
		else:
			unitList[turnCounter]=None

	turnHistory[turnCounter]=toBeBoughtThisTurn
	#print("player1:",player)
	#print("turnCounter:",turnCounter)
	#print("turnHistory:",turnHistory)

def genPurchaseBruteForce(player):
	tempResources=player.resDict # To track purchases
	#print("turnCounter:",turnCounter)
	try:
		turnHistory[turnCounter]
			######TURN HAS HISTORY !!!! WORK WITH EXISTING HISTORY TO FIND CHANGE TO MAKE
			######YOU ONLY ENTER HERE AFTER FIRST RUN THROUGH OF GAME
			######MAKE SURE ONLY LAST TURN CHANGES UNTIL YOU EXHAUST EVERYTHING IN FINAL TURN
			######MAKE CHANGE TO PREVIOUS TURN THEN RE-EXHAUST
			######MAKING CHANGES TO LAST MOVE FIRST
			######IF THIS SHIT WORKS HOLY FUCK
		numberOfTurnsInGame=len(turnHistory)
		#print("numberOfTurnsInGame",numberOfTurnsInGame)
		for tempTurn in range(numberOfTurnsInGame-1,turnCounter,-1):
			if turnHistory[tempTurn]!=[]:
				#print("Repeating turnHistory")
				for unit in turnHistory[turnCounter]:
					player.buyUnit(unit)

				#print("leaving genPurchaseBrteForce")
				return #subsequent turn must be iterated

		moveIncrementer(player) #its time

	except IndexError:
		#Initialize turn
		#print("INDEXERROR:APPENDING TO TURNHISTORY")
		#print("turnHistory:",turnHistory)
		#print("turnCounter:",turnCounter)
		#print("lenght of turnHistory:",len(turnHistory))
		turnHistory.append([])

		moveIncrementer(player)

def smartClicking(initAttackValue,clickableOtherUnits,blockers,units):
	#only works if all attack values are the same
	#print("in smartClicking")
	try:
		otherUnitsClicksPerTurn[turnCounter]
	except IndexError:
		otherUnitsClicksPerTurn.append([])

	unitsNames=[]
	count=[]
	attackValueOfUnit=[]
	tempBlockers=blockers
	tempUnits=units
	initLengthOfBlockersPlusUnits=len((blockers+units))
	possibleAttackValue=0
	fullAttacklen=0
	tracker=0
	possibleCombinationsOfAttacks=[]
	fullAttacklen=len((tempBlockers+tempUnits))
	
	for unit in clickableOtherUnits:
	
		if str(unit) in unitsNames:
			count[unitsNames.index(str(unit))]+=1
		else:
			unitsNames.append(str(unit))
			count.append(1)
			attackValueOfUnit.append(unit.onClickDict["attack"])
		
		possibleAttackValue+=unit.onClickDict["attack"]
	tempBlockers,tempUnits=smartDefending(possibleAttackValue+initAttackValue,blockers,units)
	fullAttacklen=len((tempBlockers+tempUnits))
	if fullAttacklen==initLengthOfBlockersPlusUnits:
		return 0
	attackValue=0
	#print("count:",count)
	for unitPosition in range(0,len(count)):
		for i in range(0,count[unitPosition]):
			tempBlockers,tempUnits=smartDefending(attackValue+initAttackValue,blockers,units)
			#print("full attackLen then temp len")
			#print(fullAttacklen)
			#print(len(tempBlockers+tempUnits))
			if len((tempBlockers+tempUnits))==fullAttacklen:
				#print("turnCounter:",turnCounter)
				#print("attackValue:",attackValue)
				otherUnitsClicksPerTurn[turnCounter]=attackValue
				return attackValue
			attackValue+=attackValueOfUnit[unitPosition]
	#print("turnCounter:",turnCounter)
	#print("possibleAttackValue:",possibleAttackValue)
	otherUnitsClicksPerTurn[turnCounter]=possibleAttackValue
	return possibleAttackValue

def isClickable(unit):
	if unit.cooldown>=0:
		return True

	return False
def autoTurn(player1,player2Blockers,player2Units):
	#Stage 1 - Resources
	#Dumb: always clicks on clickable units
	####DUMB CLICK
	for a in player1.resUnitsClick:
		#print("clicking:", a)
		a.onClick()
	clickableOtherUnits=[]
	for a in player1.otherUnitsClick:
		if isClickable(a):
			clickableOtherUnits.append(a)
	#print(len(clickableOtherUnits))
	for a in range(0,smartClicking(player1.resDict["attack"],clickableOtherUnits,player2Blockers,player2Units)):
		clickableOtherUnits[a].onClick()
	#Stage 2 - Attackers #####
	#Dumb attacking: click everything
	#Smart Attacking should be easy to make with dumb list of blockers hp
	player1,player2Blockers,player2Units=attacking(player1,player2Blockers,player2Units)

	#Stage 3 - BruteForce buying
	if turnCounter!=turnLimit-1:
		genPurchaseBruteForce(player1)
	
	return player1,player2Blockers,player2Units

def countNumberOfEachUnit(unitsList):
	unitsNames=[]
	count=[]
	for unit in unitsList:
		if str(unit) in unitsNames:
			count[unitsNames.index(str(unit))]+=1
		else:
			unitsNames.append(str(unit))
			count.append(1)

	return unitsNames, count

class player:
	def __init__(self):
		self.resDict={
		'gold':0,
		'blue':0,
		'red':0,
		'energy':0,
		'attack':0,
		'defence':0 }
		self.resUnits=[]
		self.resUnitsClick=[]
		self.otherUnits=[]
		self.otherUnitsClick=[]

	def turnEnd(self):
		self.resDict['energy']=0
		self.resDict['blue']=0
		self.resDict['red']=0
		self.resDict['attack']=0
		self.resDict['defence']=0
		for a in self.resUnits:
			a.cooldown+=1

		for a in self.resUnitsClick:
			a.cooldown+=1

		for a in self.otherUnits:
			a.cooldown+=1	

		for a in self.otherUnitsClick:
			a.cooldown+=1

	def startTurn(self):
		for a in self.resUnits:
			if a.cooldown>=0:
				a.startTurn()

		for a in self.resUnitsClick:
			if a.cooldown>=0:
				a.startTurn()

		for a in self.otherUnits:
			if a.cooldown>=0:
				a.startTurn()

		for a in self.otherUnitsClick:
			if a.cooldown>=0:
				a.startTurn()

	def unitStrToClass(self,unit):
		if unit == "Drone":
			self.resUnitsClick.append(Drone(self))

		elif unit == "Engineer":
			self.resUnits.append(Engineer(self))
				
		elif unit == "Animus":
			self.resUnits.append(Animus(self))

		elif unit == "Tarsier":
			self.otherUnits.append(Tarsier(self))

		elif unit == "Perforator":
			self.otherUnitsClick.append(Perforator(self))

		elif unit == "Shadowfang":
			self.otherUnits.append(Shadowfang(self))

		elif unit == "Immolite":
			self.otherUnitsClick.append(Immolite(self))
		
		elif unit == "Nitrocybe":
			self.otherUnitsClick.append(Nitrocybe(self))

		else:
			#print("ERROR:",unit,"NOT IN unitStrToClass")
			sys.exit(1)

	def buyUnit(self,unit):
		for resource in unitCostDict[unit]:
			self.resDict[resource]-=unitCostDict[unit][resource]
		
		self.unitStrToClass(unit)

	def displayUnits(self):
		unitsNames,count=countNumberOfEachUnit(self.resUnits+self.resUnitsClick+self.otherUnits+self.otherUnitsClick)
		for a in range(0,len(unitsNames)):
			print("Unit:",unitsNames[a],count[a])

	def displayResources(self):
		print("Gold:", self.resDict['gold'])
		print("Blue:", self.resDict['blue'])
		print("Red:", self.resDict['red'])
		print("Energy:" , self.resDict['energy'])

	def __str__(self):
		self.displayUnits()
		self.displayResources()
		return ""
##Initialize		if self.cooldown>=0:

counterToEndAllCounters=[0,0] #For progress dumping	
turnCounter=0 #Tracks turnNumbre
won=False #Did we win boolean
isPossible=True #Is this possible boolean
fileName="Maps/Plasma Bombs Expert4.txt" #File to initialize from
p1INIT=initializeMapFromFile(fileName)
p1=player() #Player1 (your perspective)
p2BlockersINIT=[] #Dumb list of blockers hp
for i in p1INIT[1]:
	p2BlockersINIT.append(int(i.strip()))
p2UnitsINIT=[]
for i in p1INIT[2]:
	p2UnitsINIT.append(int(i.strip())) #Dumb list of units behind blockers hp
turnLimit=5 #Turn Limit
masterUnitList=[] # All units that can be bought this game
unitList=[]#List of lists of units that can be bought each turn
unitListNotThisUnit=[]
turnHistory=[] #Units bought history
remainingOptions=[] #
otherUnitsClicksPerTurn=[]
unitCostDict={ #Dictionary of ALL unit costs added to date
'Engineer':{'gold':2},
'Drone':{'gold':3,'energy':1},
'Animus':{'gold':6},
'Tarsier':{'gold':4,'red':1},
'Perforator':{'gold':3,'red':1},
'Shadowfang':{'gold':8,'red':3},
'Immolite':{'gold':3,'red':1},
'Nitrocybe':{'gold':1,'red':1}
}
masterDoNotBuyTurnLeftUnitList=[[],['Tarsier','Nitrocybe'],[],[],['Drone'],['Engineer']] #list of what not to buy by turn
unitResOnClickList=["Drone"]
unitResList=["Engineer","Animus"]
unitOtherList=["Tarsier","Shadowfang"]
unitOtherOnClickList=["Immolite","Nitrocybe","Perforator"]
##### Prepare all possible units that can be bought this game from file
for i in p1INIT[0]:
	masterUnitList.append(i.strip())

##### Prepare list of units that can be bought by turn
doNotBuyTurnLeftUnitList=[] #templist
if len(masterDoNotBuyTurnLeftUnitList)>turnLimit:
	for a in masterDoNotBuyTurnLeftUnitList[turnLimit-1:]:
		for unit in a:	
			doNotBuyTurnLeftUnitList.append(unit)
for turnNumber in range(0,turnLimit-1):
	unitList.append([])
	#print("turnLimit-1-turnNumber:",turnLimit-1-turnNumber)
	try:
		doNotBuyTurnLeftUnitList+=masterDoNotBuyTurnLeftUnitList[turnLimit-1-turnNumber]
		#print("doNotBuyTurnLeftUnitList:",doNotBuyTurnLeftUnitList)
		for unit in masterUnitList:
			if unit not in doNotBuyTurnLeftUnitList:
				#print("turnNumber:",turnNumber)
				#print("unit:",unit)
				unitList[turnNumber].append(unit)
			else:
				#print("unit in doNotBu:TurnLeftUnitList[turnLimit-1-turnNumber:]:",unit)
				pass

	except IndexError:
		#print("turnNumber at IndexError:",turnNumber)
		unitList[turnNumber]=masterUnitList
	#print("unitList",unitList)

masterUnitList=unitList

unitList=[]
for i in range(0,turnLimit-2):
	unitList.append(None)

doNotBuyTurnLeftUnitList=None # kill temp listr
while not won and isPossible:
	turnCounter=0
	#### RESET PLAYER 1
	p1.__init__()
	for i in p1INIT[3:]:
		unitStrToClassFromFile(p1,i)
	#### RESET PLAYER 1 COMPLETE

	#### RESET PLAYER 2 BLOCKERS
	p2Blockers=p2BlockersINIT
	p2Units=p2UnitsINIT
	#### RESET PLAYER 2 COMPLETE

	while turnCounter<turnLimit:
		p1.startTurn()
		p1,p2Blockers,p2Units=autoTurn(p1,p2Blockers,p2Units)
		p1.turnEnd()
		if p2Units==[]:
			won=True
			break

		turnCounter+=1

	isPossible=False
	for i in turnHistory:
		if i!=[]:
			isPossible=True

	if counterToEndAllCounters[0]==100000:
		counterToEndAllCounters[1]+=1
		print(100000*counterToEndAllCounters[1],"attempts past:")
		print("turnHistory:",turnHistory)
		print("otherUnitsClicksPerTurn",otherUnitsClicksPerTurn)
		#print("unitList",unitList)
		counterToEndAllCounters[0]=0
		
	counterToEndAllCounters[0]+=1


#print("turnHistory:",turnHistory)
if won:
	print("u won!\n")
	print("Winning Combination:")
	print(turnHistory)
	print(otherUnitsClicksPerTurn)
	print(p1)

	#solutionFile=open(fileName,"w")
	#solutionFile.write(turnHistory)

elif not isPossible:
	print("impossible")
	print(turnHistory)
#print("INITresUnits:",INITresUnits)
#print("INITresDict:",INITresDict)


