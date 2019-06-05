#!/usr/bin.python3.6
class DeadeyeOperative:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.stamina=3
		self.cooldown=1
		self.defaultBlocking=True
		self.assignedBlocking=False
		self.health=2
		self.fragile=False
		self.attack=0
		self.startTurnDict={

		}
		self.onClickDict={

		}
		self.onClickCost={
		}

	def __str__(self):
		return "Deadeye Operative"

	def startTurn(self):
		return True

	def canClick(self):
		if self.stamina==0:
			return False
		if not self.owner.opponent.owns("Drone")
			return False
		return True

	def onClick(self):
		self.stamina-=1
		self.owner.snipe("Drone")

def DeadeyeOperativeCost():
	buyCostDict={
		"gold":5,
		"blue":2
	}
	
	return buyCostDict,True,4,[],"Deadeye Operative"