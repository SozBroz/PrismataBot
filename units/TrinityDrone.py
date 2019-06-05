#!/usr/bin/python3.6
class TrinityDrone:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=False
		self.assignedBlocking=False
		self.health=5
		self.fragile=True
		self.attack=0
		self.startTurnDict={
		"gold":3
		}
		self.onClickDict={
		"gold":1
		}
		self.onClickCost={
		"green":1
		}

	def __str__(self):
		return "Trinity Drone"

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
		"health":self.health,
		"fragile":self.fragile}

def TrinityDroneCost():
	buyCostDict={
		"gold":2,
		"energy":1,
		"green":1
	}
	
	return buyCostDict,True,10,['Drone', 'Drone'],"Trinity Drone"