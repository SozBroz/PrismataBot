#!/usr/bin.python3.6
class WildDrone:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=True
		self.cooldown=1
		self.defaultBlocking=False
		self.health=3
		self.fragile=False
		self.attack=0
		self.startTurnDict={
		"gold":2
		}

	def __str__(self):
		return "Wild Drone"

	def startTurn(self):
		return True

def WildDroneCost():
	buyCostDict={
		"gold":5,
		"energy":2
	}
	
	return buyCostDict,False,4,[],"Wild Drone"