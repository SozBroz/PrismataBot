#!/usr/bin/python3.6
class KineticDriver:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=6
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

		}
		self.onClickCost={
		"gold":2
		}

	def __str__(self):
		return "Kinetic Driver"

	def startTurn(self):
		return True

	def canClick(self):
		for i in self.OnClickCost
			if owner.resDict[i]<=onClickCost:
				return False

		if not self.owner.canSnipe(['isABC'])
			return False

		return True

	def onClick(self):
		self.owner.destroy(self)
		for i in self.onClickCost:
			player.resDict[i]-=self.onClickCost[i]

		self.owner.snipe(['isABC'])

	def info(self): 
		return {
		"lifespan":self.lifespan,
		"health":self.health}

def KineticDriverCost():
	buyCostDict={
		"gold":5,
		"green":1
	}
	
	return buyCostDict,True,4,[],"Kinetic Driver"