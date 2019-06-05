#!/usr/bin/python3.6
class Hellhound:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		for i in range(0,1):
			self.owner.addUnit("Engineer,1,-1")

		self.cooldown=1
		self.defaultBlocking=False
		self.health=1
		self.attack=1
		self.startTurnDict={
		"attack":1
		}

	def __str__(self):
		return "Hellhound"

	def startTurn(self):
		return True

	def info(self): 
		return {
		"health":self.health}

def HellhoundCost():
	buyCostDict={
		"gold":5,
		"blue":1,
		"red":1
	}
	
	return buyCostDict,False,10,[],"Hellhound"