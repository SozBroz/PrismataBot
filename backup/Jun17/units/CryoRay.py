#!/usr/bin.python3.6
class CryoRay:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=False
		self.assignedBlocking=False
		self.health=3
		self.fragile=True
		self.attack=0
		self.startTurnDict={

		}
		self.onClickDict={

		}
		self.onClickCost={
		}

	def __str__(self):
		return "Cryo Ray"

	def startTurn(self):
		return True

	def canClick(self):
		if self.health<=1:
			return False

		return True

	def onClick(self):
		self.health-=1
		self.owner.freeze(1)

	def info(self):
		print("Health: "+str(self.health))
		print("Fragile:",self.fragile)

def CryoRayCost():
	buyCostDict={
		"gold":1,
		"green":1
	}
	
	return buyCostDict,True,10,[],"Cryo Ray"