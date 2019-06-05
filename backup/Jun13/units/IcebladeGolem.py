#!/usr/bin.python3.6
class IcebladeGolem:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=True
		self.cooldown=1
		self.defaultBlocking=False
		self.assignedBlocking=False
		self.health=6
		self.fragile=False
		self.attack=1
		self.startTurnDict={
		"attack":1
		}
		self.onClickDict={

		}
		self.onClickCost={
		}

	def __str__(self):
		return "Iceblade Golem"

	def startTurn(self):
		return True

	def canClick(self):
		return True

	def onClick(self):
		self.owner.freeze(2)

def IcebladeGolemCost():
	buyCostDict={
		"gold":7,
		"blue":1,
		"red":1
	}
	
	return buyCostDict,True,10,[],"Iceblade Golem"