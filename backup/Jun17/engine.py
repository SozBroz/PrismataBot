#!/usr/bin/python3.6
#def initializePlayersCampaignStyle(player1UnitsThatCanBeBought,player1UnitsThatCanBeBoughtSupply,player1InitUnits,player2UnitsThatCanBeBought,player2UnitsThatCanBeBoughtSupply,player2InitUnits):
import sys
##Initialize		if self.cooldown>=0:
from prismataPlayerClass import *
from died import *

def importBaseUnits():
	baseUnitsFile=open("units/BaseSetList","r")
	baseUnitsFile=baseUnitsFile.readlines()
	baseUnitsFile=baseUnitsFile[0].split(",")
	return(baseUnitsFile)

def buyUnit(player,unit):
		for resource in player.unitInfoDict[unit]["resDict"]:
			player.resDict[resource]-=player.unitInfoDict[unit]["resDict"][resource]
		
		player.unitInfoDict[unit]["supply"]-=1
		exec(("player.masterUnitList.append("+unit+"(player))"))
		if unitInfoDict[unit]["onClickSpell"]==True:
			player.unitsWithOnClickList.append(player.masterUnitList[-1])

		try:
			if player.masterUnitList[-1].defaultBlocking:
				player.resDict['defence']+=player.masterUnitList[-1].health
				player.blockers.append(player.masterUnitList[-1])

		except AttributeError:
			pass

		unitsToBeSacd=[]
		for unitSac in unitInfoDict[unit]["unitSac"]:
			for MULUnit in player.masterUnitList:
				if str(MULUnit)==unitSac and MULUnit not in unitsToBeSacd:
					unitsToBeSacd.append(MULUnit)
					break
		
		for UTBSunit in unitsToBeSacd:
			player.destroy(UTBSunit)

def unitInfoDump(unit):
	print("Unit Name:", str(unit))
	if unit in unit.owner.blockers:
		print("Is currently blocking")

	if unit in unit.owner.unitsWithOnClickList and unit.owner.canClick(unit):
		print("Unit can be clicked")

	unit.info()
	print()

