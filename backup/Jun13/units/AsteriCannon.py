#!/usr/bin.python3.6
class AsteriCannon:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=False
		self.assignedBlocking=False
		self.health=16
		self.fragile=True
		self.attack=3
		self.startTurnDict={
		"attack":3
		}
		self.onClickDict={

		}
		self.onClickCost={
		}

	def __str__(self):
		return "Asteri Cannon"

	def startTurn(self):
		return True

	def canClick(self):
		if self.health<=3:
			return False

		return True

	def onClick(self):
		self.health-=3
		for i in range(0,1):
			owner.addUnit("Barrier,0,-1")


def AsteriCannonCost():
	buyCostDict={
		"gold":16,
		"green":4
	}
	
	return buyCostDict,True,4,[],"Asteri Cannon"