#!/usr/bin.python3.6
class VaiMauronax:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=False
		self.assignedBlocking=False
		self.health=6
		self.fragile=False
		self.attack=3
		self.startTurnDict={
		"attack":3
		}
		self.onClickDict={

		}
		self.onClickCost={
		"attack":1
		}

	def __str__(self):
		return "Vai Mauronax"

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

		self.owner.freeze(7)

	def info(self):
		print("Health: "+str(self.health))

def VaiMauronaxCost():
	buyCostDict={
		"gold":13,
		"blue":1,
		"red":4
	}
	
	return buyCostDict,True,1,[],"Vai Mauronax"