def inputInterpreterBuyClick(player,usrInput):
	global tempInputHistory
	tempInputHistory.append(usrInput)
	if (usrInput == "a" or usrInput == "A"):
		return player,False

	usrInput=usrInput.split(" ")
	command=usrInput[0]
	usrInputLen=len(usrInput)

	if command=="i" or command=="I":
		if usrInputLen>=2: 
			playerChoice=usrInput[1]

			if usrInputLen>=3:
				unitName=usrInput[2]
				try:
					selectedUnitNumber=int(usrInput[-1])
					for additionalInput in usrInput[3:-1]:
						unitName+=" "+additionalInput

					if unitName in fullNameToCleanNameDict:
						unitName=fullNameToCleanNameDict[unitName]

					skipCounter=0
					if playerChoice=="0":
						for unit in player.masterUnitList:
							if str(unit)==unitName:
								if skipCounter==selectedUnitNumber:
									unitInfoDump(unit)
									return player, True

								else:
									skipCounter+=1

						print("There aren't ",selectedUnitNumber+1,unitName, "in your control")

					elif playerChoice=="1":
						for unit in player.opponent.masterUnitList:
							if str(unit)==unitName:
								if skipCounter==selectedUnitNumber:
									unitInfoDump(unit)
									return player, True

								else:
									skipCounter+=1

						print("There aren't ",selectedUnitNumber+1," ",unitName, "in your opponents control")

					else:
						print("Valid PlayerChoices:")
						print("0 for yourself")
						print("1 for your opponent")

					return player, True


				except ValueError:
					counter=0
					for additionalInput in usrInput[3:]:
						unitName+=additionalInput

					if playerChoice=="0":
						for unit in player.masterUnitList:
							if str(unit)==unitName:
								print("Number:", counter)
								unitInfoDump(unit)
								counter+=1

					elif playerChoice=="1":
						for unit in player.masterUnitList:
							if str(unit)==unitName:
								print("Number:", counter)
								unitInfoDump(unit)
								counter+=1

					else:
						print("Valid PlayerChoices:")
						print("0 for yourself")
						print("1 for your opponent")

					return player, True

			counter=0
			if playerChoice=="0":
				for unit in player.masterUnitList:
					print("Number:",counter)
					unitInfoDump(unit)
					counter+=1

			elif playerChoice=="1":
				for unit in player.opponent.masterUnitList:
					print("Number:",counter)
					unitInfoDump(unit)
					counter+=1

			else:
				print("Valid PlayerChoices:")
				print("0 for yourself")
				print("1 for your opponent")

			return player, True

		print("Your units")
		
		for unitIndex in range(0,len(player.masterUnitList)):
			print("Number:",unitIndex)
			unitInfoDump(player.masterUnitList[unitIndex])
			
		print("\nOpponents Units")
		for unitIndex in range(0,len(player.opponent.masterUnitList)):
			print("Number:",unitIndex)
			unitInfoDump(player.opponent.masterUnitList[unitIndex])
			
		return player, True

	if command=="c" or command=="C":
		if usrInputLen==2:
			unitName=usrInput[1]
			amountOrSelection=-1
			
		elif usrInputLen>=3:
			unitName=usrInput[1]
			try:
				amountOrSelection=int(usrInput[-1])
				for additionalInput in usrInput[2:-1]:
					unitName+=" "+additionalInput

			except ValueError:
				amountOrSelection=-1
				for additionalInput in usrInput[2:]:
					unitName+=additionalInput

		if unitName in fullNameToCleanNameDict:
			unitName=fullNameToCleanNameDict[unitName]

		else:
			print("Command not formatted correctly")
			return player,True

		if amountOrSelection==-1: #click all
			for unitUWONCL in player.unitsWithOnClickList:
				if str(unitUWONCL)==unitName:
					if player.canClick(unitUWONCL)==True:
						player.click(unitUWONCL)

			return player,True

		else:
			skipCounter=0
			for unitUWONCL in player.unitsWithOnClickList:
				if str(unitUWONCL)==unitName:
					if player.canClick(unitUWONCL)==True:
						if skipCounter==amountOrSelection:
							player.click(unitUWONCL)
							return player,True

						else:
							skipCounter+=1

			


		print("Can't click",amountOrSelection,unitName)
		return player,True

								
	elif command=="b" or command=="B":
		if usrInputLen==2:
			unitName=usrInput[1]
			amountOrSelection=1
			
		elif usrInputLen>=3:
			unitName=usrInput[1]
			try:
				amountOrSelection=int(usrInput[-1])
				for additionalInput in usrInput[2:-1]:
					unitName+=" "+additionalInput

			except ValueError:
				amountOrSelection=1
				for additionalInput in usrInput[2:]:
					unitName+=additionalInput

		if unitName in fullNameToCleanNameDict:
			unitName=fullNameToCleanNameDict[unitName]

		if unitName in player.unitInfoDict:
			if player.canBuyUnit(unitName,amountOrSelection):
				for i in range(0,amountOrSelection):
					buyUnit(player,unitName)
			
			else:
				print("Can't buy",amountOrSelection,unitName)

		else:
			print("Unrecognized unit!")
			print("available units:")
			for unit in player.unitInfoDict:
				print(unit)

			print("\n")

		return player,True

	else:
		print("unrecognized command! (Case insenstive:a,b,c)")
		return player, True

def inputInterpreterAttackBlockers(attackChoice,tempAttackPower,opponent):
	global tempInputHistory
	tempInputHistory.append(attackChoice)
	attackChoice=attackChoice.split(" ")
	attackChoiceLen=len(attackChoice)
	if attackChoiceLen>1:
		unitToAttack=attackChoice[0]
		try:
			unitNumber=int(attackChoice[-1])
			for addToUnitName in attackChoice[1:-1]:
				unitToAttack+=addToUnitName

		except ValueError:
			unitNumber=0
			for addToUnitName in attackChoice[:-1]:
				unitToAttack+=addToUnitName

	elif attackChoiceLen==1:
		unitToAttack=attackChoice[0]
		unitNumber=0

	else:
		return tempAttackPower,opponent

	if unitToAttack in fullNameToCleanNameDict:
		unitToAttack=fullNameToCleanNameDict[unitToAttack]

	skipCounter=0
	for unit in opponent.blockers+opponent.frontLineList:
		if fullNameToCleanNameDict[str(unit)]==unitToAttack:
			if skipCounter==unitNumber:
				if tempAttackPower>=unit.health:
					tempAttackPower-=unit.health
					opponent.destroy(unit)
					return tempAttackPower,opponent

				else:
					try:
						if unit.fragile:
							unit.health-=tempAttackPower
					except AttributeError:
						pass
						
					tempAttackPower=0
					return tempAttackPower,opponent

			else:
				skipCounter+=1

	print("Couldn't find that blocker")
	return tempAttackPower, opponent

