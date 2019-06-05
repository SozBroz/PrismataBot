#!/usr/bin.python3.6
class ThoriumDynamo:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=2
		self.defaultBlocking=False
		self.assignedBlocking=False
		self.health=8
		self.fragile=True
		self.attack=0
		self.startTurnDict={
		"gold":5,
		"green":1
		}
		self.onClickDict={
		"gold":3
		}
		self.onClickCost={
		"green":3
		}

	def __str__(self):
		return "Thorium Dynamo"

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
		print("Fragile:",self.fragile)

def ThoriumDynamoCost():
	buyCostDict={
		"gold":5,
		"energy":1
	}
	
	return buyCostDict,True,4,['Drone', 'Drone', 'Drone'],"Thorium Dynamo"