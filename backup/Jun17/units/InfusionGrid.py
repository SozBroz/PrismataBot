#!/usr/bin.python3.6
class InfusionGrid:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=True
		self.assignedBlocking=False
		self.health=4
		self.fragile=False
		self.attack=0
		self.startTurnDict={

		}
		self.onClickDict={

		}
		self.onClickCost={
		"red":1
		}

	def __str__(self):
		return "Infusion Grid"

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

		for i in range(0,4):
			owner.addUnit("Husk,0,-1")


	def info(self):
		print("Health: "+str(self.health))

def InfusionGridCost():
	buyCostDict={
		"gold":5,
		"blue":1
	}
	
	return buyCostDict,True,10,[],"Infusion Grid"