#!/usr/bin.python3.6
class Conduit:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=False
		self.health=3
		self.fragile=True
		self.attack=0
		self.startTurnDict={
		"green":1
		}

	def __str__(self):
		return "Conduit"

	def startTurn(self):
		return True

	def info(self):
		print("Health: "+str(self.health))
		print("Fragile:",self.fragile)

def ConduitCost():
	buyCostDict={
		"gold":4
	}
	
	return buyCostDict,False,10,[],"Conduit"