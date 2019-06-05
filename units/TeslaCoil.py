#!/usr/bin/python3.6
class TeslaCoil:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		for i in range(0,2):
			self.owner.addUnit("Engineer,1,-1")

		self.cooldown=1
		self.defaultBlocking=False
		self.assignedBlocking=False
		self.health=3
		self.fragile=True
		self.unitsToSacrifice=[]
		self.attack=3
		self.startTurnDict={

		}
		self.onClickDict={
		"attack":3
		}
		self.onClickCost={
		}

	def __str__(self):
		return "Tesla Coil"

	def startTurn(self):
		return True

	def canClick(self):
		Sac=False
		multiplicity=1
		self.unitsToSacrifice=[]
		for unit in owner.unitsListWithOnClick:
			if str(unit)=="Engineer":
				self.unitsToSacrifice.append(unit)
				if len(self.unitsToSacrifice)==multiplicity:
					break
					Sac=True

		if Sac == False:
			return False

		return True

	def onClick(self):
		for unit in self.unitsToSacrifice:
			self.owner.destroy(unit)


	def info(self): 
		return {
		"health":self.health,
		"fragile":self.fragile}

def TeslaCoilCost():
	buyCostDict={
		"gold":11,
		"green":2,
		"blue":1
	}
	
	return buyCostDict,True,4,[],"Tesla Coil"