#!/usr/bin/python3.6
class Steelforge:
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
		"blue":2
		}
		self.onClickDict={

		}
		self.onClickCost={
		gold:1,
		"blue":2
		}

	def __str__(self):
		return "Steelforge"

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
			owner.addUnit("Steelsplitter,1,-1")


	def info(self): 
		return {
		"health":self.health}

def SteelforgeCost():
	buyCostDict={
		"gold":4
	}
	
	return buyCostDict,True,4,['Blastforge'],"Steelforge"