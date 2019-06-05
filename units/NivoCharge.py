#!/usr/bin/python3.6
class NivoCharge:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=False
		self.assignedBlocking=False
		self.health=1
		self.attack=0
		self.startTurnDict={

		}
		self.onClickDict={

		}
		self.onClickCost={
		}

	def __str__(self):
		return "Nivo Charge"

	def startTurn(self):
		return True

	def canClick(self):
		return True

	def onClick(self):
		self.owner.destroy(self)
		self.owner.freeze(5)

	def info(self): 
		return {
		"lifespan":self.lifespan,
		"health":self.health}

def NivoChargeCost():
	buyCostDict={
		"gold":2,
		"green":1
	}
	
	return buyCostDict,True,10,[],"Nivo Charge"