#!/usr/bin.python3.6
class GaussiteSymbiote:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=False
		self.assignedBlocking=False
		self.health=2
		self.fragile=False
		self.attack=1
		self.startTurnDict={
		"green":1,
		"attack":1
		}
		self.onClickDict={

		}
		self.onClickCost={
		"green":3
		}

	def __str__(self):
		return "Gaussite Symbiote"

	def startTurn(self):
		return True

	def canClick(self):
		for i in self.OnClickCost
			if owner.resDict[i]<=onClickCost:
				return False

		return True

	def onClick(self):
		self.owner.destroy(self)
		for i in self.onClickCost:
			player.resDict[i]-=self.onClickCost[i]

		for i in range(0,6):
			owner.addUnit("Gauss Charge,1,-1")


def GaussiteSymbioteCost():
	buyCostDict={
		"gold":8,
		"red":2
	}
	
	return buyCostDict,True,4,[],"Gaussite Symbiote"