#!/usr/bin.python3.6
class Hannibull:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=True
		self.cooldown=1
		self.defaultBlocking=True
		self.assignedBlocking=False
		self.health=7
		self.fragile=False
		self.attack=2
		self.startTurnDict={
		"attack":1
		}
		self.onClickDict={
		"attack":1
		}
		self.onClickCost={
		}

	def __str__(self):
		return "Hannibull"

	def startTurn(self):
		return True

	def canClick(self):
		return True

	def onClick(self):
		pass

def HannibullCost():
	buyCostDict={
		"gold":10,
		"blue":1,
		"red":1
	}
	
	return buyCostDict,True,4,[],"Hannibull"