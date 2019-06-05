#!/usr/bin.python3.6
class Electrovore:
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
		"energy":1
		}

	def __str__(self):
		return "Electrovore"

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

def ElectrovoreCost():
	buyCostDict={
		"gold":4,
		"red":1
	}
	
	return buyCostDict,True,10,[],"Electrovore"