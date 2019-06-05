#!/usr/bin.python3.6
class Militia:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=False
		self.assignedBlocking=False
		self.health=4
		self.fragile=False
		self.attack=1
		self.startTurnDict={
		"attack":1
		}
		self.onClickDict={
		"gold":1
		}
		self.onClickCost={
		"attack":1
		}

	def __str__(self):
		return "Militia"

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
		print("Health: "+str(self.health))

def MilitiaCost():
	buyCostDict={
		"gold":6,
		"blue":1
	}
	
	return buyCostDict,True,10,[],"Militia"