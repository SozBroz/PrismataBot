#!/usr/bin/python3.6
class Resophore:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=5
		self.defaultBlocking=False
		self.health=4
		self.fragile=True
		self.attack=0
		self.startTurnDict={

		}

	def __str__(self):
		return "Resophore"

	def startTurn(self):
		self.owner.resDict["attack"]+=self.owner.numberOfUnit("Forcefield")
		return True

	def info(self): 
		return {
		"health":self.health,
		"fragile":self.fragile}

def ResophoreCost():
	buyCostDict={
		"gold":1,
		"green":1,
		"red":1
	}
	
	return buyCostDict,False,1,[],"Resophore"