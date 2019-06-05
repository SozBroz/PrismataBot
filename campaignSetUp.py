#!/usr/bin/python3.6

def organizeCampaignFile(fileContents):

	player1UnitsThatCanBeBought=fileContents[0]
	player1UnitsThatCanBeBoughtSupply=fileContents[1]
	player1InitUnits=[]
	fileContentslen=len(fileContents)
	#print(fileContentslen)
	#print(fileContents[4])
	for i in range(2,fileContentslen):
		#print("i:",)
		#print(fileContents[i])

		if fileContents[i] == "\n":
			player2BeginsAt=i+1
			break

		player1InitUnits.append(fileContents[i])
		

	#Initializing Player two Part of the file
	player2InitUnits=[]
	player2UnitsThatCanBeBought=fileContents[player2BeginsAt]
	player2UnitsThatCanBeBoughtSupply=fileContents[player2BeginsAt+1]	
	for i in range(player2BeginsAt+2,fileContentslen):
		if fileContents[i]!="":
			player2InitUnits.append(fileContents[i])

	return player1UnitsThatCanBeBought.split(","),player1UnitsThatCanBeBoughtSupply.split(','),player1InitUnits,player2UnitsThatCanBeBought.split(','),player2UnitsThatCanBeBoughtSupply.split(','),player2InitUnits