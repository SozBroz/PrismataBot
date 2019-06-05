#!/usr/bin/python3.6
class Plasmafier:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=True
		self.assignedBlocking=False
		self.health=4
		self.fragile=True
		self.unitsToSacrifice=[]
		self.attack=4
		self.startTurnDict={

		}
		self.onClickDict={
		"attack":4
		}
		self.onClickCost={
		}

	def __str__(self):
		return "Plasmafier"

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


	def info(self): 
		return {
		"health":self.health,
		"fragile":self.fragile}

def PlasmafierCost():
	buyCostDict={
		"gold":12,
		"green":3,
		"blue":1
	}
	
	return buyCostDict,True,4,[],"Plasmafier"