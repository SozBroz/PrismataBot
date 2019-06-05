#!/usr/bin.python3.6
class Polywall:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=True
		self.cooldown=0
		self.defaultBlocking=True
		self.health=6
		self.fragile=False
		self.attack=0
		self.startTurnDict={

		}

	def __str__(self):
		return "Polywall"

	def startTurn(self):
		return True

def PolywallCost():
	buyCostDict={
		"gold":10,
		"blue":1
	}
	
	return buyCostDict,False,10,[],"Polywall"