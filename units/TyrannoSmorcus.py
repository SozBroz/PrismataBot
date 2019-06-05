#!/usr/bin/python3.6
class TyrannoSmorcus:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=False
		self.assignedBlocking=False
		self.health=2
		self.fragile=False
		self.attack=2
		self.startTurnDict={
		"attack":1
		}
		self.onClickDict={
		"attack":1
		}
		self.onClickCost={
		"red":2
		}

	def __str__(self):
		return "Tyranno Smorcus"

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

def TyrannoSmorcusCost():
	buyCostDict={
		"gold":5,
		"red":2
	}
	
	return buyCostDict,True,4,[],"Tyranno Smorcus"