#!/usr/bin.python3.6
class Nitrocybe:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=2
		self.defaultBlocking=True
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
		return "Nitrocybe"

	def startTurn(self):
		return True

	def canClick(self):
		return True

	def onClick(self):
		self.owner.destroy(self)

	def info(self):
		print("Health: "+str(self.health))

def NitrocybeCost():
	buyCostDict={
		"gold":1,
		"red":1
	}
	
	return buyCostDict,True,20,[],"Nitrocybe"