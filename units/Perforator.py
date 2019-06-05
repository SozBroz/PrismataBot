#!/usr/bin/python3.6
class Perforator:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=True
		self.assignedBlocking=False
		self.health=2
		self.fragile=False
		self.attack=1
		self.startTurnDict={

		}
		self.onClickDict={
		"attack":1
		}
		self.onClickCost={
		"red":1
		}

	def __str__(self):
		return "Perforator"

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

def PerforatorCost():
	buyCostDict={
		"gold":3,
		"red":1
	}
	
	return buyCostDict,True,10,[],"Perforator"