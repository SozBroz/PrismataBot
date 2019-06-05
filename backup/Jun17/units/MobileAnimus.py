#!/usr/bin.python3.6
class MobileAnimus:
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
		"red":1
		}
		self.onClickDict={

		}
		self.onClickCost={
		"gold":3
		}

	def __str__(self):
		return "Mobile Animus"

	def startTurn(self):
		return True

	def canClick(self):
		for i in self.OnClickCost
			if owner.resDict[i]<=onClickCost:
				return False

		return True

	def onClick(self):
		self.owner.destroy(self)
		for i in self.onClickCost:
			player.resDict[i]-=self.onClickCost[i]

		for i in range(0,1):
			owner.addUnit("Rhino,0,-1")


	def info(self):
		print("Health: "+str(self.health))

def MobileAnimusCost():
	buyCostDict={
		"gold":4
	}
	
	return buyCostDict,True,10,[],"Mobile Animus"