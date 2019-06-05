#!/usr/bin/python3.6
class Scorchilla:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=3
		self.defaultBlocking=True
		self.assignedBlocking=False
		self.health=3
		self.fragile=True
		self.delay=0
		self.attack=3
		self.startTurnDict={

		}
		self.onClickDict={
		"attack":3
		}
		self.onClickCost={
		}

	def __str__(self):
		return "Scorchilla"

	def startTurn(self):
		self.delay-=1
		return True

	def canClick(self):
		if self.delay>0:
			return False

		return True

	def onClick(self):
		self.delay=3

	def info(self): 
		return {
		"health":self.health,
		"fragile":self.fragile,
		"delay":self.delay}

def ScorchillaCost():
	buyCostDict={
		"gold":3,
		"green":1,
		"red":1
	}
	
	return buyCostDict,True,10,[],"Scorchilla"