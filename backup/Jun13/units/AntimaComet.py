#!/usr/bin.python3.6
class AntimaComet:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=2
		self.defaultBlocking=False
		self.health=1
		self.attack=0
		self.startTurnDict={

		}

	def __str__(self):
		return "Antima Comet"

	def startTurn(self):
		self.owner.resDict["attack"]+=self.owner.numberOfUnit("Engineer")
		self.owner.destroy(self)
		return True

def AntimaCometCost():
	buyCostDict={
		"gold":3,
		"green":1,
		"blue":1,
		"red":1
	}
	
	return buyCostDict,False,1,[],"Antima Comet"