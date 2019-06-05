#!/usr/bin.python3.6
class ShiverYeti:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=0
		self.defaultBlocking=True
		self.assignedBlocking=False
		self.health=2
		self.fragile=False
		self.attack=0
		self.startTurnDict={

		}
		self.onClickDict={

		}
		self.onClickCost={
		}

	def __str__(self):
		return "Shiver Yeti"

	def startTurn(self):
		return True

	def canClick(self):
		return True

	def onClick(self):
		self.owner.freeze(2)

def ShiverYetiCost():
	buyCostDict={
		"gold":5,
		"red":1
	}
	
	return buyCostDict,True,10,[],"Shiver Yeti"