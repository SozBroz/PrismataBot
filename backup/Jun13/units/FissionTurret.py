#!/usr/bin.python3.6
class FissionTurret:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=5
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=False
		self.assignedBlocking=False
		self.health=1
		self.attack=1
		self.startTurnDict={
		"attack":1
		}
		self.onClickDict={
		"green":3
		}
		self.onClickCost={
		"energy":3
		}

	def __str__(self):
		return "Fission Turret"

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


def FissionTurretCost():
	buyCostDict={
		"gold":4,
		"green":1
	}
	
	return buyCostDict,True,10,[],"Fission Turret"