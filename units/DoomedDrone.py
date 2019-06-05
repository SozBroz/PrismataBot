#!/usr/bin/python3.6
class DoomedDrone:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=4
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=True
		self.assignedBlocking=False
		self.health=1
		self.attack=0
		self.startTurnDict={

		}
		self.onClickDict={
		"gold":1
		}
		self.onClickCost={
		}

	def __str__(self):
		return "Doomed Drone"

	def startTurn(self):
		return True

	def canClick(self):
		return True

	def onClick(self):
		pass

	def info(self): 
		return {
		"lifespan":self.lifespan,
		"health":self.health}

def DoomedDroneCost():
	buyCostDict={
		"gold":2,
		"energy":1
	}
	
	return buyCostDict,True,10,[],"Doomed Drone"