#!/usr/bin/python3.6
class DefenseGrid:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=7
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=True
		self.health=7
		self.fragile=False
		self.attack=0
		self.startTurnDict={

		}

	def __str__(self):
		return "Defense Grid"

	def startTurn(self):
		for i in range(0,1):
			self.owner.addUnit("Drone,1,-1")

		return True

	def info(self): 
		return {
		"lifespan":self.lifespan,
		"health":self.health}

def DefenseGridCost():
	buyCostDict={
		"gold":16,
		"blue":3
	}
	
	return buyCostDict,False,1,[],"Defense Grid"