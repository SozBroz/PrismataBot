#!/usr/bin.python3.6
class Cauterizer:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		for i in range(0,4):
			owner.player.addUnit("Engineer,1,-1")

		self.cooldown=1
		self.defaultBlocking=True
		self.assignedBlocking=False
		self.health=3
		self.fragile=False
		self.attack=2
		self.startTurnDict={

		}
		self.onClickDict={
		"attack":2
		}
		self.onClickCost={
		"energy":4
		}

	def __str__(self):
		return "Cauterizer"

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


def CauterizerCost():
	buyCostDict={
		"gold":11,
		"blue":1,
		"red":2
	}
	
	return buyCostDict,True,4,[],"Cauterizer"