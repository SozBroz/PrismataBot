#!/usr/bin.python3.6
class Barrier:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=1
		self.frontline=False
		self.cooldown=0
		self.defaultBlocking=True
		self.health=1
		self.attack=0
		self.startTurnDict={

		}

	def __str__(self):
		return "Barrier"

	def startTurn(self):
		return True

	def info(self):
		print("Lifespan: "+str(self.lifespan))
		print("Health: "+str(self.health))

def BarrierCost():
	buyCostDict={
		"gold":1,
		"green":1
	}
	
	return buyCostDict,False,20,[],"Barrier"