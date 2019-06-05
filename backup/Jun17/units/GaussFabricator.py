#!/usr/bin.python3.6
class GaussFabricator:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=8
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=False
		self.health=10
		self.fragile=True
		self.attack=0
		self.startTurnDict={

		}

	def __str__(self):
		return "Gauss Fabricator"

	def startTurn(self):
		for i in range(0,1):
			owner.player.addUnit("Gauss Cannon,1,-1")

		return True

	def info(self):
		print("Lifespan: "+str(self.lifespan))
		print("Health: "+str(self.health))
		print("Fragile:",self.fragile)

def GaussFabricatorCost():
	buyCostDict={
		"gold":12,
		"green":4
	}
	
	return buyCostDict,False,1,[],"Gauss Fabricator"