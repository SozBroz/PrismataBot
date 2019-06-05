#!/usr/bin.python3.6
class FeralWarden:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=0
		self.defaultBlocking=True
		self.assignedBlocking=False
		self.health=3
		self.fragile=True
		self.attack=1
		self.startTurnDict={

		}
		self.onClickDict={
		"attack":1
		}
		self.onClickCost={
		}

	def __str__(self):
		return "Feral Warden"

	def startTurn(self):
		return True

	def canClick(self):
		return True

	def onClick(self):
		pass

def FeralWardenCost():
	buyCostDict={
		"gold":5,
		"green":1,
		"red":1
	}
	
	return buyCostDict,True,10,[],"Feral Warden"