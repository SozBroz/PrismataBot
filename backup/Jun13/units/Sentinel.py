#!/usr/bin.python3.6
class Sentinel:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.stamina=3
		self.cooldown=1
		self.defaultBlocking=True
		self.assignedBlocking=False
		self.health=4
		self.fragile=True
		self.attack=1
		self.startTurnDict={

		}
		self.onClickDict={
		"attack":1
		}
		self.onClickCost={
		}

	def __str__(self):
		return "Sentinel"

	def startTurn(self):
		return True

	def canClick(self):
		if self.stamina==0:
			return False
		return True

	def onClick(self):
		self.stamina-=1
		for i in range(0,1):
			owner.addUnit("Engineer,1,-1")


def SentinelCost():
	buyCostDict={
		"gold":7,
		"green":1,
		"red":1
	}
	
	return buyCostDict,True,10,[],"Sentinel"