def inputInterpreterAttackBreach(attackChoice,tempAttackPower,opponent):
	global tempInputHistory
	tempInputHistory.append(attackChoice)
	attackChoice=attackChoice.split(" ")
	attackChoiceLen=len(attackChoice)
	if attackChoiceLen>1:
		unitToAttack=attackChoice[0]
		try:
			unitNumber=int(attackChoice[-1])
			for addToUnitName in attackChoice[1:-1]:
				unitToAttack+=addToUnitName

		except ValueError:
			unitNumber=0
			for addToUnitName in attackChoice[:-1]:
				unitToAttack+=addToUnitName

	elif attackChoiceLen==1:
		unitToAttack=attackChoice[0]
		unitNumber=0

	else:
		return tempAttackPower,opponent

	if unitToAttack in fullNameToCleanNameDict:
		unitToAttack=fullNameToCleanNameDict[unitToAttack]

	skipCounter=0
	for unit in opponent.masterUnitList:
		if fullNameToCleanNameDict[str(unit)]==unitToAttack:
			if skipCounter==unitNumber:
				if tempAttackPower>=unit.health:
					tempAttackPower-=unit.health
					opponent.destroy(unit)
					return tempAttackPower,opponent

				else:
					unit.health-=tempAttackPower
					tempAttackPower=0
					return tempAttackPower,opponent
			else:
				skipCounter+=1

	print("Couldn't find that unit")
	return tempAttackPower,opponent

def turn(player,opponent):
	#### CALL START TURN SCRIPTS
	player.startTurn()

	#### WRITE INSTRUCTIONS AND RESOURCES 
	print(player)
	print("c Name (a|#):to click (leave # empty for next available)")  #Clean Name:Cut out spaces,
	print("b cleanName #: to buy")
	print("a: to enter attack phase") # periods and apostrophes
	print("i player unit unit#: for info units\n")

	while True:
		####ATTEMPT TO CLICK/BUY as per the user wants until they exit
		player,results=inputInterpreterBuyClick(player,input()) #Click Options
		if results==False: #### Results are false when user calls to enter attack phase
			break

		print(player)

	if player.resDict["attack"]==0: ### Skip Attack Phase if no attack power
			print("You have no attack power")
			return player,opponent

	####Print initial Attack/Defence totals
	print("attack phase")
	print("Your Attack Power:",player.resDict["attack"])
	print("opponents Defence Power:",opponent.resDict["defence"])

	tempAttackPower=player.resDict["attack"] #Work with temp for rest of turn

	#If User can punch through all available blockers then branch into BREACH
	#Breach means Attacker choices which order the opponents units take damage
	#As opposed to the opponent choosing the order
	global tempInputHistory

	if tempAttackPower>=opponent.resDict["defence"]: 
		print("BREACH") #Oh FUCK
		tempAttackPower-=opponent.resDict["defence"]

		for unitIndex in range(0,len(opponent.blockers)):
			print("unit:",str(opponent.blockers[-1]))
			opponent.destroy(opponent.blockers[-1])

		if died(opponent) or tempAttackPower==0:
			return player, opponent

		opponent.displayUnits("all") # Dump out every unit

		while True:
			tempAttackPower,opponent=inputInterpreterAttackBreach(input("write name and number of unit to attack: "),tempAttackPower,opponent)
			print("tempAttackPower:",tempAttackPower)
			print("died(opponent):",died(opponent))
			if tempAttackPower==0 or died(opponent):
				return player,opponent

			print("Remaining attackPower:",tempAttackPower)
			print("Remaining Units:",opponent.displayUnits("all"))

	else:
		opponent.displayUnits("blockers")
		while True:
			tempAttackPower,opponent=inputInterpreterAttackBlockers(input("write name and number of blocker to defend with: "),tempAttackPower,opponent)
			print("tempAttackPower:",tempAttackPower)
			if tempAttackPower==0 or died(opponent):
				print("Defence Over")
				return player,opponent

			print("Remaining attackPower:",tempAttackPower)
			print("Remaining Blockers:")
			opponent.displayUnits("blockers")
