#!/usr/bin/python3.6
class Redeemer:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		for i in range(0,6):
			self.owner.addUnit("Gauss Charge,3,-1")

		self.cooldown=1
		self.defaultBlocking=True
		self.assignedBlocking=False
		self.health=4
		self.fragile=False
		self.attack=3
		self.startTurnDict={

		}
		self.onClickDict={
		"attack":3
		}
		self.onClickCost={
		}

	def __str__(self):
		return "Redeemer"

	def startTurn(self):
		return True

	def canClick(self):
		return True

	def onClick(self):
		pass

	def info(self): 
		return {
		"health":self.health}

def RedeemerCost():
	buyCostDict={
		"gold":10,
		"green":1,
		"blue":1
	}
	
	return buyCostDict,True,4,[],"Redeemer"