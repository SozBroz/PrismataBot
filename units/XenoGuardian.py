#!/usr/bin/python3.6
class XenoGuardian:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=True
		self.health=4
		self.fragile=False
		self.attack=1
		self.startTurnDict={
		"attack":1
		}

	def __str__(self):
		return "Xeno Guardian"

	def startTurn(self):
		return True

	def info(self): 
		return {
		"health":self.health}

def XenoGuardianCost():
	buyCostDict={
		"gold":5,
		"green":1,
		"blue":2
	}
	
	return buyCostDict,False,10,[],"Xeno Guardian"