#!/usr/bin/python3.6
class Forcefield:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=0
		self.defaultBlocking=True
		self.health=2
		self.fragile=True
		self.attack=0
		self.startTurnDict={

		}

	def __str__(self):
		return "Forcefield"

	def startTurn(self):
		return True

	def info(self): 
		return {
		"health":self.health,
		"fragile":self.fragile}

def ForcefieldCost():
	buyCostDict={
		"gold":1,
		"green":1
	}
	
	return buyCostDict,False,20,['Drone'],"Forcefield"