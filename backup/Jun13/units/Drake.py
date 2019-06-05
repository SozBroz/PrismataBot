#!/usr/bin.python3.6
class Drake:
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
		self.attack=4
		self.startTurnDict={
		"attack":2
		}
		self.onClickDict={
		"attack":2
		}
		self.onClickCost={
		}

	def __str__(self):
		return "Drake"

	def startTurn(self):
		return True

	def canClick(self):
		Sac=False
		multiplicity=1
		self.unitsToSacrifice=[]
		for unit in owner.unitsListWithOnClick:
			if str(unit)=="Blastforge":
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


def DrakeCost():
	buyCostDict={
		"gold":12,
		"blue":2
	}
	
	return buyCostDict,True,4,[],"Drake"