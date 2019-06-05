#!/usr/bin.python3.6
class GaussCannon:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=False
		self.health=5
		self.fragile=True
		self.attack=1
		self.startTurnDict={
		"attack":1
		}

	def __str__(self):
		return "Gauss Cannon"

	def startTurn(self):
		return True

def GaussCannonCost():
	buyCostDict={
		"gold":6,
		"green":1
	}
	
	return buyCostDict,False,10,[],"Gauss Cannon"