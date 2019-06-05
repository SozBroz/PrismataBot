#!/usr/bin.python3.6
class Manticore:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=False
		self.assignedBlocking=False
		self.health=4
		self.fragile=False
		self.attack=2
		self.startTurnDict={
		"attack":2
		}
		self.onClickDict={
		"gold":3
		}
		self.onClickCost={
		"attack":2
		}

	def __str__(self):
		return "Manticore"

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

def ManticoreCost():
	buyCostDict={
		"gold":3,
		"blue":2
	}
	
	return buyCostDict,True,4,['Steelsplitter'],"Manticore"