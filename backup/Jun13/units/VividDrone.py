#!/usr/bin.python3.6
class VividDrone:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=False
		self.health=1
		self.attack=0
		self.startTurnDict={
		"gold":3
		}

	def __str__(self):
		return "Vivid Drone"

	def startTurn(self):
		return True

def VividDroneCost():
	buyCostDict={
		"gold":2,
		"energy":2
	}
	
	return buyCostDict,False,10,['Drone', 'Drone'],"Vivid Drone"