# Run end turn

def playGame(player1,player2):
	for unit in unitInfoDict:
		print(unitInfoDict[unit]["fullName"] + " is buyable this game")

	turnNumber=0
	while not died(player1) and not died(player2):
		turnNumber+=1
		global tempInputHistory
		tempInputHistory=[]
		print("Turn #",turnNumber)

		if not turnNumber % 2 == 0:
			print("Player one's turn")
			player1,player2=turn(player1,player2)
			player1.endTurn()
			inputHistoryPlayer1.append(tempInputHistory)

		else:	
			print("player two's turn")
			player2,player1=turn(player2,player1)
			player2.endTurn()
			inputHistoryPlayer2.append(tempInputHistory)

def initializePlayers():
	player1=player()
	player2=player()
	player1.opponent=player2
	player2.opponent=player1
	return(player1,player2)

def initializeRegularGame(player1,player2):
	player1.unitInfoDict=unitInfoDict
	player1.fullNameToCleanNameDict=fullNameToCleanNameDict
	player2.unitInfoDict=unitInfoDict
	player2.fullNameToCleanNameDict=fullNameToCleanNameDict
	for temp in range(0,6):
		player1.masterUnitList.append(Drone(player1))
		player2.masterUnitList.append(Drone(player2))
		player1.unitsWithOnClickList.append(player1.masterUnitList[-1])
		player2.unitsWithOnClickList.append(player2.masterUnitList[-1])

	player1.unitInfoDict["Drone"]["supply"]=21
	player2.masterUnitList.append(Drone(player2))
	player2.unitsWithOnClickList.append(player2.masterUnitList[-1])
	
	for temp in range(0,2):
		player1.masterUnitList.append(Engineer(player1))
		player2.masterUnitList.append(Engineer(player2))

	return player1,player2
	
tempInputHistory=[]
silentTestingMode=False
inputHistoryPlayer1=[]
inputHistoryPlayer2=[]
player1,player2=initializePlayers()
unitInfoDict={}
fullNameToCleanNameDict={}
additionalUnits=[]
#if len(sys.argv)>=3:
	#if "-s" in sys.argv: #silent mode for running script and comparing final output
	#if "-d" in sys.argv: #Dump entry and exit of each function and all relevant variables

if sys.argv[1] == "-c":
	from campaignSetUp import *
	organizeCampaignFile(readFileContents(sys.argv[2]))

elif sys.argv[1]  == "-r":

	#Ask for additional units to import into game
	# for i in range(0,int(input("How many Additional Units?\n"))):
	# 	additionalUnits.append(input("Enter clean unit name: "))

	player1,player2=initializePlayers()
	baseUnitsFile=importBaseUnits()
	sys.path.insert(0,'units/')
	for unitToImport in baseUnitsFile+additionalUnits: #+additionalUnits
		unitInfoDict[unitToImport]={}
		temp={}
		exec(("from "+unitToImport+" import *"))
		exec(("resDict,onClickSpell,supply,unitSac,fullName="+unitToImport+"Cost()"))
		unitInfoDict[unitToImport]["resDict"]=resDict
		unitInfoDict[unitToImport]["onClickSpell"]=onClickSpell
		unitInfoDict[unitToImport]["supply"]=int(supply)
		unitInfoDict[unitToImport]["unitSac"]=unitSac
		unitInfoDict[unitToImport]["fullName"]=fullName
		fullNameToCleanNameDict[fullName]=unitToImport #So you can jump from fullname to cleanName as well
		
	player1,player2=initializeRegularGame(player1,player2)
	playGame(player1,player2)

if died(player1):
	print("Player2 Wins")
else:
	print("Player1 Wins")

print("inputHistoryPlayer Dump:")
if len(inputHistoryPlayer1)==len(inputHistoryPlayer2):
	for i in range(0,len(inputHistoryPlayer1)):
		for turnClicks in inputHistoryPlayer1[i]:
			print(turnClicks)
		for turnClicks in inputHistoryPlayer2[i]:
			print(turnClicks)
else:
	for i in range(0,len(inputHistoryPlayer1)-1):
		for turnClicks in inputHistoryPlayer1[i]:
			print(turnClicks)
		for turnClicks in inputHistoryPlayer2[i]:
			print(turnClicks)
	for turnClicks in inputHistoryPlayer1[-1]:
		print(turnClicks)