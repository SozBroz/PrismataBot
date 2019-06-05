#!/usr/bin.python3.6
class EbbTurbine:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=False
		self.assignedBlocking=False
		self.health=4
		self.fragile=False
		self.unitsToSacrifice=[]
		self.attack=0
		self.startTurnDict={
		"gold":2
		}
		self.onClickDict={
		"gold":3,
		"energy":1
		}
		self.onClickCost={
		}

	def __str__(self):
		return "Ebb Turbine"

	def startTurn(self):
		return True

	def canClick(self):
		Sac=False
		multiplicity=1
		self.unitsToSacrifice=[]
		for unit in owner.unitsListWithOnClick:
			if str(unit)=="Drone":
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


def EbbTurbineCost():
	buyCostDict={
		"gold":6,
		"energy":1,
		"blue":1
	}
	
	return buyCostDict,True,10,[],"Ebb Turbine"