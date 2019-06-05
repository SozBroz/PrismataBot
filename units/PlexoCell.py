#!/usr/bin/python3.6
class PlexoCell:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=1
		self.frontline=False
		self.cooldown=0
		self.defaultBlocking=True
		self.health=4
		self.fragile=False
		self.attack=0
		self.startTurnDict={

		}

	def __str__(self):
		return "Plexo Cell"

	def startTurn(self):
		return True

	def info(self): 
		return {
		"lifespan":self.lifespan,
		"health":self.health}

def PlexoCellCost():
	buyCostDict={
		"gold":2,
		"green":2
	}
	
	return buyCostDict,False,10,['Drone'],"Plexo Cell"