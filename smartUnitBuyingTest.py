#!/usr/bin/python3.6
turnLimit=5
masterUnitList=['Engineer','Drone','Tarsier','Nitrocybe','NightCrawler']
unitList=[]
masterDoNotBuyTurnLeftUnitList=[[],['Tarsier','Nitrocybe'],[],['Drone'],['Engineer']]
doNotBuyTurnLeftUnitList=[]
if len(masterDoNotBuyTurnLeftUnitList)>turnLimit:
	for a in masterDoNotBuyTurnLeftUnitList[turnLimit-1:]:
		for unit in a:	
			doNotBuyTurnLeftUnitList.append(unit)
for turnNumber in range(0,turnLimit):
	unitList.append([])
	print("turnLimit-1-turnNumber:",turnLimit-1-turnNumber)
	try:
		doNotBuyTurnLeftUnitList+=masterDoNotBuyTurnLeftUnitList[turnLimit-1-turnNumber]
		print("doNotBuyTurnLeftUnitList:",doNotBuyTurnLeftUnitList)
		for unit in masterUnitList:
			if unit not in doNotBuyTurnLeftUnitList:
				print("turnNumber:",turnNumber)
				print("unit:",unit)
				unitList[turnNumber].append(unit)
			else:
				print("unit in doNotBuyTurnLeftUnitList[turnLimit-1-turnNumber:]:",unit)
	except IndexError:
		print("turnNumber at IndexError:",turnNumber)
		unitList[turnNumber].append(masterUnitList)
		
	

	print("unitList:",unitList)

print(unitList)
	