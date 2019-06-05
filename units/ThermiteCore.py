#!/usr/bin/python3.6
class ThermiteCore:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=5
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
		"attack":2
		}

	def __str__(self):
		return "Thermite Core"

	def startTurn(self):
		return True

	def canClick(self):
		for i in self.OnClickCost
			if owner.resDict[i]<=onClickCost:
				return False

		return True

	def onClick(self):
		for i in self.onClickCost:
			player.resDict[i]-=self.onClickCost[i]

		for i in range(0,2):
			owner.addUnit("Pixie,1,-1")


	def info(self): 
		return {
		"lifespan":self.lifespan,
		"health":self.health}

def ThermiteCoreCost():
	buyCostDict={
		"gold":1,
		"blue":1
	}
	
	return buyCostDict,True,4,[],"Thermite Core"