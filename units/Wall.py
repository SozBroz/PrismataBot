#!/usr/bin/python3.6
class Wall:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=0
		self.defaultBlocking=True
		self.health=3
		self.fragile=False
		self.attack=0
		self.startTurnDict={

		}

	def __str__(self):
		return "Wall"

	def startTurn(self):
		return True

	def info(self): 
		return {
		"health":self.health}

def WallCost():
	buyCostDict={
		"gold":5,
		"blue":1
	}
	
	return buyCostDict,False,10,[],"Wall"