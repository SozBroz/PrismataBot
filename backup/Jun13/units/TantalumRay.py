#!/usr/bin.python3.6
class TantalumRay:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=False
		self.assignedBlocking=False
		self.health=11
		self.fragile=True
		self.attack=1
		self.startTurnDict={
		"attack":1
		}
		self.onClickDict={

		}
		self.onClickCost={
		}

	def __str__(self):
		return "Tantalum Ray"

	def startTurn(self):
		return True

	def canClick(self):
		if self.health<=3:
			return False

		return True

	def onClick(self):
		self.health-=3
		for i in range(0,1):
			owner.addUnit("Gauss Charge,1,-1")


def TantalumRayCost():
	buyCostDict={
		"gold":7,
		"green":2
	}
	
	return buyCostDict,True,10,[],"Tantalum Ray"