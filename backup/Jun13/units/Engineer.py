#!/usr/bin.python3.6
class Engineer:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=True
		self.health=1
		self.attack=0
		self.startTurnDict={
		"energy":1
		}

	def __str__(self):
		return "Engineer"

	def startTurn(self):
		return True

def EngineerCost():
	buyCostDict={
		"gold":2
	}
	
	return buyCostDict,False,20,[],"Engineer"