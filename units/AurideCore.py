#!/usr/bin/python3.6
class AurideCore:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=False
		self.assignedBlocking=False
		self.health=1
		self.attack=0
		self.startTurnDict={

		}
		self.onClickDict={
		"gold":2
		}
		self.onClickCost={
		"attack":1
		}

	def __str__(self):
		return "Auride Core"

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


	def info(self): 
		return {
		"health":self.health}

def AurideCoreCost():
	buyCostDict={
		"gold":1,
		"blue":1
	}
	
	return buyCostDict,True,4,[],"Auride Core"