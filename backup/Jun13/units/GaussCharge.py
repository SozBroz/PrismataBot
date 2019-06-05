#!/usr/bin.python3.6
class GaussCharge:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=False
		self.health=1
		self.attack=1
		self.startTurnDict={
		"attack":1
		}

	def __str__(self):
		return "Gauss Charge"

	def startTurn(self):
		self.owner.destroy(self)
		return True

def GaussChargeCost():
	buyCostDict={
		"gold":1,
		"green":1
	}
	
	return buyCostDict,False,20,[],"Gauss Charge"