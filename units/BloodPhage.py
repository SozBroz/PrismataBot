#!/usr/bin/python3.6
class BloodPhage:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=False
		self.assignedBlocking=False
		self.health=2
		self.fragile=False
		self.attack=1
		self.startTurnDict={
		"gold":1,
		"attack":1
		}
		self.onClickDict={
		"gold":1
		}
		self.onClickCost={
		"red":1
		}

	def __str__(self):
		return "Blood Phage"

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

def BloodPhageCost():
	buyCostDict={
		"gold":8,
		"energy":1,
		"red":1
	}
	
	return buyCostDict,True,4,[],"Blood Phage"