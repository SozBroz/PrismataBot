#!/usr/bin.python3.6
class Xaetron:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=0
		self.defaultBlocking=True
		self.assignedBlocking=False
		self.health=4
		self.fragile=True
		self.attack=0
		self.startTurnDict={

		}
		self.onClickDict={

		}
		self.onClickCost={
		}

	def __str__(self):
		return "Xaetron"

	def startTurn(self):
		self.maxHealth=12
		self.health=min(self.health+4,self.maxHealth)
		return True

	def canClick(self):
		if self.health<=7:
			return False

		return True

	def onClick(self):
		self.health-=7
		for i in range(0,5):
			owner.addUnit("Gauss Charge,1,-1")


	def info(self):
		print("Health: "+str(self.health))
		print("Fragile:",self.fragile)

def XaetronCost():
	buyCostDict={
		"gold":11,
		"green":5
	}
	
	return buyCostDict,True,1,[],"Xaetron"