#!/usr/bin/python3.6
class ToughFabricator:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.health=20
		self.fragile=False
		self.attack=0
		self.startTurnDict={

		}

	def __str__(self):
		return "Tough Fabricator"

	def startTurn(self):
		for i in range(0,1):
			self.owner.addUnit("Steelsplitter,1,-1")

		return True

	def info(self): 
		return {
		"health":self.health}

def ToughFabricatorCost():
	buyCostDict={
		"green":66
	}
	
	return buyCostDict,False,0,[],"Tough Fabricator"