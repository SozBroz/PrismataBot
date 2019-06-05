#!/usr/bin/python3.6
class Pixie:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=False
		self.assignedBlocking=False
		self.health=1
		self.attack=1
		self.startTurnDict={

		}
		self.onClickDict={
		"attack":1
		}
		self.onClickCost={
		}

	def __str__(self):
		return "Pixie"

	def startTurn(self):
		return True

	def canClick(self):
		return True

	def onClick(self):
		self.owner.destroy(self)

	def info(self): 
		return {
		"health":self.health}

def PixieCost():
	buyCostDict={
		"gold":1,
		"blue":1
	}
	
	return buyCostDict,True,20,[],"Pixie"