#!/usr/bin/python3.6
class player:
	def __init__(self):
		self.resDict={
		'gold':0,
		'blue':0,
		'red':0,
		'green':0,
		'energy':0,
		'attack':0,
		'defence':0 }
		self.opponent=None
		self.masterUnitList=[]
		self.unitsWithOnClickList=[]
		self.masterUnitNameList=[]
		self.frontLineList=[]
		self.blockers=[]
		self.freezeCounters=[]
		self.unitInfoDict={}
		self.fullNameToCleanNameDict={}

	def startTurn(self):
		self.resDict['attack']=0
		for unit in self.masterUnitList:
			if unit.lifespan>-1:
				unit.lifespan-=1
				if unit.lifespan==0:
					print("trying to destroy",str(unit))
					self.destroy(unit)

			unit.cooldown=(max(0,unit.cooldown-1))
			if unit.cooldown==0:
				for resource in unit.startTurnDict:
					self.resDict[resource]+=unit.startTurnDict[resource]

				if self.unitInfoDict[self.fullNameToCleanNameDict[str(unit)]]["onClickSpell"]=="True":
					self.unitsWithOnClickList.append(unit)
				
				try:
					if unit.assignedBlocking==True:
						if unit not in self.blockers:
							self.blockers.append(unit)

				except AttributeError:
					pass

				try:
					if unit.frontLineList:
						if unit not in self.frontLineList:
							self.frontLineList.append(unit)

				except AttributeError:
					pass

			try:
				if unit.defaultBlocking==True:
					if unit not in self.blockers:
						self.blockers.append(unit)

			except AttributeError:
				pass
			
		self.resDict['defence']=0
		for unit in self.blockers:
			self.resDict['defence']+=unit.health

		####Put units in correct blockers/backLine

	def destroy(self,unitToBeDestroyed):
		unitToBeDestroyedIndex=self.masterUnitList.index(unitToBeDestroyed)
		self.masterUnitList.pop(unitToBeDestroyedIndex)

		if unitToBeDestroyed in self.unitsWithOnClickList:
			unitToBeDestroyedIndex=self.unitsWithOnClickList.index(unitToBeDestroyed)
			self.unitsWithOnClickList.pop(unitToBeDestroyedIndex)
		
		if unitToBeDestroyed in self.blockers:
			unitToBeDestroyedIndex=self.blockers.index(unitToBeDestroyed)
			self.resDict['defence']-=unitToBeDestroyed.health
			self.blockers.pop(unitToBeDestroyedIndex)
					

	def addUnit(self,unit):
		masterUnitList.append(unit(self))
		
	def canClick(self,unit):
		if unit.canClick() and unit.cooldown==0:
			return True

		return False

	def click(self,unit):
		for resource in unit.onClickCost:
			self.resDict[resource]-=unit.onClickCost[resource]
		for resource in unit.onClickDict:
			self.resDict[resource]+=unit.onClickDict[resource]

		unit.onClick()

		if unit in self.blockers:
			self.resDict["defence"]-=unit.health
			self.blockers.pop(self.blockers.index(unit))

		if unit in self.frontLineList:
			self.frontLineList.pop(self.frontLineList.index(unit))

		unit.cooldown+=1

		return self

	def endTurn(self):
		self.resDict['energy']=0
		self.resDict['blue']=0
		self.resDict['red']=0
		
	def canBuyUnit(self,unit,amount):
		if self.unitInfoDict[unit]["supply"]==0:
			print("Out of supply")
			return False

		for resource in self.unitInfoDict[unit]["resDict"]:
			if self.resDict[resource]<self.unitInfoDict[unit]["resDict"][resource]*amount:
				print("Not enough",resource)
				return False

		unitsToBeSacd=[]
		UTBSLen=0
		for unitSac in self.unitInfoDict[unit]["unitSac"]:
			for MULUnit in self.masterUnitList:
				if str(MULUnit)==unitSac and MULUnit not in unitsToBeSacd:
					unitsToBeSacd.append(MULUnit)
					break

			if len(unitsToBeSacd)==unitsToBeSacd:
				return False

		return True

	def displayUnits(self,option):
		if option=="all":
			unitsNames,count=countNumberOfEachUnit(self.masterUnitList)
			for unitIndex in range(0,len(unitsNames)):
				print("Unit:",unitsNames[unitIndex],count[unitIndex])

		elif option=="blockers":
			unitNames,count=countNumberOfEachUnit(self.blockers)
			for unitIndex in range(0,len(unitNames)):
				print("Unit:",unitNames[unitIndex],count[unitIndex])

			unitNames,count=countNumberOfEachUnit(self.frontLineList)
			if len(unitNames)>0:
				print("\nFrontLine Targets")
				for unitIndex in range(0,len(unitNames)):
					print("Unit:",unitNames[unitIndex],count[unitIndex])

	def displayResources(self):
		print("Gold:", self.resDict['gold'])
		print("Blue:", self.resDict['blue'])
		print("Red:", self.resDict['red'])
		print("Green:",self.resDict['green'])
		print("Energy:" , self.resDict['energy'])
		print("Attack:", self.resDict['attack'])
		print("Defence:", self.resDict['defence'])

	def __str__(self):
		self.displayUnits("all")		
		self.displayResources()
		return ""

	def freeeze(self,amount):
		selectedUnit=input("pick a blocking unit to apply "+str(amount)+" freezeCounters on") 
		#Will access self.opponent.blockers and remove any unit with freeze counters > it's hp
		#At End of turn something will have to flush the created list of unit/freeze counter pairings

	def canSnipe(self,unitName):#This function has to handle a list of conditions 
		pass 				   #OR a unitName

	def snipe (self,unitName): #This function has to handle a list of conditions 
		pass 				   #OR a unitName
	
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

def unitStrToClassFromFile(owner,initUnitOptions):
	for initUnitOptions in player1InitUnits:
		unitStrToClass(owner,initUnitOptions)