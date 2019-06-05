#!/usr/bin/python3.6
class BoreholePatroller:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		for i in range(0,1):
			self.owner.addUnit("Pixie,1,-1")

		self.cooldown=1
		self.defaultBlocking=True
		self.health=2
		self.fragile=False
		self.attack=1
		self.startTurnDict={
		"attack":1
		}

	def __str__(self):
		return "Borehole Patroller"

	def startTurn(self):
		return True

	def info(self): 
		return {
		"health":self.health}

def BoreholePatrollerCost():
	buyCostDict={
		"gold":6,
		"green":1,
		"blue":1
	}
	
	return buyCostDict,False,10,[],"Borehole Patroller"