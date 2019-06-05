#!/usr/bin.python3.6
class Drone:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
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
		return "Drone"

	def startTurn(self):
		return True

	def canClick(self):
		return True

	def onClick(self):
		pass

	def info(self):
		print("Health: "+str(self.health))

def DroneCost():
	buyCostDict={
		"gold":3,
		"energy":1
	}
	
	return buyCostDict,True,20,[],"Drone"