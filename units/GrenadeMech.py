#!/usr/bin/python3.6
class GrenadeMech:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		for i in range(0,3):
			self.owner.addUnit("Pixie,1,-1")

		self.cooldown=1
		self.defaultBlocking=False
		self.assignedBlocking=False
		self.health=4
		self.fragile=False
		self.unitsToSacrifice=[]
		self.attack=1
		self.startTurnDict={
		"attack":1
		}
		self.onClickDict={

		}
		self.onClickCost={
		"gold":1
		}

	def __str__(self):
		return "Grenade Mech"

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

		for i in self.OnClickCost
			if owner.resDict[i]<=onClickCost:
				return False

		return True

	def onClick(self):
		for unit in self.unitsToSacrifice:
			self.owner.destroy(unit)

		for i in self.onClickCost:
			player.resDict[i]-=self.onClickCost[i]

		for i in range(0,3):
			owner.addUnit("Pixie,1,-1")


	def info(self): 
		return {
		"health":self.health}

def GrenadeMechCost():
	buyCostDict={
		"gold":10,
		"blue":2
	}
	
	return buyCostDict,True,4,[],"Grenade Mech"