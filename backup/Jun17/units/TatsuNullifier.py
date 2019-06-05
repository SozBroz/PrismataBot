#!/usr/bin.python3.6
class TatsuNullifier:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=False
		self.assignedBlocking=False
		self.health=2
		self.fragile=False
		self.attack=2
		self.startTurnDict={
		"attack":2
		}
		self.onClickDict={

		}
		self.onClickCost={
		}

	def __str__(self):
		return "Tatsu Nullifier"

	def startTurn(self):
		return True

	def canClick(self):
		return True

	def onClick(self):
		self.owner.freeze(5)

	def info(self):
		print("Health: "+str(self.health))

def TatsuNullifierCost():
	buyCostDict={
		"gold":12,
		"red":4
	}
	
	return buyCostDict,True,4,[],"Tatsu Nullifier"