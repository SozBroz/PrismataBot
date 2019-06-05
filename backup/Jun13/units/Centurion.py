#!/usr/bin.python3.6
class Centurion:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=0
		self.defaultBlocking=True
		self.health=6
		self.fragile=False
		self.attack=2
		self.startTurnDict={
		"attack":2
		}

	def __str__(self):
		return "Centurion"

	def startTurn(self):
		return True

def CenturionCost():
	buyCostDict={
		"gold":18,
		"green":2,
		"blue":2,
		"red":1
	}
	
	return buyCostDict,False,1,[],"Centurion"