#!/usr/bin.python3.6
class DoomedWall:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=3
		self.frontline=False
		self.cooldown=0
		self.defaultBlocking=True
		self.health=4
		self.fragile=False
		self.attack=0
		self.startTurnDict={

		}

	def __str__(self):
		return "Doomed Wall"

	def startTurn(self):
		return True

def DoomedWallCost():
	buyCostDict={
		"gold":7,
		"blue":1
	}
	
	return buyCostDict,False,10,[],"Doomed Wall"