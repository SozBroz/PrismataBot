#!/usr/bin.python3.6
class GalvaniDrone:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=True
		self.cooldown=1
		self.defaultBlocking=False
		self.assignedBlocking=False
		self.health=1
		self.attack=0
		self.startTurnDict={

		}
		self.onClickDict={
		"gold":1
		}
		self.onClickCost={
		"energy":1
		}

	def __str__(self):
		return "Galvani Drone"

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
		print("Frontline:"+self.frontline)
		print("Health: "+str(self.health))

def GalvaniDroneCost():
	buyCostDict={
		"gold":1,
		"energy":1
	}
	
	return buyCostDict,True,10,[],"Galvani Drone"