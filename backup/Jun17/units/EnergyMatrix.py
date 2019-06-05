#!/usr/bin.python3.6
class EnergyMatrix:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=0
		self.defaultBlocking=True
		self.health=5
		self.fragile=False
		self.attack=0
		self.startTurnDict={

		}

	def __str__(self):
		return "Energy Matrix"

	def startTurn(self):
		return True

	def info(self):
		print("Health: "+str(self.health))

def EnergyMatrixCost():
	buyCostDict={
		"gold":8,
		"blue":2
	}
	
	return buyCostDict,False,4,[],"Energy Matrix"