#!/usr/bin.python3.6
class Husk:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=0
		self.defaultBlocking=True
		self.health=1
		self.attack=0
		self.startTurnDict={

		}

	def __str__(self):
		return "Husk"

	def startTurn(self):
		return True

def HuskCost():
	buyCostDict={
		"gold":2,
		"red":1
	}
	
	return buyCostDict,False,20,[],"Husk"