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
		
		exec(("player.masterUnitList.append("+unit+"(player))"))
		if unitInfoDict[unit]["onClickSpell"]==True:
			player.unitsWithOnClickList.append(player.masterUnitList[-1])

def inputInterpreterBuyClick(player,usrInput):
	if usrInput == "a":
		return player,False

	usrInput=usrInput.split(" ")
	if len(usrInput)<2:
		print("Invalid format")
		return player,True

	command=usrInput[0]
	unit=usrInput[1]
	try:
		amount=int(usrInput[2])

	except ValueError:
		print("amount must be an integer")
		return player, True

	except IndexError:
		amount=1

	if command=="c":
		unitsToBeClicked=[]
		for unitUWONCL in player.unitsWithOnClickList:
			if str(unitUWONCL)==unit:
				if player.canClick(unitUWONCL)==True:
					unitsToBeClicked.append(unitUWONCL)
					if len(unitsToBeClicked)==amount:
						for unitToBeClicked in unitsToBeClicked:
							player.click(unitToBeClicked)

						return player,True
		print("Can't click",str(amount),unit)
		return player,True

								
	elif command=="b":
		for i in range(0,amount):
			if unit in player.unitInfoDict:
				if player.canBuyUnit(unit):
					buyUnit(player,unit)
				else:
					print("can't buy "+str(amount),unit)
			else:
				print("Unrecognized unit!")
				print("available units:")
				for unit in player.unitInfoDict:
					print(unit)
				print("\n")
				return player,True

		return player,True

	else:
		print("unrecognized command! (a,b,c)")
		return player, True

def inputInterpreterAttackBlockers(attackChoice,tempAttackPower,opponent):
	for unit in opponent.masterUnitList:
		if fullNameToCleanNameDict[str(unit)]==attackChoice:
			if tempAttackPower>=unit.health:
				tempAttackPower-=unit.health
				print("Killing: ",attackChoice)
				opponent.destroy(unit)
				print("attackPower",tempAttackPower)
				return tempAttackPower,opponent

			else:
				unit.health-=tempAttackPower
				return tempAttackPower,opponent
			

	print("attackChoice:",attackChoice)
	print("opponent.blockers:",opponent.displayUnits("blockers"))
	sys.exit("fk in inputInterpreterAttackBlockers")
#def inputInterpreterAttackBreach(player,attackChoice,AttackPower):

def turn(player,opponent):
	#### CALL START TURN SCRIPTS
	player.startTurn()

	#### WRITE INSTRUCTIONS AND RESOURCES 
	print(player)
	print("c Name # to click (leave # empty for 1)")     #Clean Name:Cut out spaces,
	print("or a to enter attack phase") # periods and apostrophes
	print("b cleanName # to buy")

	while True:
		####ATTEMPT TO CLICK/BUY as per the user wants until they exit
		player,results=inputInterpreterBuyClick(player,input()) #Click Options
		if results==False: #### Results are false when user calls to enter attack phase
			break

		print(player)

	if player.resDict['attack']==0: ### Skip Attack Phase if no attack power
			print("You have no attack power")
			return player,opponent

	####Print initial Attack/Defence totals
	print("attack phase")
	print("Your Attack Power:",player.resDict['attack'])
	print("opponents Defence Power:",opponent.resDict['defence'])

	tempAttackPower=player.resDict["attack"] #Work with temp for rest of turn

	#If User can punch through all available blockers then branch into BREACH
	#Breach means Attacker choices which order the opponents units take damage
	#As opposed to the opponent choosing the order

	if tempAttackPower>=opponent.resDict["defence"]: 
		print("BREACH") #Oh FUCK
		tempAttackPower-=opponent.resDict["defence"]
		for unit in opponent.blockers:
			opponent.destroy(unit)

		opponent.displayUnits("all") # Dump out every unit
		while True:
			tempAttackPower,opponent,results==inputInterpreterAttackBreach(input("write name of unit to attack: "),tempAttackPower,opponent)
			if tempAttackPower==0 or died(opponent.masterUnitList):
				return player,opponent

	else:
		opponent.displayUnits("blockers")
		while True:
			tempAttackPower,opponent=inputInterpreterAttackBlockers(input("write name of blocker to defend with: "),tempAttackPower,opponent)
			print("tempAttackPower:",tempAttackPower)
			if tempAttackPower==0:
				print("Defence Over")
				return player,opponent

			print("Remaining attackPower:",tempAttackPower)
			print("Remaining Blockers:",opponent.displayUnits("blockers"))

			


# Run end turn

def playGame(player1,player2):
	for unit in unitInfoDict:
		print(unitInfoDict[unit]["fullName"] + " is buyable this game")

	while not died(player1.masterUnitList) and not died(player2.masterUnitList):
		print("Player ones")
		player1,player2=turn(player1,player2)
		player1.endTurn()
		print("player two")
		player2,player1=turn(player2,player1)
		player2.endTurn()
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

	player2.masterUnitList.append(Drone(player2))
	player2.unitsWithOnClickList.append(player2.masterUnitList[-1])


	for temp in range(0,2):
		player1.masterUnitList.append(Engineer(player1))
		player2.masterUnitList.append(Engineer(player2))

	return player1,player2
	

# if len(sys.argv)==1:
	# sys.exit("-c for campaign follow by map filepath\n-r for playing regular games")

player1,player2=initializePlayers()
unitInfoDict={}
fullNameToCleanNameDict={}
#if sys.argv[1] == "-c":
#	from campaignSetUp import *
#	organizeCampaignFile(readFileContents(sys.argv[2]))

#elif sys.argv[1]  == "-r":
	#Ask for additional units to import into game
	#if sys.argv[2] ###Player one or two as option
player1,player2=initializePlayers()
baseUnitsFile=importBaseUnits()
sys.path.insert(0,'units/')
for unitToImport in baseUnitsFile:
	unitInfoDict[unitToImport]={}
	temp={}
	exec(("from "+unitToImport+" import *"))
	exec(("resDict,onClickSpell,supply,unitSac,fullName="+unitToImport+"Cost()"))
	temp["resDict"]=resDict
	temp["onClickSpell"]=onClickSpell
	temp["supply"]=supply
	temp["unitSac"]=unitSac
	temp["fullName"]=fullName
	fullNameToCleanNameDict[fullName]=unitToImport
	unitInfoDict[unitToImport]=temp		

player1,player2=initializeRegularGame(player1,player2)
playGame(player1,player2)

sys.exit("made it")
