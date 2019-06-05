#!/usr/bin.python3.6
class LucinaSpinos:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=False
		self.assignedBlocking=False
		self.health=1
		self.unitsToSacrifice=[]
		self.attack=4
		self.startTurnDict={
		"attack":4
		}
		self.onClickDict={

		}
		self.onClickCost={
		"red":1
		}

	def __str__(self):
		return "Lucina Spinos"

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

		for i in self.OnClickCost
			if owner.resDict[i]<=onClickCost:
				return False

		return True

	def onClick(self):
		for unit in self.unitsToSacrifice:
			self.owner.destroy(unit)

		for i in self.onClickCost:
			player.resDict[i]-=self.onClickCost[i]

		for i in range(0,1):
			owner.addUnit("Perforator,1,-1")


def LucinaSpinosCost():
	buyCostDict={
		"gold":17,
		"red":4
	}
	
	return buyCostDict,True,1,[],"Lucina Spinos"