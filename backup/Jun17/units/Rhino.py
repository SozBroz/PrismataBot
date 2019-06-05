#!/usr/bin.python3.6
class Rhino:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.stamina=2
		self.cooldown=0
		self.defaultBlocking=True
		self.assignedBlocking=False
		self.health=2
		self.fragile=False
		self.attack=1
		self.startTurnDict={

		}
		self.onClickDict={
		"attack":1
		}
		self.onClickCost={
		}

	def __str__(self):
		return "Rhino"

	def startTurn(self):
		return True

	def canClick(self):
		if self.stamina==0:
			return False

		return True

	def onClick(self):
		self.stamina-=1

	def info(self):
		print("Stamina: "+str(self.stamina))
		print("Health: "+str(self.health))

def RhinoCost():
	buyCostDict={
		"gold":5,
		"red":1
	}
	
	return buyCostDict,True,10,[],"Rhino"